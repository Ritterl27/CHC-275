mylist = [5,10,15,20,25,30,35]
print(mylist[0])
#counting in com sci starts from 0 not 1
product = (mylist[0] * mylist[1])
print(product)
#negative values will traverese the list backwards
#list attributes do not have to be the same data type
mylist2 = [1,True,"hello"]
print(mylist2[2])
i = 0
#how many are in the list
while i <= len(mylist) - 1:
    print(mylist[i])
    i = i + 1
for num in mylist:
    print(num)
print(mylist)
for num in mylist:
    num = num + 5
print(mylist)
while i <= len(mylist) - 1:
    mylist[i] = mylist[i] + 5
    i = i + 1
print(mylist)