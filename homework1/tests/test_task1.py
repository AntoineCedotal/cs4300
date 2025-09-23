import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import task1

def test_hello_world(capsys):
    task1.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World!"


def main():
    test_hello_world("")


if __name__ == '__main__':
    main()