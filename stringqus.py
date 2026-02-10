# s = input("enter the string:-") 
# count = 0
# for i in s :
#     count+= 1
# print(count)

# a = input("enter the email:-") 
# posion = a.index('@') # find the postion of @  
# print(a[0:posion])

# count frequency
# b = input("enter the string:-")
# terms = input("what would like to search:-")
# countforterms = 0
# for i in b:
#     if i == terms :
#         countforterms += 1
# print(countforterms)

#remove particular character from string
# c = input("enter the string:-")
# remove = input("what would like to remove:-")
# ans = ''
# for i in c:
#     if i != remove:
#         ans = ans + i
# print(ans)


# check palidrome string
# d = input("enter the string:-")
# flag = True
# for i in range(0,len(d)//2) :
#     if d[i] != d[len(d)-i-1] :
#         flag = False
#         print("not a palidrome")
#         break
# if flag :
#     print("string is palidrome")

# count the word 
# e = input("enter the string:-")
# list = []
# space = ''
# for i in e :
#     if i != ' ' :
#         space = space + i 
#     else :
#         list.append(space)
#         space = ''
# final =list.append(space) #for last word
# print(final)

# title string without using title()
# f = input("enter the string:-")
# upl = []
# for i in f.split():
#     upl.append(i[0].upper() + i[1:].lower())
# print(" ".join(upl))


# conver integer to sting without using str()
g = int(input("enter the number:-"))
digit = '0123456789'
lol = ''
while g != 0 :
    lol = digit[g % 10] + lol
    g = g // 10
print(lol)
print(type(lol))

