list = []
for x in range (0,3):
    print ("")
    list.append ([])
    for y in range (0,3):
        print ("*",end = "")
        list [x].append ("*")
print (list, end = "")

for x in range (0, len (list)) :
    print ("")
    for y in range (0, len (list)) :
        print (list [x] [y], end = "")

bol = True
num = 0 + 1
while (bol):
    word1 = int (input ("which row would you like to go in? (0,1,2)"))
    word2 = int (input ("which column would you like to go in? (0,1,2)"))
    list [word1] [word2] = "X"
    for x in range (0, len (list)) :
        print ("")
        for y in range (0, len (list)) :
            print (list [x] [y], end = "")
    if (num == 1)
