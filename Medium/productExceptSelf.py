'''
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product
of all the elements of nums except nums[i].
'''


def productExceptSelf(nums):
    left = [1 for i in range(len(nums))]
    for index in range(len(nums)):
        if index != 0:
            left[index] = left[index-1]*nums[index-1]
    output = [1 for i in range(len(nums))]
    current = 1
    for index in range(len(nums)-1, -1, -1):
        if index == len(nums)-1:
            output[index] = left[index]
        elif index == 0:
            current = nums[index+1]*current
            output[index] = current*left[index]
        else:
            current = nums[index+1]*current
            output[index] = left[index]*current
    return output


assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

assert productExceptSelf([4, 3, 2, 1, 2]) == [12, 16, 24, 48, 24]
