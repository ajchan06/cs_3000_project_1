# Anthony Chan
# CS 3000 - Algorithms and Data Structures
# Group Project 1, Problem 1: Find Median from Data Stream (LeetCode 295)
# May 31, 2026

import heapq, random, time
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


class MedianFinder:
    def __init__(self):
        self.lo = []; self.hi = []
    def addNum(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2


class NaiveMedian:
    def __init__(self):
        self.data = []  # kept in insertion order (not sorted)
    def addNum(self, num):
        self.data.append(num)
    def findMedian(self):
        s = sorted(self.data)   # re-sort the whole list from scratch every query
        n = len(s)
        if n % 2:
            return float(s[n // 2])
        return (s[n // 2 - 1] + s[n // 2]) / 2


ns = [1000, 2000, 4000, 8000, 16000]
heap_times, naive_times = [], []

for n in ns:
    nums = [random.randint(-100000, 100000) for _ in range(n)]  # built before timing

    mf = MedianFinder()
    t0 = time.perf_counter()
    for x in nums:
        mf.addNum(x); mf.findMedian()
    heap_times.append(time.perf_counter() - t0)

    nv = NaiveMedian()
    t0 = time.perf_counter()
    for x in nums:
        nv.addNum(x); nv.findMedian()
    naive_times.append(time.perf_counter() - t0)

    speedup = naive_times[-1] / heap_times[-1]
    print(f"n={n:6d}  two-heap={heap_times[-1]:.4f}s  "
          f"naive={naive_times[-1]:.4f}s  speedup={speedup:.0f}x")

plt.figure(figsize=(8, 5))
plt.plot(ns, naive_times, "o-", color="#d1622b", linewidth=2, markersize=7,
         label="Sort each query  \u2014 O(n\u00b2 log n)")
plt.plot(ns, heap_times, "o-", color="#185FA5", linewidth=2, markersize=7,
         label="Two heaps  \u2014 O(n log n)")
plt.xlabel("Number of operations (add + median query)")
plt.ylabel("Total time (seconds)")
plt.title("Running median: two heaps vs. naive sort-per-query")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("median_timing.png", dpi=130)
print("saved median_timing.png")