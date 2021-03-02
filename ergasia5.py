import random
row=[]
table=[]
quad=0

tableWidth = input("Insert number of colums.  ")
tableHeight = input("Insert number of rows.  ")

if (tableWidth*tableHeight)%2 != 0:
    tableContents = tableWidth*tableHeight/2 + 1
else:tableContents = (tableWidth * tableHeight)/2
#print(tableContents)

def fillTable(x,y):
        table=[]
        for i in range(x):
            row = []    #del row[:] edw den douleuei gia kapoio logo
            table.append(row)
            for z in range(y):
                row.append('O')
        #    print(row)
        #print("")

        count = 0
        while count < tableContents:
            sum = random.randrange(0,tableHeight)
            if len(table[sum]) < tableWidth * 2:
                table[sum].append('S')
                count = count + 1

        #for u in range(tableHeight):
        #    print(table[u])

        for k in range(tableHeight):
            for j in range(table[k].count('S')):
                table[k].pop(0)
            random.shuffle(table[k])
        #print("")
        #for u in range(tableHeight):
        #    print(table[u])
        #print("")



        return table

#fillTable(tableHeight,tableWidth)

def findSOS(x,y,z):
    sum = 0
    for i in range(x):
        for j in range(y):
            if j+2<y:
                if z[i][j]=='S':
                    if z[i][j+1]=='O':
                        if z[i][j+2]=='S':
                            #print("hitH")
                            sum = sum + 1
            #elif j-3>0:
            #    print(i,j)
            #    if z[i][j] + z[i][j-1] + z[i][j-2] + z[i][j-3] == 4:
            #        print("hitH",i,j)
            if i+2<x:
                if z[i][j]=='S':
                    if z[i+1][j]=='O':
                        if z[i+2][j]=='S':
                            #print('hitV')
                            sum = sum + 1
            if ((j+2)<y) & ((i+2)<x):
                if z[i][j]=='S':
                    if z[i+1][j+1]=='O':
                        if z[i+2][j+2]=='S':
                            #print('hitD')
                            sum = sum + 1
            if ((j-2)>0) & ((i+2)<x):
                if z[i][j]=='S':
                    if z[i+1][j-1]=='O':
                        if z[i+2][j-2]=='S':
                            #print('hitRD')
                            sum = sum + 1
    #print('number of SOS= ',sum)
    return sum

count=0
for i in range(100):
    count += findSOS(tableHeight,tableWidth,fillTable(tableHeight,tableWidth))

print(count)
