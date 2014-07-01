temp = open("E:\pythonFile\нд╪Ч\StuCourses.txt","r")
s0=temp.read()
s=s0.split("\n")
a=s[0].split("\t")
b=s[1].split("\t")
c=s[2].split("\t")
d=s[3].split("\t")

courses0=a[3].split(",")
courses1=b[3].split(",")
courses2=c[3].split(",")
courses3=d[3].split(",")

ID=[a[0],b[0],c[0],d[0]]
Name=[a[1],b[1],c[1],d[1]]
Age=[a[2],b[2],c[2],d[2]]

dic_1={ID[1]:{'Courses':courses1,'Age':Age[1],'Name':Name[1]}}
dic_2={ID[2]:{'Courses':courses2,'Age':Age[2],'Name':Name[2]}}
dic_3={ID[3]:{'Courses':courses3,'Age':Age[3],'Name':Name[3]}}
dic=[dic_1,dic_2,dic_3]
print dic
