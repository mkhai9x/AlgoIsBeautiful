'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
'''


import unittest


def largestRange(array):
    longest_range = 0
    # Create a hash to keep track which elements are visited
    nums = {}
    for num in array:
        nums[num] = True

    for num in array:
        if not nums[num]:  # check if nums[num] is False, it means we already visited this num
            continue
        nums[num] = False  # mark this as visited
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            left -= 1
        while right in nums:
            nums[right] = False
            right += 1
        current_length = right - left
        if current_length > longest_range:
            longest_range = current_length
    return longest_range - 1


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(largestRange([1]), 1)

    def test_case_2(self):
        self.assertEqual(largestRange([1, 2]), 2)

    def test_case_3(self):
        self.assertEqual(largestRange([4, 2, 1, 3]), 4)

    def test_case_4(self):
        self.assertEqual(largestRange([4, 2, 1, 3, 6]), 4)

    def test_case_5(self):
        self.assertEqual(largestRange([8, 4, 2, 10, 3, 6, 7, 9, 1]), 5)

    def test_case_6(self):
        self.assertEqual(largestRange(
            [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]), 8)

    def test_case_7(self):
        self.assertEqual(
            largestRange([19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4,
                          11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]),
            10,
        )

    def test_case_8(self):
        self.assertEqual(
            largestRange(
                [0, 9, 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4,
                    11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]
            ),
            21,
        )


if __name__ == "__main__":
    unittest.main()
