'''
Imagine that you are a teacher who's just graded the final exam in a class.
You have a list of student scores on the final exam in particular order (not necessarily sorted),
and you want to reward your students.
You decide to do so fairly by giving them arbitrary rewards following two rules:
    1) All students must receive at least on reward
    2) Any given student must receive strictly more rewards than a adjancent student (a student immediately
    to the left or to the right) with a lower score and must receive strictly fewer rewards than an adjacent
    student with a higher score.

Example:

Input:
    scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
Output:
    25
'''
# Time = O(n^2) and Space = O(N)


import unittest


def minRewards_method1(scores):
    rewards = [1]*len(scores)
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j+1]:
                rewards[j] = max(rewards[j], rewards[j+1]+1)
                j -= 1
    return sum(rewards)

# Time = O(N) and Space = O(N)


def minRewards_method2(scores):
    # Finding all the local minimums
    rewards = [1]*len(scores)
    localMinIdxs = getLocalMinIdxs(scores)
    for localMinIdx in localMinIdxs:
        expandFromLocalMinIdx(localMinIdx, scores, rewards)
    return sum(rewards)


def getLocalMinIdxs(array):
    if len(array) == 1:
        return [0]
    localMinIdxs = []
    for i in range(len(array)):
        if i == 0 and array[i] < array[i+1]:
            localMinIdxs.append(i)
        if i == len(array)-1 and array[i] < array[i-1]:
            localMinIdxs.append(i)
        if i == 0 or i == len(array) - 1:
            continue
        if array[i] < array[i+1] and array[i] < array[i-1]:
            localMinIdxs.append(i)
    return localMinIdxs


def expandFromLocalMinIdx(localMinIdx, scores, rewards):
    leftIdx = localMinIdx - 1
    while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx+1]:
        rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx+1]+1)
        leftIdx -= 1
    rightIdx = localMinIdx + 1
    while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx-1]:
        rewards[rightIdx] = rewards[rightIdx-1]+1
        rightIdx -= 1


# Time = O(N) and Space = O(N)

def minRewards(scores):
    rewards = [1]*len(scores)
    for i in range(1, len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1]+1
    for i in reversed(range(len(scores)-1)):
        if scores[i] > scores[i+1]:
            rewards[i] = max(rewards[i], rewards[i+1] + 1)
    return sum(rewards)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minRewards([1]), 1)

    def test_case_2(self):
        self.assertEqual(minRewards([5, 10]), 3)

    def test_case_3(self):
        self.assertEqual(minRewards([10, 5]), 3)

    def test_case_4(self):
        self.assertEqual(minRewards([4, 2, 1, 3]), 8)

    def test_case_5(self):
        self.assertEqual(minRewards([0, 4, 2, 1, 3]), 9)

    def test_case_6(self):
        self.assertEqual(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]), 25)

    def test_case_7(self):
        self.assertEqual(minRewards(
            [2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0]), 52)

    def test_case_8(self):
        self.assertEqual(minRewards([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]), 15)

    def test_case_9(self):
        self.assertEqual(
            minRewards(
                [
                    800,
                    400,
                    20,
                    10,
                    30,
                    61,
                    70,
                    90,
                    17,
                    21,
                    22,
                    13,
                    12,
                    11,
                    8,
                    4,
                    2,
                    1,
                    3,
                    6,
                    7,
                    9,
                    0,
                    68,
                    55,
                    67,
                    57,
                    60,
                    51,
                    661,
                    50,
                    65,
                    53,
                ]
            ),
            93,
        )


if __name__ == "__main__":
    unittest.main()
