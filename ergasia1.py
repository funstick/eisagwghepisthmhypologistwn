import random
row=[]
table=[]
quad=0

tableWidth = input("Insert number of colums.  ")
tableHeight = input("Insert number of rows.  ")

if (tableWidth*tableHeight)%2 != 0:
    tableContents = tableWidth*tableHeight/2 + 1
else:tableContents = (tableWidth * tableHeight)/2


def fillTable(x,y):

        for i in range(x):
            row = []    #del row[:] edw den douleuei gia kapoio logo
            table.append(row)
            for z in range(y):
                row.append(0)
        

        count = 0
        while count < tableContents:
            sum = random.randrange(0,tableHeight)
            if len(table[sum]) < tableWidth * 2:
                table[sum].append(1)
                count = count + 1

        

        for k in range(tableHeight):
            for j in range(table[k].count(1)):
                table[k].pop(0)
            random.shuffle(table[k])
        



        return table

def find4(x,y,z):
    sum = 0
    for i in range(x):
        for j in range(y):
            if j+3<y:
                if z[i][j] + z[i][j+1] + z[i][j+2] + z[i][j+3] == 4:
                    #print("hitH")
                    sum = sum + 1            
            if i+3<x:
                if z[i][j] + z[i+1][j] + z[i+2][j] + z[i+3][j] == 4:
                    #print('hitV')
                    sum = sum + 1
            if ((j+3)<y) & ((i+3)<x):
                if z[i][j] + z[i+1][j+1] + z[i+2][j+2] + z[i+3][j+3] == 4:
                    #print('hitD')
                    sum = sum + 1
            if ((j-3)>0) & ((i+3)<x):
                if z[i][j] + z[i+1][j-1] + z[i+2][j-2] + z[i+3][j-3] == 4:
                    #print('hitRD')
                    sum = sum + 1    
    return sum
#fillTable(tableHeight,tableWidth)

#find4(tableHeight,tableWidth,fillTable(tableHeight,tableWidth))
total = 0
for g in range(100):
    sum = find4(tableHeight,tableWidth,fillTable(tableHeight,tableWidth))
    #print(sum)
    total = total + sum
    #print(total)
    table=[]
print('MO total',total/100)
