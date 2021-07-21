for x in range (0,5) :
    print ("")
    for y in range (0,5) :
        print ("*",end = "")

for x in range (0,5) :
    print ("")
    for y in range (0,x) :
        print ("*", end = "")

for x in range (0,5) :
    print ("")   
    for y in range (5,x,-1) :
        print (" ", end = "")
    for z in range (0,x) :
        print ("*", end = "")

for x in range (0,5) :
    print ("")
    for y in range (5,x,-1) :
        print (" ", end = "")
    for z in range (-1,x) :
        print ("*", end = "")
    for a in range (0,x) :
        print ("*", end = "")

for x in range (5,0,-1) :
    print ("")
    for y in range (-1,x) :
        print (" ", end = "")
    for z in range (-1,x) :
        print ("*", end = "")
    for a in range (-1,x) :
        print ("*", end = "")
