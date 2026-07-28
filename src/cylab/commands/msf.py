"""
CYLAB Metasploit Command
"""

from cylab.core.metasploit import msf_available, search_modules


def run(args):
    if not msf_available():
        print("Metasploit is not installed.")
        print("Run: cylab install metasploit")
        return

    if not args.query:
        print("Usage: cylab msf search <query>")
        return

    print(f"Searching Metasploit modules for: {args.query}")
    print("This may take a moment (msfconsole startup is slow).\n")

    output = search_modules(args.query)

    if output == "TIMEOUT":
        print("Search timed out.")
        return

    if output is None:
        print("Search failed.")
        return

    print(output)
