'''
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.
Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example:
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.
uppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
'''
'''
In this problem, we use heap to solve our problem
'''




import heapq
def lastStoneWeight(stones):
    stones = [-var for var in stones]
    # the function heapify implement the heap in place
    heapq.heapify(stones)
    while len(stones) > 1:
        # get two largest stones
        stone_one = heapq.heappop(stones)
        stone_two = heapq.heappop(stones)
        if stone_one != stone_two:
            heapq.heappush(stones, -abs(stone_one-stone_two))
        # we dont nead to push to the heap if stone_one == stone_two
    if len(stones) == 0:
        return 0
    return -stones[0]


if __name__ == "__main__":
    assert lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
