from ft_filter import ft_filter
import sys


def main():
    """
    Program that filters words longer than a given length N from a string S.

    Args:
        sys.argv[1] (str): The input string.
        sys.argv[2] (int): The minimum word length.

    Raises:
        AssertionError: If arguments are missing or invalid.
    """
    if (len(sys.argv) != 3):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    try:
        S = sys.argv[1]
        N = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    words = S.split()
    result = ft_filter(lambda word: len(word) > N, words)
    print(list(result))


if __name__ == "__main__":
    main()
