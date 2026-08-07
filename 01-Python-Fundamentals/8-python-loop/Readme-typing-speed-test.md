# Typing Speed Test

A CLI typing speed test — same idea as sites like Monkeytype or 10FastFingers. Shows you a sentence, times how fast you type it back, and calculates your WPM, CPM, and accuracy.

## Why this exists

Wanted to build the actual logic behind typing test sites instead of just using one — turns out it's mostly loops (comparing characters/words) and a bit of math (speed formulas) once you break it down.

## How it works

1. Pick a difficulty level — a random sentence gets picked from that bank
2. Timer starts the moment the sentence is shown
3. You type it and hit Enter — timer stops
4. Your typed text gets compared against the original, character by character and word by word
5. Results are calculated and saved

## Features

| Feature | What it does |
|---|---|
| Take a test | Single round — pick a difficulty, type the sentence, get instant results |
| Multi-round test | Play several rounds back to back, see your average WPM/accuracy across all of them |
| Show best score | Looks through your history and shows your highest WPM ever recorded |
| Show average stats | Averages your speed and accuracy across every test you've taken |

## What gets calculated

- **WPM (Words Per Minute)** — `(word count / time taken in seconds) * 60`
- **CPM (Characters Per Minute)** — `(character count / time taken in seconds) * 60`
- **Accuracy %** — character-by-character match between what you typed and the original sentence
- **Wrong words** — tells you exactly which words you got wrong and what you typed instead

## Difficulty levels

| Level | Sentence style |
|---|---|
| Easy | Short, simple sentences |
| Medium | Slightly longer, everyday phrases |
| Hard | Long, technical sentences |

## Usage

```bash
python typing_speed_test.py
```

```
===== Typing Speed Test =====
1. Take a test
2. Multi-round test (average score)
3. Show best score
4. Show average stats
0. Exit
```

## Example

```
Choose difficulty: 2
Press Enter when you're ready to start...

the quick brown fox jumps over the lazy dog

> the quick brown fox jump over the lazy dog

----- Result -----
Time taken   : 6.42 seconds
Speed        : 84.11 WPM  (467.29 CPM)
Accuracy     : 97.67%

Words you got wrong (1):
  expected 'jumps' -> you typed 'jump'
```

## Files

- `typing_scores.txt` — every test result gets appended here (difficulty, WPM, accuracy), used for the best score and average stats

## Notes

Results depend a lot on your own typing rhythm and how fast you hit Enter, so treat the numbers as a rough gauge rather than a lab-accurate measurement — same limitation any browser-based typing test has too.