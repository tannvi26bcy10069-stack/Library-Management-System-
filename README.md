# Library Management System

## About the Project

For this project, I am making a simple Library Management System using Python. The idea is to make everyday library work a little easier. Instead of keeping every detail in a notebook, the user can use the program to add books, search for them, and keep track of books that have been issued or returned.

I have kept the project simple because it is part of my first-semester programming work. It uses Python concepts that I have been learning, such as variables, conditions, loops, functions, lists, dictionaries, and modules.

## What Can the Program Do?

The program is planned to include these features:

- Add a new book to the library record.
- Display the books entered in the system.
- Search for a book by its ID or title.
- Enter and view basic student details.
- Issue an available book to a student.
- Record when a book is returned.
- Calculate a simple late fine.
- Show a short summary of the library records.

Only mention a feature as completed if it is actually working in your code.

## Tools and Concepts Used

- **Language:** Python 3
- **Editor:** VS Code or another Python editor
- **Python concepts:** input and output, variables, `if-else`, loops, functions, lists, dictionaries, and modules
- **Version control:** Git and GitHub

## Project Files

- `main.py` – shows the menu and connects the different parts of the program.
- `book.py` – contains functions for adding, displaying, and searching for books.
- `student.py` – handles basic student details.
- `issue_return.py` – handles issuing and returning books.
- `fine.py` – calculates a simple fine.
- `report.py` – displays a summary of the library records.

The documentation files are `README.md` and `statement.md`.

## How to Run the Program

1. Install Python 3 on your computer.
2. Download or clone this project from GitHub.
3. Open the project folder in VS Code or another Python editor.
4. Make sure the required Python files are in the same folder.
5. Open the terminal in that folder and run:

   `python main.py`

6. Follow the options shown on the screen.

If your computer uses the `python3` command, run `python3 main.py` instead.

## How to Test It

I can test the program by adding a book, displaying the list, and searching for a book that exists. I can then try issuing an available book, returning it, and entering an invalid menu option. These checks help me see whether the program behaves as expected.

I should also test what happens if someone tries to issue a book that is already issued or searches for a book that is not in the list.

## Current Limitations

In the basic version, the records are stored in Python lists and dictionaries while the program is running. This means the information may be lost when the program is closed. The program is meant for learning and demonstration, rather than for running a real library.

## Ideas for Future Improvement

If I continue working on this project, I would like to save the records permanently in a file or database. I could also add book due dates, improve fine calculation, and create a simple graphical interface.

## Student Details

- **Name:** [Your Name]
- **Course:** CSE – Cyber Security and Digital Forensics
- **Semester:** First Semester
- **Institution:** VIT Bhopal University
