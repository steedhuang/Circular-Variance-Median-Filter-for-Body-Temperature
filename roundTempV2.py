#The program is to fusion head ear and wrist temperatures
#By Lishen Wang and Steed Huang et al from Suqian Collegue
#March 2020 for Wuhan COVID19 Epidemic

import csv,os,math
#import pandas as pd

print("current fold is %s"%os.getcwd())
#Read files and extract data for each column
with open("Data/head.csv") as csvfile:
    reader = csv.reader(csvfile)
    list_1 = [row[1]for row in reader]

with open("Data/ear.csv") as csvfile:
    reader = csv.reader(csvfile)
    list_2 = [row[1]for row in reader] 

with open("Data/wrist.csv") as csvfile:
    reader = csv.reader(csvfile)
    list_3 = [row[1]for row in reader]

#the data of 1/2/3
#the sort of first data
list_1.sort()
#the sort of second data
list_2.sort()
#the sort of third data
list_3.sort()

#apply Median filter directly
#choose the middle number of list_1
if len(list_1)%2==1:
    mid_number_1 = (float)(list_1[(int)((len(list_1)+1)/2)-1] )
else :
    mid_number_1 = ((float)(list_1[(int)((len(list_1)+2)/2)-1]) + (float)(list_1[(int)((len(list_1))/2)-1]))/2
#chocie the middle number of list_2   
if len(list_2)%2==1:
    mid_number_2 = (float)(list_2[(int)((len(list_2)+1)/2)-1])
else :
    mid_number_2 = ((float)(list_2[(int)((len(list_2)+2)/2)-1]) + (float)(list_2[(int)((len(list_2))/2)-1]))/2
#chocie the middle number of list_3
if len(list_3)%2==1:
    mid_number_3 = (float)(list_3[(int)((len(list_3)+1)/2)-1] )
else :
    mid_number_3 = ((float)(list_3[(int)((len(list_3)+2)/2)-1]) + (float)(list_3[(int)((len(list_3))/2)-1]))/2

#apply Meridian filter first and then Median filter
#circlevar of data_1 slice
circlevar_1 = 100
circlevar_ori = 0
averange_ori = 0.0
index_1 = 0
li_1 = []
N = eval(input("Pls input sliding window length, say 10："))

#calculate Meridian
for i in range(0,len(list_1)-N+1):
    total_1 = 0
    for j in range(i,i+N):
        total_1 +=float(list_1[j])
    averange_ori = total_1/N
    for j in range(i,i+N):
        circlevar_ori = circlevar_ori + (float(list_1[j])-averange_ori)**(math.sqrt(2)*(1+1j)*(j+1))
        circlevar_ori = abs(circlevar_ori)
    if circlevar_1>circlevar_ori:
        circlevar_1 = circlevar_ori
        averange_1 = averange_ori
        index_1=i
for i in range(index_1,index_1+N):
	li_1.append(list_1[i])

#calculate Median
if len(li_1)%2==1:
    mid_1 = (float)(li_1[(int)((len(li_1)+1)/2)-1] )
else :
    mid_1 = ((float)(li_1[(int)((len(li_1)+2)/2)-1]) + (float)(li_1[(int)((len(li_1))/2)-1]))/2

# circlevar of data_2 slice
circlevar_2 = 100
circlevar_ori = 0
averange_ori = 0.0
index_2 = 0
li_2 = []
for i in range(0,len(list_2)-N+1):
    total_2 = 0
    for j in range(i,i+N):
        total_2 +=float(list_2[j])
    averange_ori = total_2/N
    for j in range(i,i+N):
        circlevar_ori = circlevar_ori + (float(list_2[j])-averange_ori)**(math.sqrt(2)+(1.414j)*(j+1))
        circlevar_ori = abs(circlevar_ori)
    if circlevar_2>circlevar_ori:
        circlevar_2 = circlevar_ori
        averange_2 = averange_ori
        index_2 = i
for i in range(index_2,index_2+N):
	li_2.append(list_2[i])

if len(li_2)%2==1:
    mid_2 = (float)(li_2[(int)((len(li_2)+1)/2)-1] )
else :
    mid_2 = ((float)(li_2[(int)((len(li_2)+2)/2)-1]) + (float)(li_2[(int)((len(li_2))/2)-1]))/2

# circlevar of data_3 slice
circlevar_3 = 100
circlevar_ori = 0
averange_ori = 0.0
index_3 = 0
li_3 = []
for i in range(0,len(list_3)-N+1):
    total_3 = 0
    for j in range(i,i+N):
        total_3 +=float(list_3[j])
    averange_ori = total_3/N
    for j in range(i,i+N):
        circlevar_ori = circlevar_ori + (float(list_3[j])-averange_ori)**(math.sqrt(2)+(1.414j)*(j+1))
        circlevar_ori = abs(circlevar_ori)
    if circlevar_3>circlevar_ori:
        circlevar_3 = circlevar_ori
        averange_3 = averange_ori
        index_3 = i
for i in range(index_3,index_3+N):
	li_3.append(list_3[i])
if len(li_3)%2==1:
    mid_3 = (float)(li_3[(int)((len(li_3)+1)/2)-1] )
else :
    mid_3 = ((float)(li_3[(int)((len(li_3)+2)/2)-1]) + (float)(li_3[(int)((len(li_3))/2)-1]))/2  

#Write three filter output to file
#Meridian and Median, Meridian and Average, Median only
with open("Result/Result.csv","w",newline='') as f:
    head = ['','circlevar_m','circlevar_a','middle']
    rows = [
        ['forehead',mid_1,averange_1,mid_number_1],
        ['ear',mid_2,averange_2,mid_number_2],
        ['wrist',mid_3,averange_3,mid_number_3]
    ]
    writer = csv.writer(f)
    writer.writerow(head)
    writer.writerows(rows)
    f.close()

input("Result has been generate!,Press 'Enter' to close!")