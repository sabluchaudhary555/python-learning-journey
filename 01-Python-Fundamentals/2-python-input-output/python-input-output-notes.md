# Python Input & Output Operations — Short Notes

## 1. The `input()` Function
- Reads input from console, **always returns a string**.
```python
name = input("Enter your name: ")
```

| Feature | Description |
|---|---|
| Return Type | Always `str` |
| Blocking | Waits for Enter key |
| Prompt | Optional display message |
| Whitespace | Preserved (leading/trailing spaces) |

⚠️ Even numbers typed by user come back as strings — must convert to use as numbers.
```python
num = input("Enter a number: ")   # "42"
num + 5   # TypeError - str + int
```

---

## 2. Type Conversion with `input()`
```python
age = int(input("Enter your age: "))       # str -> int
price = float(input("Enter price: "))       # str -> float
```

**Safe conversion:**
```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input! Please enter a number.")
```

---

## 3. Taking Multiple Inputs

**Separate calls:**
```python
name = input("Name: ")
age = int(input("Age: "))
```

**Single line with `split()`:**
```python
x, y = input("Enter two numbers: ").split()   # "10 20" -> x='10', y='20'
```

**With type conversion via `map()`:**
```python
x, y = map(int, input("Enter two numbers: ").split())
print(x + y)
```

**Custom delimiter:**
```python
values = input("Enter (comma-separated): ").split(',')
values = [v.strip() for v in input("Enter: ").split(',')]   # strip extra spaces
```
> `split()` always returns strings — use `map()` to convert.

---

## 4. The `print()` Function
Outputs data to console (or a file).

**Syntax:**
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

| Parameter | Default | Description |
|---|---|---|
| `*objects` | — | Values to print |
| `sep` | `' '` | Separator between objects |
| `end` | `'\n'` | Appended after output |
| `file` | `sys.stdout` | Output destination |
| `flush` | `False` | Force immediate output |

```python
print("Name:", "Alice", "Age:", 25)   # Name: Alice Age: 25
```

---

## 5. `print()` Parameters in Detail

### `sep`
```python
print("2024", "03", "07", sep="-")     # 2024-03-07
print("H","e","l","l","o", sep="")     # Hello
```

### `end`
```python
print("Hello", end=" ")
print("World")                          # Hello World (same line)

for i in range(5):
    print(i, end=" ")                    # 0 1 2 3 4
```

### Printing to a File
```python
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)
```

### `flush` — Immediate Output
- Python buffers output by default; `flush=True` forces it to show immediately.
- Use for: progress bars, real-time logging, long-running loops.
```python
print(f"Counting: {i}", flush=True)
```

---

## 6. String Formatting

### Method 1: f-strings (✅ Recommended, Python 3.6+)
```python
print(f"{name} is {age} years old")
print(f"Price: ${price:.2f}")            # 2 decimal places
print(f"Population: {population:,}")     # thousands separator
print(f"|{name:>10}|")                    # right-align
print(f"|{name:<10}|")                    # left-align
print(f"|{name:^10}|")                    # center
print(f"{text.upper()} has {len(text)} letters")   # expressions/method calls inline
```

### Method 2: `.format()` (legacy, still fine)
```python
"{} is {}".format(name, age)
"{0} is {1}, {0} lives in NYC".format(name, age)   # positional
"{name} is {age}".format(name="Bob", age=30)        # named
```

### Method 3: `%` Formatting (❌ outdated)
```python
"Name: %s, Age: %d" % (name, age)
```

### Method 4: String Concatenation (❌ error-prone)
```python
"Name: " + name + ", Age: " + str(age)   # must convert numbers manually
```

### Comparison
| Method | Version | Readability | Recommended? |
|---|---|---|---|
| f-strings | 3.6+ | ⭐⭐⭐⭐⭐ | ✅ Yes |
| `.format()` | 2.7+ | ⭐⭐⭐⭐ | ✅ Legacy code |
| `%` formatting | All | ⭐⭐ | ❌ No |
| Concatenation | All | ⭐ | ❌ No |

---

## 7. Common Patterns
```python
# Simple calculator
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
print(f"Sum: {num1 + num2}")
print(f"Division: {num1 / num2:.2f}")

# Progress bar
for i in range(total + 1):
    percent = (i / total) * 100
    print(f"\rProgress: {percent:.0f}%", end="", flush=True)
```

---

## 📋 Quick Recap
| Concept | Key Point |
|---|---|
| `input()` | Always returns a string, needs explicit conversion |
| `int()/float()` | Convert input to number types |
| `split()` | Splits input line into multiple values (as strings) |
| `map()` | Applies conversion (int/float) to split values |
| `print()` | `sep` controls separator, `end` controls line ending |
| `flush=True` | Forces immediate output — real-time feedback |
| f-strings | Best/modern way to format strings — supports `.2f`, `,`, alignment |
| Best Practice | Use f-strings + try-except for safe conversion + meaningful prompts |