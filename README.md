# AlgoIsBeautiful

Practice makes perfect

Solutions to problems from leetcode and other resources.

#### [Classical problems](#classical-problems)

- _[Binary Trees](#binary-trees)_
- _[Graphs](#graphs)_

#### [Easy problems](#easy)

#### [Medium problems](#medium)

#### [Hard problems](#hard)

#### [Very Hard problems](#verry-hard)

---

## Classical problems

### - **Binary Trees**

#### _**Problem: Diameter of Binary Tree**_

> Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

#### [Solution](ClassicalProblems/Trees/diameterOfBinaryTree.py)

---

### - **Graphs**

#### _**Problem: Network Delay Time**_

> There are N network nodes, labelled 1 to N.
> Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
> Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

#### [Solution](ClassicalProblems/Graphs/networkDelayTime.py)

---

## Easy

#### _**Problem: Height Checker**_

> Students are asked to stand in non-decreasing order of heights for an annual photo.

> Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.

#### [Solution](Easy/heighChecker.py)

#### _**Problem: Last Stone Weight**_

> We have a collection of stones, each stone has a positive integer weight.

> Each turn, we choose the two heaviest stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

> - If x == y, both stones are totaly destroyed.
> - If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y - x

> At the end, there is at most 1 stone left. Return the weight of this stone (0 if there are no stones left.)

#### [Solution](Easy/lastStoneWeight.py)

---

## Medium

#### _**Problem: Simplify Path**_

> Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path

#### [Solution](Medium/simplifyPath.py)

#### _**Problem: Climbing the Leaderboard**_

> Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. The game uses Dense Ranking, so its leaderboard works like this:

> - The player with the highest score is ranked number 1 on the leaderboard
> - Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

#### [Solution](Medium/climbingLeaderboard.py)

#### _**Problem: Find Peak Element**_

> A peak element is an element that is greater than its neighbors.

> Given an input array <code> nums </code>, where <code> nums[i] ≠ nums[i+1]</code> find a peak element and return its index.

> Bonus: Can you do in <code>log(N)</code> time?

#### [Solution](Medium/findPeakElement.py)

---

## Hard

#### _**Problem: Largest Range**_

> Write a function that takes in an array of integers and find the length of the longest consecutive elements sequence.

> Bonus: Can you do this in one pass?

#### [Solution](Hard/largestRange.py)

#### _**Problem: Min Rewards**_

> Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out to students to satisfy the two rules:

> 1.  All students must receive at least one reward.
> 2.  Any give student must receive strictly more rewards than an adjacent student with a lower score and must receive striclty fewer rewards than an adjacent student with a higher score.

#### [Solution](Hard/minRewards.py)

## Very Hard

---
