#!/usr/bin/env python3
"""Starter code: search and sort algorithms with a benchmarking CLI."""
import argparse
import csv
import random
import time
from typing import List, Callable, Tuple


def linear_search(a: List[int], target: int) -> int:
    for i, v in enumerate(a):
        if v == target:
            return i
    return -1


def binary_search(a: List[int], target: int) -> int:
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def bubble_sort(a: List[int]) -> List[int]:
    arr = a.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def merge_sort(a: List[int]) -> List[int]:
    if len(a) <= 1:
        return a[:]
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    res.extend(left[i:]); res.extend(right[j:])
    return res


def quick_sort(a: List[int]) -> List[int]:
    if len(a) <= 1:
        return a[:]
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


ALGORITHMS = {
    "linear": linear_search,
    "binary": binary_search,
    "bubble": bubble_sort,
    "merge": merge_sort,
    "quick": quick_sort,
}


def time_function(func: Callable, args: Tuple = (), trials: int = 3) -> float:
    times = []
    for _ in range(trials):
        t0 = time.perf_counter()
        func(*args)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return sum(times) / len(times)


def generate_random_list(n: int, seed: int = None) -> List[int]:
    if seed is not None:
        random.seed(seed)
    return [random.randint(0, n * 10) for _ in range(n)]


def bench_sorts(sizes: List[int], trials: int, algorithms: List[str]):
    rows = []
    for n in sizes:
        arr = generate_random_list(n)
        for alg in algorithms:
            func = ALGORITHMS.get(alg)
            if func is None:
                continue
            # For search algorithms, prepare a target
            if alg in ("linear", "binary"):
                target = -1  # use a value unlikely to be found to exercise worst-case
                if alg == "binary":
                    data = sorted(arr)
                    avg = time_function(func, args=(data, target), trials=trials)
                else:
                    avg = time_function(func, args=(arr, target), trials=trials)
            else:
                # sorting algorithms: measure sorting
                avg = time_function(func, args=(arr,), trials=trials)
            rows.append((alg, n, avg))
            print(f"{alg:6} | n={n:6} | avg_time={avg:.6f}s")
    return rows


def parse_sizes(s: str) -> List[int]:
    return [int(x.strip()) for x in s.split(",") if x.strip()]


def main():
    p = argparse.ArgumentParser(description="Benchmark search and sort algorithms")
    p.add_argument("--bench", action="store_true", help="Run benchmarks")
    p.add_argument("--algorithms", default="bubble,merge,quick", help="Comma list of algorithms (linear,binary,bubble,merge,quick)")
    p.add_argument("--sizes", default="100,500,1000", help="Comma-separated input sizes")
    p.add_argument("--trials", type=int, default=3, help="Trials per measurement")
    p.add_argument("--csv", help="Write results to CSV file")
    args = p.parse_args()

    algs = [a.strip() for a in args.algorithms.split(",") if a.strip()]
    sizes = parse_sizes(args.sizes)

    if args.bench:
        rows = bench_sorts(sizes, args.trials, algs)
        if args.csv:
            with open(args.csv, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["algorithm", "n", "avg_time_s"])
                for r in rows:
                    writer.writerow(r)


if __name__ == "__main__":
    main()
