myset={10,20,30,10,30,40,"string","String"}
print(myset)

for i in myset:
    print(i)


if 10 in myset:
    print("yes")

myset.add("hello")
myset.update([10,30,23,1,2,5])
print(myset)

print(len(myset))
myset.remove(30)
myset.pop()
s2={'x'}
s3=myset.union(s2)

print(myset,s3)

md={
    "Name":"Bharath",
    "age":30,
    "address":"MRPalli"
}
print(md)

for i in md:
    print(i,md[i])

for x,y in md.items():
    print(x, y)
for i in md.values():
    print(i)







