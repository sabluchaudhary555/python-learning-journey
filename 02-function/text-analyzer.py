"""
Text Analyzer Tool
Analyzes a block of text and gives word count, longest word,
average word length, and most common word.
"""

from functools import reduce
import string


def clean_words(text):
    # remove punctuation and lowercase everything so "Hi," and "hi" count same
    no_punct = text.translate(str.maketrans('', '', string.punctuation))
    return no_punct.lower().split()


def word_count(words):
    return len(words)


def char_count(text):
    return len(text.replace(" ", ""))


def longest_word(words):
    return reduce(lambda a, b: a if len(a) >= len(b) else b, words)


def average_word_length(words):
    total_len = sum(map(len, words))
    return round(total_len / len(words), 2)


def most_common_word(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return max(counts.items(), key=lambda pair: pair[1])


def analyze(text):
    words = clean_words(text)

    if not words:
        print("No text to analyze.")
        return

    common_word, common_count = most_common_word(words)

    print("----- Text Analysis Report -----")
    print(f"Total words       : {word_count(words)}")
    print(f"Total characters  : {char_count(text)}")
    print(f"Longest word      : {longest_word(words)}")
    print(f"Average word len  : {average_word_length(words)}")
    print(f"Most common word  : '{common_word}' ({common_count} times)")


if __name__ == "__main__":
    sample_text = """
    Python is a powerful and easy to learn programming language.
    Python is widely used for web development, data analysis,
    automation and machine learning. Many beginners choose Python
    as their first programming language because it is simple and readable.
    """

    analyze(sample_text)