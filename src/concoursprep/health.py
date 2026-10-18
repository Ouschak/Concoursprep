import sys
import argparse
from importlib.metadata import version


def health_status() -> str:
    return "ConcoursPrep health: OK- dev"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version",action="version",version="ConcoursPrep " + version("concoursprep"))
    parser.add_argument("health",choices=["health"])



    args = parser.parse_args()

    if args.health=="health":
        print(health_status())

    return 0




if __name__ == "__main__":
    sys.exit(main())