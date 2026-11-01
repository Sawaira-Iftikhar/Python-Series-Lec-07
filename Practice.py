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

word = "Python"

with open("practice.txt", "r") as f:
    data = f.read()

if word in data:
    print("Q3: Found")

else:
    print("Q3: Not found")

#-----------------------------------------------------------------------------------------

# ---------------------------------------------------------
# Q4. Write a function to find in which line of the file the
#     word "learning" occurs first. Print -1 if not found.
# ---------------------------------------------------------

def check_line(word):
    line_no = 1
    with open("practice.txt", "r") as f:
        for line in f:              # reads one line at a time
            if word in line:
                return line_no
            line_no += 1
    return -1

print("Q4:", check_line("learning"))
print("Q4:", check_line("hello"))

#-----------------------------------------------------------------------------------------

# ---------------------------------------------------------
# Q5. From a file containing numbers separated by commas,
#     print the count of even numbers.
#     
# ---------------------------------------------------------

count = 0

with open("data/numbers.txt", "r") as f:
    data = f.read()

nums = data.strip() .split(",")              # list of strings
for num in nums:
      if num != "":
         if int(num) % 2 == 0:
             count += 1

print("Q5: Even numbers:", count)

#-----------------------------------------------------------------------------------------

# ---------------------------------------------------------
# Q6. Count the number of lines, words and characters
#     in data/sample.txt
# ---------------------------------------------------------

lines = 0
words = 0
chars = 0

with open("data/sample.txt", "r") as f:
     for line in f:
        lines += 1
        words += len(line.split())
        chars += len(line)

print("Q6: Lines:", lines, "| Words:", words, "| Characters:", chars)

#-----------------------------------------------------------------------------------------

# ---------------------------------------------------------
# Q7. Copy the content of data/sample.txt into a new file
#     copy.txt, then print the new file.
# ---------------------------------------------------------

with open("data/sample.txt", "r") as f:
    data = f.read()

with open("copy.txt", "w") as f:
    f.write(data)

with open("copy.txt", "r") as f:
    print("Q7: copy.txt contains:")
    print(f.read(), end="")

#-----------------------------------------------------------------------------------------

# ---------------------------------------------------------
# Q8. Read data/numbers.txt, find the sum and average of the
#     numbers, and save the result in result.txt
# ---------------------------------------------------------

with open("data/numbers.txt", "r") as f:
    data = f.read()

nums = data.split(",")
total = 0
for num in nums:
    total += int(num)
