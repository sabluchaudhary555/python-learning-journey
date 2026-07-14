# Python — Variables

> One concept. One example. No fluff.

---

## What is a Variable?

A label that points to a value stored in memory. No type declaration needed — Python infers it.

```python
x    = 5
name = "Hacker"
print(x)      # 5
print(name)   # Hacker
```

---

## Naming Rules

| Rule | Valid | Invalid |
|---|---|---|
| Letters, digits, underscore only | `user_1` | `user-1` |
| Cannot start with a digit | `_score` | `1score` |
| Case-sensitive | `name` ≠ `Name` | — |
| No Python keywords | `total` | `class`, `if`, `for` |

```python
age         = 21     # ✓
_colour     = "red"  # ✓
total_score = 90     # ✓

# 1name = "x"     ❌ starts with digit
# class = 10      ❌ reserved keyword
# user-name = "x" ❌ hyphen not allowed
```

---

## Assigning Values

```python
x = 5          # int
y = 3.14       # float
z = "Hello"    # str
```

**Dynamic typing** — same variable can change type:

```python
x = 10               # int
x = "Now a string"   # str — perfectly valid
```

---

## Multiple Assignments

```python
# same value to multiple variables
a = b = c = 100
print(a, b, c)        # 100 100 100

# different values in one line (tuple unpacking)
x, y, z = 1, 2.5, "Python"
print(x, y, z)        # 1 2.5 Python

# swap without a temp variable
a, b = 5, 10
a, b = b, a
print(a, b)           # 10 5
```

> Right-hand side is fully evaluated **before** any assignment happens — that's why swap works.

---

## Object References

Variables are **labels pointing to objects**, not containers holding values.

```python
x = 5       # x ──► [object: 5]
y = x       # y ──► same object

print(id(x) == id(y))   # True — same memory address
```

**Reassignment breaks the link:**

```python
x = 5
y = x
x = "Geeks"

print(x)    # Geeks
print(y)    # 5  ← unchanged, still points to original object
```

**⚠️ Mutable objects (lists) behave differently:**

```python
rgb  = ["Red", "Green", "Blue"]
rgba = rgb              # both point to same list

rgba.append("Alpha")
print(rgb)              # ["Red", "Green", "Blue", "Alpha"] ← rgb changed too!

# to make a true independent copy
correct = rgba[:]       # shallow copy
correct[-1] = "X"
print(rgba)             # unchanged
```

---

## The `_` Variable (REPL only)

In interactive mode, `_` stores the last printed result:

```python
>>> 2 + 2
4
>>> _           # 4

>>> 100 * 0.125
12.5
>>> 100 + _     # 112.5
```

> Treat `_` as read-only. Don't assign to it manually.

---

## Type Checking

```python
x = 10
y = 3.14
z = "hello"

print(type(x))              # <class 'int'>
print(type(y))              # <class 'float'>
print(type(z))              # <class 'str'>

print(isinstance(x, int))           # True
print(isinstance(x, str))           # False
print(isinstance(x, (int, float)))  # True — check multiple types at once
```

---

## Type Casting

| Function | Converts to | Example |
|---|---|---|
| `int()` | Integer | `int("10")` → `10` |
| `float()` | Float | `float(5)` → `5.0` |
| `str()` | String | `str(100)` → `"100"` |
| `bool()` | Boolean | `bool(0)` → `False` |

```python
print(float(5))     # 5.0
print(int("42"))    # 42
print(str(100))     # "100"
print(4 * 3.75)     # 15.0 ← int auto-promoted to float in mixed arithmetic
```

---

## Deleting a Variable — del

```python
x = 10
del x
print(x)    # NameError: name 'x' is not defined
```

```python
x = 5
y = x
del x
print(y)    # 5 ← y still works — object not collected while y points to it
```

---

## Naming Conventions (PEP 8)

| Convention | Used for | Example |
|---|---|---|
| `snake_case` | Variables, functions | `user_name`, `total_score` |
| `UPPER_SNAKE_CASE` | Constants | `MAX_SIZE`, `PI` |
| `_single_leading` | Internal / private | `_helper` |
| `__double_leading` | Name mangling (classes) | `__private` |
| `CamelCase` | Class names only | `MyClass` |

```python
user_age      = 22       # variable
MAX_RETRIES   = 3        # constant
_internal_flag = True    # private/internal
```

---

## Practical Patterns

```python
# swap two variables
a, b = 5, 10
a, b = b, a
print(a, b)           # 10 5

# running total
total  = 0
total += 10
total += 20
print(total)          # 30

# chained comparison
x = 15
print(10 < x < 20)   # True

# fibonacci using multiple assignment
a, b = 0, 1
while a < 100:
    print(a, end=", ")
    a, b = b, a + b
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
```