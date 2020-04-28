from collections import deque
'''
Given a stream of integers and a window size, calculate the moving average of all integers 
in the sliding window.
'''

'''
Here, we can approach this problem using method Circular Queue with Array
We will implement a circular queue with a fixed-size arrays. The key to the implementation
is the correlation between the index of Head and Tail elements, which we could summarize in the following formula:
tail = (head+1) mod size
'''


class MovingAverage_with_circularQueue:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0]*self.size
        self.head = self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head+1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # self.head = (self.head+1) % self.size
        self.head = tail
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)


'''
Another method
'''


class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque()
        self.total = 0
        self.size = size

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
        if len(self.queue) == 0:
            return 0
        return self.total/len(self.queue)
