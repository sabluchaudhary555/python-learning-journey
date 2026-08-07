# Python Loops — Short Notes

## 1. What Are Loops?
- Execute a block of code repeatedly until a condition ends or a sequence is exhausted.
- **Types:** `for` (iterate over a sequence), `while` (run while condition is True)
- **Control statements:** `break`, `continue`, `pass`

---

## 2. `for` Loop
Iterates over a sequence (list, tuple, string, range, dict, set) — no manual index handling needed.
```python
for i in ["Geeks", "for", "Geeks"]:
    print(i)
```

### Index Iteration
```python
for idx in range(len(a)):
    print(a[idx])
```

### String Iteration
```python
for ch in "Geeks":
    print(ch)
```

### `range()` Function
| Form | Meaning |
|---|---|
| `range(stop)` | 0 to stop-1 |
| `range(start, stop)` | start to stop-1 |
| `range(start, stop, step)` | custom step (negative = countdown) |

```python
range(0, 10, 2)    # 0 2 4 6 8
range(5, 0, -1)     # 5 4 3 2 1
```

### `enumerate()` — index + value together
```python
for i, v in enumerate(b, start=1):   # start optional, default 0
    print(i, v)
```

### `else` with `for`
- Runs **only if the loop finishes without `break`**.
```python
for i in range(1, 4):
    print(i)
else:
    print("No Break")   # runs — no break hit
```

---

## 3. `while` Loop
Runs as long as the condition is `True`; condition checked **before** every iteration.
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

### Infinite Loop
```python
while True:
    print("runs forever")   # needs break to exit
```
⚠️ Always ensure the condition can become False, or use `break` — otherwise the program freezes.

### `else` with `while`
- Runs only when the condition becomes False naturally (not via `break`).

---

## 4. Loop Control Statements

### `break`
- Exits the loop **immediately**; skips remaining iterations and the loop's `else`.
```python
for i in range(5):
    if i == 3:
        break
    print(i)   # 0 1 2
```

### `continue`
- Skips the rest of the **current** iteration only; loop continues.
```python
for i in range(5):
    if i == 3:
        continue
    print(i)   # 0 1 2 4
```
⚠️ In `while` loops, increment the counter **before** `continue`, or it becomes infinite.

### `pass`
- Does nothing — a placeholder where a statement is syntactically required.
- Loop continues normally; nothing is skipped.
```python
def future_function():
    pass   # to be implemented later
```

### Quick Comparison
| Statement | What it Does | Loop Ends? | Iteration Skipped? |
|---|---|---|---|
| `break` | Exits loop immediately | ✅ Yes | ✅ Yes (all remaining) |
| `continue` | Skips current iteration | ❌ No | ✅ Yes (current only) |
| `pass` | Does nothing | ❌ No | ❌ No |

---

## 5. Nested Loops
- A loop inside another — inner loop runs **completely** for every outer iteration.
- Total iterations = outer × inner.
```python
for i in x:
    for j in y:
        print(i, j)
```

### Pattern Printing Example
```python
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
# 1
# 2 2
# 3 3 3
# 4 4 4 4
```

### `break` / `continue` in Nested Loops
- Both only affect the **innermost** loop — outer loop keeps running.

### Single-Line Nested Loop (List Comprehension)
```python
l1 = [[j for j in range(3)] for i in range(5)]
```

---

## 6. `for` vs `while`

| Feature | `for` Loop | `while` Loop |
|---|---|---|
| Use when | Number of iterations known | Condition-based |
| Iterates over | Sequences/iterables | Boolean condition |
| Counter | Automatic | Manual |
| Infinite loop risk | Very low | High if condition never False |
| Best for | Lists, strings, ranges | User input, waiting for events |

---

## 7. Practical Examples
```python
# Sum of 1-10
total = 0
for i in range(1, 11):
    total += i               # 55

# Fibonacci under 100
a, b = 0, 1
while a < 100:
    print(a, end=" ")
    a, b = b, a + b

# Search with for + else
for n in numbers:
    if n == target:
        print("Found")
        break
else:
    print("Not found")

# Skip even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")        # 1 3 5 7 9
```

---

## 📋 Cheat Sheet

| Concept | Syntax | Key Point |
|---|---|---|
| for loop | `for i in seq:` | Iterates over every item |
| for with range | `for i in range(n):` | Runs n times (0 to n-1) |
| range(start,stop,step) | `range(0,10,2)` | Custom start, end, step |
| Index iteration | `for i in range(len(a)):` | Access by index |
| String iteration | `for ch in "text":` | One character per iteration |
| enumerate() | `for i, v in enumerate(seq):` | Index + value together |
| while loop | `while condition:` | Runs while condition is True |
| Infinite loop | `while True:` | Runs forever — use break to exit |
| break | `break` | Exit loop immediately |
| continue | `continue` | Skip current iteration |
| pass | `pass` | Do nothing — placeholder |
| else with loop | `for/while ... else:` | Runs if loop ends without break |
| Nested loop | loop inside loop | Inner runs fully per outer iteration |
| break in nested | `break` | Exits innermost loop only |
| Single-line nested | `[expr for i in s for j in s]` | List comprehension |
| Countdown | `range(5, 0, -1)` | 5 4 3 2 1 |
| Sum with loop | `total += i` | Accumulate values |