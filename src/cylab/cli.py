import argparse

from cylab.version import __version__
from cylab.core.logger import get_logger
from cylab.commands import doctor
from cylab.commands import config as config_cmd


def main():
    parser = argparse.ArgumentParser(
        prog="cylab",
        description="Cyber AI Laboratory"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"CYLAB {__version__}"
    )

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("doctor", help="Diagnose your CYLAB environment")

    config_parser = subparsers.add_parser("config", help="Manage CYLAB configuration")
    config_sub = config_parser.add_subparsers(dest="config_action")
    config_sub.add_parser("show", help="Show current configuration")
    set_parser = config_sub.add_parser("set", help="Set a configuration value")
    set_parser.add_argument("key")
    set_parser.add_argument("value")

    args = parser.parse_args()

    logger = get_logger()
    logger.info("CYLAB started")

    if args.command == "doctor":
        doctor.run(args)
    elif args.command == "config":
        config_cmd.run(args)
    else:
        print("Welcome to CYLAB")
        print("Run 'cylab --help' to see available commands")


if __name__ == "__main__":
    main()
