import sys
from pathlib import Path
from flask import Flask, render_template, request

# -------------------------------------------------
# Fix Python path to import from src/
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.log_gap_analyzer import run_log_gap_analysis

app = Flask(__name__)

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# -------------------------------------------------
# HOME / UPLOAD PAGE
# -------------------------------------------------
@app.route("/", methods=["GET"])
def upload():
    return render_template("upload.html")


# -------------------------------------------------
# DASHBOARD PAGE
# -------------------------------------------------
@app.route("/analyze", methods=["POST"])
def analyze():
    uploaded_file = request.files.get("file")

    if not uploaded_file or uploaded_file.filename == "":
        return "No file uploaded", 400

    temp_file = OUTPUT_DIR / uploaded_file.filename
    uploaded_file.save(temp_file)

    result = run_log_gap_analysis(temp_file, OUTPUT_DIR)

    return render_template(
        "dashboard.html",

        # Tables
        full_analysis=result["full_analysis"].to_dict(orient="records"),
        weaknesses=result["monitoring_weaknesses"].to_dict(orient="records"),
        mitre_gaps=result["mitre_gaps"].to_dict(orient="records"),

        # Stats
        risk_summary=result["risk_summary"].to_dict(orient="records"),
        covered_stride=result["covered_stride"],
        missing_stride=result["missing_stride"],
    )


# -------------------------------------------------
# START SERVER
# -------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
