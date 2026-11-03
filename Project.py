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
