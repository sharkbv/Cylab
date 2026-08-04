"""
CYLAB Assess Command
"""

from cylab.core.pipeline import run_assessment


def run(args):
    if not args.target:
        print("Usage: cylab assess <target> [--web-url http://target]")
        return

    print(run_assessment(args.target, web_url=args.web_url))
