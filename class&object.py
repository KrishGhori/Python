class student :
    name = "krish"
    occupation = "student"
    work = "maja ni life"
    id = 84
    def info(self):
        print(f"name is {self.name}, occupation is {self.occupation}, work is {self.work} then id is {self.id}")

a = student()
a.name = "krishva"
print(a.name,a.occupation)
a.info()
