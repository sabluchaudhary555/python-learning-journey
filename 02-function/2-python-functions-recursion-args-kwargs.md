# Python Functions — Recursion, *args/**kwargs & First-Class Functions

## 1. Recursion
Recursion is when a function calls itself, directly or indirectly, to break a problem into smaller identical sub-problems — useful for math calculations, tree traversal, and divide-and-conquer.
- Base case → stops the recursion
- Recursive case → calls itself with modified (usually smaller) input
- No base case → infinite calls, eventually `RecursionError`

**Syntax**
```python
def recursive_function(parameters):
    if base_case_condition:
        return base_result
    else:
        return recursive_function(modified_parameters)
```

```python
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))
# Output: 10
```

## 2. Tail vs Non-Tail Recursion
Tail recursion is when the recursive call is the last action performed, with no work left after it returns; non-tail recursion still has pending work (like a multiplication) after the call returns.
- Some languages optimize tail recursion into a loop
- Python does **not** perform tail-call optimization — every call still uses a stack frame

```python
def tail_sum(n, acc=0):
    if n == 0:
        return acc
    return tail_sum(n - 1, acc + n)

def nontail_sum(n):
    if n == 0:
        return 0
    return n + nontail_sum(n - 1)

print(tail_sum(5), nontail_sum(5))
# Output: 15 15
```

## 3. Recursion vs Iteration
Recursion solves a problem by having a function call itself, while iteration repeats steps using loops; recursion is generally more memory-hungry and slower, but reads more naturally for problems like tree traversal.
- Recursion: more memory (stack frames), risk of stack overflow, best for divide-and-conquer
- Iteration: less memory, generally faster, best for straightforward repeated steps

```python
def factorial_recursive(n):
    return 1 if n == 0 else n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_recursive(6), factorial_iterative(6))
# Output: 720 720
```

## 4. `*args` — Variable Positional Arguments
`*args` lets a function accept any number of positional arguments, which Python collects into a tuple inside the function.
- Useful when the number of positional values isn't known ahead of time
- `args` is just a naming convention — the `*` is what matters syntactically

```python
def total_price(*prices):
    return sum(prices)

print(total_price(199, 349, 99))
# Output: 647
```

## 5. `**kwargs` — Variable Keyword Arguments
`**kwargs` lets a function accept any number of keyword arguments, collected into a dictionary where parameter names become keys.

```python
def build_profile(**fields):
    return {k.lower(): v for k, v in fields.items()}

print(build_profile(Name="Riya", Age=22))
# Output: {'name': 'Riya', 'age': 22}
```

## 6. Using `*args` and `**kwargs` Together
A single function can take both kinds of variable arguments — plain values land in `*args`, named ones land in `**kwargs`.
- `*args` must come before `**kwargs` in the function definition
- Any named parameter placed after `*args` becomes keyword-only

```python
def log_event(*tags, **meta):
    print("Tags:", tags)
    print("Meta:", meta)

log_event("login", "success", user="admin", retries=0)
# Output: Tags: ('login', 'success')
# Output: Meta: {'user': 'admin', 'retries': 0}
```

## 7. First-Class Functions
In Python, functions are first-class objects, treated like any other value — they can be assigned to variables, passed as arguments, returned from other functions, and stored in data structures.
- Assign a function to a variable
- Pass a function as an argument
- Return a function from another function
- Store functions in lists/dicts

```python
def shout(text):
    return text.upper() + "!"

speak = shout   # assigned to a variable
print(speak("hello"))
# Output: HELLO!
```

## 8. Higher-Order Functions
A higher-order function is one that accepts another function as a parameter and/or returns one — this is what enables passing custom logic into another function.

```python
def apply_twice(func, value):
    return func(func(value))

def increment(x):
    return x + 1

print(apply_twice(increment, 5))
# Output: 7
```

## 9. Function Factories (Returning Functions / Closures)
A function can return another function object instead of a value — the returned inner function still "remembers" variables from the outer function's scope even after the outer function has finished, which is called a closure.

```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

triple = make_multiplier(3)
print(triple(7))
# Output: 21
```

## 10. Storing Functions in Data Structures
Since functions are ordinary objects, they can be stored in lists, dicts, tuples, or sets, and called later by reference — commonly used as a lightweight alternative to a long `if/elif` chain (a dispatch table).

```python
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

ops = {"add": add, "multiply": multiply}
print(ops["multiply"](4, 5))
# Output: 20
```