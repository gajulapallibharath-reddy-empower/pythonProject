# This is sample python practice program

'''Helllo
Sample'''
import keyword

num=int(input("Enter a Number"))
if num%2==0:
    print(num, "is even number ")

weeknum=input("Enter a week Number")
if weeknum==1:
    print("Monday")
elif weeknum==2:
    print("Tue")
elif weeknum==3:
    print("Wed")
elif weeknum == 4:
    print("Thu")
elif weeknum == 5:
    print("Fri")
elif weeknum == 6:
    print("Sat")
elif weeknum == 7:
    print("Sun")
else:
    print("invalid")

print("welcome") if(1) else print("hi")
{print("welcome"),print("hi")} if(1) else {print("hi"),print("hello") }

name,age,sal="bharath",34,234000

print("Name is :%s age is:%s Salary:%s" %(name,age,sal))
print("Name is :{} age is:{} Salary:{}" .format(name,age,sal))

print(keyword.kwlist)