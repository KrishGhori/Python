# The is operator compares the identity of two objects
# you can't change the value of a,b ,so it is store in one
a = "4"
b = "4"
print(a is b) #exact location of object in memory
print(a==b) # value

# you can change the value of array ,so it is store saprate
x = [1,2,3]
y= [1,2,3]
print(x is y)
print(x==y)