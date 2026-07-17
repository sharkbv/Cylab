"""
CYLAB Profile Command
"""

from cylab.core.profiles import (
    list_profiles,
    create_profile,
    load_profile,
    get_active_profile,
    set_active_profile,
    profile_exists,
)


def run(args) -> None:
    action = args.profile_action

    if action == "list":
        profiles = list_profiles()
        active = get_active_profile()
        if not profiles:
            print("No profiles found. Create one with: cylab profile create <name>")
            return
        print("Available profiles:")
        for p in profiles:
            marker = " (active)" if p == active else ""
            print(f"  - {p}{marker}")

    elif action == "create":
        if not args.name:
            print("Usage: cylab profile create <name>")
            return
        description = args.description or ""
        created = create_profile(args.name, description)
        if created:
            print(f"Profile '{args.name}' created.")
        else:
            print(f"Profile '{args.name}' already exists.")

    elif action == "use":
        if not args.name:
            print("Usage: cylab profile use <name>")
            return
        if not profile_exists(args.name):
            print(f"Profile '{args.name}' does not exist.")
            print("Create it first with: cylab profile create <name>")
            return
        set_active_profile(args.name)
        print(f"Active profile set to '{args.name}'.")

    elif action == "show":
        active = get_active_profile()
        data = load_profile(active)
        print(f"Active profile: {active}")
        if data:
            for key, value in data.items():
                print(f"  {key} = {value}")
        else:
            print("  (no data found, profile file may be missing)")

    else:
        print("Usage: cylab profile [list|create <name>|use <name>|show]")
