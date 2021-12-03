import csv
import math

with open('data.csv',newline="") as f:
    r = csv.reader(f)
    ls = list(r)
data1 = ls[0]

def mean(data) :
    n = len(data)
    total = 0
    for num in data:
        total += float(num)
    mean= total/n
 
    return mean

squaredList = []

for number in data1 :
    a = int(number)-mean(data1)
    a = a**2

    squaredList.append(a)

sum = 0

for i in squaredList:
    sum = sum + i

result = sum/(len(data1)-1)

std_deviation = math.sqrt(result)

print(std_deviation)


