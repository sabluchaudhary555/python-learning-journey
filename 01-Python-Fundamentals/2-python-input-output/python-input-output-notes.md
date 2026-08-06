# Python Input & Output Operations

Notes on reading user input, converting types, and formatting console output in Python.

---

## Table of Contents

- [1. The `input()` Function](#1-the-input-function)
- [2. Type Conversion with `input()`](#2-type-conversion-with-input)
- [3. Taking Multiple Inputs](#3-taking-multiple-inputs)
- [4. The `print()` Function](#4-the-print-function)
- [5. `print()` Parameters in Detail](#5-print-parameters-in-detail)
- [6. String Formatting in Python](#6-string-formatting-in-python)
- [7. Common Use Cases](#7-common-use-cases)
- [Best Practices](#best-practices)

---

## 1. The `input()` Function

`input()` reads user input from the console and always returns it as a **string**. It's the primary way to make Python programs interactive.

### Syntax

```python
variable = input(prompt)
```

- **prompt** *(optional)* — string displayed to the user before input
- **Returns** — user input as a string

### Basic Usage

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Output:
# Enter your name: Alice
# Hello, Alice!
```

### Key Characteristics

| Feature       | Description                                  |
|---------------|-----------------------------------------------|
| Return Type   | Always returns a string                       |
| Blocking      | Waits for user to press Enter before continuing |
| Prompt        | Optional message to display to the user       |
| Input Reading | Reads entire line until Enter is pressed      |
| Whitespace    | Preserves leading/trailing spaces             |

### Important Notes

```python
# input() always returns a string
age = input("Enter your age: ")
print(type(age))  # <class 'str'>

# Even if user types a number
num = input("Enter a number: ")  # User types: 42
print(type(num))                  # <class 'str'>
print(num + 5)                    # TypeError: can only concatenate str to str
```

> **Important:** `input()` always returns a string, even if the user enters numbers. You must convert (typecast) to use as numbers.

---

## 2. Type Conversion with `input()`

### Converting String Input to Other Types

```python
# Convert to integer
age = int(input("Enter your age: "))
print(type(age))        # <class 'int'>
print(age + 5)          # Works! Adds 5 to the number

# Convert to float
price = float(input("Enter price: "))
print(type(price))      # <class 'float'>

# No conversion (keep as string)
name = input("Enter your name: ")
print(type(name))       # <class 'str'>
```

### Safe Type Conversion with Error Handling

```python
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Invalid input! Please enter a number.")

# Example run with invalid input:
# Enter your age: twenty
# Invalid input! Please enter a number.
```

### Type Conversion Examples

| Input Type Needed | Code Example                          | User Input | Result         |
|--------------------|----------------------------------------|-------------|----------------|
| String             | `name = input("Name: ")`              | Alice       | `"Alice"` (str) |
| Integer            | `age = int(input("Age: "))`           | 25          | `25` (int)      |
| Float              | `price = float(input("Price: "))`     | 19.99       | `19.99` (float) |
| Boolean            | `bool(input("Enter: "))`              | yes         | `True` (non-empty) |

---

## 3. Taking Multiple Inputs

### Method 1: Separate `input()` Calls

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print(f"Name: {name}, Age: {age}, City: {city}")
```

### Method 2: Single Line with `split()`

`split()` divides a string into a list based on whitespace (or a specified delimiter).

```python
# Taking two inputs
x, y = input("Enter two numbers: ").split()
print(f"x = {x}, y = {y}")
# User input: 10 20
# Output: x = 10, y = 20

# Taking three inputs
a, b, c = input("Enter three values: ").split()
print(f"a = {a}, b = {b}, c = {c}")
# User input: apple banana cherry
# Output: a = apple, b = banana, c = cherry
```

### Method 3: Multiple Inputs with Type Conversion

```python
# Convert to integers
x, y = map(int, input("Enter two numbers: ").split())
print(f"Sum: {x + y}")
# User input: 10 20
# Output: Sum: 30

# Convert to floats
a, b, c = map(float, input("Enter three decimals: ").split())
print(f"Average: {(a + b + c) / 3}")
# User input: 1.5 2.5 3.0
# Output: Average: 2.333333
```

### Method 4: Custom Delimiter

```python
# Split by comma
values = input("Enter values (comma-separated): ").split(',')
print(values)
# User input: red, green, blue
# Output: ['red', ' green', ' blue']

# Split and strip whitespace
values = [x.strip() for x in input("Enter values: ").split(',')]
print(values)
# User input: red, green, blue
# Output: ['red', 'green', 'blue']
```

> **Note:** `split()` always returns strings. Convert to `int`/`float` using `map()` if needed.

---

## 4. The `print()` Function

`print()` outputs data to the console (or a file). It's the primary way to display results in Python.

### Syntax

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

### Parameters Explained

| Parameter  | Type       | Default        | Description                                  |
|------------|------------|----------------|-----------------------------------------------|
| `*objects` | Any        | —              | One or more objects to print (converted to strings) |
| `sep`      | str        | `' '` (space)  | Separator between multiple objects            |
| `end`      | str        | `'\n'` (newline) | String appended after the output            |
| `file`     | file object| `sys.stdout`   | Output destination (console by default)       |
| `flush`    | bool       | `False`        | Forces immediate output (bypasses buffer)      |

### Basic Usage

```python
print("Hello, World!")
# Output: Hello, World!

print("Name:", "Alice", "Age:", 25)
# Output: Name: Alice Age: 25

name = "Bob"
age = 30
print(name, age)
# Output: Bob 30
```

---

## 5. `print()` Parameters in Detail

### 5.1 Using `sep` (Separator)

```python
print("a", "b", "c")
# Output: a b c

print("a", "b", "c", sep=", ")
# Output: a, b, c

print("2024", "03", "07", sep="-")
# Output: 2024-03-07

print("Python", "is", "awesome", sep=" | ")
# Output: Python | is | awesome

print("H", "e", "l", "l", "o", sep="")
# Output: Hello
```

### 5.2 Using `end` (End Character)

```python
print("Hello")
print("World")
# Output:
# Hello
# World

print("Hello", end=" ")
print("World")
# Output: Hello World

print("a", "b", "c", sep=", ", end="!")
# Output: a, b, c!

for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4
```

### 5.3 Printing to a File

```python
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)
    print("This is line 2", file=f)

# output.txt now contains:
# Hello, file!
# This is line 2
```

### 5.4 Using `flush` (Immediate Output)

By default, Python buffers output (stores it temporarily before displaying). `flush=True` forces immediate display.

```python
import time

# Without flush (buffered)
for i in range(3):
    print(f"Counting: {i}")
    time.sleep(1)
# Output appears all at once after 3 seconds

# With flush (immediate)
for i in range(3):
    print(f"Counting: {i}", flush=True)
    time.sleep(1)
# Output appears immediately, one per second
```

**When to use `flush=True`:**
- Progress bars
- Real-time logging
- Long-running operations
- When you need immediate visual feedback

**How flush works:**
- Normally, Python buffers output (holds it in memory)
- `flush=True` forces immediate display, bypassing the buffer
- Useful for real-time feedback in loops or time-sensitive operations

---

## 6. String Formatting in Python

String formatting creates dynamic, readable output by embedding variables and expressions inside strings.

### Method 1: f-strings (Formatted String Literals) — ✅ Recommended

Python 3.6+ — the most modern and readable way to format strings.

```python
name = "Alice"
age = 25
city = "New York"

# Basic f-string
print(f"Name: {name}, Age: {age}")
# Output: Name: Alice, Age: 25

# Expressions inside f-strings
print(f"In 5 years, {name} will be {age + 5}")
# Output: In 5 years, Alice will be 30

# Multiple variables
print(f"{name} is {age} years old and lives in {city}")
# Output: Alice is 25 years old and lives in New York
```

#### Advanced f-string Features

```python
# Format numbers
price = 19.99
print(f"Price: ${price:.2f}")
# Output: Price: $19.99

# Thousands separator
population = 1234567
print(f"Population: {population:,}")
# Output: Population: 1,234,567

# Padding and alignment
name = "Bob"
print(f"|{name:>10}|")  # Right-align
# Output: |       Bob|

print(f"|{name:<10}|")  # Left-align
# Output: |Bob       |

print(f"|{name:^10}|")  # Center
# Output: |   Bob    |

# Expressions and method calls
text = "python"
print(f"{text.upper()} has {len(text)} letters")
# Output: PYTHON has 6 letters
```

### Method 2: `.format()` Method

```python
name = "Alice"
age = 25

# Basic usage
print("Name: {}, Age: {}".format(name, age))
# Output: Name: Alice, Age: 25

# Positional arguments
print("{0} is {1} years old. {0} lives in NYC.".format(name, age))
# Output: Alice is 25 years old. Alice lives in NYC.

# Named arguments
print("{name} is {age} years old".format(name="Bob", age=30))
# Output: Bob is 30 years old

# Number formatting
print("Price: ${:.2f}".format(19.99))
# Output: Price: $19.99
```

### Method 3: `%` Formatting (Old Style) — ❌ Not Recommended

```python
name = "Alice"
age = 25

print("Name: %s, Age: %d" % (name, age))
# Output: Name: Alice, Age: 25

print("Price: $%.2f" % 19.99)
# Output: Price: $19.99
```

### Method 4: String Concatenation (Simple Cases)

```python
name = "Alice"
age = 25

print("Name: " + name + ", Age: " + str(age))
# Output: Name: Alice, Age: 25

# Need to convert numbers to strings manually
```

### Formatting Comparison Table

| Method         | Python Version | Readability | Performance | Recommended?         |
|----------------|-----------------|--------------|--------------|------------------------|
| f-strings      | 3.6+            | ⭐⭐⭐⭐⭐        | Fast         | ✅ Yes                 |
| `.format()`    | 2.7+            | ⭐⭐⭐⭐         | Medium       | ✅ Yes (legacy code)   |
| `%` formatting | All             | ⭐⭐           | Fast         | ❌ No (outdated)       |
| Concatenation  | All             | ⭐            | Slow         | ❌ No (error-prone)    |

---

## 7. Common Use Cases

### Example 1: User Profile

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print(f"\n--- User Profile ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"You will be {age + 10} in 10 years.")
```

### Example 2: Simple Calculator

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\n--- Results ---")
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Division: {num1 / num2:.2f}")
```

### Example 3: Shopping Cart

```python
item = input("Item name: ")
quantity = int(input("Quantity: "))
price = float(input("Price per item: "))

total = quantity * price

print(f"\n--- Receipt ---")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Price: ${price:.2f}")
print(f"Total: ${total:.2f}")
```

### Example 4: Progress Bar

```python
import time

total = 10
for i in range(total + 1):
    percent = (i / total) * 100
    print(f"\rProgress: {percent:.0f}%", end="", flush=True)
    time.sleep(0.3)
print("\nComplete!")
```

---

