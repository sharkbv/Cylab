import argparse
import sys

from cylab.version import __version__
from cylab.core.logger import get_logger
from cylab.commands import doctor
from cylab.commands import config as config_cmd
from cylab.commands import install as install_cmd
from cylab.commands import profile as profile_cmd
from cylab.commands import report as report_cmd
from cylab.commands import models as models_cmd
from cylab.commands import agent as agent_cmd
from cylab.commands import plugin as plugin_cmd
from cylab.commands import mcp as mcp_cmd
from cylab.commands import scan as scan_cmd
from cylab.commands import webscan as webscan_cmd
from cylab.commands import exploit as exploit_cmd
from cylab.commands import msf as msf_cmd
from cylab.commands import sqlmap as sqlmap_cmd
from cylab.commands import pwaudit as pwaudit_cmd
from cylab.commands import trivy as trivy_cmd
from cylab.commands import osint as osint_cmd
from cylab.commands import assess as assess_cmd
from cylab.commands import fuzz as fuzz_cmd
from cylab.commands import nuclei as nuclei_cmd


def build_parser():
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

    models_parser = subparsers.add_parser("models", help="Manage AI models via Ollama")
    models_sub = models_parser.add_subparsers(dest="models_action")
    models_sub.add_parser("list", help="List local models")
    pull_p = models_sub.add_parser("pull", help="Pull a model")
    pull_p.add_argument("name", nargs="?", default=None)
    run_p = models_sub.add_parser("run", help="Run a model interactively")
    run_p.add_argument("name", nargs="?", default=None)

    agent_parser = subparsers.add_parser("agent", help="AI-powered analysis")
    agent_sub = agent_parser.add_subparsers(dest="agent_action")
    analyze_p = agent_sub.add_parser("analyze", help="Analyze latest report with AI")
    analyze_p.add_argument("--model", default=None)
    advise_p = agent_sub.add_parser("advise", help="Suggest next steps based on scan results")
    advise_p.add_argument("--model", default=None)

    plugin_parser = subparsers.add_parser("plugin", help="Manage and run plugins")
    plugin_sub = plugin_parser.add_subparsers(dest="plugin_action")
    plugin_sub.add_parser("list", help="List available plugins")
    plugin_run_p = plugin_sub.add_parser("run", help="Run a plugin")
    plugin_run_p.add_argument("name", nargs="?", default=None)

    mcp_parser = subparsers.add_parser("mcp", help="Manage MCP servers")
    mcp_sub = mcp_parser.add_subparsers(dest="mcp_action")
    mcp_sub.add_parser("list", help="List configured MCP servers")
    mcp_add_p = mcp_sub.add_parser("add", help="Add an MCP server")
    mcp_add_p.add_argument("name", nargs="?", default=None)
    mcp_add_p.add_argument("mcp_command", nargs="?", default=None)
    mcp_add_p.add_argument("mcp_args", nargs="*", default=[])
    mcp_remove_p = mcp_sub.add_parser("remove", help="Remove an MCP server")
    mcp_remove_p.add_argument("name", nargs="?", default=None)

    scan_parser = subparsers.add_parser("scan", help="Run an Nmap scan")
    scan_parser.add_argument("target", nargs="?", default=None)
    scan_parser.add_argument("--profile", default=None, choices=["quick", "full"])

    webscan_parser = subparsers.add_parser("webscan", help="Run Nikto/Gobuster against a web target")
    webscan_parser.add_argument("target", nargs="?", default=None)
    webscan_parser.add_argument("--tool", default=None, choices=["nikto", "gobuster", "both"])

    exploit_parser = subparsers.add_parser("exploit", help="Search known exploits")
    exploit_sub = exploit_parser.add_subparsers(dest="exploit_action")
    search_p = exploit_sub.add_parser("search", help="Search Exploit-DB")
    search_p.add_argument("query", nargs="?", default=None)

    msf_parser = subparsers.add_parser("msf", help="Search Metasploit modules")
    msf_sub = msf_parser.add_subparsers(dest="msf_action")
    msf_search_p = msf_sub.add_parser("search", help="Search Metasploit modules")
    msf_search_p.add_argument("query", nargs="?", default=None)

    sqlmap_parser = subparsers.add_parser("sqlmap", help="Run SQLMap against a target")
    sqlmap_parser.add_argument("target", nargs="?", default=None)

    pwaudit_parser = subparsers.add_parser("pwaudit", help="Password auditing (Hydra/John)")
    pwaudit_sub = pwaudit_parser.add_subparsers(dest="pwaudit_action")

    hydra_p = pwaudit_sub.add_parser("hydra", help="Run Hydra brute-force")
    hydra_p.add_argument("target", nargs="?", default=None)
    hydra_p.add_argument("--service", default=None)
    hydra_p.add_argument("--userlist", default=None)
    hydra_p.add_argument("--passlist", default=None)

    john_p = pwaudit_sub.add_parser("john", help="Run John the Ripper")
    john_p.add_argument("hashfile", nargs="?", default=None)

    trivy_parser = subparsers.add_parser("trivy", help="Scan a Docker image for vulnerabilities")
    trivy_parser.add_argument("image", nargs="?", default=None)

    osint_parser = subparsers.add_parser("osint", help="Gather OSINT info (theHarvester/SpiderFoot)")
    osint_parser.add_argument("domain", nargs="?", default=None)
    osint_parser.add_argument("--tool", default=None, choices=["harvester", "spiderfoot", "both"])

    fuzz_parser = subparsers.add_parser("fuzz", help="Fuzz a web target with ffuf")
    fuzz_parser.add_argument("target", nargs="?", default=None)

    nuclei_parser = subparsers.add_parser("nuclei", help="Run Nuclei template-based scanning")
    nuclei_parser.add_argument("target", nargs="?", default=None)

    assess_parser = subparsers.add_parser("assess", help="Full pipeline: scan + webscan + exploit lookup")
    assess_parser.add_argument("target", nargs="?", default=None)
    assess_parser.add_argument("--web-url", dest="web_url", default=None)

    return parser


