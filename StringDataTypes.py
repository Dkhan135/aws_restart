myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall" 
thirdString = firstString + secondString
print(thirdString)
print(secondString + " " + firstString) 


name = input("what is your name? ")
print(name)



colour = input("what is your favorite colour? ")
animal = input("what is your favorite animal? ")
print("{}, you like a {} {}!".format(name,colour,animal))