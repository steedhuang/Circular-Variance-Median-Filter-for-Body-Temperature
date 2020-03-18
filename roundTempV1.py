#The program is to fusion head ear and wrist temperature
#By Lishen Wang and Steed Huang et al from Suqian Collegue
#March 2020 for Wuhan Epidemic

import csv,os,math
import pandas as pd
import matplotlib.pyplot as plt

print("current fold is %s"%os.getcwd())
# string = os.getcwd()
# string_final = ""
# for s in string:
#     if s == '\\':
#         string_final += '/' 
#     else:
#         string_final += s  
#the data of first list
with open("head.csv") as csvfile:
    reader = csv.reader(csvfile)
    list_1 = [row[1]for row in reader]

with open("ear.csv") as csvfile:
    reader = csv.reader(csvfile)
    list_2 = [row[1]for row in reader] 

with open("wrist.csv") as csvfile:
    reader = csv.reader(csvfile)
    list_3 = [row[1]for row in reader]


#the data of 1/2/3
#the sort of first data
list_1.sort()
#the sort of second data
list_2.sort()
#the sort of third data
list_3.sort()

#choose the middle number of list_1

if len(list_1)%2==1:
    mid_number_1 = (float)(list_1[(int)((len(list_1)+1)/2)-1] )
else :
    mid_number_1 = ((float)(list_1[(int)((len(list_1)+1)/2)-1]) + (float)(list_1[(int)((len(list_1))/2)-1]))/2
#chocie the middle number of list_2   
if len(list_2)%2==1:
    mid_number_2 = (float)(list_2[(int)((len(list_2)+1)/2)-1])
else :
    mid_number_2 = ((float)(list_2[(int)((len(list_2)+1)/2)-1]) + (float)(list_2[(int)((len(list_2))/2)-1]))/2
#chocie the middle number of list_3
if len(list_3)%2==1:
    mid_number_3 = (float)(list_3[(int)((len(list_3)+1)/2)-1] )
else :
    mid_number_3 = ((float)(list_3[(int)((len(list_3)+1)/2)-1]) + (float)(list_3[(int)((len(list_3))/2)-1]))/2


circlevar_1 = 100
circlevar_ori = 0
averange_ori = 0.0
N = eval(input("Pls input sliding window length, say 10："))

for i in range(0,len(list_1)-N+1):
    total_1 = 0
    for j in range(i,i+N):
        total_1 +=float(list_1[j])
    averange_ori = total_1/N
    for j in range(i,i+N):
        circlevar_ori = circlevar_ori + (float(list_1[j])-averange_ori)**(math.sqrt(2)+math.sqrt(-2)*(j+1))
        circlevar_ori = abs(circlevar_ori)
    if circlevar_1>circlevar_ori:
        circlevar_1 = circlevar_ori
        averange_1 = averange_ori


circlevar_2 = 100
circlevar_ori = 0
averange_ori = 0.0
for i in range(0,len(list_2)-N+1):
    total_2 = 0
    for j in range(i,i+N):
        total_2 +=float(list_2[j])
    averange_ori = total_2/N
    for j in range(i,i+N):
        circlevar_ori = circlevar_ori + (float(list_2[j])-averange_ori)**(math.sqrt(2)+math.sqrt(-2)*(j+1))
        circlevar_ori = abs(circlevar_ori)
    if circlevar_2>circlevar_ori:
        circlevar_2 = circlevar_ori
        averange_2 = averange_ori


circlevar_3 = 100
circlevar_ori = 0
averange_ori = 0.0
for i in range(0,len(list_3)-N+1):
    total_3 = 0
    for j in range(i,i+N):
        total_3 +=float(list_3[j])
    averange_ori = total_3/N
    for j in range(i,i+N):
        circlevar_ori = circlevar_ori + (float(list_3[j])-averange_ori)**(math.sqrt(2)+math.sqrt(-2)*(j+1))
        circlevar_ori = abs(circlevar_ori)
    if circlevar_3>circlevar_ori:
        circlevar_3 = circlevar_ori
        averange_3 = averange_ori

circlevar = [circlevar_1,circlevar_2,circlevar_3]
mid_number = [mid_number_1,mid_number_2,mid_number_3]

with open("Outcome.csv","w",newline='') as f:
    head = ['','circlevar(℃)','middle(℃)']
    rows = [
        ['forehead',averange_1,mid_number_1],
        ['ear',averange_2,mid_number_2],
        ['wrist',averange_3,mid_number_3]
    ]
    writer = csv.writer(f)
    writer.writerow(head)
    writer.writerows(rows)
    f.close()

csv = pd.read_csv('Outcome.csv',encoding="ISO-8859-1")
csv.to_excel('Outcome.xlsx', sheet_name='data')
if os.path.exists('Outcome.csv'):  # if file exists
    # delete file with either method below
    os.remove('Outcome.csv')  
    #os.unlink(path)
else:
    print('no such file')


# print("There is temperature's data of circlevar:")
# print("The temperature of Forehead is %f" %averange_1)
# print("The temperature of Behind ear is %f" %averange_2)
# print("The temperature of Wrist is %f" %averange_3)

# print("There is temperature's data of middle number:")
# print("The temperature of Forehead is %f" %mid_number_1)
# print("The temperature of Behind ear is %f" %mid_number_2)
# print("The temperature of Wrist is %f" %mid_number_3)
