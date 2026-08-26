# Python Functions — Basics

## 1. What is a Function?
A function is a reusable block of code that performs one specific task, letting you run the same logic multiple times just by calling it instead of rewriting it.
- Avoids repeating code
- Makes programs modular and easier to read
- Makes debugging/testing easier (test small units in isolation)
- Improves reusability across projects

## 2. Defining a Function
A function is created with the `def` keyword, followed by a name and a parenthesized parameter list; the body must be indented.

**Syntax**
```python
def function_name(parameters):
    """docstring (optional)"""
    # function body
    return value   # optional
```

```python
def cube(n):
    """Returns the cube of a number."""
    return n ** 3

print(cube(3))
# Output: 27
```

## 3. Function With / Without `return`
A function without `return` just performs an action and gives back `None`. A function with `return` sends a value back to the caller, which can be stored or reused.
- No `return` (or falls off the end) → result is `None`
- `return value` → exits immediately, code after `return` never runs
- Return value can be stored, printed, or passed elsewhere

```python
def greet_silent():
    print("hi")

def greet_return():
    return "hi"

a = greet_silent()   # prints hi, a is None
b = greet_return()   # nothing printed, b holds "hi"
print(a, b)
# Output: None hi
```

## 4. Parameters vs Arguments
A parameter is the placeholder variable in the function definition; an argument is the actual value passed in when calling it.
- Parameter → written inside `()` in `def`
- Argument → the real value supplied at call time

```python
def power_of(base, exponent):
    return base ** exponent

print(power_of(2, 5))
# Output: 32
```

## 5. Calling a Function
A function runs when its name is followed by `()`, optionally with arguments. Defining a function just links its name to a function object, so other names can point to the same object.

**Syntax**
```python
function_name(arguments)
```

```python
def area(radius):
    return 3.14 * radius ** 2

calc = area   # another name bound to the same function
print(calc(4))
# Output: 50.24
```

## 6. The `return` Statement
`return` ends execution and sends a value back to the caller. With no expression (or no `return` at all), Python returns `None` by default, and a function can return any type, including a tuple of multiple values.

**Syntax**
```python
return [expression]
```

```python
def min_max(nums):
    return min(nums), max(nums)

print(min_max([4, 9, 1, 7]))
# Output: (1, 9)
```

## 7. Default Arguments
A default argument supplies a fallback value used automatically when the caller doesn't pass one. Defaults are evaluated once, at definition time, in the defining scope — not on every call.
- Skipping an argument at call time uses its default
- A mutable default (list/dict) is shared across all calls — a common bug
- Fix: default to `None`, then create a new object inside the function

```python
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("pen"))
print(add_item("book"))
# Output: ['pen']
# Output: ['book']
```

## 8. Keyword Arguments
Keyword arguments are passed as `name=value`, so their order at the call site doesn't matter.
- Must come after positional arguments in a call
- The keyword must match an actual parameter name
- The same argument can't be given a value twice

```python
def book_ticket(destination, seat="Window"):
    print(f"To {destination}, seat: {seat}")

book_ticket(seat="Aisle", destination="Goa")
# Output: To Goa, seat: Aisle
```

## 9. Positional Arguments
Values are matched to parameters purely by their order in the call, so swapping the order swaps the results.

```python
def rectangle_area(length, width):
    return length * width

print(rectangle_area(10, 5))
print(rectangle_area(5, 10))
# Output: 50
# Output: 50
```

## 10. Arbitrary Arguments — `*args` and `**kwargs`
Used when the number of arguments isn't known in advance: `*args` collects extra positional values into a tuple, `**kwargs` collects extra keyword values into a dictionary.
- `*args` must appear before `**kwargs` in the signature
- Any parameter listed after `*args` becomes keyword-only

```python
def order_summary(*items, **extras):
    print("Items:", items)
    print("Extras:", extras)

order_summary("pizza", "coke", size="large", spicy=True)
# Output: Items: ('pizza', 'coke')
# Output: Extras: {'size': 'large', 'spicy': True}
```

## 11. Nested / Inner Functions
An inner function is defined inside another function, used to group related logic and access the enclosing function's variables.

```python
def outer_report(title):
    def print_line():
        print(f"Report: {title}")
    print_line()

outer_report("Sales")
# Output: Report: Sales
```

## 12. Scope and Name Lookup (LEGB)
Running a function creates its own local symbol table; Python looks up a name locally first, then in enclosing functions, then globally, then in built-ins. Arguments are passed as object references, so mutable objects can be changed in place while rebinding an immutable one doesn't affect the caller.
- L → Local, E → Enclosing, G → Global, B → Built-in
- Modifying an enclosing/global variable needs `nonlocal`/`global`
- Mutable objects (lists, dicts) show caller-visible changes; immutables (int, str) don't

```python
def double_in_place(nums):
    for i in range(len(nums)):
        nums[i] *= 2

values = [1, 2, 3]
double_in_place(values)
print(values)
# Output: [2, 4, 6]
```

## 13. Global and Local Variables
A local variable exists only during its function's execution; a global variable is declared outside all functions and is readable everywhere. A same-named local variable shadows the global one only inside its own function.

```python
counter = 0

def show_local():
    counter = 100
    print("local:", counter)

show_local()
print("global:", counter)
# Output: local: 100
# Output: global: 0
```

## 14. The `global` Keyword
`global` lets a function reassign a variable defined outside it; without it, any assignment inside the function creates a new local variable instead, and merely reading a global needs no declaration.

**Syntax**
```python
global variable_name
```

```python
score = 0

def add_point():
    global score
    score += 1

add_point()
add_point()
print(score)
# Output: 2
```

## 15. The `nonlocal` Keyword
`nonlocal` lets an inner function modify a variable belonging to its enclosing function (not the module-level global). Without it, assigning inside the inner function creates a separate local variable and leaves the outer one untouched.

**Syntax**
```python
nonlocal variable_name
```

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

tick = make_counter()
print(tick())
print(tick())
# Output: 1
# Output: 2
```

## 16. Pass by Reference vs Pass by Value
Python passes object references, so whether a call "changes the original" depends on whether the object is mutable or immutable: mutable objects can be edited in place, immutable ones can't be changed by rebinding the parameter.

```python
def try_reset(x):
    x = 0

def clear_list(lst):
    lst.clear()

n = 5
try_reset(n)
data = [1, 2, 3]
clear_list(data)
print(n, data)
# Output: 5 []
```

## 17. The `pass` Statement
`pass` is a null operation used purely as a placeholder wherever Python's syntax requires an indented block but no logic is ready yet.

**Syntax**
```python
pass
```

```python
def not_implemented_yet():
    pass

class Draft:
    pass

not_implemented_yet()
print(Draft)
# Output: <class '__main__.Draft'>
```

## 18. Docstrings
The first statement in a function body can be a string literal documenting the function's purpose, accessible via `function.__doc__`; convention is a short summary line, optionally followed by a blank line and more detail.

```python
def is_even(n):
    """Check whether a number is even."""
    return n % 2 == 0

print(is_even.__doc__)
# Output: Check whether a number is even.
```

## 19. Function Annotations
Annotations are optional metadata about expected parameter and return types, stored in `__annotations__`; Python doesn't enforce them, but tools like IDEs and type-checkers can use them.

**Syntax**
```python
def function_name(param: type = default) -> return_type:
    ...
```

```python
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply.__annotations__)
# Output: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```