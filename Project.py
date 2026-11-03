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