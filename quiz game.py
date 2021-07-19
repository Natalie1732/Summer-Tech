print ("PLANT QUIZ")
print ("What is the purpose of flower petals?")
word = input ("To attract bees (1)     To protect flower seeds (2)" )
if (word == "1") :
    print ("correct, they are used to attract bees")
elif (word == "2") :
    print ("wrong, petals are used to attract bees")
else :
    print ("that wasn't an option")
print ("What is an autotroph?")
word = input ("A type of bacteria (1)      An organism that can make its own food (2)      An organism that reproduces asexually (3)")
if (word == "1") :
    print ("wrong, there are no bacteria called autotrophs")
elif (word == "2") :
    print ("correct, autotrophs can make their own food")
if (word == "3") :
    print ("wrong, an autotroph is an organism that makes its own food")
print ("How can you tell when a flower is a dicot?")
word = input ("It has petals in multiples of five (5, 10) (1)      It has petals in multiples of three (3, 6) (2)")
if (word == "1") :
    print ("correct, dicots have petals in multiples of five")
elif (word == "2") :
    print ("wrong, monocots have petals in multiples of three, not dicots")
else :
    print ("that wasn't an option")
print ("What's the difference between a gymosperm and an angiosperm?")
word = input ("Gymnosperms produce fruit but angiosperms don't (1)      Angiosperms don't use pollenation to reproduce, but gymnosperms do (2)       Angiosperms produce fruit but gymnosperms don't (3)")
if (word == "1") :
    print ("wrong, it's the opposite")
elif (word == "2") :
    print ("wrong, both use pollenation to reproduce")
if (word == "3") :
    print ("correct, only angiosperms have fruit")
else :
    print ("that wasn't an option")
print ("Are plants autotrophs or heterotrophs (organisms that can't make their own food)?")
word = input ("Heterotrophs (1)     Autotrophs (2)      Neither (3)")
if (word == "1") :
    print ("wrong, plants don't need to get food")
elif (word == "2") :
    print ("correct, plants are autotrophs")
if (word == "3") :
    print ("wrong, plants are autotrophs")
