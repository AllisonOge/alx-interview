#!/usr/bin/python3
"""l0-stats.py"""


def main(cmdline, store={"size": 0, "count": 0}):
    """process args in command line and update store"""
    # process args in command line
    ip, cmdline_ = cmdline.split("-", 1)
    cmdline = cmdline_.strip()
    date, cmdline_ = cmdline.split("]", 1)
    date = date.replace("[", "")
    cmdline = cmdline_.strip()
    url, cmdline_ = cmdline.split("\"", 2)[1:]
    cmdline = cmdline_.strip()
    status_code, file_size = list(map(int, cmdline.split()))

    # update store
    new_file_size = store.get("size") + file_size
    new_count = store.get("count") + 1
    new_status_count = store.get(str(status_code), 0) + 1
    store.update({"size": new_file_size,
                 "count": new_count,
                  str(status_code): new_status_count})


if __name__ == "__main__":
    store = {"size": 0, "count": 0}
    cmdline = input()
    try:
        while cmdline:
            main(cmdline, store)

            if store.get("count") % 10 == 0:
                size = store.get("size", 0)
                count = store.get("count", 0)
                print(f"File size: {size}")
                for k, v in sorted(store.items()):
                    if k not in ["size", "count"]:
                        print(f"{k}: {v}")
                # reset store
                store = {"size": size, "count": count}

            cmdline = input()
    except KeyboardInterrupt as e:
        pass
