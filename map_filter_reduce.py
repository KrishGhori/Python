def cube (x):
    return x*x*x

l = [1,2,4,6,8,10]
# Cube each number using the map function
newl = list(map(cube,l))
print(newl)


def filter_funtion(a):
    return a>4

newnewl= list(filter(filter_funtion,l))
print(newnewl)

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x,y :x+y , numbers)
print(sum)