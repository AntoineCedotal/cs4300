## Create a new file named task5.py and inside create a list of your favorite books, including book
## titles and authors. Use list slicing to print the first three books in the list. Create a dictionary that
## represents a basic student database, including student names and their corresponding student IDs.
## Implement pytest test cases to verify the correctness of your code for each data structure.

# Python list of favorite books (each book is a dictionary)
favorite_books = [
    {"title": "Lord of the Mysteries", "author": "Cuttlefish That Loves Diving"},
    {"title": "The Beggining After The End", "author": "TurtleMe"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "Shadow Slave", "author": "GuiltyThree"},
    {"title": "Omniscient Reader's Viewpoint", "author": "Sing Shong"}
]

def get_first_n_books(n=3):
    """Return the first n books from the favorite_books list"""
    # Using list slicing
    return favorite_books[:n]

# Python dictionary representing a basic student database
student_db = {
    "Klein": 1001,
    "Arthur": 1002,
    "Merlin": 1003,
    "Sunny": 1004
}

def get_student_id(name):
    """Return the student ID for a given student name"""
    # Dictionary lookup, returns None if not found
    return student_db.get(name)


if __name__ == "__main__":
    # Demonstration using f-strings
    print(f"First 3 favorite books: {get_first_n_books()}")
    print(f"Student ID for Alice: {get_student_id('Alice')}")
