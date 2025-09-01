import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def main():
    """
    Converts a given string into Morse code.
    Usage: python sos.py "your text"
    """

    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    recieved_string = sys.argv[1].upper()
    output = ""
    for char in recieved_string:
        if char in NESTED_MORSE:
            output += NESTED_MORSE[char]
        else:
            print("AssertionError: the argumenents are bad")
            sys.exit(1)
    print(output.rstrip())


if __name__ == "__main__":
    main()
