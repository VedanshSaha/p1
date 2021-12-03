import csv

with open("SOCR-HeightWeight.csv",newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    height = fileData[i][1]
    newData.append(float(height))
    
total = 0
length1 = len(newData)

for i in range(length1) :
    total += i

mean = total/length1

print("The mean is : "+str(mean))
