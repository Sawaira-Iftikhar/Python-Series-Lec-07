"""
============================================
  LECTURE 7 - Main-File: 
  Creating and Writing to a File
  Find and Replace in a File
  Searching a Word in a File
  Finding the Line Number of a Word
  Counting Even Numbers from a File
  Counting Lines, Words and Characters
  Copying a File
  Sum and Average Saved to a File
Total Questions: 0
============================================
"""

# ---------------------------------------------------------
# Q1. Create a new file "practice.txt" and add the following data:
#     Hi everyone
#     we are learning File I/O
#     using Java.
#     I like programming in Java.
# ---------------------------------------------------------

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")

    print("Q1: practice.txt created")

#-------------------------------------------------------------------------------------------

# ---------------------------------------------------------
# Q2. Write a function that replaces all occurrences of
#     "Java" with "Python" in the above file.
# ---------------------------------------------------------

def replace_java():
    with open("practice.txt", "r") as f:
        data = f.read()

    new_data = data.replace("Java", "Python")

    with open("practice.txt", "w") as f:
        f.write(new_data)

replace_java()

with open("practice.txt", "r") as f:
    print("Q2:", f.read())

#-----------------------------------------------------------------------------------------

# ---------------------------------------------------------
# Q3. Search if the word "learning" exists in the file or not.
# ---------------------------------------------------------

word = "learning"

with open("practice.txt", "r") as f:
    data = f.read()

if word in data:
    print("Q3: Found")