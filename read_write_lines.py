f= open('myfile.txt','r')

while True:
    i=0
    line = f.readline()
    if not line :
        break
    i=i+1 
    m1= line.split(",")[0]
    m2= line.split(",")[1]
    m3= line.split(",")[2]
    
    print(f"marks of student {i} in maths {m1}")
    print(f"marks of student {i} in maths {m2}")
    print(f"marks of student {i} in maths {m3}")
    
print(line)

w= open('myfile_2.txt','w')

lines = ['line 1\n','line 2\n','line 3\n']
w.writelines(lines)
w.close()