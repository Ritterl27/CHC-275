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

msftavg1 = sum(msft)/len(msft)
amznavg1 = sum(amzn)/len(amzn)
nvdaavg1 = sum(nvda)/len(nvda)



file = open("day2.txt","r")
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

msftavg2 = sum(msft)/len(msft)
amznavg2 = sum(amzn)/len(amzn)
nvdaavg2 = sum(nvda)/len(nvda)
buys = []
if msftavg2 > msftavg1:
    buys.append("msft")
if amznavg2 > amznavg1:
    buys.append("amzn")
if nvdaavg2 > nvdaavg1:
    buys.append("nvda")
line0 = f"msftavg1: {msftavg1}, msftavg2: {msftavg2}\n"
line1 = f"amznavg1: {amznavg1}, amznavg2: {amznavg2}\n"
line2 = f"nvdaavg1: {nvdaavg1}, nvdaavg2: {nvdaavg2}\n"
line3 = f"buys: {buys}"
buffer = [line0,line1,line2,line3]
file = open("report.txt","w")
file.writelines(buffer)
file.close()





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