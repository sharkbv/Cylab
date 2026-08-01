"""
CYLAB Fuzz Command
"""

from cylab.core.fuzzer import ffuf_available, run_ffuf
from cylab.core.advisor import save_scan_output


def run(args):
    if not ffuf_available():
        print("ffuf is not installed.")
        print("Run: cylab install ffuf")
        return

    if not args.target:
        print("Usage: cylab fuzz <url>")
        return

    print(f"Fuzzing {args.target}...")
    print("This may take a while depending on the wordlist size.\n")

    output = run_ffuf(args.target)

    if output == "TIMEOUT":
        print("Fuzzing timed out.")
        return

    if output is None:
        print("Fuzzing failed.")
        return

    save_scan_output("ffuf", output)
    print(output)
