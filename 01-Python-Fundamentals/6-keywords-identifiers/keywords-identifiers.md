# Python: Keywords, Identifiers, Literals & Tokens — Short Notes

## 1. Character Set
- The raw set of valid characters Python understands: **alphabets** (A-Z, a-z), **digits** (0-9), **special symbols** (`+ - * / % = @ # $ &` etc.), **whitespace**, and **Unicode** characters.
- Source code is read as Unicode; default file encoding is **UTF-8** unless declared otherwise → wrong decoding raises `SyntaxError`.

---

## 2. Tokens
- The **smallest meaningful unit** in a program — code is broken into tokens before parsing.
- Categories: **Keywords, Identifiers, Literals, Operators, Punctuators/Delimiters** (+ NEWLINE/INDENT/DEDENT markers).

```python
for x in range(1, 6):
    if x < 4:
        continue
    break
```
- Keywords → `for, if, continue, break`
- Identifiers → `x, range`
- Literals → `1, 6, 4`
- Operator → `<`
- Punctuators → `:`, `()`

---

## 3. Keywords
- Reserved words that define Python's syntax → **cannot** be used as identifiers.
- All lowercase except `True`, `False`, `None`.
- **35 keywords** (Python 3.11).

```python
import keyword
keyword.kwlist            # list of all keywords
keyword.iskeyword("for")  # True
```

**Grouped by category:**
| Category | Keywords |
|---|---|
| Value | `True, False, None` |
| Operator | `and, or, not, is, in` |
| Control Flow | `if, else, elif, for, while, break, continue, pass, try, except, finally, raise, assert` |
| Function/Class | `def, return, lambda, yield, class` |
| Context Mgmt | `with, as` |
| Import/Module | `import, from` |
| Scope | `global, nonlocal` |
| Async | `async, await` |
| Deletion | `del` |

**Quick meanings:**
- `is` → identity check | `in` → membership check
- `pass` → null placeholder statement
- `try/except/finally/raise` → exception handling
- `assert` → checks a condition, raises `AssertionError` if false
- `lambda` → anonymous function
- `yield` → pauses a function, builds a generator
- `global` → modify a variable from global scope inside a function
- `nonlocal` → modify a variable from nearest enclosing (non-global) scope
- `async/await` → asynchronous function definition & pausing

### Soft Keywords
Not reserved — only special in specific contexts, usable as normal identifiers elsewhere.
| Soft Keyword | Meaning |
|---|---|
| `match` | starts a `match` statement |
| `case` | pattern inside `match` block |
| `_` | wildcard pattern / throwaway variable |
| `type` | declares a type alias |

### Keywords vs Identifiers vs Variables
- **Keywords** — fixed, reserved, cannot be redefined.
- **Identifiers** — programmer-defined names (variables, functions, classes...).
- **Variables** — identifiers that specifically store data. Every variable is an identifier, not every identifier is a variable.

---

## 4. Identifiers
- User-defined names for variables, functions, classes, etc.
- **Case-sensitive** (`num`, `Num`, `NUM` are different).
- Check validity: `"name".isidentifier()`

**Rules:**
- Cannot be a keyword.
- No whitespace.
- Only letters, digits, underscore (`_`).
- Must start with a letter or `_` — never a digit.

```python
# Valid:   var1, _var1, _1_var, var_1
# Invalid: !var1, 1var, var#1, var 1, for
```

---

## 5. Literals
Fixed constant values written directly in code.

### 5.1 Numeric
| Type | Example |
|---|---|
| Integer | `10, -25, 0` |
| Float | `3.14, -0.01` |
| Complex | `4 + 7j` |

### 5.2 String
| Type | Example |
|---|---|
| Single-quoted | `'Hello'` |
| Double-quoted | `"Python"` |
| Triple-quoted | `'''multi-line'''` |
| Raw string | `r"C:\Users\Python"` (backslashes literal) |

### 5.3 Boolean
- `True` / `False` — behave like `1`/`0` in arithmetic: `True + 5 → 6`

### 5.4 Collection
| Type | Example | Mutable? |
|---|---|---|
| List | `[1, 2, 3]` | Yes |
| Tuple | `(1, 2, 3)` | No |
| Dict | `{"key": "value"}` | Yes |
| Set | `{1, 2, 3}` | Yes |

### 5.5 Special — `None`
- Represents absence of value / null.

### 5.6 Mutability Recap
- Immutable: int, float, complex, str, bool, tuple, `None`
- Mutable: list, dict, set

---

## 6. Operators (as Tokens)
- Symbols that perform operations on operands: `+ - ~` etc.
- Full detail covered separately — here just noted as a token category.

---

## 7. Punctuators / Delimiters
- Symbols that shape code structure (don't compute): `[ ] { } ( ) @ -= += *= //= **= = ,`
- e.g. `()` grouping/calls, `[]` lists/indexing, `{}` dict/set, `,` separating items.

---

