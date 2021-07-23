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

word = input ("where would you like to go?")
if (input == "1,1"):
    list [0] [0] = "X"
    print (list [x] [y], end = "")
elif (input == "1,2"):
    list [0] [1] = "x"
    print (list [x] [y], end = "")
if (input == "1,3"):
    list [0] [2] = "x"
    print (list [x] [y], end = "")
