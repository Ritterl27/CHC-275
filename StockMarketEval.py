file = open("day.txt","r")
buffer = file.readlines()
file.close()
msft = buffer[0].split(",")
amzn = buffer[1].split(",")
nvda = buffer[2].split(",")
msft.pop(0)
amzn.pop(0)
nvda.pop(0)

for i in range(len(msft)):
    msft[i] = int(msft[i])
    amzn[i] = int(amzn[i])
    nvda[i] = int(nvda[i])

print(msft)
msftavg1 = sum(msft)/len(msft)
print(msftavg1)









"""file = open("day2.txt","r")
buffer = file.readlines()
file.close()
msft2 = buffer[0].split(",")
amzn2 = buffer[1].split(",")
nvda2 = buffer[2].split(",")
msft2.pop(0)
amzn2.pop(0)
nvda2.pop(0)
for i in range(len(msft2)):
    msft2[i] = int(msft2[i])
    amzn2[i] = int(amzn2[i])
    nvda2[i] = int(nvda2[i])

buffer2 = []
buffer2.append()
buffer2.append()
buffer2.append()
file = open("report.txt","w")
file.writelines(buffer)
"""