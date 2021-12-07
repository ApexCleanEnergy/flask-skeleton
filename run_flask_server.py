"""
This script runs the ApyxEngine application using a development server.
"""

from os import chdir, path, environ
from Skeleton import app


def parseInputParameters():
    import argparse

    # Create the parser
    parser = argparse.ArgumentParser(
        description="Run flask application in browser",
        epilog="Enjoy the program! :)",
    )

    # Add as many arguments as necessary
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Debug mode flag (just call this variable to run in debug mode)",
    )
    # Parse args
    args = parser.parse_args()

    return args


if __name__ == "__main__":

    chdir(path.dirname(path.realpath(__file__)))

    args = parseInputParameters()

    HOST = environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(environ.get("SERVER_PORT", "6969"))
    except ValueError:
        PORT = 6969
    app.run(HOST, PORT, debug=args.debug)
