import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import task3

def test_check_number():
    assert task3.check_number(5) == "Positive!"
    assert task3.check_number(-3) == "Negative!"
    assert task3.check_number(0) == "Zero!"

def test_first_n_primes():
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert task3.first_n_primes(10) == expected_primes

def test_sum_to_100():
    assert task3.sum_to_100() == 5050