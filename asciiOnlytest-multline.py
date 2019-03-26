#Tests if string is all ascii, accepts multiline user input.
#https://stackoverflow.com/questions/11664443/how-do-i-read-multiple-lines-of-raw-input-in-python - Junuxx
#https://stackoverflow.com/questions/35889505/check-that-a-string-contains-only-ascii-characters/35895857 - warvariuc

print("Paste string here. Hit enter, then input ';;' then hit enter again")

daString = ""
stopword = ";;"
while True:
    line = input()
    if line.strip() == stopword:
        break
    daString += "%s\n" % line

if all(ord(char) < 128 for char in daString):
    print("All characters are ascii")
else:
    print("There are non ascii characters in this string!")