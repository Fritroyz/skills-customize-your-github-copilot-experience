# 📘 Assignment: Algorithms — Search & Sort

## 🎯 Objective

Implement and analyze classic search and sorting algorithms to build algorithmic thinking and understand time/space complexity.

## 📝 Tasks

### 🛠️ Implement algorithms and measurements

#### Description
Using the provided `starter-code.py`, implement the following algorithms and a small benchmarking harness that measures empirical runtime on different input sizes.

#### Requirements
Completed work should:

- Implement search algorithms: linear search and binary search (binary search should require sorted input).
- Implement sorting algorithms: bubble sort, merge sort, and quick sort.
- Provide a simple benchmarking CLI to measure runtime (average over multiple trials) for each algorithm on randomly generated integer lists.
- Output timings in a readable table or CSV for later analysis; include brief commentary on observed time complexity.
- Include docstrings and example commands in the README.

### 🛠️ Optional Extensions

#### Description
Enhance the assignment with tests or improved analysis.

#### Suggestions

- Add `pytest` tests that verify algorithm correctness on edge cases.
- Plot runtimes using `matplotlib` and include sample graphs.
- Compare built-in `sorted()` performance to your implementations.

## 📁 Starter Files

- `starter-code.py` — starter implementations and a benchmarking CLI.

## ▶️ Run

No external dependencies required to run basic benchmarks. Example commands:

```bash
python3 assignments/algorithms-search-sort/starter-code.py --bench --algorithms linear,binary --sizes 1000,5000,10000 --trials 5
python3 assignments/algorithms-search-sort/starter-code.py --bench --algorithms bubble,merge,quick --sizes 500,1000 --trials 3
```

These commands generate runtime measurements printed to stdout.

Good luck — aim to explain your observed runtimes briefly in a short report.
