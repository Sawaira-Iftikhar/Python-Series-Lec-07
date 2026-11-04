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
9. [Practice Questions](#9-practice-questions)
10. [Mini Project](#10-mini-project)
11. [How to Run](#11-how-to-run)

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