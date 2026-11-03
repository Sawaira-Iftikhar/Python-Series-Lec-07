"""
============================================
  LECTURE 7 - Mini-Project: Personal Diary
  Total Challenge: 01
============================================
"""


import os

DIARY_FILE = "Diary.txt"


def add_entry():
    date = input("Date (e.g. 22-11-2026): ")
    text = input("Write your entry: ")

    with open(DIARY_FILE, "a") as f:        # 'a' keeps old entries
        f.write(date + " | " + text + "\n")

    print("Entry saved.")


def view_entries():
    if not os.path.exists(DIARY_FILE):
        print("Diary is empty. Add an entry first.")
        return

    with open(DIARY_FILE, "r") as f:
        data = f.read()

    if data == "":
        print("Diary is empty.")

    else:
        print("\n----- My Diary -----")
        print(data, end="")
        print("--------------------")


def search_word():
    if not os.path.exists(DIARY_FILE):
        print("Diary is empty. Add an entry first.")
        return

    word = input("Word to search: ")

    with open(DIARY_FILE, "r") as f:
        data = f.read()

    if word in data:
        print("Found:", word)

    else:
        print("Not found:", word)


def find_line():
    if not os.path.exists(DIARY_FILE):
        print("Diary is empty. Add an entry first.")
        return

    word = input("Word to find: ")
    line_no = 1
    found = False

    with open(DIARY_FILE, "r") as f:
        for line in f:
            if word in line:
                 print("Line", line_no, "->", line, end="")
                 found = True
            line_no += 1

    if not found:
        print(-1)


def count_entries():
    if not os.path.exists(DIARY_FILE):
        print("Total entries: 0")
        return

    count = 0
    with open(DIARY_FILE, "r") as f:
        for line in f:
            count += 1

    print("Total entries:", count)


def delete_diary():
    if not os.path.exists(DIARY_FILE):
        print("No diary file to delete.")
        return

    confirm = input("Delete the whole diary? (yes/no): ")
    if confirm == "yes":
        os.remove(DIARY_FILE)
        print("Diary deleted.")

    else:
        print("Cancelled.")

def menu():
    while True:
         print("\n===== Personal Diary =====")
         print("1. Add entry")
         print("2. View all entries")
         print("3. Search a word")
         print("4. Find lines with a word")
         print("5. Count entries")
         print("6. Delete diary")
         print("7. Exit")

         choice = input("Choose (1-7): ")

         if choice == "1":
            add_entry()
         elif choice == "2":
            view_entries()
         elif choice == "3":
            search_word()
         elif choice == "4":
            find_line()
         elif choice == "5":
            count_entries()
         elif choice == "6":
            delete_diary()
         elif choice == "7":
            print("Goodbye!")
            break