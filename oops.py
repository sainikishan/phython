# oop is python
# to map with real world scenarios,we started using object in code.ConnectionAbortedError
# this is called oop
# oop is python
#  redenacy redurceuse reusabilty are increaes
#class is a blueprint for creating object
# class Student:
#     name="kishan"
#     age=20
# # crreatimg a object
# s1=Student()
# print(s1.name)
# print(s1.age)
# print(s1)

# facotry
# class Car:
#     color= "blue"
# car1=Car()
# print(car1.color)


# constructor
# all calsses have a function called init(),whick is always excuted when the class is beigninitated.

        

class Student:
    def __init__(self, fullname):
        self.name = fullname
        print("This is a constructor")

# Creating an object outside the class
s1 = Student("kishan kishan")
print(s1.name)

