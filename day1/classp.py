

class one:
    def fun1(self):
        print("hello func1")
    def fun2(self,a):
        print("hellow fun2", a)

ob1=one()
ob1.fun1()
ob1.fun2(10)

g_v1,g_v2=10,20
class two:
    c_v1,c_v2=23,34

    def fun1(self):
        print(self.c_v1,self.c_v2)
        print(g_v1,g_v2)

    def fun2(self):
        l_v1,l_v2=45,56
        print(l_v1,l_v2)
        print(self.c_v1,self.c_v2)
        print(g_v1)

    def __init__(self):
        print("this is class constructor")

ob2=two()
ob2.fun2()
ob2.fun1()

ob2=two()

class emp:
    def __init__(self,empname,empid,empsal):
        self.empname=empname
        self.empid=empid
        self.empsal=empsal

    def __str__(self):
        return self.empname+self.empid

    def display(self):
        print(self.empname,self.empid,self.empsal)


e1=emp("bharath","12",250000)
e1.display()
print(e1)
