'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
'''


def search(nums, target):
    n = len(nums)
    if n == 0:
        return -1
    low = 0
    high = n - 1
    while low <= high:
        mid = int(low + (high-low)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[low]:
            if target >= nums[low] and target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if target <= nums[high] and target > nums[mid]:
                low = mid + 1
            else:
                high = mid-1
    return -1
