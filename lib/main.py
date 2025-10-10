# lib/main.py

import argparse
from logger import log_action, search_logs

def main():
    parser = argparse.ArgumentParser(description="User Log Management CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Log subcommand
    log_parser = subparsers.add_parser("log", help="Log a user action")
    log_parser.add_argument("action", type=str, help="The action to log")

    # Search subcommand
    search_parser = subparsers.add_parser("search", help="Search log file")
    search_parser.add_argument("keyword", type=str, help="Keyword to search in logs")

    args = parser.parse_args()

    if args.command == "log":
        log_action(args.action)
    elif args.command == "search":
        search_logs(args.keyword)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
