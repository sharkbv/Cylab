"""
CYLAB Web Scan Command
"""

from cylab.core.webscan import (
    nikto_available,
    gobuster_available,
    run_nikto,
    run_gobuster,
)
from cylab.core.advisor import save_scan_output


def run(args):
    if not args.target:
        print("Usage: cylab webscan <target> [--tool nikto|gobuster|both]")
        return

    tool = args.tool or "both"

    if tool in ("nikto", "both"):
        if not nikto_available():
            print("Nikto is not installed.")
            print("Run: cylab install nikto")
        else:
            print(f"Running Nikto against {args.target}...\n")
            output = run_nikto(args.target)
            if output == "TIMEOUT":
                print("Nikto scan timed out.")
            elif output is None:
                print("Nikto scan failed.")
            else:
                save_scan_output("nikto", output)
                print(output)

    if tool in ("gobuster", "both"):
        if not gobuster_available():
            print("Gobuster is not installed.")
            print("Run: cylab install gobuster")
        else:
            print(f"\nRunning Gobuster against {args.target}...\n")
            output = run_gobuster(args.target)
            if output == "TIMEOUT":
                print("Gobuster scan timed out.")
            elif output is None:
                print("Gobuster scan failed.")
            else:
                save_scan_output("gobuster", output)
                print(output)
