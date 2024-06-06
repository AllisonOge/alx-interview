#!/usr/bin/python3
"""
Module that creates the function that determines if all
the boxes can be opened given n number of locked boxes
containing keys to other boxes
"""


def canUnlockAll(boxes):
    """
    params:
      boxes: list of lists

    returns:
      True if all boxes can be opened, else False

    examples:
    >> boxes = [[1], [2], [3], [4], []]
    >> canUnlockAll(boxes) # True
    >>
    >> boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    >> canUnlockAll(boxes) # True
    >>
    >> boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    >> canUnlockAll(boxes) # False
    """
    # first box (boxes[0]) is unlocked
    # assume all keys are positive integers that match
    # the number as the box it opens.

    hash_map = {k: v for k, v in enumerate(boxes)}
    if len(hash_map) == 0:
        return False
    stack = hash_map.get(0)  # open first box
    del hash_map[0]
    while len(hash_map) > 0:
        if len(stack) == 0:
            return False  # couldn't open all boxes
        key = stack.pop()
        keys = hash_map.get(key)
        if keys is None:  # box has been visited or does not exist
            continue
        if not keys:  # box is empty
            if len(stack) == 0:
                return len(hash_map) == 1
        stack.extend(keys)  # stack the keys
        del hash_map[key]  # trash the box
    return True  # opened all boxes
