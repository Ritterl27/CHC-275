reverse =  ""
pal = input("what is your word? ").strip().lower()
for char in pal:
    reverse = char + reverse 
print(reverse)
