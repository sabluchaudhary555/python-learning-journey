# Python Conditional Statements — Short Notes

## 1. What Are Conditional Statements?
- Control program flow by running certain code **only when a condition is met**.
- Tools: `if`, `if-else`, `if-elif-else`, nested if-else, ternary operator, `match-case` (3.10+).

---

## 2. `if` Statement
- Runs a block only when condition is `True`; skipped otherwise.
```python
age = 20
if age >= 18:
    print("Eligible to vote.")
```
**Shorthand (one-line):**
```python
if age > 18: print("Eligible to Vote.")
```

---

## 3. `if-else`
- One of the two blocks **always** runs.
```python
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")
```

### Ternary (Shorthand if-else)
**Syntax:** `value_if_true if condition else value_if_false`
```python
res = "Pass" if marks >= 40 else "Fail"
```

### Logical Operators with if-else
```python
if age > 23 and exp > 8:
    print("Eligible.")
```

---

## 4. `if-elif-else`
- Checks conditions top to bottom, runs the **first True match** only; `else` is optional.
```python
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
```

---

## 5. Nested if-else
- An `if`/`if-else` placed inside another `if`/`else`.
- Outer condition must be `True` before inner is even checked.
```python
if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
```

---

## 6. Ternary Operator (Conditional Expression)
**Syntax:** `value_if_true if condition else value_if_false`
```python
s = "Adult" if age >= 18 else "Minor"
```
- **Nested ternary** (avoid beyond 2 levels for readability):
```python
result = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
```
- Works inside `lambda` and directly inside `print()`.

---

## 7. `match-case` (Python 3.10+)
- Structural pattern matching — modern alternative to long `if-elif` chains.
- Only the **first matching case** runs, no fall-through.
```python
match number:
    case 1:
        print("One")
    case 2 | 3:              # OR pattern
        print("Two or Three")
    case _:                   # wildcard/default
        print("Other")
```

**Key patterns:**
| Pattern | Example | Matches |
|---|---|---|
| Constant | `case "A":` | Exact value |
| OR | `case 10 \| 20 \| 30:` | Any listed value |
| Guard | `case n if n > 0:` | Pattern + extra condition |
| Sequence | `case [x, y]:` | List/tuple of exact length, unpacks values |
| Dict | `case {"name": name}:` | Dict containing that key, extracts value |
| Class | `case Circle(radius):` | Object type + attrs via `__match_args__` |
| Wildcard | `case _:` | Always matches (default) |

---

## 8. Checking Multiple Conditions
```python
if x > 10 and x < 20: ...      # AND — both True
if x < 10 or x > 12: ...        # OR — at least one True
if not x == 5: ...              # NOT — reverses condition
if 10 < x < 20: ...             # Chained comparison (Python-unique)
```

---

## 9. if-else in Lambda
```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"
classify = lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")
```

---

## 10. `else` with `for`/`while` Loop
- `else` block runs **only if the loop completes without `break`**.
```python
for n in numbers:
    if n == 4:
        print("Found 4")
        break
else:
    print("4 not found in list")   # runs since loop didn't break
```

---

## 📋 Cheat Sheet

| Statement | Syntax | Use When |
|---|---|---|
| if | `if cond:` | Run block only when True |
| if-else | `if cond: ... else:` | Choose between two blocks |
| if-elif-else | `if ... elif ... else:` | Multiple conditions, first match wins |
| Nested if | `if` inside `if` | Multiple criteria checked sequentially |
| Ternary | `val if cond else val` | One-line conditional assignment |
| Nested ternary | `a if c1 else b if c2 else c` | Multiple values in one line |
| Shorthand if | `if cond: statement` | Single-line if (no else) |
| match-case | `match val: case p:` | Pattern matching (3.10+) |
| OR pattern | `case a \| b \| c:` | Match any of multiple values |
| Guard | `case n if n > 0:` | Pattern + extra condition |
| Sequence match | `case [x, y]:` | Match list/tuple by structure |
| Dict match | `case {"key": val}:` | Match dict by keys |
| Class match | `case ClassName(attr):` | Match object type + extract attrs |
| Wildcard | `case _:` | Default — matches anything |
| else with loop | `for ... else:` | Runs if loop didn't break |
| and / or / not | `if a and b:` etc. | Combine/reverse conditions |
| Chained compare | `if 10 < x < 20:` | Range check in one expression |