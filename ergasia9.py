f = open("sample.txt","r")

txt=f.read()
ascii={}
monoi=[]

for i in range(len(txt)):
    if ord(txt[i]) % 2 == 1:
        monoi.append(ord(txt[i]))

for i in range(len(monoi)):
    ascii[monoi[i]] = 0
for i in range(len(monoi)):
    if ascii[monoi[i]] == 0:
        ascii[monoi[i]] = 1
    else:
        tmp = ascii[monoi[i]]
        ascii[monoi[i]] = tmp + 1
sum = 0
for i in ascii.keys():
    sum = sum + ascii[i]

perc={}
for i in ascii.keys():
    perc[i] = (ascii[i]*100)/sum

perclist=[]
for i in perc.keys():
        for j in range(perc[i]):
            perclist.append('*')
        print(chr(i),':',perclist)
        perclist=[]
print(monoi)
print(ascii)
print(sum)
print(perc)
