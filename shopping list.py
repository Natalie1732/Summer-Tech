print ("SHOPPING LIST")
bol = True
while (bol) :
    word1 = input ("Add something to the list.")
    word2 = input ("Are you done with the shopping list?")
    list = [word1]
    if (word2 == " yes") :
        bol = False
        print (list)
    elif (word2 == " no") :
        print ("What else do you need?")
