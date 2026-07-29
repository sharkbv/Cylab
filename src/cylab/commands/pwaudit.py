"""
CYLAB Password Audit Command
"""

from cylab.core.pwaudit import (
    hydra_available,
    john_available,
    hashcat_available,
    run_hydra,
    run_john,
)


def run(args):
    action = args.pwaudit_action

    if action == "hydra":
        if not hydra_available():
            print("Hydra is not installed.")
            print("Run: cylab install hydra")
            return
        if not all([args.target, args.service, args.userlist, args.passlist]):
            print("Usage: cylab pwaudit hydra <target> --service <svc> --userlist <file> --passlist <file>")
            return
        print(f"Running Hydra against {args.target} ({args.service})...\n")
        output = run_hydra(args.target, args.service, args.userlist, args.passlist)
        if output == "TIMEOUT":
            print("Hydra timed out.")
        elif output is None:
            print("Hydra failed.")
        else:
            print(output)

    elif action == "john":
        if not john_available():
            print("John the Ripper is not installed.")
            print("Run: cylab install john")
            return
        if not args.hashfile:
            print("Usage: cylab pwaudit john <hashfile>")
            return
        print(f"Running John the Ripper on {args.hashfile}...\n")
        output = run_john(args.hashfile)
        if output == "TIMEOUT":
            print("John timed out.")
        elif output is None:
            print("John failed.")
        else:
            print(output)

    else:
        print("Usage: cylab pwaudit [hydra|john] ...")
