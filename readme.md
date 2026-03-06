# 🐍 Python Internship Projects – CodSoft

A collection of Python projects completed during my **Python Programming Internship at CodSoft**.  
Each project demonstrates practical Python skills, problem-solving, and hands-on coding experience.

---

## 📁 Project Overview

| Task | Project | Description | Key Concepts |
|------|---------|-------------|--------------|
| 1 | To-Do List | Command-line To-Do List for managing tasks | Lists, Loops, Conditionals, File Handling, Exception Handling |
| 2 | Calculator | Simple Calculator with addition, subtraction, multiplication, division | Functions, Input Handling, Loops, Conditionals, Error Handling |
| 3 | Password Generator | Generates strong and random passwords based on user input | Random, String Manipulation, Join, Input Handling |
| 4 | Rock-Paper-Scissors | Interactive CLI game with score tracking | Random, Loops, Conditionals, Input Validation |
| 5 | Contact Book | Manage contacts: add, view, search, update, delete | CRUD, Lists & Dictionaries, Loops, Conditionals, Input Validation |

---


#  📝 Task 1 — To-Do List Application

## 📌 Overview

A simple and user-friendly **To-Do List** application built with Python that helps users manage their daily tasks efficiently.
The application allows users to **add, view, and delete tasks** making task management easy through a command-line interface.


This project was developed as **Task 1** of the Python Programming Internship at CodSoft.
---

## ✨ Features

- ➕ Add new tasks to the list
- 📋 View all saved tasks
- ❌ Delete tasks from the list
- 💾 Tasks are saved using file handling so they persist after closing the program
- ⚡ Simple and easy-to-use interface
---

## 🧠 Concepts Used

- Python Lists for storing tasks

- File Handling for saving and loading tasks

- Loops (while)

- Conditional Statements (if-else)

- Exception Handling (try-except)
---

## ⚙️ How to Run

### 1. Navigate to the Project Folder
	cd Task1_Todo_List
### 2. Run the program
	python todo_list.py


## 💻 Example Output
===== TO-DO LIST =====

1. Add Task

2. View Tasks

3. Delete Task

4. Exit

Enter your choice: 1
Enter task: Complete Python assignment
Task added successfully!
---



# 🧮 Task 2 — Simple Calculator

## 📌 Overview
A simple command-line **Calculator Application** built using Python.  
The program allows users to perform basic arithmetic operations such as **addition, subtraction, multiplication, and division**.

This project was developed as **Task 2** for the Python Programming Internship at CodSoft.
---

## ✨ Features
- ➕ Perform Addition

- ➖ Perform Subtraction

- ✖ Perform Multiplication

- ➗ Perform Division

- 📋 Menu-driven command-line interface

- ⚠ Handles invalid input errors

- 🚫 Prevents division by zero

- 🔁 Supports multiple calculations

- ❌ Option to exit the program
---

## 🧠 Concepts Used

- 🧩 Python functions for arithmetic operations

- ⌨ User input handling using input()

- 🔀 Control flow using if-elif conditions

- 🔄 Continuous execution using while loop

- 🛡 Error handling using try-except

- ⚠ Division by zero protection

---

## ⚙️ How to Run

### 1. Navigate to the Project Folder
	cd Task2_Calculator
### 2. Run the program
	python calculator.py

## 💻 Example Output

===== SIMPLE CALCULATOR =====

Enter first number: 10
Enter second number: 5

Select Operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit

Enter choice: 1

Result: 15

===================================================================================================================================================

# 🔐 Task 3 -- Password Generator 
## 📌 Overview

A simple and secure **Password Generator** built using Python.  
This application generates strong and random passwords based on the length provided by the user.

The goal of this project is to create a tool that helps users generate secure passwords quickly using random combinations of characters.

## 🚀 Features

🔹 Generate strong and random passwords  
🔹 User can choose the password length  
🔹 Uses a mix of letters, numbers, and symbols  
🔹 Simple command-line interface  
🔹 Lightweight and easy to use


## 🧠 Concepts Applied

- 🎲 Random password generation using Python
- ⌨️ User input handling with `input()`
- 📦 Use of Python standard libraries (`random`, `string`)
- 🔤 String manipulation and character combination
- 🔗 Efficient string construction using `join()`


## 💻 Example Output

===== PASSWORD GENERATOR =====

Enter the desired password length: 10
Generated Password: A7!xP3@dQ9


## ⚙️ How to Run

### 1. Navigate to the Project Folder
	cd Task3_Password_Generator
### 2. Run the program
	python password_generator.py

===================================================================================================================================================

# 🎮 Task 4 -- Rock-Paper-Scissors Game 
## 📌 Overview

An interactive **Rock-Paper-Scissors** game built using Python.  
This project allows the user to play against the computer while tracking scores over multiple rounds.
---

## 🚀 Features

- User chooses **rock, paper, or scissors**  
- Computer randomly selects its move  
- Determines **winner using classic game rules**  
- Displays both **user and computer choices**  
- Tracks **scores for multiple rounds**  
- Option to **play again or exit**  
- Simple **command-line interface**  

---

## 🧠 Concepts Applied

- 🎲 Random choice generation for computer moves

- ⌨️ User input handling with validation

- 🔤 Conditional statements and game logic

- 🔄 Loops for multiple rounds and replay option

- 📊 Score tracking

## 💻 Example Output

===== 🎮 Welcome to Rock-Paper-Scissors Game! =====

Choose your move: rock, paper, or scissors
Your choice: rock
Computer chose: scissors
You win! 🎉

Score -> You: 1 | Computer: 0

Do you want to play another round? (y/n): n
Thanks for playing! Final Score -> You: 1 | Computer: 0

## ⚙️ How to Run

### 1. Navigate to the Project Folder
	cd Task4_Rock_Paper_Scissors
### 2. Run the program
	python rock_paper_scissors.py

===================================================================================================================================================


# 📇 Task 5 -- Contact Book Application 

## 📌 Overview

A simple **Contact Book** built using Python.  
This project allows users to manage contacts by adding, viewing, searching, updating, and deleting them through a user-friendly command-line interface.
---

## 🚀 Features

- ➕ Add a contact with name, phone number, email, and address  
- 📋 View all saved contacts  
- 🔍 Search for contacts by name or phone number  
- ✏️ Update contact details  
- 🗑️ Delete a contact  
- 🖥️ Interactive command-line interface with clear prompts and feedback  

---

## 🧠 Concepts Applied

- ➕ CRUD operations using lists and dictionaries

- ⌨️ User input handling

- 🔤 String manipulation and formatting

- 🔄 Loops and conditionals for menu navigation

- ❌ Input validation and error handling

## 💻 Example Output

=====  Contact Book =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 1

Enter name: John Doe
Enter phone number: 9876543210
Enter email: john@example.com
Enter address: 123, Elm Street
Contact 'John Doe' added successfully!


## ⚙️ How to Run

### 1. Navigate to the Project Folder
	cd Task5_Contact_Book
### 2. Run the program
	python python contact_book.py
