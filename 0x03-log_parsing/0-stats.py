#!/usr/bin/python3
"""l0-stats.py"""

import sys
import signal

valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
store = {"size": 0, "count": 0,
         "status_codes": {k: 0 for k in valid_status_codes}}


def print_stats():
    """Print the accumulated statistics"""
    print(f"File size: {store['size']}")
    for code in sorted(store['status_codes'].keys()):
        if store["status_codes"][code] > 0:
            print(f"{code}: {store['status_codes'][code]}")


def process_line(cmdline):
    """Process each line and update store"""
    parts = cmdline.split()
    if len(parts) != 9:
        return
    ip, dash, year, time, method, url, protocol, status_code, file_size = parts
    if not status_code.isdigit() or not file_size.isdigit():
        return
    status_code, file_size = list(map(int, [status_code, file_size]))
    if status_code not in valid_status_codes:
        return

    store["size"] += file_size
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
