# Python-Series-Lec-07

Variables lose their data when a program ends. **Files** store data permanently.
Python can **read** data from a file and **write** data to it.

## 📚 Topics Covered

| # | Topic | Status |
|:-:|---|:-:|
| 1 | Types of Files (Text & Binary) | ✅ |
| 2 | Open, Read & Close a File (`open()`, `close()`) | ✅ |
| 3 | File Modes (`r`, `w`, `x`, `a`, `b`, `t`, `+`) | ✅ |
| 4 | Reading a File (`read()`, `readline()`, Looping over Lines) | ✅ |
| 5 | Writing to a File (`w` Overwrite vs `a` Append) | ✅ |
| 6 | `with` Syntax (Auto-close Files) | ✅ |
| 7 | Deleting a File (`os` Module, `os.remove()`) | ✅ |

## 📂 Practice Files

| File | Topics | Questions |
|---|---|:-:|
| [Practice.py](Practice.py) | Create, Write, Find & Replace, Search, Line Number, `split()`, Copy File, Sum & Average | 08 |
| [Project.py](Project.py) | Mini Project: Personal Diary (`a` mode, Read, Search, Count, `os.remove()`) | 06 |
| [data/numbers.txt](data/numbers.txt) | Sample numbers used in Q5 & Q8 | — |
| [data/sample.txt](data/sample.txt) | Sample text used in Q6 & Q7 | — |

## Contents

1. [Types of Files](#1-types-of-files)
2. [Open, Read and Close a File](#2-open-read-and-close-a-file)
3. [File Modes](#3-file-modes)
4. [Reading a File](#4-reading-a-file)
5. [Writing to a File](#5-writing-to-a-file)
6. [The `with` Syntax](#6-the-with-syntax)
7. [Deleting a File](#7-deleting-a-file)
8. [Common Mistakes](#8-common-mistakes)

---

## 1. Types of Files

| Type | What it stores | Examples |
|---|---|---|
| Text files | Plain, readable text | `.txt`, `.log`, `.csv`, `.py` |
| Binary files | Data in binary (0s and 1s) form | `.mp4`, `.mov`, `.png`, `.jpeg` |

> **Note:** A Word file (`.docx`) is stored as a **binary** file, even though it contains text.

---

## 2. Open, Read and Close a File

A file must be **opened** before reading or writing, and **closed** when you are done.

```python
f = open("file_name", "mode")
data = f.read()
f.close()
```

---

## 3. File Modes

| Mode | Meaning |
|---|---|
`'r'` | Open for reading (default) |
| `'w'` | Open for writing — **erases the file first** (creates it if missing) |
| `'x'` | Create a new file and open it for writing (error if it already exists) |
| `'a'` | Open for writing — **adds to the end** of the file (creates it if missing) |
| `'b'` | Binary mode |
| `'t'` | Text mode (default) |
| `'+'` | Open for updating (reading **and** writing) |

Modes can be combined:

| Combined mode | Meaning |
|---|---|
| `'rb'` | Read a binary file |
| `'r+'` | Read and write |

---

## 4. Reading a File

Suppose `sample.txt` contains:

```
Hi everyone
we are learning File I/O
using Python.
```

| Function | What it does |
|---|---|
| `f.read()` | Reads the **entire file** as one string |
| `f.readline()` | Reads **one line** at a time |

### Read the whole file

```python
f = open("sample.txt", "r")
data = f.read()
print(data)
f.close()
```

Output:

```
Hi everyone
we are learning File I/O
using Python.
```

### Read line by line

```python
f = open("sample.txt", "r")
line1 = f.readline()
line2 = f.readline()
print(line1, end="")
print(line2, end="")
f.close()
```

Output:

```
Hi everyone
we are learning File I/O
```

> Each line read from a file ends with `\n` (new line), so we use `end=""` to avoid blank lines.

---

## 5. Writing to a File

### `'w'` mode — overwrites the entire file

```python
f = open("demo.txt", "w")
f.write("this is a new line")
f.close()
```

### `'a'` mode — adds to the end of the file

```python
f = open("demo.txt", "a")
f.write("\nthis line is added")
f.close()
```

### Check the result

```python
f = open("demo.txt", "r")
print(f.read())
f.close()
```

Output:

```
this is a new line
this line is added
```
---

## 6. The `with` Syntax

With `with`, Python **closes the file automatically** when the block ends, so `f.close()` is not needed.

```python
with open("demo.txt", "r") as f:
    data = f.read()

print(data)
````

Output:

```
this is a new line
this line is added
```

```python
with open("demo.txt", "w") as f:
    f.write("new data")
```

> **Note:** To read a file, open it in `'r'` mode. Reading a file opened in `'w'` or `'a'` mode gives an error.

---

## 7. Deleting a File

Files are deleted with the `os` module. A **module** is a file (like a code library) written by another programmer that contains functions we can use.

```python
import os

os.remove("demo.txt")
```
---

## 8. Common Mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Opening a file with data in `'w'` mode | All old data is **erased** without warning | Use `'a'` to add data |
| Reading a file opened in `'w'` or `'a'` mode | `io.UnsupportedOperation: not readable` | Open it in `'r'` mode |
| Opening a missing file in `'r'` mode | `FileNotFoundError` | Check first with `os.path.exists("file.txt")` |
| Using `'x'` on a file that already exists | `FileExistsError` | Use `'x'` only for brand-new files |
| Printing lines without `end=""` | Extra blank lines in the output | `print(line, end="")` |
| Forgetting `f.close()` | Data may not be saved | Use `with open(...)` |
| Deleting a file that doesn't exist | `FileNotFoundError` | Check with `os.path.exists()` first |
| `replace("Java", "Python")` | Only replaces `Java` with a capital J, not `java` | `replace()` is case-sensitive, so replace each spelling you need |

---

## 🗓️ Series Progress

- [x] **Lecture 01** — Basics, Data Types & Operators ✅
- [x] **Lecture 02** — Strings, Slicing & Conditionals ✅
- [x] **Lecture 03** — Lists, Tuples & Methods ✅
- [x] **Lecture 04** — Dictionaries & Sets ✅
- [x] **Lecture 05** — Loops, Lists & Tuples in Loops ✅
- [x] **Lecture 06** — Functions, Default Params & Recursion ✅
- [x] **Lecture 07** — File I/O (Read, Write, Append, `with` & `os`) 📍 *(Current)*
- [ ] **Lecture 08** — Coming Soon
- [ ] **Lecture 09** — Coming Soon

## 🤝 Connect & Feedback

If you found this helpful or have any questions:

💬 Found a bug / Have a solution? Open an [Issue](../../issues) or submit a [Pull Request](../../pulls).

## ⭐ Support

If you find this repository helpful, please consider giving it a Star (⭐)! It helps others discover this learning roadmap.
