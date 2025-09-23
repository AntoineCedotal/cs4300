# Homework 1: Introduction to Python & Unit Testing

Overview:
This repository contains Homework 1 for CS4300, focusing on Python programming and unit testing using pytest. The assignment introduces Python basics, package management, file handling, and testing techniques.

Project Structure:
```
cs4300/
├── homework1/
│   ├── src/
│   │   ├── task1.py
│   │   ├── task2.py
│   │   ├── task3.py
│   │   ├── task4.py
│   │   ├── task5.py
│   │   ├── task6.py
│   │   └── task7.py
│   ├── tests/
│   │   ├── test_task1.py
│   │   ├── test_task2.py
│   │   ├── test_task3.py
│   │   ├── test_task4.py
│   │   ├── test_task5.py
│   │   ├── test_task6.py
│   │   └── test_task7.py
│   └── task6_read_me.txt
└── homework2/
```

Setup and Test Instructions:
1. Download the repo

2. Set directory:

   ```cd /cs4300/homework1```

4. Activate your virtual environment each time you start working:

   ```source hw1_env/bin/activate```

6. Once within the environment, run pytest and each test_task# will run:

   ```pytest```

To run a specific test file:

```pytest tests/test_task1.py```

*Replace the number with any numuber between 1-7 for each test.*

---
**Homework 1 Tasks:**

**Task 1:** Introduction to Python and Testing
-  Print "Hello World!"

**Task 2:** Variables and Data Types
- Demonstrate integers, floats, strings, and booleans.

**Task 3:** Control Structures
- If/else statement for positive, negative, zero numbers.
- For loop to print first 10 prime numbers.
- While loop to sum numbers from 1 to 100.

**Task 4:** Functions and Duck Typing
- calculate_discount(price, discount) function accepting any numeric type

**Task 5:** Lists and Dictionaries
- Create a list of favorite books and slice first 3 items.
- Create a dictionary with student names and IDs.

**Task 6:** File Handling and Metaprogramming
- task6_read_me.txt with sample text
- task6.py to count words in the tast6_read_me.py file.

**Task 7:** Package Management
- Install a Python package (numpy).
- task7.py demonstrates its use.
