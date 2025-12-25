# 🔍 Log Gap Analyzer Dashboard

A **Flask-based security analytics web application** that performs
**log audit and gap analysis** using **MITRE ATT&CK** and **STRIDE** frameworks.

This tool helps SOC teams understand:
- What logs are collected
- What attacker behaviors are covered
- Where detection and monitoring gaps exist

---

## 🚀 Features
- Upload log audit Excel file
- Color-coded **risk summary**
- **MITRE ATT&CK gap identification**
- **STRIDE coverage analysis**
- Monitoring weaknesses detection
- Full log analysis dashboard
- Optional Excel export

---

## 🧠 Why this project?
Many organizations collect logs and alerts but:
- Cannot explain which attacker TTPs are covered
- Lack visibility into detection blind spots
- Fail audits due to unclear logging coverage

This project solves that problem.

---

## 🛠 Tech Stack
- Python
- Pandas
- Flask
- HTML / Jinja2
- MITRE ATT&CK
- STRIDE Threat Model

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python web/app.py