def dispatch(args, logger):
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
    elif args.command == "models":
        models_cmd.run(args)
    elif args.command == "agent":
        agent_cmd.run(args)
    elif args.command == "plugin":
        plugin_cmd.run(args)
    elif args.command == "mcp":
        mcp_cmd.run(args)
    elif args.command == "scan":
        scan_cmd.run(args)
    elif args.command == "webscan":
        webscan_cmd.run(args)
    elif args.command == "exploit":
        args.query = getattr(args, "query", None)
        exploit_cmd.run(args)
    elif args.command == "msf":
        args.query = getattr(args, "query", None)
        msf_cmd.run(args)
    elif args.command == "sqlmap":
        sqlmap_cmd.run(args)
    elif args.command == "pwaudit":
        pwaudit_cmd.run(args)
    elif args.command == "trivy":
        trivy_cmd.run(args)
    elif args.command == "osint":
        osint_cmd.run(args)
    elif args.command == "fuzz":
        fuzz_cmd.run(args)
    elif args.command == "nuclei":
        nuclei_cmd.run(args)
    elif args.command == "assess":
        assess_cmd.run(args)
    else:
        print("Welcome to CYLAB")
        print("Run 'cylab --help' to see available commands")


def main():
    parser = build_parser()
    args = parser.parse_args()

    logger = get_logger()
    logger.info("CYLAB started")

    try:
        dispatch(args, logger)
    except KeyboardInterrupt:
        print("\nCancelled by user.")
        sys.exit(130)
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        print(f"Error: required file not found ({e.filename}).")
        sys.exit(1)
    except PermissionError as e:
        logger.error(f"Permission denied: {e}")
        print("Error: permission denied. Try running with appropriate privileges.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Error: {e}")
        print("Run with --help for usage, or check ~/.cylab/logs/cylab.log for details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
