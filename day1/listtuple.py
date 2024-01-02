mylist1=[10,20,30,40,50]
mylist2=["apple","rajh",10,30,30,"orangle"]

print(mylist1)
print(mylist2)

print(mylist2[0],mylist1[-1])
print(mylist2[2:5])
print(mylist1[2:5])
print(mylist1[-4:-1])

for i in mylist2:
    print(i, end=' ')

for i in mylist1:
    print(i, end=" ")

print(len(mylist2),len(mylist1))

if 10 in mylist1:
    print("yes")
else:
    print("no")
print(mylist1.append("bharath"))
print(mylist1)
mylist1.insert(1,"kumar")
print(mylist1)

mylist1.pop()
print(mylist1)
mylist1.pop(1)
print(mylist1)
del mylist1[3]
print(mylist1)
print(mylist1.count(10))
mylist3=mylist1.copy()
mylist1.extend(mylist3)
print(mylist3)

mylist3.clear()
print(mylist1)
mylist1.append(mylist2)
print(mylist1)
mylist3=mylist1+mylist2
print(mylist3)
print(mylist3[8])


mytuple=(1,"hello",30)
print(mytuple[2])


# // create
# // Access using index and range
# // append
# // insert
# // pop
# // del
# // clear
# // copy
# combine append copy entends


