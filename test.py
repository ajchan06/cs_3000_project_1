# Anthony Chan
# CS 3000 - Algorithms and Data Structures
# Group Project 1, Problem 1: Find Median from Data Stream (LeetCode 295)
# May 31, 2026

import heapq

class MedianFinder:
    def __init__(self):
        self.lo = []   # max-heap (stored negated) -> smaller half
        self.hi = []   # min-heap -> larger half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2