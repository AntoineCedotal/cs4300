## Create a new file named task2.py demonstrating the use of various data types, including integers,
## floating-point numbers, strings, and boolean. Implement a Python using pytest to test case for each
## data type, ensuring that the script’s behavior matches the expected outcomes.

def get_int():
    return 16

def get_float():
    return 3.14

def get_string():
    return "Task 2"

def get_bool():
    return False

def main():
    print(f"Int: {get_int()}")
    print(f"Float: {get_float()}")
    print(f"String: {get_string()}")
    print(f"Bool: {get_bool()}")

if __name__ == '__main__':
    main()