import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import task2

def test_integer():
    assert isinstance(task2.get_int(), int)
    assert task2.get_int() == 16

def test_float():
    assert isinstance(task2.get_float(), float)
    assert task2.get_float() == 3.14

def test_string():
    assert isinstance(task2.get_string(), str)
    assert task2.get_string() == "Task 2"

def test_boolean():
    assert isinstance(task2.get_bool(), bool)
    assert task2.get_bool() is False