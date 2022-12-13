#single inheritance

# class Me :
#     def mname():
#         print("Me")
# class So(Me):
#     def sname():
#         print("So")

# s1 =So
# s1.mname()
# s1.sname()



# Multiple inheritance 

# class Base1:
#     def b1name():
#         print("Base1 Class")

# class Base2:
#     def b2name():
#         print("Base2 Class")
# class Derived(Base1, Base2):
#     def derived():
#         print("Derived Class")

# d1= Derived 
# d1.b1name()
# d1.b2name()
# d1.derived()


# Multilevel Inheritance 

# class Grandfather:
#     def gname():
#         print("chetan")
# class Father(Grandfather):
#     def fname():
#         print("rohan")
# class Son(Father):
#     def sname():
#         print("aniket")


# s1 = Son
# s1.fname()
# s1.gname()
# s1.sname()


# Hirarchical inheritance 

# class Parent():
#     def pdisplay():
#         print("Parent Name")

# class Child1(Parent):
#     def c1display():
#         print("Child1 Name")
# class Child2(Parent):
#     def c2display():
#         print("Child2 Name")
# class Child3(Parent):
#     def c3display():
#         print("Child3 Name")

# c1= Child1
# c1.c1display()
# c1.pdisplay()
# c2 = Child2
# c2.c2display()

# c3 =Child3
# c3.c3display()


# hybrid inheritance

class School:
    def func1(self):
        print("This function is in school.")


class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()





