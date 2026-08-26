# Python Functions — Lambda, map(), filter(), reduce(), Inner Functions & Decorators

## 1. Lambda Functions
A lambda function is a small, anonymous, single-expression function used to pass simple logic somewhere without writing a full `def` block; its expression's result is returned automatically, with no `return` keyword.
- One expression only — no statements, loops, or multiple lines
- No name required, though it can be assigned to a variable

**Syntax**
```python
lambda arguments: expression
```

```python
square = lambda x: x * x
print(square(6))
# Output: 36
```

## 2. Lambda With Conditional Expressions
A lambda can branch using an inline `if...else` conditional expression to return different results based on a condition.

```python
grade = lambda score: "Pass" if score >= 40 else "Fail"
print(grade(55))
print(grade(30))
# Output: Pass
# Output: Fail
```

## 3. Lambda With List Comprehension
Lambdas can be generated in bulk with a list comprehension; using a default argument to "lock in" the loop variable's current value avoids the common late-binding closure bug.

```python
adders = [lambda n, x=x: n + x for x in range(3)]
print([f(10) for f in adders])
# Output: [10, 11, 12]
```

## 4. Lambda Returning Multiple Results
A lambda's single expression can still return multiple values by packing them into a tuple.

```python
stats = lambda a, b: (a + b, a - b)
print(stats(10, 4))
# Output: (14, 6)
```

## 5. The `filter()` Function
`filter()` extracts elements from an iterable for which a given function returns `True`, discarding the rest; it returns a lazy `filter` object that must be wrapped (e.g. in `list()`) to view.

**Syntax**
```python
filter(function, iterable)
```

```python
nums = [10, 15, 22, 33, 40]
evens = filter(lambda n: n % 2 == 0, nums)
print(list(evens))
# Output: [10, 22, 40]
```

## 6. `filter()` With `None`
Passing `None` as the function tells `filter()` to keep only the truthy values of the iterable, dropping falsy ones like `""`, `None`, `0`, and `False`.

```python
mixed = ["data", "", 0, "ready", None, False]
cleaned = filter(None, mixed)
print(list(cleaned))
# Output: ['data', 'ready']
```

## 7. The `map()` Function
`map()` applies a given function to every element of one or more iterables and returns a lazy `map` object, useful for uniform element-wise transformations without writing an explicit loop.

**Syntax**
```python
map(function, iterable, ...)
```

```python
prices = [100, 250, 999]
with_tax = map(lambda p: round(p * 1.18, 2), prices)
print(list(with_tax))
# Output: [118.0, 295.0, 1178.82]
```

## 8. `map()` With Multiple Iterables
If the function takes more than one argument, `map()` can pull one value from each of several iterables in parallel, on each step.

```python
a = [1, 2, 3]
b = [10, 20, 30]
combined = map(lambda x, y: x * y, a, b)
print(list(combined))
# Output: [10, 40, 90]
```

## 9. The `reduce()` Function
`reduce()` (from `functools`) cumulatively applies a two-argument function across an iterable, combining elements pairwise until a single final value remains.

**Syntax**
```python
from functools import reduce
reduce(function, iterable[, initializer])
```

```python
from functools import reduce

nums = [3, 7, 2, 9, 4]
largest = reduce(lambda a, b: a if a > b else b, nums)
print(largest)
# Output: 9
```

## 10. `reduce()` vs `accumulate()`
Both apply a function cumulatively across a sequence, but `reduce()` (functools) returns only the single final value, while `accumulate()` (itertools) returns an iterator of every intermediate result.

```python
from itertools import accumulate
from operator import mul

nums = [1, 2, 3, 4]
running_product = accumulate(nums, mul)
print(list(running_product))
# Output: [1, 2, 6, 24]
```

## 11. `def` vs `lambda`
A `def` function has a name, can hold multiple statements, and needs an explicit `return`; a `lambda` is anonymous, limited to a single expression, and returns its result automatically — best for short, throwaway logic passed into things like `sorted()` or `map()`.
- `def` → reusable, documented, supports docstrings
- `lambda` → quick, inline, no docstring support

```python
students = [("Amit", 82), ("Sara", 91), ("Neel", 75)]
top_student = max(students, key=lambda s: s[1])
print(top_student)
# Output: ('Sara', 91)
```

## 12. Inner (Nested) Functions
An inner function is defined inside another function — used for encapsulating helper logic, keeping related code together, and enabling closures/decorators, since it can freely read the enclosing function's variables.

```python
def send_report(name):
    def format_header():
        return f"--- Report for {name} ---"
    print(format_header())

send_report("Q3")
# Output: --- Report for Q3 ---
```

## 13. LEGB Scope in Inner Functions
Inner functions resolve names using Local → Enclosing → Global → Built-in lookup; reading an enclosing variable needs nothing special, but modifying it requires `nonlocal`.

```python
def bank_account(balance):
    def withdraw(amount):
        nonlocal balance
        balance -= amount
        return balance
    return withdraw

pay = bank_account(1000)
print(pay(300))
print(pay(200))
# Output: 700
# Output: 500
```

## 14. Decorators
A decorator is a function that takes another function as input and returns a new function with added behavior, without changing the original function's source code — commonly used for logging, authentication, and caching. `@decorator` above a function is shorthand for `func = decorator(func)`.

**Syntax**
```python
def decorator_name(func):
    def wrapper(*args, **kwargs):
        # extra behavior
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorator_name
def some_function():
    ...
```

```python
def timer_log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@timer_log
def add(a, b):
    return a + b

print(add(4, 6))
# Output: Calling add
# Output: 10
```

## 15. Method Decorators
A decorator applied to a method inside a class must account for the `self` parameter, forwarding it along with any other arguments to the wrapped method.

```python
def log_call(func):
    def wrapper(self, *args, **kwargs):
        print(f"Method {func.__name__} called")
        return func(self, *args, **kwargs)
    return wrapper

class Calculator:
    @log_call
    def square(self, n):
        return n * n

calc = Calculator()
print(calc.square(5))
# Output: Method square called
# Output: 25
```

## 16. Class Decorators
A class decorator takes a class itself as its argument and returns a (possibly modified) version of that class, rather than wrapping a function.

```python
def add_greeting(cls):
    cls.greeting = f"Hello from {cls.__name__}"
    return cls

@add_greeting
class Robot:
    pass

print(Robot.greeting)
# Output: Hello from Robot
```

## 17. Chaining Multiple Decorators
Several decorators can be stacked on one function; they apply bottom-up, meaning the decorator closest to the function runs first, and swapping the stacking order changes the final result.

```python
def add_ten(func):
    def wrapper():
        return func() + 10
    return wrapper

def double(func):
    def wrapper():
        return func() * 2
    return wrapper

@add_ten
@double
def base():
    return 5

print(base())
# Output: 20
```

## 18. Built-in Decorators — `@staticmethod`, `@classmethod`, `@property`
`@staticmethod` defines a method that doesn't use the instance (`self`) or class (`cls`); `@classmethod` operates on the class itself via `cls`, affecting class-level state; `@property` lets a method be accessed like a plain attribute, optionally paired with a setter for validated assignment.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0

t = Temperature(25)
print(t.fahrenheit)
print(Temperature.is_freezing(-2))
# Output: 77.0
# Output: True
```