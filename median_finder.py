# Anthony Chan
# CS 3000 - Algorithms and Data Structures
# Group Project 1, Problem 1: Find Median from Data Stream (LeetCode 295)
# May 31, 2026

import heapq

class MedianFinder:
    def __init__(self):
        self.lo = []  # max-heap (stored negated) -> smaller half
        self.hi = []  # min-heap -> larger half

    def addNum(self, num: int) -> None:
        # 1. Add the new value to the lower half (negated for the max-heap).
        heapq.heappush(self.lo, -num)
        # 2. Move lo's current largest into hi. This guarantees every value
        #    in lo stays <= every value in hi, so the halves remain ordered.
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        # 3. Rebalance: lo must never be smaller than hi. If hi grew larger,
        #    push its smallest value back down into lo.
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        # Odd count: lo holds the extra element, so its top IS the median.
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        # Even count: median is the average of the two inner tops.
        return (-self.lo[0] + self.hi[0]) / 2
