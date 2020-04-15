'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.
'''

#  O(N) Time


def findPeakElement(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return i
    return len(nums)-1

# O(log(N)) Time


def findPeakElement_Binaray(nums):
    return search(nums, 0, len(nums)-1)


def search(nums, low, high):
    if low == high:
        return low
    mid = int((low + high) / 2)
    if nums[mid] > nums[mid+1]:
        return search(nums, low, mid)
    return search(nums, mid, high)


assert findPeakElement([1, 2, 3, 1]) in {2}
assert findPeakElement([1]) in {0}
