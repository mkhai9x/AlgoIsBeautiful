'''
Given an array of positive integers representing coin denominations and a single non-negative integer n
representing a target amount of money, write a function that returns the number of ways
to make change for that target amount using given coin denominations.
'''


def numberOfWaysToMakeChange(n, denoms):
    # creat an array with index from 0 to n, represeting each amount of money from 0 to n
    # each index present number of ways to make change for that index amount of money.
    # Example:
    # at index 1, the value at index 1 will represent number of ways to make change for $1
    # at index 2, the value at index 2 will represent number of ways to make change for $2
    # and so on

    ways = [0 for i in range(n+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]


assert numberOfWaysToMakeChange(0, [2, 3, 4, 7]) == 1
assert numberOfWaysToMakeChange(9, [5]) == 0
assert numberOfWaysToMakeChange(5, [1, 5, 10, 25]) == 2
assert numberOfWaysToMakeChange(25, [1, 5, 10, 25]) == 13
