#The program is to fusion head ear and wrist temperatures
#By Lishen Wang and Steed Huang et al from Suqian Collegue
#March 2020 for Wuhan COVID19 Epidemic

#Import external package
import math,os,csv,xlrd,io

#Read files and extract data for each column
with open("Result/Result.csv",'r') as csvfile:
    reader = csv.reader(csvfile)
    #Traversal file
    list_1 = [row[1]for row in reader]
    #Reset file pointer
    csvfile.seek(0)
    list_2 = [row[2]for row in reader]
    csvfile.seek(0)
    list_3 = [row[3]for row in reader]

#delete the title of data
del list_1[0]
del list_2[0]
del list_3[0]

#Convert string to integer
list_1=list(map(eval,list_1))
list_2=list(map(eval,list_2))
list_3=list(map(eval,list_3))

#Revise data by row according to BodyTempModel
for i in range(0,3):
    if(i==0):
    #adjust head 
        list_1[i]+=0.757
        list_2[i]+=0.757
        list_3[i]+=0.757
    elif(i==1):
    #adjust ear
        list_1[i]+=0.497
        list_2[i]+=0.497
        list_3[i]+=0.497

    elif(i==2):
    #adjust wrist
        list_1[i]+=0.743
        list_2[i]+=0.743
        list_3[i]+=0.743

#Fusion data with self weight
total_1 = list_1[0]+list_1[1]+list_1[2]
fusion_1 = (list_1[0]**2+list_1[1]**2+list_1[i]**2)/total_1

total_2 = list_2[0]+list_2[1]+list_2[2]
fusion_2 = (list_2[0]**2+list_2[1]**2+list_2[i]**2)/total_2

total_3 = list_3[0]+list_3[1]+list_3[2]
fusion_3 = (list_3[0]**2+list_3[1]**2+list_3[i]**2)/total_3

# Write data to file
with open("Result/realTemperate.csv","w",newline='') as f:
    head = ['','circlevar_m','circlevar_a','middle']
    rows = [
        ['data',fusion_1,fusion_2,fusion_3]
    ]
    writer = csv.writer(f)
    writer.writerow(head)
    writer.writerows(rows)
    f.close()
