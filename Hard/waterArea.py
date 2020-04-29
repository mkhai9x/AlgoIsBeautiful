'''
You're given an array of non-negative integers where each non-zero integer represents the height
of a pillar of width <code>1</code>. Imagine water being poured over all the pillars; write a function that
returns the surface area of the water trapped between the pillars viewed from the front. Note that spilled
water should be ingored.
'''
'''
Example:
heights = [0,8,0,0,5,0,0,10,0,0,1,1,0,3]
output = 48
'''


def waterArea(heights):
    leftmax = [0]*len(heights)
    # leftmax represent the maximum height on the left of index i
    for index in range(len(heights)):
        if index == 0:
            leftmax[index] = 0
        else:
            leftmax[index] = heights[index-1] if heights[index -
                                                         1] > leftmax[index-1] else leftmax[index-1]
    rightmax = [0]*len(heights)
    for index in reversed(range(len(heights))):
        if index == len(heights)-1:
            rightmax[index] = 0
        else:
            rightmax[index] = heights[index+1] if heights[index +
                                                          1] > rightmax[index+1] else rightmax[index+1]
    water_above = [0]*len(heights)
    i = 0
    while i < len(heights):
        smaller = min(leftmax[i], rightmax[i])
        if heights[i] < smaller:
            water_above[i] = smaller - heights[i]
        else:
            water_above[i] = 0
        i += 1
    return sum(water_above)


print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
