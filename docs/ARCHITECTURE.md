# CYLAB Architecture

## Goal
Unified CLI for managing an AI-powered cybersecurity lab.

## Rules
- Python only, no Bash except via subprocess.
- No abstraction until needed twice in practice.
- cli.py only wires argparse to command modules.
- One command = one file in commands/.
- System changes (sudo) always require user confirmation.

## Layout
src/cylab/core/     - shared logic (logger, config, profiles, installer)
src/cylab/commands/ - one file per subcommand

## Data
~/.cylab/config.toml
~/.cylab/logs/cylab.log
~/.cylab/profiles/<name>.toml
~/.cylab/active_profile

## Roadmap
v1.0: CLI, Doctor, Config, Installer, Profiles, Reports
v2.0: GUI, AI Agents, MCP, Burp/Nmap automation
