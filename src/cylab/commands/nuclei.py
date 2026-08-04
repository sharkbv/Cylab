"""
CYLAB Nuclei Command
"""

from cylab.core.nuclei import nuclei_available, run_nuclei
from cylab.core.advisor import save_scan_output


def run(args):
    if not nuclei_available():
        print("Nuclei is not installed.")
        print("Run: cylab install nuclei")
        return

    if not args.target:
        print("Usage: cylab nuclei <target>")
        return

    print(f"Running Nuclei against {args.target}...")
    print("This may take a while (updating templates on first run).\n")

    output = run_nuclei(args.target)

    if output == "TIMEOUT":
        print("Nuclei scan timed out.")
        return

    if output is None:
        print("Nuclei scan failed.")
        return

    save_scan_output("nuclei", output)
    print(output if output.strip() else "No findings reported by Nuclei.")
