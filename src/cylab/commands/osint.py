"""
CYLAB OSINT Command
"""

from cylab.core.osint import (
    theharvester_available,
    spiderfoot_available,
    run_theharvester,
    run_spiderfoot,
)
from cylab.core.advisor import save_scan_output


def run(args):
    if not args.domain:
        print("Usage: cylab osint <domain> [--tool harvester|spiderfoot|both]")
        return

    tool = args.tool or "both"

    if tool in ("harvester", "both"):
        if not theharvester_available():
            print("theHarvester is not installed.")
            print("Run: cylab install theharvester")
        else:
            print(f"Running theHarvester against {args.domain}...\n")
            output = run_theharvester(args.domain)
            if output == "TIMEOUT":
                print("theHarvester timed out.")
            elif output is None:
                print("theHarvester failed.")
            else:
                save_scan_output("osint", output)
                print(output)

    if tool in ("spiderfoot", "both"):
        if not spiderfoot_available():
            print("SpiderFoot is not installed.")
            print("Run: cylab install spiderfoot")
        else:
            print(f"\nRunning SpiderFoot against {args.domain}...\n")
            output = run_spiderfoot(args.domain)
            if output == "TIMEOUT":
                print("SpiderFoot timed out.")
            elif output is None:
                print("SpiderFoot failed.")
            else:
                save_scan_output("spiderfoot", output)
                print(output)
