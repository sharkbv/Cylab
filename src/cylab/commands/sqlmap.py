"""
CYLAB SQLMap Command
"""

from cylab.core.sqlmap import sqlmap_available, run_sqlmap


def run(args):
    if not sqlmap_available():
        print("SQLMap is not installed.")
        print("Run: cylab install sqlmap")
        return

    if not args.target:
        print("Usage: cylab sqlmap <target_url>")
        return

    print(f"Running SQLMap against {args.target}...")
    print("This may take a while depending on the target.\n")

    output = run_sqlmap(args.target)

    if output == "TIMEOUT":
        print("SQLMap scan timed out.")
        return

    if output is None:
        print("SQLMap scan failed.")
        return

    print(output)
