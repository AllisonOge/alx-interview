#!/usr/bin/python3
"""
Prime game challenge
"""


def isWinner(x, nums):
    """
    Determin the person with the most wins between `Ben` and `Maria`

    :params x: number of rounds
    :type x: int
    :params nums: list of n
    :type nums: list
    """
    players = ['Maria', 'Ben']
    num_wins = [0, 0]

    for n in nums:
        # condition for ending game
        p = 2  # 2 is a prime number
        li = list(xrange(2, n))
        count = 1
        while p*p <= n:
            # remove all multiples
            for i in xrange(p*2, n, p):
                li[i - 2] = 0
            # print("->", li)
            p += 1

            # ensure p is only a prime number (is in the list)
            while p not in li:
                p += 1

            # one turn complete
            count += 1
        num_wins[count % 2] += 1

    idx = num_wins.index(max(num_wins))
    return players[idx]
