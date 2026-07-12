# countdown-timer ⏳

> A terminal countdown timer with 4 modes — quick timer, Pomodoro,
> multi-timer queue, and stopwatch. No libraries needed beyond Python stdlib.

---

## Features

| Mode | What it does |
|---|---|
| **Quick timer** | Single countdown with live progress bar and warning |
| **Pomodoro** | Configurable work/break cycles with long break every 4 sessions |
| **Multi-timer** | Queue multiple named timers, runs them back to back |
| **Stopwatch** | Count up — stop with Ctrl+C |

---

## Install & Run

```bash
# no dependencies — pure Python stdlib
python timer.py
```

Requires Python 3.6+ (uses f-strings)

---

## Time Formats Accepted

All of these mean the same thing or similar:

```
90           → 1 minute 30 seconds (plain seconds)
1:30         → 1 minute 30 seconds
2m30s        → 2 minutes 30 seconds
1h30m        → 1 hour 30 minutes
1h30m20s     → 1 hour 30 minutes 20 seconds
45s          → 45 seconds
2h           → 2 hours
```

---

## Output

### Quick timer

```
  Timer : Study session
  Total : 25:00

  🟢  24:47   [████░░░░░░░░░░░░░░░░░░░░░░░░░░]  1%

  ⚠️   00:08   [█████████████████████████████░]  98%

  ✅  'Study session' — done!
```

### Pomodoro mode

```
  How many pomodoro sessions? (default 4): 4
  Work duration in minutes? (default 25): 25
  Short break in minutes?   (default 5): 5
  Long break in minutes?    (default 15): 15

  Starting 4 pomodoro session(s)...

  ──── Session 1/4 ────
  🟢  24:55   [█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]  0%
  ...
  ✅  'Work block 1' — done!

  ☕  Short break time!
  ...
  🎉  4 sessions done! Taking a long break...

  ── Pomodoro Summary ──────────────────
  Sessions completed : 4/4
  Total work time    : 01:40:00
```

### Multi-timer queue

```
  Add timers one by one. Leave name blank to start.

  Timer 1 name (or Enter to start): Warm up
  Duration for 'Warm up' (e.g. 2m, 1:30, 90): 5m
  Added: Warm up — 05:00

  Timer 2 name (or Enter to start): Main workout
  Duration for 'Main workout' (e.g. 2m, 1:30, 90): 20m
  Added: Main workout — 20:00

  Timer 3 name (or Enter to start): Cool down
  Duration for 'Cool down' (e.g. 2m, 1:30, 90): 5m
  Added: Cool down — 05:00

  Timer 4 name (or Enter to start):

  3 timer(s) queued — total time: 30:00

  [1/3] Timer : Warm up ...
  [2/3] Timer : Main workout ...
  [3/3] Timer : Cool down ...
```

### Stopwatch

```
  ⏱  Stopwatch started — press Ctrl+C to stop

  Elapsed: 01:23

  Stopped at: 01:23
```

---

## Python Variables Concepts Used

| Concept | Where it shows up |
|---|---|
| Variable assignment | `remaining = total_seconds`, `start_time = time.time()` |
| Dynamic typing | `total` starts as `int`, reassigned from different parse branches |
| Multiple assignment | `hours, minutes, secs = ...` in `format_time()` |
| Reassignment in loop | `remaining -= 1` every second — core of the countdown |
| Type casting | `int(input(...))`, `int(time.time() - start)` |
| `+=` running total | `total_elapsed += work_secs`, `completed += 1` |
| `f-strings` | All terminal output uses f-string formatting |
| `type()` / `isinstance()` | `warn.isdigit()` checks before `int()` cast |
| Object references | `timers` list accumulates `(name, secs)` tuples |
| `del` / scope | `remaining` resets cleanly per `run_countdown()` call |

---

## File Structure

```
countdown-timer/
├── timer.py       ← main script
└── README.md      ← this file
```

---

## Requirements

- Python 3.6+
- No external packages — uses only `time`, `sys`, `os`, `re` from stdlib

---

> **Tip:** Use Pomodoro mode for study sessions — 25 min focus,
> 5 min break, and a longer 15 min break every 4 sessions.
> Backed by research on sustained concentration.

---

