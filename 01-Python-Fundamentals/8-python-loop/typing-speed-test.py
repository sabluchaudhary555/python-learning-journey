import time
import random
import os

# typing speed test - shows a sentence, times how fast you type it back
# calculates WPM, CPM and accuracy just like real typing test sites do

SCORE_FILE = "typing_scores.txt"

# sentence banks for each difficulty - easy = short/simple, hard = long/technical
EASY_SENTENCES = [
    "the cat sat on the mat",
    "i like to read books",
    "python is fun to learn",
    "the sun is bright today",
]

MEDIUM_SENTENCES = [
    "the quick brown fox jumps over the lazy dog",
    "practice makes a person perfect at any skill",
    "programming requires patience logic and lots of practice",
    "she sells seashells by the seashore every morning",
]

HARD_SENTENCES = [
    "the electromagnetic spectrum encompasses radio waves microwaves and gamma rays",
    "photosynthesis is the process by which plants convert sunlight into chemical energy",
    "the entrepreneur meticulously analyzed quarterly financial statements before investing",
    "artificial intelligence algorithms require substantial computational resources to train",
]


def pick_sentence(level):
    # returns a random sentence from the bank matching the chosen difficulty
    if level == "1":
        return random.choice(EASY_SENTENCES)
    elif level == "2":
        return random.choice(MEDIUM_SENTENCES)
    else:
        return random.choice(HARD_SENTENCES)


def calculate_accuracy(original, typed):
    # compares character by character, counts how many match at the same position
    length = min(len(original), len(typed))
    correct = 0
    for i in range(length):
        if original[i] == typed[i]:
            correct += 1

    # penalize for length mismatch too (missing or extra chars typed)
    total = max(len(original), len(typed))
    if total == 0:
        return 0
    return round((correct / total) * 100, 2)


def find_wrong_words(original, typed):
    # word-by-word comparison so we can tell the user exactly which words they messed up
    orig_words = original.split()
    typed_words = typed.split()
    wrong = []

    for i in range(min(len(orig_words), len(typed_words))):
        if orig_words[i] != typed_words[i]:
            wrong.append((orig_words[i], typed_words[i]))

    return wrong


def run_test():
    # step 1: let user pick a difficulty level
    print("\nChoose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    level = input("Choice: ").strip()

    sentence = pick_sentence(level)

    # step 2: show the sentence only after user is ready, so timer starts fair
    print("\nType the following sentence as fast and accurately as you can.")
    print("Press Enter when you're ready to start...")
    input()

    # step 3: start the clock right before showing the sentence to type
    print(f"\n{sentence}\n")
    start = time.time()
    typed = input("> ")
    end = time.time()   # stop the clock the moment they hit Enter

    time_taken = end - start
    if time_taken <= 0:
        time_taken = 0.01  # avoid divide by zero on freakishly fast input

    word_count = len(sentence.split())
    char_count = len(sentence)

    # step 4: core speed formulas - same ones real typing test sites use
    wpm = round((word_count / time_taken) * 60, 2)
    cpm = round((char_count / time_taken) * 60, 2)
    accuracy = calculate_accuracy(sentence, typed)

    # step 5: show the result summary
    print("\n----- Result -----")
    print(f"Time taken   : {round(time_taken, 2)} seconds")
    print(f"Speed        : {wpm} WPM  ({cpm} CPM)")
    print(f"Accuracy     : {accuracy}%")

    # step 6: point out exactly which words were typed wrong
    wrong = find_wrong_words(sentence, typed)
    if wrong:
        print(f"\nWords you got wrong ({len(wrong)}):")
        for correct_word, your_word in wrong:
            print(f"  expected '{correct_word}' -> you typed '{your_word}'")
    else:
        print("\nPerfect match, no wrong words!")

    save_score(wpm, accuracy, level)
    return wpm, accuracy


def save_score(wpm, accuracy, level):
    # appends this attempt's result to the score file so history builds up over time
    level_name = {"1": "Easy", "2": "Medium", "3": "Hard"}.get(level, "Medium")
    with open(SCORE_FILE, "a") as f:
        f.write(f"{level_name},{wpm},{accuracy}\n")


def show_best_score():
    # reads every saved attempt and picks out the highest WPM ever recorded
    if not os.path.exists(SCORE_FILE):
        print("No scores recorded yet, take a test first.")
        return

    with open(SCORE_FILE) as f:
        lines = f.readlines()

    if not lines:
        print("No scores recorded yet.")
        return

    best_wpm = 0
    best_line = None
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 3:
            wpm = float(parts[1])
            if wpm > best_wpm:
                best_wpm = wpm
                best_line = parts

    if best_line:
        print(f"\nYour best score: {best_line[1]} WPM at {best_line[2]}% accuracy ({best_line[0]} level)")


def show_average():
    # goes through every saved attempt and averages out speed + accuracy
    if not os.path.exists(SCORE_FILE):
        print("No scores recorded yet.")
        return

    with open(SCORE_FILE) as f:
        lines = f.readlines()

    if not lines:
        print("No scores recorded yet.")
        return

    total_wpm = 0
    total_acc = 0
    count = 0
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 3:
            total_wpm += float(parts[1])
            total_acc += float(parts[2])
            count += 1

    if count > 0:
        print(f"\nTests taken: {count}")
        print(f"Average speed: {round(total_wpm / count, 2)} WPM")
        print(f"Average accuracy: {round(total_acc / count, 2)}%")


def multi_round_test():
    # runs the test back to back for however many rounds the user wants,
    # then averages the WPM/accuracy across all rounds
    rounds = input("How many rounds do you want to play? ").strip()
    if not rounds.isdigit() or int(rounds) < 1:
        print("Enter a valid number.")
        return

    rounds = int(rounds)
    total_wpm = 0
    total_acc = 0

    for r in range(1, rounds + 1):
        print(f"\n=== Round {r} of {rounds} ===")
        wpm, acc = run_test()
        total_wpm += wpm
        total_acc += acc

    print(f"\n----- Overall Average ({rounds} rounds) -----")
    print(f"Average speed: {round(total_wpm / rounds, 2)} WPM")
    print(f"Average accuracy: {round(total_acc / rounds, 2)}%")


def menu():
    # main menu shown every time we loop back after an action finishes
    print("\n===== Typing Speed Test =====")
    print("1. Take a test")
    print("2. Multi-round test (average score)")
    print("3. Show best score")
    print("4. Show average stats")
    print("0. Exit")


def main():
    # keeps showing the menu and routing to the right function until user exits
    while True:
        menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            run_test()
        elif choice == "2":
            multi_round_test()
        elif choice == "3":
            show_best_score()
        elif choice == "4":
            show_average()
        elif choice == "0":
            print("Keep practicing, bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()