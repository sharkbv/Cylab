"""
CYLAB Scan Command
"""

from cylab.core.scanner import nmap_available, run_scan
from cylab.core.advisor import save_scan_output


def run(args):
    if not nmap_available():
        print("Nmap is not installed.")
        print("Run: cylab install nmap")
        return

    if not args.target:
        print("Usage: cylab scan <target> [--profile quick|full]")
        return

    profile = args.profile or "quick"
    print(f"Scanning {args.target} (profile: {profile})...")
    print("This may take a while depending on the target and profile.\n")

    output = run_scan(args.target, profile)

    if output == "TIMEOUT":
        print("Scan timed out. Try the 'quick' profile or a smaller target.")
        return

    if output is None:
        print("Scan failed. Check the target and your permissions.")
        return

    save_scan_output("nmap", output)
    print(output)
