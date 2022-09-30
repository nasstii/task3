print("Как Вас зовут?")
name=input()
print("Какая у Вас фамилия?")
sname=input()
print("В каком году Вы родились?")
data=int(input())
print(name,sname,data,sep="_")
data=data+60
name,sname=sname,name
print(name,sname,data,sep="_")
