import sys, os, pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import task5

def test_favorite_books_type():
    # Ensure favorite_books is a Python list
    assert isinstance(task5.favorite_books, list)

def test_get_first_n_books():
    first_three = task5.get_first_n_books()
    assert isinstance(first_three, list)
    assert len(first_three) == 3
    assert first_three[0]["title"] == "Lord of the Mysteries"
    assert first_three[1]["author"] == "TurtleMe"

def test_student_db_type():
    # Ensure student_db is a Python dictionary
    assert isinstance(task5.student_db, dict)

def test_get_student_id():
    assert task5.get_student_id("Klein") == 1001
    assert task5.get_student_id("Arthur") == 1002
    assert task5.get_student_id("Unknown") is None

def test_student_db_keys():
    # Check all student names exist as keys
    assert set(task5.student_db.keys()) == {"Klein", "Arthur", "Merlin", "Sunny"}
