<<<<<<< HEAD
pal = input("what is your word? ").strip().lower()
pal2 = "".join(pal.split())
reverse = ""
for char in pal2:
    reverse = char + reverse
if reverse == pal2:
    print("your word is a palindrome")
else:
    print("your word is not a palindrome ")

=======
reverse =  ""
pal = input("what is your word? ").strip().lower()
for char in pal:
    reverse = char + reverse 
print(reverse)
>>>>>>> 4202eb13c5bc337bd2784c53b51787b9dfdb5f10
