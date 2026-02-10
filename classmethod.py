class employee :
    company = "apple"

    def details(self) :
        print(f"the company name is {self.company} and the employee name is {self.name}")

    # def changecompany(self,newcompany):
    #     self.company = newcompany
     
    @classmethod  #if you want change the name of company then ues the @classmethod
    def changecompany(self,newcompany):  #commant it
        self.company = newcompany   #commant it
       
    
    
e1 = employee()
e1.name = "krish" 
e1.details()
e1.changecompany("ABC")
e1.details()
print(employee.company)
    
    