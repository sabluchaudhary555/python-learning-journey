# Python Data Types — Short Notes

## 1. What Are Data Types?
- Classify data items → represent the kind of value held → determine what operations are valid.
- Everything in Python is an object → data types are classes, variables are instances of those classes.
- Variables have no fixed type — reassigning changes type automatically.

```python
x = 50                          # int
x = "Hello World"               # str
x = ["geeks", "for", "geeks"]   # list
```

**Categories:**
| Category | Types |
|---|---|
| Numeric | int, float, complex |
| Sequence | str, list, tuple |
| Mapping | dict |
| Boolean | bool |
| Set | set, frozenset |
| Binary | bytes, bytearray, memoryview |

---

## 2. Numeric Types
- **int** — whole numbers, no size limit.
- **float** — decimal numbers, supports scientific notation (e/E).
- **complex** — `real + imaginaryj` form, e.g. `2+3j`.

```python
type(5)      # <class 'int'>
type(5.0)    # <class 'float'>
type(2+4j)   # <class 'complex'>
```

---

## 3. Sequence Types

### 3.1 String (`str`)
- Immutable array of Unicode characters; no separate char type (single char = string of length 1).
- Indexed with `[]`, negative index counts from end.

```python
s = 'Welcome'
s[1]     # e
s[-1]    # e (last char)
```

### 3.2 List
- Ordered, **mutable**, items can be mixed type.

```python
a = [1, 2, 3]
b = ["Geeks", "For", 4, 5]
a[0]     # 1
a[-1]    # 3
```

### 3.3 Tuple
- Ordered, **immutable**.
- Single-element tuple needs trailing comma: `(5,)`.
- Without parentheses = "Tuple Packing".

```python
tup1 = (1, 2, 3, 4, 5)
tup1[0]    # 1
tup1[-1]   # 5
```

---

## 4. Boolean (`bool`)
- Only `True` / `False` (capitalized — lowercase `true` → NameError).
- **Truthy/Falsy:** non-bool values evaluated in boolean context (`0`, `''`, `None`, `[]` → falsy; rest → truthy).

```python
type(True)   # <class 'bool'>
if 1: print("truthy")
if not 0: print("falsy")
```

---

## 5. Set Types

### 5.1 Set (`set`)
- Unordered, **mutable**, no duplicates, no indexing.
- Access only via loop or `in`.

```python
s = set(["Geeks", "For", "Geeks"])   # duplicates auto-removed
"Geeks" in s
```

### 5.2 Frozenset (`frozenset`)
- Immutable version of set → hashable → usable as dict key / set element.
- No indexing/slicing on set or frozenset.

```python
fs = frozenset([1, 2, 3, 2, 1])   # frozenset({1, 2, 3})
```

---

## 6. Dictionary (`dict`)
- Key–value pairs; keys unique & immutable, values any type.
- Keys are case-sensitive.

```python
d = {1: 'Geeks', 'name': 'For'}
d['name']    # For
d.get(1)     # Geeks
```

---

## 7. Binary Types
| Type | Mutability | Description |
|---|---|---|
| `bytes` | Immutable | Sequence of ints (0–255); made via `b"..."` or `bytes()` |
| `bytearray` | Mutable | Mutable version of bytes |
| `memoryview` | View | Access buffer-protocol object's data without copying |

```python
b1 = bytes([72, 101, 108, 108, 111])     # b'Hello'
b2 = bytearray([72, 101, 108, 108, 111])
b2[0] = 74                                # bytearray(b'Jello')
mv = memoryview(b2)
mv[0]                                     # 74
```
> `str` = text (Unicode); `bytes`/`bytearray` = binary data.

---

## 8. Cheat Sheet

| Category | Type | Mutable? | Ordered? |
|---|---|---|---|
| Numeric | int, float, complex | Immutable | N/A |
| Sequence | str | Immutable | Ordered |
| Sequence | list | Mutable | Ordered |
| Sequence | tuple | Immutable | Ordered |
| Boolean | bool | Immutable | N/A |
| Set | set | Mutable | Unordered |
| Set | frozenset | Immutable | Unordered |
| Mapping | dict | Mutable (values) | Insertion-ordered (3.7+) |
| Binary | bytes | Immutable | Ordered |
| Binary | bytearray | Mutable | Ordered |
| Binary | memoryview | View | Ordered |