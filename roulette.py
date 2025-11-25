red = []
black = []
even = []
odd = []
file = open("number.txt","r")
buffer = file.readlines()
file.close()
even.append(buffer[1])
print(even)