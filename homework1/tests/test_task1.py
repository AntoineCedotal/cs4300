import task1

def test_hello_world(capsys):
    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"


def main():
    test_hello_world("")


if __name__ == '__main__':
    main()