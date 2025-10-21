reverse = ""
pal = input("what is your word? ").strip().lower()
for char in pal:
    pal2 = char - char
    reverse = pal2 + pal
print(reverse)
