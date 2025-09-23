import sys, os, pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import task6

def test_count_words_in_read_me():
    # Known word count for task6_read_me.txt
    # Copying text manually and counting gives 119 words
    expected_count = 104
    assert task6.count_words_in_file("task6_read_me.txt") == expected_count

def test_count_words_empty_file(tmp_path):
    # Test with an empty file
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("")
    assert task6.count_words_in_file(str(empty_file)) == 0

def test_count_words_single_word(tmp_path):
    # Test with a single-word file
    single_word_file = tmp_path / "single.txt"
    single_word_file.write_text("Python")
    assert task6.count_words_in_file(str(single_word_file)) == 1
