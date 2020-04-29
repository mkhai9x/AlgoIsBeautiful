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

#### _**Problem: Moving Average from Data Stream**_

> Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

> **Example :**

<pre><span>
m = MovingAverage(3)
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
</span>
</pre>

#### [Solution](Easy/MovingAverage.py)

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

#### _**Problem: Number of Ways to make Change**_

> Given an array of positive integers representing coin denominations and a single non-negative integer <code>n</code>
> representing a target amount of money, write a function that returns the number of ways
> to make change for that target amount using given coin denominations.

#### [Solution](Medium/numberOfWaysToMakeChange.py)

#### _**Problem: Product of Array Except Self**_

> Given an array <code>nums</code> of _n_ integers where _n_ > 1, return an array <code>ouput</code> such that <code>output[i]</code> is equal to the product of all elements of <code>nums</code> except <code>nums[i]</code>.

<pre>
<strong>Input:</strong> [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre>

> Bonus: Can you do it in O(N) time and not using division?

#### [Solution](Medium/productExceptSelf.py)

#### _**Problem: K Closest Points to Origin**_

> We have a list of <code>points</code> on the plane. Find the <code>K</code> closest points to the

> origin <code>(0,0)</code>. (Here, the distance between two
> points on a plane is the Euclidean distance.)

> You may return the answer in any order. The answer is guaranteed
> to be unique (except for the order that it is in.)

> **Example 1:**

<pre>
<strong>Input:</strong> points = <span>[[1,3],[-2,2]], K = 1</span>
<strong>Output:</strong> <span>[[-2,2]]</spane>
<strong>Explanation:</strong>
<span>The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].</span>
</pre>

#### [Solution](Medium/kClosest.py)

#### _**Problem: Fruit Into Baskets**_

> In a row of trees, the <code>i</code>-th tree produces fruit with type <code>tree[i]</code>.

> You **start at any tree of your choice**, then repeatedly perform the following steps:

> 1. Add one piece of fruit from this tree to your baskets. If you cannot, stop.
> 2. Move to the next tree to the right of the current tree. If there is no tree to the right, stop.

> Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

> You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

> What is the total amount of fruit you can collect with this procedure?

> **Example:**

<pre>
<strong>Input:</strong> <span>[3,3,3,1,2,1,1,2,3,3,4]</span>
<strong>Output:</strong> <span>5</span>
<strong>Explanation: </strong>
<span> We can collect [1,2,1,1,2].</span>
<span> If we started at the first tree or the eighth tree, we would only collect 4 fruits.</span>
</pre>

#### [Solution](Medium/totalFruit.py)

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

#### _**Problem: Water Area**_

> You're given an array of non-negative integers where each non-zero integer represents the height of a pillar of width <code>1</code>.

> Imagine water being poured over all of the pillars

> Write a function that returns the surface area of the water trapped between the pillars viewed from the front.

<pre>
<strong>Input:</strong> <span>[0, 8, 0, 0, 5, 0, 10, 0, 0, 1, 1, 0, 3]</span>
<strong>Output:</strong> <span>48</span>
</pre>

#### [Solution](Hard/waterArea.py)

## Very Hard

---
