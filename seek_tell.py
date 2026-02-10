with open('myfile_3.txt','r') as f:
    print(type(f))
    f.seek(9) #move to the 10 byte in the file
    data = f.read(5) 
    print(f.tell()) # return current position in the file
    print(data)

with open('sample.txt','w') as w:
    w.write("hello hanji, namste!")
    w.truncate(10)
