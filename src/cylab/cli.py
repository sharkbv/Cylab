import argparse

from cylab.version import __version__
from cylab.core.logger import get_logger
from cylab.commands import doctor
from cylab.commands import config as config_cmd
from cylab.commands import install as install_cmd
from cylab.commands import profile as profile_cmd
from cylab.commands import report as report_cmd


def main():
    parser = argparse.ArgumentParser(prog="cylab", description="Cyber AI Laboratory")
    parser.add_argument("--version", action="version", version=f"CYLAB {__version__}")

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("doctor", help="Diagnose your CYLAB environment")

    config_parser = subparsers.add_parser("config", help="Manage configuration")
    config_sub = config_parser.add_subparsers(dest="config_action")
    config_sub.add_parser("show", help="Show current configuration")
    set_p = config_sub.add_parser("set", help="Set a configuration value")
    set_p.add_argument("key")
    set_p.add_argument("value")

    install_p = subparsers.add_parser("install", help="Install a required tool")
    install_p.add_argument("target", nargs="?", default=None)

    profile_parser = subparsers.add_parser("profile", help="Manage profiles")
    profile_sub = profile_parser.add_subparsers(dest="profile_action")
    profile_sub.add_parser("list", help="List all profiles")
    profile_sub.add_parser("show", help="Show the active profile")
    create_p = profile_sub.add_parser("create", help="Create a new profile")
    create_p.add_argument("name")
    create_p.add_argument("--description", default="")
    use_p = profile_sub.add_parser("use", help="Switch to a profile")
    use_p.add_argument("name")

    report_parser = subparsers.add_parser("report", help="Generate or list reports")
    report_sub = report_parser.add_subparsers(dest="report_action")
    report_sub.add_parser("generate", help="Generate a new report")
    report_sub.add_parser("list", help="List saved reports")

    args = parser.parse_args()

    logger = get_logger()
    logger.info("CYLAB started")

    if args.command == "doctor":
        doctor.run(args)
    elif args.command == "config":
        config_cmd.run(args)
    elif args.command == "install":
        install_cmd.run(args)
    elif args.command == "profile":
        profile_cmd.run(args)
    elif args.command == "report":
        report_cmd.run(args)
    else:
        print("Welcome to CYLAB")
        print("Run 'cylab --help' to see available commands")


if __name__ == "__main__":
    main()
