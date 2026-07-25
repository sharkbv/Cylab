"""
CYLAB MCP
Manages a registry of MCP (Model Context Protocol) servers.
"""

import json
from pathlib import Path

MCP_FILE = Path.home() / ".cylab" / "mcp_servers.json"


def load_servers():
    if not MCP_FILE.exists():
        return {}
    with open(MCP_FILE) as f:
        return json.load(f)


def save_servers(servers):
    MCP_FILE.parent.mkdir(parents=True, exist_ok=True)
    MCP_FILE.write_text(json.dumps(servers, indent=2))


def add_server(name, command, args):
    servers = load_servers()
    servers[name] = {"command": command, "args": args}
    save_servers(servers)


def remove_server(name):
    servers = load_servers()
    if name not in servers:
        return False
    del servers[name]
    save_servers(servers)
    return True


def get_server(name):
    servers = load_servers()
    return servers.get(name)
