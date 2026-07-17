"""
CYLAB Install Command
"""

from cylab.core.installer import install, INSTALLERS


def run(args) -> None:
    if not args.target:
        print("Usage: cylab install <target>")
        print(f"Available targets: {', '.join(INSTALLERS.keys())}")
        return

    install(args.target)
