class one:
    def fun1(self):
        print(" this is fun 1 in one class")


class two(one):
    def fun2(self):
        print(" this is fun 2 in two class")


class three(two):
    def fun3(self):
        print(" this is fun 3 in three class")


class four(two):
    def fun4(self):
        print(" this is fun 4 four calss")
        super().fun2()
        super().fun1()


f4=four()
f4.fun1()
f4.fun2()
f3=three()
f3.fun2()
f3.fun3()
f4.fun4()


class four(two):
    def fun4(self,name=None):
        print(name)
        super().fun2()
        super().fun1()


f4=four()
f4.fun4()
f4.fun4("bharath")

