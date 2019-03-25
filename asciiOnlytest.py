#tests if string is all ascii
#https://stackoverflow.com/questions/35889505/check-that-a-string-contains-only-ascii-characters/35895857
daString = input("Paste string here: ")


if all(ord(char) < 128 for char in daString):
    print("All characters are ascii")
else:
    print("There are non ascii characters in this string!")