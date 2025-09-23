import sys, os, pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import task4

def test_calculate_discount_with_ints():
    assert task4.calculate_discount(100, 20) == 80
    assert task4.calculate_discount(50, 0) == 50
    assert task4.calculate_discount(200, 100) == 0

def test_calculate_discount_with_floats():
    assert task4.calculate_discount(100.0, 20.0) == 80.0
    assert task4.calculate_discount(250.0, 15.5) == pytest.approx(211.25)

def test_calculate_discount_invalid_discount():
    with pytest.raises(ValueError):
        task4.calculate_discount(100, -10)
    with pytest.raises(ValueError):
        task4.calculate_discount(100, 150)