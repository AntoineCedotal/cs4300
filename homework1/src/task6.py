# task6.py

def count_words_in_file(file_path: str) -> int:
    """
    Reads a text file and returns the number of words in it.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    words = content.split()  # split by whitespace
    return len(words)


if __name__ == "__main__":
    file_path = "task6_read_me.txt"
    word_count = count_words_in_file(file_path)
    print(f"The file '{file_path}' contains {word_count} words.")
