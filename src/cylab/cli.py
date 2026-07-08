import argparse

from cylab.version import __version__
from cylab.core.logger import get_logger


def main():
    parser = argparse.ArgumentParser(
        prog="cylab",
        description="Cyber AI Laboratory"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"CYLAB {__version__}"
    )

    args = parser.parse_args()

    logger = get_logger()
    logger.info("CYLAB started")


if __name__ == "__main__":
    main()
