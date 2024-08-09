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
    players = ['Ben', 'Maria']
    num_wins = [0, 0]

    for n in nums:
        # condition for ending game
        p = 2  # 2 is a prime number
        li = list(range(2, n+1))
        while p*p <= n:
            # remove all multiples
            for i in range(p*2, n+1, p):
                li[i-2] = 0
            p += 1

            # ensure p is only a prime number (is in the list)
            while p not in li:
                p += 1

        # print("End of game->", li, n)
        num_wins[len([i for i in li if i != 0]) % 2] += 1
        # print(num_wins)

    idx = num_wins.index(max(num_wins))
    return players[idx]
