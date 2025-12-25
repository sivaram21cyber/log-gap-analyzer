**Project:**
  Name: Log Gap Analyzer Dashboard
  Description: >
    A Flask-based security analytics web application that performs
    log audit and gap analysis using MITRE ATT&CK and STRIDE frameworks.
    It helps SOC teams understand detection coverage and identify monitoring gaps.

**Author:**
  name: Sivaram Ganesan
  domain: Cyber Security / SOC / Detection Engineering

**Tech_stack:**
  backend:
    - Python
    - Pandas
    - Flask
  frontend:
    - HTML
    - Jinja2
  frameworks:
    - MITRE ATT&CK
    - STRIDE

**Project_structure:**
  src: Core log gap analysis engine (business logic)
  web: Flask web application (routes and UI)
  data: Sample input Excel file for testing
  output: Generated analysis results (optional export)

**Purpose:**
  log_audit: >
    Validate whether collected logs are available, useful,
    retained properly, and support detection and investigation.
  mitre_gap_analysis: >
    Identify logs and detections that are not mapped to
    MITRE ATT&CK attacker techniques.
  stride_analysis: >
    Assess coverage across STRIDE threat model categories
    such as Spoofing, Tampering, and Elevation of Privilege.

**Why_this_tool_exists:**
  problem:
    - Logs are collected but not evaluated
    - Alerts exist but attacker behavior is unclear
    - Organizations cannot explain detection coverage
  solution:
    - Visual dashboard showing risk, gaps, and weaknesses
    - Clear mapping to MITRE and STRIDE
    - Actionable insights for SOC teams

**Dashboard_sections:**
  Risk_summary
    description: >
      Color-coded High / Medium / Low risk summary
      based on detection status, STRIDE coverage, and retention.
  Mitre_gaps:
    description: >
      Logs that are not mapped to any MITRE ATT&CK techniques.
      Indicates lack of clarity, not lack of detections.
  Monitoring_weaknesses:
    description: >
      Logs with missing or partial detections
      or insufficient retention period.
  Full_analysis:
    description: >
      Complete log audit view including availability,
      collection method, detection utility,
      STRIDE coverage, MITRE coverage, and risk level.

**Mitre_gap_definition:**
  meaning: >
    MITRE gap occurs when logs, rules, or alerts exist,
    but the organization is unsure which attacker TTPs they cover.
  does_not_mean:
    - Tools are broken
    - Logs are useless
    - Security failure
  actually_means:
    - Missing documentation
    - Missing mapping
    - Detection maturity gap

**How_to_use:**
  **Prerequisites:**
    - Python 3.9 or higher
    - pip package manager
  **install_dependencies:**
    command: pip install -r requirements.txt
    
  start_application:
    command: python web/app.py
    expected_output: Running on http://127.0.0.1:5000
  access_ui:
    url: http://127.0.0.1:5000
  upload_process:
    steps:
      - Open web UI
      - Upload Excel log audit file
      - Click "Run Analysis"
  results_displayed:
    - Risk summary cards
    - MITRE ATT&CK gaps table
    - Monitoring weaknesses table
    - Full analysis table
  optional_output:
    file: output/Log_Gap_Analysis_Result.xlsx
    usage:
      - Audit evidence
      - Offline review
      - Management reporting

**sample_input:**
  file_path: data/Log_Gap_Analyzer_Sample_Audit.xlsx
  purpose: Quick testing and demo

**benefits:**
  - Improves SOC visibility
  - Highlights detection blind spots
  - Supports audits and compliance
  - Reduces false sense of security


