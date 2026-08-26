# Python Variables — Short Notes

## 1. What is a Variable?
- A name that refers to a value stored in memory — like a label on a box.
- No explicit type declaration needed — Python infers type from the assigned value.
- Created the moment a value is assigned.
```python
x = 5
name = "Hacker"
```

---

## 2. Rules for Naming Variables
| Rule | Valid | Invalid |
|---|---|---|
| Letters, digits, underscore only | `user_1` | `user-1` (hyphen) |
| Cannot start with a digit | `_score` | `1score` |
| Case-sensitive | `Name ≠ name` | — |
| Cannot use keywords | `total` | `class`, `if` |

> `myVar`, `myvar`, `MYVAR` are three **different** variables — Python is case-sensitive.

---

## 3. Assigning Values

### Basic Assignment
- `=` means "store this value", not "equal to".
```python
x = 5
```

### Dynamic Typing
- Same variable can hold different types over time.
```python
x = 10                # int
x = "Now a string"    # str — valid
```

---

## 4. Multiple Assignments

**Same value to multiple variables:**
```python
a = b = c = 100
```

**Different values in one line (tuple unpacking):**
```python
x, y, z = 1, 2.5, "Python"
```

**Fibonacci-style swap (no temp variable):**
```python
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b
```
> Right-hand side is fully evaluated **before** any assignment happens — that's why `a, b = b, a+b` works without a temp variable.

---

## 5. Object Reference

- `x = 5` → Python creates an object `5`; `x` stores a **reference** to it (not the value itself).
- `y = x` → `y` points to the **same object**, doesn't copy it.
```python
x = 5
y = x
print(id(x) == id(y))   # True — same object
```

**Reassignment breaks the link:**
```python
x = 5
y = x
x = "Geeks"
print(x)   # Geeks
print(y)   # 5 ← unchanged, y still points to old object
```

**Immutable reassignment doesn't affect other variables:**
```python
x = 1
y = x
y = y + 1
print(x)   # 1 ← unaffected
print(y)   # 2 ← new object created
```

### ⚠️ Lists Behave Differently (Mutable)
```python
rgb = ["Red", "Green", "Blue"]
rgba = rgb            # both point to SAME list
rgba.append("Alpha")
print(rgb)             # also changed! ["Red","Green","Blue","Alpha"]
```
**True copy → use slicing:**
```python
correct = rgba[:]     # shallow copy, independent list
```

---

## 6. The Special `_` Variable (REPL only)
- In interactive mode, `_` auto-stores the **last printed expression**.
```python
>>> 2 + 2
4
>>> _
4
```
> Treat as read-only — don't manually assign to `_`.

---

## 7. Type Checking & Type Casting

### `type()` — check data type
```python
type(x)   # <class 'int'>
```

### `isinstance()` — check instance (True/False)
```python
isinstance(x, int)             # True
isinstance(x, (int, float))    # checks against multiple types
```

### Type Casting Functions
| Function | Converts To | Example |
|---|---|---|
| `int()` | Integer | `int("10") → 10` |
| `float()` | Float | `float(5) → 5.0` |
| `str()` | String | `str(100) → "100"` |
| `bool()` | Boolean | `bool(0) → False` |

```python
print(4 * 3.75)   # 14.0 — int auto-promoted to float in mixed arithmetic
```

---

## 8. Deleting a Variable — `del`
- Removes variable from namespace; object becomes eligible for garbage collection **if nothing else references it**.
```python
x = 10
del x
print(x)   # NameError

# if another variable still references the object, it survives:
x = 5
y = x
del x
print(y)   # 5 ← still works
```

---

## 9. Naming Conventions (PEP 8)
| Convention | Usage | Example |
|---|---|---|
| `snake_case` | Variables, functions | `user_name` |
| `UPPER_SNAKE_CASE` | Constants | `MAX_SIZE` |
| `_single_leading` | Internal/private use | `_helper` |
| `__double_leading` | Name mangling (classes) | `__private` |
| `CamelCase` | Class names only | `MyClass` |

---

## 10. Practical Patterns
```python
# Swap without temp variable
a, b = 5, 10
a, b = b, a                     # 10 5

# String length
length = len("Python")           # 6

# Running total
total = 0
total += 10
total += 20                      # 30

# Chained comparison
x = 15
print(10 < x < 20)               # True
```

---

## 📋 Quick Recap
| Concept | Key Point |
|---|---|
| Variable | Label pointing to an object in memory, no type declaration needed |
| Naming rules | Letters/digits/underscore, no digit-start, no keywords, case-sensitive |
| Dynamic typing | Same variable can change type over time |
| Multiple assignment | `a=b=c=val` or `x,y,z = 1,2,3` |
| Object reference | Variables store references, not values |
| Mutable objects (list) | Shared reference — changes reflect across all pointers |
| Immutable objects (int/str) | Reassignment creates a new object, old references unaffected |
| `del` | Removes variable; object GC'd only if no other reference exists |
| `type()` / `isinstance()` | Check data type / check instance type |
| Type casting | `int()`, `float()`, `str()`, `bool()` |
| PEP 8 | `snake_case` vars, `UPPER_CASE` constants, `CamelCase` classes |