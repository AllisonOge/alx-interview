#!/usr/bin/python3
"""l0-stats.py"""

import sys
import signal
import re

valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
store = {"size": 0, "count": 0,
         "status_codes": {k: 0 for k in valid_status_codes}}
line_regex = re.compile(
    r'^(\S+)\s*-\s*\[(.*?)\]\s*"(GET /projects/260 HTTP/1.1)"'
    + r'\s*([\d,\w]+)\s*([\d,\w]+)$')


def print_stats():
    """Print the accumulated statistics"""
    print(f"File size: {store['size']}")
    for code in sorted(store['status_codes'].keys()):
        if store["status_codes"][code] > 0:
            print(f"{code}: {store['status_codes'][code]}")


def process_line(cmdline):
    """Process each line and update store"""
    match = line_regex.match(cmdline)
    if not match:
        return
    ip, date, request, status_code, file_size = match.groups()
    if not file_size.isdigit():
        return
    file_size = int(file_size)
    store["size"] += file_size

    if not status_code.isdigit():
        return
    status_code = int(status_code)
    if status_code not in valid_status_codes:
        return
    store["status_codes"][status_code] += 1

    store["count"] += 1


def main():
    """main"""
    # Define a function to handle keyboard interruption
    def signal_handler(sig=None, frame=None):
        """keyboard interupt signal handler"""
        print_stats()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    for cmdline in sys.stdin:
        process_line(cmdline)

        if store["count"] % 10 == 0:
            print_stats()

    print_stats()


if __name__ == "__main__":
    main()
