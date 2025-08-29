import sys

if len(sys.argv) == 1:
    sys.exit(0)
if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)
arg = sys.argv[1]
try:
    number = int(arg)
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit(1)
if number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
