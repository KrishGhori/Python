#strings are immutable
a="hello!!!!!"
print(a.upper())

b="HII"
print(b.lower)

# using rstrip()
print(a.rstrip("!"))

# replace()
print(a.replace("hello","hmm"))

# split()
print(a.split("o"))

# capitalize()
c="how are you : "
print(a.capitalize())
print(c.capitalize())

# center()
print(a.center(20))
print(b.center(20))
print(c.center(20))

# count()
print(a.count("!"))

# endswith()
print(a.endswith("h"))
print(a.endswith("!"))

# startswith()
# if the string start with given value than return true
print(a.startswith("h"))

# they are find a indax tu use find()
# if word was not there then return -1
print(a.find("l"))


# index
# if word was not there then return error
print(a.index("!"))
# print(a.index("u"))

# isalnum
# if A-Z , a-z , 0-9 then return gives true
# then returns false
print(a.isalnum())

# isalpha
# if A-Z,a-z then return true
# otherwaise return false
print(a.isalpha())

# islower
# if all caracter was lower case return true otherwaise false
print(a.islower())

# isupper()
# if string are upper case then return true
# else return false
print(a.isupper())
print(b.isupper())


# isprintable()
# example (/n) this is not pritable so that ruteurn false
d="this is you \n"
print(a.isprintable())
print(d.isprintable())


# isspace()
# if there is any space(      ) then return true otherwaise false
e=" F h  F "
print(d.isspace())

# istitle()
# if frist latter of each word is capitalized then return ture
# else return false
print(a.istitle())
print(b.istitle())

# swapcase()
# uppercase to convert lowercase and lower - upper case
print(a.swapcase())

# title()
# all word first leter to convert uppaer case
print(c.title())




