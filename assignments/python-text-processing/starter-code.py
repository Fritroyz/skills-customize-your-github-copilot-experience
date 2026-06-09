#!/usr/bin/env python3
"""Starter CLI for Python Text Processing assignment.

Provides basic operations: count, find, replace, top-N words.
"""
import argparse
import collections
import os
import re
import sys


def iter_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line


def count_lines_words(path):
    lines = 0
    words = 0
    for line in iter_lines(path):
        lines += 1
        words += len(line.split())
    return lines, words


def count_occurrences(path, term, case_insensitive=True):
    term_cmp = term.lower() if case_insensitive else term
    count = 0
    for line in iter_lines(path):
        hay = line.lower() if case_insensitive else line
        count += hay.count(term_cmp)
    return count


def replace_and_write(path, old, new, out_path=None, case_insensitive=False):
    if out_path is None:
        out_path = path
    flags = re.IGNORECASE if case_insensitive else 0
    pattern = re.compile(re.escape(old), flags)
    with open(path, "r", encoding="utf-8") as rf, open(out_path, "w", encoding="utf-8") as wf:
        for line in rf:
            wf.write(pattern.sub(new, line))


def top_n_words(path, n=10):
    counter = collections.Counter()
    word_re = re.compile(r"\b[\w']+\b")
    for line in iter_lines(path):
        for m in word_re.findall(line.lower()):
            counter[m] += 1
    return counter.most_common(n)


def main(argv=None):
    p = argparse.ArgumentParser(description="Text processing helper")
    p.add_argument("file", help="Path to input text file")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--count", action="store_true", help="Count lines and words")
    group.add_argument("--find", metavar="TERM", help="Count occurrences of TERM")
    group.add_argument("--replace", nargs=2, metavar=("OLD", "NEW"), help="Replace OLD with NEW")
    group.add_argument("--top", type=int, metavar="N", help="Show top N frequent words")
    p.add_argument("--out", help="Output file for replace (default: overwrite)")
    p.add_argument("--ignore-case", action="store_true", help="Case-insensitive operations")
    args = p.parse_args(argv)

    if not os.path.isfile(args.file):
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        sys.exit(2)

    if args.count:
        lines, words = count_lines_words(args.file)
        print(f"Lines: {lines}\nWords: {words}")
    elif args.find:
        c = count_occurrences(args.file, args.find, case_insensitive=args.ignore_case)
        print(f"Occurrences of '{args.find}': {c}")
    elif args.replace:
        old, new = args.replace
        out = args.out if args.out else args.file
        replace_and_write(args.file, old, new, out_path=out, case_insensitive=args.ignore_case)
        print(f"Replaced '{old}' with '{new}' -> {out}")
    elif args.top:
        for word, cnt in top_n_words(args.file, args.top):
            print(f"{word}: {cnt}")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""Starter CLI for Python Text Processing assignment.

Provides basic operations: count, find, replace, top-N words.
"""
import argparse
import collections
import os
import re
import sys


def iter_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line


def count_lines_words(path):
    lines = 0
    words = 0
    for line in iter_lines(path):
        lines += 1
        words += len(line.split())
    return lines, words


def count_occurrences(path, term, case_insensitive=True):
    term_cmp = term.lower() if case_insensitive else term
    count = 0
    for line in iter_lines(path):
        hay = line.lower() if case_insensitive else line
        count += hay.count(term_cmp)
    return count


def replace_and_write(path, old, new, out_path=None, case_insensitive=False):
    if out_path is None:
        out_path = path
    flags = re.IGNORECASE if case_insensitive else 0
    pattern = re.compile(re.escape(old), flags)
    with open(path, "r", encoding="utf-8") as rf, open(out_path, "w", encoding="utf-8") as wf:
        for line in rf:
            wf.write(pattern.sub(new, line))


def top_n_words(path, n=10):
    counter = collections.Counter()
    word_re = re.compile(r"\b[\w']+\b")
    for line in iter_lines(path):
        for m in word_re.findall(line.lower()):
            counter[m] += 1
    return counter.most_common(n)


def main(argv=None):
    p = argparse.ArgumentParser(description="Text processing helper")
    p.add_argument("file", help="Path to input text file")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--count", action="store_true", help="Count lines and words")
    group.add_argument("--find", metavar="TERM", help="Count occurrences of TERM")
    group.add_argument("--replace", nargs=2, metavar=("OLD", "NEW"), help="Replace OLD with NEW")
    group.add_argument("--top", type=int, metavar="N", help="Show top N frequent words")
    p.add_argument("--out", help="Output file for replace (default: overwrite)")
    p.add_argument("--ignore-case", action="store_true", help="Case-insensitive operations")
    args = p.parse_args(argv)

    if not os.path.isfile(args.file):
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        sys.exit(2)

    if args.count:
        lines, words = count_lines_words(args.file)
        print(f"Lines: {lines}\nWords: {words}")
    elif args.find:
        c = count_occurrences(args.file, args.find, case_insensitive=args.ignore_case)
        print(f"Occurrences of '{args.find}': {c}")
    elif args.replace:
        old, new = args.replace
        out = args.out if args.out else args.file
        replace_and_write(args.file, old, new, out_path=out, case_insensitive=args.ignore_case)
        print(f"Replaced '{old}' with '{new}' -> {out}")
    elif args.top:
        for word, cnt in top_n_words(args.file, args.top):
            print(f"{word}: {cnt}")


if __name__ == "__main__":
    main()
