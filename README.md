# 🛡️ Log Gap Analyzer Dashboard

**A Flask-based security analytics tool for SOC teams to visualize detection coverage, audit logs, and identify gaps using MITRE ATT&CK and STRIDE.**

## 📖 Overview

Modern SOCs collect massive amounts of logs, but often struggle to answer the simple question: **"What are we actually detecting?"**

The **Log Gap Analyzer** solves this by ingesting your log audit data and mapping it against industry frameworks. It helps you move from "we have logs" to "we have coverage."

### 🚀 Key Capabilities
- **Risk Visualization:** Instantly see High/Medium/Low risk areas based on detection maturity.
- **MITRE ATT&CK Mapping:** Identify logs that aren't mapped to specific TTPs.
- **STRIDE Analysis:** Assess coverage across Spoofing, Tampering, Repudiation, etc.
- **Retention Auditing:** Flag log sources that don't meet retention policies.

### Prerequisites
- Python 3.9+
- `pip`

### Installation

**Clone the repository**
   ```bash
   git clone https://github.com/sivaram21cyber/log-gap-analyzer.git
   cd log-gap-analyzer

**Set up a virtual environment:**
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

**Install dependencies**
pip install -r requirements.txt

**Run the application**
python web/app.py

**Access the Dashboard **
Open your browser and navigate to: http://127.0.0.1:5000

**How to Use**
**1. Prepare Your Data**
The tool works by analyzing an Excel log audit file. A sample is provided in data/Log_Gap_Analyzer_Sample_Audit.xlsx.

Tip: Keep the column headers from the sample file but populate the rows with your own log sources (e.g., Firewall, EDR, AD Logs).
**2. Upload & Analyze**
Go to the web UI.
Upload your Excel file.
Click "Run Analysis".
**3. Interpret Results**
Risk Summary: Executive-level view of your logging health.
MITRE Gaps: Shows logs that exist but lack clear TTP mapping (often a documentation issue).
Monitoring Weaknesses: Highlights logs with missing detections or poor retention.
Full Analysis: The deep-dive view for auditors and engineers.

🧠 Concepts
What is a "MITRE Gap"?
In this tool, a MITRE Gap doesn't necessarily mean you are vulnerable. It means:

"We have logs/alerts here, but we haven't explicitly mapped them to an attacker technique."

This is often a documentation or maturity gap rather than a technology failure.

Why STRIDE?
While MITRE covers attacks, STRIDE covers threats to the system model. This tool ensures you aren't just looking for hackers (MITRE) but also fundamental security failures (STRIDE), like unlogged administrative access (Elevation of Privilege).

🤝** Contributing**
We love contributions! Whether it's fixing a bug, adding a new chart, or improving the UI.

Fork the project.
Create your feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a Pull Request.
📂 **Project Structure:**
├── data/          # Sample input files for testing
├── output/        # Generated analysis reports (Excel exports)
├── src/           # Core analysis logic (Pandas/Python)
├── web/           # Flask application (Routes & UI)
│   ├── static/    # CSS/JS assets
│   └── templates/ # HTML templates
├── requirements.txt
└── README.md

👤** Author**
Sivaram Ganesan
Domain: Cyber Security / SOC / Detection Engineering
GitHub: @sivaram21cyber
