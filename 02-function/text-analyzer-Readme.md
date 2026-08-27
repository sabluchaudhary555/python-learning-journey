# Text Analyzer Tool

A small Python script that analyzes a block of text and reports basic
statistics about it — word count, character count, longest word,
average word length, and the most frequently used word.

## Why this project

Built as a practical way to apply Python's functional tools — `map()`,
`reduce()`, and `lambda` — on a real, everyday problem instead of a
toy example.

## Features

- Cleans text (removes punctuation, lowercases) before analysis
- Total word count
- Total character count (excluding spaces)
- Longest word in the text
- Average word length
- Most common word and how many times it appears

## How it works

| Function | Purpose |
|---|---|
| `clean_words()` | strips punctuation and splits text into lowercase words |
| `word_count()` | returns total number of words |
| `char_count()` | returns total characters, ignoring spaces |
| `longest_word()` | uses `reduce()` to find the longest word |
| `average_word_length()` | uses `map()` + `sum()` to compute average length |
| `most_common_word()` | builds a frequency dict and returns the top word |

## Usage

Run the script directly — it analyzes a sample paragraph included in the file:

```bash
python text_analyzer.py
```

To analyze your own text, replace `sample_text` in the `__main__` block,
or import `analyze()` into another script:

```python
from text_analyzer import analyze

analyze("Your custom paragraph goes here.")
```

## Sample Output

```
----- Text Analysis Report -----
Total words       : 38
Total characters  : 219
Longest word      : programming
Average word len  : 5.5
Most common word  : 'python' (3 times)
```

## Possible Extensions

- Read text from a `.txt` file instead of a hardcoded string
- Add sentence count and reading-time estimate
- Export the report as a `.json` or `.csv` file