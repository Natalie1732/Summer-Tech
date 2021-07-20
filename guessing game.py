import random
num = random.randint (0,10)
bol = True
while (bol):
    word = int ( input ("Input a number from 0-10"))
    if (word == num) :
        bol = False + print ("correct")
    elif (word !=num) :
        print ("wrong")
    if (word < num) :
        print ("it's greater than that number")
    elif (word > num) :
        print ("it's less than that number")
