#tests if string is all ascii
daString = input("Paste string here: ")


if all(ord(char) < 128 for char in daString):
    print("All characters are ascii")
else:
    print("There are non ascii characters in this string!")