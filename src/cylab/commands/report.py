"""
CYLAB Report Command
"""

from cylab.core.doctor_checks import run_checks
from cylab.core.reports import build_report, save_report, list_reports


def run(args):
    action = args.report_action

    if action == "generate":
        checks = run_checks()
        report = build_report(checks)
        path = save_report(report)
        print(f"Report saved: {path}")
        print(f"{report['passed']}/{report['total']} checks passed")

    elif action == "list":
        reports = list_reports()
        if not reports:
            print("No reports found.")
            return
        for r in reports:
            print(f"  - {r.name}")

    else:
        print("Usage: cylab report [generate|list]")
