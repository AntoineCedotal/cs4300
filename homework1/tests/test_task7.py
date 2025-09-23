import sys, os, pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import task7
import math

def test_compute_statistics_basic():
    data = [1, 2, 3, 4, 5]
    stats = task7.compute_statistics(data)
    
    assert math.isclose(stats["mean"], 3.0)
    assert math.isclose(stats["median"], 3.0)
    assert math.isclose(stats["std"], 1.4142135623730951)  # sqrt(2)

def test_compute_statistics_floats():
    data = [2.5, 3.5, 4.5, 5.5]
    stats = task7.compute_statistics(data)
    
    assert math.isclose(stats["mean"], 4.0)
    assert math.isclose(stats["median"], 4.0)
    assert math.isclose(stats["std"], 1.118033988749895)  # sqrt(5/4)

def test_compute_statistics_single_value():
    data = [10]
    stats = task7.compute_statistics(data)
    
    assert stats["mean"] == 10
    assert stats["median"] == 10
    assert stats["std"] == 0
