# f = open('myfile.txt','r')

# tamp = f.read()
# print(tamp)
# f.close()

w= open('myfile.txt','w')
w.write("km chho?")
w.close()

with open('myfile.txt','a') as w :
    w.write("how are you")