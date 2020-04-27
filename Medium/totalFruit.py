'''
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?
'''


def totalFruit(tree):
    types = {tree[0]}
    total = current = 1
    index = 0
    i = 1
    while i < len(tree):
        if len(types) < 2:
            types.add(tree[i])
            if tree[i] != tree[i-1]:
                index = i
            current += 1
        else:
            if tree[i] in types:
                if tree[i] != tree[i-1]:
                    index = i
                current += 1
            else:
                types = {tree[index], tree[i]}
                total = max(current, total)
                current = i - index + 1
                index = i
        total = max(current, total)
        i += 1
    return total


print(totalFruit([1, 2, 1]))
print(totalFruit([0, 1, 2, 2]))
print(totalFruit([1, 2, 3, 2, 2]))
print(totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
