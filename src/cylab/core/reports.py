"""
CYLAB Reports
"""

import json
from datetime import datetime
from pathlib import Path

REPORTS_DIR = Path.home() / ".cylab" / "reports"


def build_report(checks):
    return {
        "timestamp": datetime.now().isoformat(),
        "checks": checks,
        "passed": sum(1 for c in checks if c["passed"]),
        "total": len(checks),
    }


def save_report(report):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = REPORTS_DIR / f"report_{stamp}.json"
    path.write_text(json.dumps(report, indent=2))
    return path


def list_reports():
    if not REPORTS_DIR.exists():
        return []
    return sorted(REPORTS_DIR.glob("report_*.json"))


def load_latest_report():
    import json
    reports = list_reports()
    if not reports:
        return {}
    with open(reports[-1]) as f:
        return json.load(f)
