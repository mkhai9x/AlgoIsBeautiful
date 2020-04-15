'''
You have N bulbs in a row numbered from 1 to N. Initially, all the bulbs are turned off. 
We turn on exactly one bulb everyday until all bulbs are on after N days.

You are given an array bulbs of length N where bulbs[i] = x means that on the (i+1)th day, 
we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.

Given an integer K, find out the minimum day number such that there exists two turned on 
bulbs that have exactly K bulbs between them that are all turned off.

If there isn't such day, return -1.
'''
import heapq
import bisect


def kEmptySlots(bulbs, K):
    positions = [bulbs[0]]
    heapq.heapify(positions)
    i = 1
    while i < len(bulbs):
        target = bulbs[i]
        index = bisect.bisect_left(positions, target)
        if index == 0:
            if abs(target - positions[index]) - 1 == K:
                return i + 1
        elif index == len(positions):
            if abs(target - positions[index-1]) - 1 == K:
                return i + 1
        else:
            print(target)
            print(positions)
            print(index)
            if abs(target - positions[index]) - 1 == K:
                return i + 1
            if abs(target - positions[index-1]) - 1 == K:
                return i + 1
        heapq.heappush(positions, target)
        i += 1
    return -1


# print(kEmptySlots([1, 3, 2], 1))

# print(kEmptySlots([1, 2, 3], 1))

# print(kEmptySlots([8, 5, 6, 2, 4, 10, 9, 1, 7, 3], 5))

print(kEmptySlots([3, 9, 2, 8, 1, 6, 10, 5, 4, 7], 1))
