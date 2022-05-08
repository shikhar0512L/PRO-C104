import csv

with open("data.csv", newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)

#pop the titles of the list
file_data.pop(0)

new_data=[]

for i in range(len(file_data)):
    n_num=file_data[i][2]
    new_data.append(float(n_num))

#getting the mean
n=len(new_data)
total=0

for i in new_data:
    total=total+i

mean=total/n

print(mean)