def average(*numbers) :
    sum=0
    for i in numbers :
        sum = sum + i
        return sum/len(numbers)

c=average(6,4) 
print(c)



# def name(**name) :
#     print("hello",name["fname"],name["mname"],name["lname"])

# name(fname="v",mname="g",lname="K")