class employee :
    comanyname = "GK"
    def __init__(self,name):
        self.name =name
        self.raise_amount= 0.05
        
    def showdetails(self):
        print(f"name is {self.name} and  the raise amount  is {self.raise_amount} in {self.comanyname} company")
        
e1 = employee("krish")
e1.raise_amount = 0.2
e1.showdetails()

e2 = employee("RK")
e2.comanyname = "KG"
e2.showdetails()