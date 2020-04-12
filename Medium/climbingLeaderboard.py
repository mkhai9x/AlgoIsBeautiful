'''
Alice is playing an arcade game and wants to climb to the top of the leaderboard and 
wants to track her ranking. The game uses Dense Ranking, so its leaderboard works like this:

    The player with the highest score is ranked number 1 on the leaderboard.

    Players who have equal scores receive the same ranking number, 
    and the next player(s) receive the immediately following ranking number.

For example, the four players on the leaderboard have high scores of 100, 90, 90 and 80. 
Those players will have ranks 1, 2, 2, and 3, respectively. 
If Alice's scores are 70, 80 and 105, her rankings after each game are 4th, 3rd and 1st.
'''


import math
import os
import random
import re
import sys
import bisect


def binary_search(scores, target):
    # We treat the scores in descending order
    low = 0
    high = len(scores) - 1
    index = 0
    while low <= high:
        mid = int(low + (high - low)/2)
        if scores[mid] <= target:
            index = mid
            high = mid - 1
        else:
            low = mid + 1
    return index + 1


def climbingLeaderboard(scores, alice):
    ranks = []
    # simplify the scores to get rid all the duplicate elements
    # add extra -1 for the case the target in binary search is the smallest in scores
    scores = sorted(list(set(scores)), reverse=True) + [-1]

    # print(scores)
    for i in range(len(alice)):
        ranks.append(binary_search(scores, alice[i]))
    return ranks


if __name__ == "__main__":
    scores = [100, 100, 50, 40, 40, 20, 10]
    alice = [5, 25, 50, 120]
    assert climbingLeaderboard(scores, alice) == [6, 4, 2, 1]
    scores = [100, 90, 90, 80, 75, 60]
    alice = [50, 65, 77, 90, 102]
    assert climbingLeaderboard(scores, alice) == [6, 5, 4, 2, 1]
