import pandas as pd
from pathlib import Path

# =================================================
# STEP 11: CORE FUNCTION (REUSABLE / PRODUCTION)
# =================================================
def run_log_gap_analysis(input_file: Path, output_dir: Path):
    # -------------------------------------------------
    # Load Excel
    # -------------------------------------------------
    df = pd.read_excel(input_file)

    # -------------------------------------------------
    # Validate Mandatory Columns
    # -------------------------------------------------
    required_columns = {
        "Log Name",
        "Available?",
        "Data Model?",
        "Detections Active?",
        "Retention Period",
    }

    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"❌ Missing mandatory columns: {', '.join(sorted(missing))}")

    # -------------------------------------------------
    # Normalize Columns
    # -------------------------------------------------
    df["Available?"] = (
        df["Available?"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map(lambda x: "yes" if x in {"yes", "y", "true", "1"} else "no")
    )

    df["Data Model?"] = df["Data Model?"].astype(str).str.strip()

    df["Detections Active?"] = (
        df["Detections Active?"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map(
            lambda x: {
                "yes": "yes",
                "y": "yes",
                "partial": "partial",
                "p": "partial",
                "no": "no",
                "n": "no",
            }.get(x, x)
        )
    )

    # -------------------------------------------------
    # STRIDE Mapping
    # -------------------------------------------------
    stride_map = {
        "Network Traffic": ["Denial of Service", "Information Disclosure"],
        "Endpoint": ["Elevation of Privilege", "Tampering", "Repudiation"],
        "Authentication": ["Spoofing", "Repudiation"],
        "Cloud": ["Elevation of Privilege", "Tampering"],
    }

    df["STRIDE Coverage"] = df["Data Model?"].map(
        lambda x: ", ".join(stride_map.get(x, []))
    )

    # -------------------------------------------------
    # STRIDE Gap Analysis
    # -------------------------------------------------
    stride_required = {
        "Spoofing",
        "Tampering",
        "Repudiation",
        "Information Disclosure",
        "Denial of Service",
        "Elevation of Privilege",
    }

    covered_stride = set()
    for val in df["STRIDE Coverage"]:
        for item in str(val).split(","):
            if item.strip():
                covered_stride.add(item.strip())

    missing_stride = stride_required - covered_stride

    # -------------------------------------------------
    # MITRE Mapping
    # -------------------------------------------------
    mitre_map = {
        "Palo Alto FW Traffic": ["T1046", "T1071"],
        "CrowdStrike Falcon EDR": ["T1059", "T1068"],
        "Windows Security Logs": ["T1110"],
        "Azure AD Sign-In Logs": ["T1078"],
    }

    df["MITRE Coverage"] = df["Log Name"].map(
        lambda x: ", ".join(mitre_map.get(x, []))
    )

    # -------------------------------------------------
    # Monitoring Weaknesses
    # -------------------------------------------------
    weaknesses = df.loc[
        (df["Detections Active?"].isin(["no", "partial"]))
        | (pd.to_numeric(df["Retention Period"], errors="coerce") < 90),
        ["Log Name", "Detections Active?", "Retention Period", "MITRE Coverage"],
    ]

    # -------------------------------------------------
    # MITRE Gaps
    # -------------------------------------------------
    mitre_gap = df.loc[
        df["MITRE Coverage"].astype(str).str.strip() == "",
        ["Log Name"],
    ].copy()

    mitre_gap["Reason"] = "No MITRE mapping"

    # -------------------------------------------------
    # Risk Scoring
    # -------------------------------------------------
    def risk_level(row):
        if row["Detections Active?"] == "no" or not row["STRIDE Coverage"]:
            return "High"
        if row["Detections Active?"] == "partial":
            return "Medium"
        return "Low"

    df["Risk Level"] = df.apply(risk_level, axis=1)

    # -------------------------------------------------
    # Optional: Export to Excel (can keep or remove)
    # -------------------------------------------------
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "Log_Gap_Analysis_Result.xlsx"

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Full_Analysis", index=False)
        weaknesses.to_excel(writer, sheet_name="Monitoring_Weaknesses", index=False)
        mitre_gap.to_excel(writer, sheet_name="MITRE_Gaps", index=False)
        df[["Log Name", "Risk Level"]].to_excel(
            writer, sheet_name="Risk_Summary", index=False
        )

    # -------------------------------------------------
    # ✅ FINAL RETURN SECTION (FOR WEB DASHBOARD)
    # -------------------------------------------------
    return {
        # Tables for UI
        "full_analysis": df,
        "monitoring_weaknesses": weaknesses,
        "mitre_gaps": mitre_gap,
        "risk_summary": df[["Log Name", "Risk Level"]],

        # Stats for cards
        "covered_stride": sorted(covered_stride),
        "missing_stride": sorted(missing_stride),

        # Optional file output
        "output_file": output_file,
    }


# =================================================
# CLI ENTRY POINT (STILL WORKS)
# =================================================
if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent
    input_file = BASE_DIR / "data" / "Log_Gap_Analyzer_Sample_Audit.xlsx"
    output_dir = BASE_DIR / "output"

    result = run_log_gap_analysis(input_file, output_dir)

    print("✅ Analysis completed successfully")
    print("Covered STRIDE:", result["covered_stride"])
    print("Missing STRIDE:", result["missing_stride"] or "None")
    print("Output file:", result["output_file"])
