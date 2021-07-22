print ("SHOPPING LIST")
list = []
bol = True
while (bol) :
    word1 = input ("Add something to the list:")
    list.append (word1)
    word2 = input ("Are you done with the shopping list?")
    if (word2 == " yes") :
        bol = False
    elif (word2 == " no") :
        print ("What else do you need?")
for x in range (0,len (list)) :
    print (list [x], end = "")
