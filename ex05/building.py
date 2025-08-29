import sys


def main() -> int:
    """
    Analyzes a given string (from command-line argument or user input)
    and counts:
    - upper-case letters
    - lower-case letters
    - digits
    - spaces
    - punctuation marks

    Prints:
        AssertionError: If more than one argument is provided.
    """
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)

    if len(sys.argv) == 2:
        text_input = sys.argv[1]
    else:
        text_input = input("What is the text to count?\n")

    count_upper = 0
    count_lower = 0
    count_spaces = 0
    count_digits = 0
    count_punctuation = 0

    for char in text_input:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif char.isspace():
            count_spaces += 1
        elif char.isdigit():
            count_digits += 1
        else:
            count_punctuation += 1

    print(f"The text contains {len(text_input)} characters:")
    print(f"{count_upper} upper letters")
    print(f"{count_lower} lower letters")
    print(f"{count_punctuation} punctuation marks")
    print(f"{count_spaces} spaces")
    print(f"{count_digits} digits")
    return (0)


if __name__ == "__main__":
    # print(main.__doc__)
    main()
