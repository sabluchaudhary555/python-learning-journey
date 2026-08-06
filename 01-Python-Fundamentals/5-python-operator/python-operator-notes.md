# Python Operators — Short Notes

## 1. What Are Operators?
- **Operators** → special symbols (`+`, `-`, `*`, `/`, etc.) that perform operations.
- **Operands** → the values the operator acts on.

**Types:** Arithmetic, Comparison, Logical, Bitwise, Assignment, Identity, Membership, Ternary.

---

## 2. Arithmetic Operators
| Op | Meaning |
|---|---|
| `+` `-` `*` | Add, Subtract, Multiply |
| `/` | Float division (always returns float) |
| `//` | Floor division (rounds toward smaller integer) |
| `%` | Modulus (remainder) |
| `**` | Exponentiation |

```python
a, b = 15, 4
a / b    # 3.75
a // b   # 3
a % b    # 3
a ** b   # 50625
```
**Precedence:** `**` (right→left) > `%,*,/,//` (left→right) > `+,-` (left→right)

---

## 3. Comparison Operators
- `> < == != >= <=` → return `True`/`False`.
- Chaining allowed: `x < y < z` ≡ `x < y and y < z`.

---

## 4. `is` vs `==`
- `==` → compares **values**.
- `is` → compares **memory identity**.

```python
a = [1,2,3]; b = [1,2,3]
a == b   # True  (same values)
a is b   # False (different objects)
```
- Mutable objects (list/dict/set) → `is` almost always `False` between look-alikes.
- Immutable objects (int/str/tuple) → `is` may return `True` due to caching/interning (don't rely on it).

---

## 5. Logical Operators
| Op | Rule |
|---|---|
| `and` | True if both True |
| `or` | True if either True |
| `not` | Reverses Boolean |

- **Precedence:** `not` > `and` > `or`
- **Short-circuit:** `and` stops at first `False`; `or` stops at first `True`.

---

## 6. Bitwise Operators
| Op | Meaning |
|---|---|
| `&` | AND |
| `\|` | OR |
| `^` | XOR |
| `~` | NOT (one's complement) |
| `>>` | Right shift (÷ by 2ⁿ) |
| `<<` | Left shift (× by 2ⁿ) |

- Works only on integers.
- Custom classes can overload via `__and__`, `__or__`, `__xor__`, `__lshift__`, `__rshift__`, `__invert__`.

---

## 7. Assignment Operators
- Basic: `=`
- Compound: `+= -= *= /= %= //= **= &= |= ^= >>= <<=` → shorthand for `a = a <op> b`.
- **Walrus operator (`:=`)** — Python 3.8+, assigns inside an expression.
```python
while (x := len(a)) > 2:
    a.pop()
```

---

## 8. Membership Operators
| Op | Meaning |
|---|---|
| `in` | True if value found in sequence |
| `not in` | True if value NOT found |

- Works on str, list, tuple, set, dict (checks **keys** for dict).
- Function form: `operator.contains(seq, value)`.

---

## 9. Identity Operators
| Op | Meaning |
|---|---|
| `is` | Same object (memory) |
| `is not` | Different objects |

```python
n1, n2 = 5, 5
n1 is n2   # True — small ints cached
```

---

## 10. Ternary Operator (Conditional Expression)
**Syntax:** `[on_true] if [condition] else [on_false]`
```python
res = "Even" if n % 2 == 0 else "Odd"
```
**5 ways to write conditional logic:**
1. Nested if-else: `"Positive" if n>0 else "Negative" if n<0 else "Zero"`
2. Tuple indexing: `("Odd","Even")[n % 2 == 0]`
3. Dict mapping: `{True: a, False: b}[a > b]`
4. Inside lambda: `(lambda x,y: x if x>y else y)(a,b)`
5. Directly in `print()`

---

## 11. Precedence & Associativity
- **Precedence** → which operator runs first.
- **Associativity** → direction of evaluation when precedence is equal (mostly left→right; `**` and assignment ops are right→left).

**Quick order (high → low):**
`()` → `[]` slicing → `**` → unary `+x -x ~x` → `* / // %` → `+ -` → `<< >>` → `&` → `^` → `|` → comparisons/membership/identity → `not` → `and` → `or` → ternary → `lambda` → `:=`

```python
2 ** 3 ** 2      # 512 → right-to-left
100 / 10 * 10    # 100.0 → left-to-right
```
> `=` and compound assignment (`+=`) are **non-associative** — can't be chained together in one expression.

---

## 12. Cheat Sheet

| Category | Operators |
|---|---|
| Arithmetic | `+ - * / // % **` |
| Comparison | `> < == != >= <=` |
| Logical | `and or not` |
| Bitwise | `& \| ^ ~ >> <<` |
| Assignment | `= += -= *= /= %= //= **= &= \|= ^= >>= <<= :=` |
| Membership | `in`, `not in` |
| Identity | `is`, `is not` |
| Ternary | `x if cond else y` |