"""
CYLAB Trivy Command
"""

from cylab.core.trivy import trivy_available, scan_image


def run(args):
    if not trivy_available():
        print("Trivy is not installed.")
        print("Run: cylab install trivy")
        return

    if not args.image:
        print("Usage: cylab trivy <image_name>")
        return

    print(f"Scanning Docker image: {args.image}...")
    print("This may take a while (downloading vulnerability database on first run).\n")

    output = scan_image(args.image)

    if output == "TIMEOUT":
        print("Trivy scan timed out.")
        return

    if output is None:
        print("Trivy scan failed.")
        return

    print(output)
