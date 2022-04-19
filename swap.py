def swapFile():
    fileA = input('Enter 1st file name: ')
    fileB = input('Enter 2nd file name: ')

    a = open(fileA,'r')
    data1 = a.read()
    
    b = open(fileB,'r')
    data2 = b.read()

    c = open(fileA,'w')
    c.write(data2)

    d = open(fileB,'w')
    d.write(data1)

swapFile()