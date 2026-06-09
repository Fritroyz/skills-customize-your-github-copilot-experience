# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice working with strings, file I/O, and text manipulation by building command-line tools that analyze and transform plain text files.

## 📝 Tasks

### 🛠️ Implement text-processing utilities

#### Description
Using the provided `starter-code.py`, implement functions and a small CLI that can read a text file and perform common text-processing tasks such as counting lines and words, searching for a term, replacing text, and reporting the most frequent words.

#### Requirements
Completed program should:

- Read input from a text file supplied as a command-line argument.
- Provide at least these operations (via flags or a simple interactive menu):
  - Count lines and words.
  - Count occurrences of a given word (case-insensitive).
  - Replace all occurrences of a substring and optionally write output to a new file.
  - Show the top N most frequent words and their counts.
- Handle large files reasonably (read line-by-line) and avoid loading huge files wholly into memory when possible.
- Include helpful `--help` output and basic error handling for missing files or invalid inputs.

### 🛠️ Optional Extensions

#### Description
Enhance the tool with one or more advanced features.

#### Suggestions

- Add support for regular-expression search/replace.
- Provide case-sensitive and case-insensitive modes.
- Normalize punctuation and stopwords when computing top-N frequent words.
- Add a `--stats` mode that prints readability metrics (e.g., average sentence length).

## 📁 Starter Files

- `starter-code.py` — starter CLI and helper functions.
- `sample.txt` — small sample text for manual testing.

## ▶️ Run

No external dependencies required. Run examples:

```bash
python3 assignments/python-text-processing/starter-code.py assignments/python-text-processing/sample.txt --count
python3 assignments/python-text-processing/starter-code.py assignments/python-text-processing/sample.txt --find python
python3 assignments/python-text-processing/starter-code.py assignments/python-text-processing/sample.txt --replace old new --out out.txt
python3 assignments/python-text-processing/starter-code.py assignments/python-text-processing/sample.txt --top 10
```

Good luck — try the optional extensions if you finish early.
# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice working with strings, file I/O, and text manipulation by building command-line tools that analyze and transform plain text files.

## 📝 Tasks

### 🛠️ Implement text-processing utilities

#### Description
Using the provided `starter-code.py`, implement functions and a small CLI that can read a text file and perform common text-processing tasks such as counting lines and words, searching for a term, replacing text, and reporting the most frequent words.

#### Requirements
Completed program should:

- Read input from a text file supplied as a command-line argument.
- Provide at least these operations (via flags or a simple interactive menu):
  - Count lines and words.
  - Count occurrences of a given word (case-insensitive).
  - Replace all occurrences of a substring and optionally write output to a new file.
  - Show the top N most frequent words and their counts.
- Handle large files reasonably (read line-by-line) and avoid loading huge files wholly into memory when possible.
- Include helpful `--help` output and basic error handling for missing files or invalid inputs.

### 🛠️ Optional Extensions

#### Description
Enhance the tool with one or more advanced features.

#### Suggestions

- Add support for regular-expression search/replace.
- Provide case-sensitive and case-insensitive modes.
- Normalize punctuation and stopwords when computing top-N frequent words.
- Add a `--stats` mode that prints readability metrics (e.g., average sentence length).

## 📁 Starter Files

- `starter-code.py` — starter CLI and helper functions.
- `sample.txt` — small sample text for manual testing.

## ▶️ Run

Install no external dependencies (uses Python 3 standard library). Run examples:

```bash
python3 assignments/python-text-processing/starter-code.py sample.txt --count
python3 assignments/python-text-processing/starter-code.py sample.txt --find python
python3 assignments/python-text-processing/starter-code.py sample.txt --replace old new --out out.txt
python3 assignments/python-text-processing/starter-code.py sample.txt --top 10
```

Good luck — try the optional extensions if you finish early.
