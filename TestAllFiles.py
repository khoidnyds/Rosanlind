import os


def main():
    os.system("python -m unittest discover -s . -p '*_test.py'")


if __name__ == "__main__":
    main()
