"""
CYLAB Plugin Command
"""

from cylab.core.plugins import discover_plugins, run_plugin, PLUGINS_DIR


def run(args):
    action = args.plugin_action

    if action == "list":
        plugins = discover_plugins()
        if not plugins:
            print("No plugins found.")
            print(f"Add .py files to: {PLUGINS_DIR}")
            return
        print("Available plugins:")
        for name in sorted(plugins.keys()):
            print(f"  - {name}")

    elif action == "run":
        if not args.name:
            print("Usage: cylab plugin run <name>")
            return
        ok = run_plugin(args.name, args)
        if not ok:
            print(f"Plugin '{args.name}' not found or invalid.")
            print("A plugin must be a .py file with a run(args) function.")

    else:
        print("Usage: cylab plugin [list|run <name>]")
