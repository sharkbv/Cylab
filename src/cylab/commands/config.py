"""
CYLAB Config Command
"""

from cylab.core.config import load_config, save_config, get_config_path


def run(args) -> None:
    if args.config_action == "show":
        config = load_config()
        print(f"Config file: {get_config_path()}")
        for key, value in config.items():
            print(f"  {key} = {value}")
    elif args.config_action == "set":
        config = load_config()
        config[args.key] = args.value
        save_config(config)
        print(f"Set {args.key} = {args.value}")
    else:
        print("Usage: cylab config [show|set <key> <value>]")
