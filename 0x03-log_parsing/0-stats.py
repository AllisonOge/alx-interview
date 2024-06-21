#!/usr/bin/python3
"""l0-stats.py"""

import sys
import signal

valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
store = {"size": 0, "count": 0,
         "status_codes": {int(k): 0 for k in valid_status_codes}}


def print_stats():
    """Print the accumulated statistics"""
    print(f"File size: {store['size']}")
    for code in sorted(store['status_codes'].keys()):
        print(f"{code}: {store['status_codes'][code]}")


def main():
    """main"""
    for cmdline in sys.stdin:
        ip, cmdline_ = cmdline.split("-", 1)
        cmdline = cmdline_.strip()
        date, cmdline_ = cmdline.split("]", 1)
        date = date.replace("[", "")
        cmdline = cmdline_.strip()
        url, cmdline_ = cmdline.split("\"", 2)[1:]
        cmdline = cmdline_.strip()
        status_code, file_size = list(map(int, cmdline.split()))

        store["size"] += int(file_size)
        store["status_codes"][status_code] += 1
        store["count"] += 1

        if store["count"] % 10 == 0:
            print_stats()

    # Define a function to handle keyboard interruption
    def signal_handler(sig=None, frame=None):
        """keyboard interupt signal handler"""
        print_stats()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    main()
