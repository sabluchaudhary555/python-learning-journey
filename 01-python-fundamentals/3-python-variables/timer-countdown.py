import time
import sys
import os

# ── helpers ───────────────────────────────────────────────────────────────────

def clear_line():
    # overwrite the current line in terminal
    sys.stdout.write("\r" + " " * 60 + "\r")
    sys.stdout.flush()

def beep(times=3):
    # ASCII bell character — works in most terminals
    for _ in range(times):
        sys.stdout.write("\a")
        sys.stdout.flush()
        time.sleep(0.3)

def format_time(seconds):
    # break seconds into h / m / s
    hours   = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs    = seconds % 60

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"

def progress_bar(remaining, total, width=30):
    # visual bar showing how much time has passed
    elapsed  = total - remaining
    filled   = int((elapsed / total) * width)
    bar      = "█" * filled + "░" * (width - filled)
    percent  = int((elapsed / total) * 100)
    return f"[{bar}] {percent}%"

def parse_input(raw):
    # accept formats: 90 / 1:30 / 1h30m / 30m / 45s
    raw = raw.strip().lower()
    total = 0

    # format: 1:30:00 or 1:30 or 0:45
    if ":" in raw:
        parts = raw.split(":")
        if len(parts) == 3:
            total = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
        elif len(parts) == 2:
            total = int(parts[0]) * 60 + int(parts[1])
        return total

    # format: 1h30m20s / 2h / 45m / 30s (any combo)
    if any(c in raw for c in ["h", "m", "s"]):
        import re
        h = re.search(r"(\d+)h", raw)
        m = re.search(r"(\d+)m", raw)
        s = re.search(r"(\d+)s", raw)
        total  = int(h.group(1)) * 3600 if h else 0
        total += int(m.group(1)) * 60   if m else 0
        total += int(s.group(1))        if s else 0
        return total

    # plain number — treat as seconds
    return int(raw)

# ── timer modes ───────────────────────────────────────────────────────────────

def run_countdown(label, total_seconds, warn_at=10):
    remaining  = total_seconds
    start_time = time.time()

    print(f"\n  Timer : {label}")
    print(f"  Total : {format_time(total_seconds)}")
    print()

    try:
        while remaining >= 0:
            bar  = progress_bar(remaining, total_seconds)
            time_str = format_time(remaining)

            # warning color indicator
            if remaining <= warn_at:
                indicator = "⚠️ "
            elif remaining <= total_seconds * 0.25:
                indicator = "🔶"
            else:
                indicator = "🟢"

            sys.stdout.write(f"\r  {indicator}  {time_str}   {bar}  ")
            sys.stdout.flush()

            if remaining == 0:
                break

            time.sleep(1)
            remaining -= 1

    except KeyboardInterrupt:
        elapsed = int(time.time() - start_time)
        print(f"\n\n  ⏸  Paused at {format_time(remaining)} remaining")
        print(f"  Elapsed before pause: {format_time(elapsed)}")
        return "paused"

    print(f"\n\n  ✅  '{label}' — done!")
    beep(3)
    return "done"

def run_pomodoro():
    # classic pomodoro: 25 min work, 5 min break × 4, then 15 min long break
    sessions      = int(input("  How many pomodoro sessions? (default 4): ") or 4)
    work_min      = int(input("  Work duration in minutes? (default 25): ")  or 25)
    short_min     = int(input("  Short break in minutes?   (default 5): ")   or 5)
    long_min      = int(input("  Long break in minutes?    (default 15): ")  or 15)

    work_secs     = work_min  * 60
    short_secs    = short_min * 60
    long_secs     = long_min  * 60

    total_elapsed = 0
    completed     = 0

    print(f"\n  Starting {sessions} pomodoro session(s)...\n")

    for i in range(1, sessions + 1):
        print(f"\n  ──── Session {i}/{sessions} ────")
        result = run_countdown(f"Work block {i}", work_secs)

        if result == "paused":
            break

        completed    += 1
        total_elapsed += work_secs

        if i < sessions:
            # short break between sessions, long break every 4
            if i % 4 == 0:
                print(f"\n  🎉  4 sessions done! Taking a long break...")
                run_countdown("Long break", long_secs)
            else:
                print(f"\n  ☕  Short break time!")
                run_countdown("Short break", short_secs)

    print(f"\n  ── Pomodoro Summary ──────────────────")
    print(f"  Sessions completed : {completed}/{sessions}")
    print(f"  Total work time    : {format_time(completed * work_secs)}")

def run_multi_timer():
    # set multiple named timers in sequence
    print("\n  Add timers one by one. Leave name blank to start.\n")

    timers = []
    while True:
        name = input(f"  Timer {len(timers)+1} name (or Enter to start): ").strip()
        if not name:
            break
        duration = input(f"  Duration for '{name}' (e.g. 2m, 1:30, 90): ").strip()
        secs     = parse_input(duration)
        timers.append((name, secs))
        print(f"  Added: {name} — {format_time(secs)}\n")

    if not timers:
        print("  No timers added.")
        return

    total_time = sum(s for _, s in timers)
    print(f"\n  {len(timers)} timer(s) queued — total time: {format_time(total_time)}\n")

    for i, (name, secs) in enumerate(timers, 1):
        print(f"\n  [{i}/{len(timers)}]", end="")
        run_countdown(name, secs)

def run_stopwatch():
    # count up instead of down
    print("\n  ⏱  Stopwatch started — press Ctrl+C to stop\n")

    start   = time.time()
    elapsed = 0

    try:
        while True:
            elapsed  = int(time.time() - start)
            sys.stdout.write(f"\r  Elapsed: {format_time(elapsed)}  ")
            sys.stdout.flush()
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

    print(f"\n\n  Stopped at: {format_time(elapsed)}")

# ── main menu ─────────────────────────────────────────────────────────────────

def show_menu():
    print("\n" + "─" * 44)
    print("  ⏳  countdown timer")
    print("─" * 44)
    print("  1.  Quick timer")
    print("  2.  Pomodoro mode")
    print("  3.  Multi-timer (queue)")
    print("  4.  Stopwatch")
    print("  0.  Exit")
    print("─" * 44)

def main():
    print("\n  Welcome to countdown timer!")
    print("  Time formats accepted: 90  |  1:30  |  2m30s  |  1h")

    while True:
        show_menu()
        choice = input("\n  Pick a mode: ").strip()

        if choice == "1":
            raw   = input("\n  Enter duration (e.g. 90, 1:30, 2m30s): ").strip()
            label = input("  Label (optional, press Enter to skip): ").strip()
            label = label if label else "Timer"
            warn  = input("  Warn at N seconds left? (default 10): ").strip()
            warn  = int(warn) if warn.isdigit() else 10

            try:
                secs = parse_input(raw)
                if secs <= 0:
                    print("  Please enter a time greater than 0.")
                    continue
                run_countdown(label, secs, warn_at=warn)
            except ValueError:
                print("  Could not parse that format. Try: 90 / 1:30 / 2m30s")

        elif choice == "2":
            run_pomodoro()

        elif choice == "3":
            run_multi_timer()

        elif choice == "4":
            run_stopwatch()

        elif choice == "0":
            print("\n  Goodbye!\n")
            break

        else:
            print("  Invalid choice. Pick 0–4.")

        again = input("\n  Back to menu? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Goodbye!\n")
            break

if __name__ == "__main__":
    main()