class MyClass:
    def __init__(self, name,id):
        self.name= name
        self.id =id

    def information(self):
        print(f"hello my name is{self.name} and my id is {self.id}")


# Inheritance 
class detailsofclass(MyClass):
    def details(self):
        print(f"from detailsofclass beacuse of Inheritance hello my name is{self.name} and my id is {self.id}")
    
e1 = MyClass("krish ghori",59)
e1.information()

e2 =MyClass("krishva",72)
e2.information()

E1= detailsofclass("vanshi",72)
E1.details()






