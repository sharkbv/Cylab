"""
CYLAB MCP Command
"""

from cylab.core.mcp import load_servers, add_server, remove_server


def run(args):
    action = args.mcp_action

    if action == "list":
        servers = load_servers()
        if not servers:
            print("No MCP servers configured.")
            print("Add one with: cylab mcp add <name> <command> [args...]")
            return
        print("Configured MCP servers:")
        for name, info in servers.items():
            cmd = info.get("command", "")
            cmd_args = " ".join(info.get("args", []))
            print(f"  - {name}: {cmd} {cmd_args}")

    elif action == "add":
        if not args.name or not args.mcp_command:
            print("Usage: cylab mcp add <name> <command> [args...]")
            return
        add_server(args.name, args.mcp_command, args.mcp_args or [])
        print(f"MCP server '{args.name}' added.")

    elif action == "remove":
        if not args.name:
            print("Usage: cylab mcp remove <name>")
            return
        ok = remove_server(args.name)
        if ok:
            print(f"MCP server '{args.name}' removed.")
        else:
            print(f"MCP server '{args.name}' not found.")

    else:
        print("Usage: cylab mcp [list|add <name> <command>|remove <name>]")
