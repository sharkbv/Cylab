"""
CYLAB Doctor Command
"""

from cylab.core.doctor_checks import run_checks


def run(args):
    print("Running CYLAB Doctor...\n")

    checks = run_checks()

    for c in checks:
        status = "OK  " if c["passed"] else "FAIL"
        print(f"[{status}] {c['name']}")
        if not c["passed"] and c["hint"]:
            print(f"       Fix: {c['hint']}")

    passed = sum(1 for c in checks if c["passed"])
    total = len(checks)
    print(f"\n{passed}/{total} checks passed")
