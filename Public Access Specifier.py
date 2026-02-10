#  in python are by default public
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(20,"krish")
print(obj.age)
print(obj.name)

# Private Access Modifier
class Student: 
    def __init__(self, age, name): 
        self._age = age      # An indication of private variable
        self._name =name



obj = Student(20,"krish")


# calling by object of class Student
# print(obj.__age)    #we can't acess that , beacuse of private 
# print(obj.__name)   #we can't acess that , beacuse of private 
# print(obj.__funName())


print(obj._age)  ##we can acess that  
