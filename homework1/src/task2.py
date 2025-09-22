## Create a new file named task2.py demonstrating the use of various data types, including integers,
## floating-point numbers, strings, and boolean. Implement a Python using pytest to test case for each
## data type, ensuring that the script’s behavior matches the expected outcomes.

def int_task():
    int_test = 123
    print(int_test)

def float_task():
    float_test = 3.14
    print(float_test)

def string_task():
    string_test = "Hello World"
    print(string_test)

def bool_task():
    bool_test = True
    print(bool_test)

def main():
    int_task()
    float_task()
    string_task()
    bool_task()

if __name__ == '__main__':
    main()