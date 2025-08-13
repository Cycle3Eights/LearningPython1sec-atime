gum = 5*5
print(gum)
print(-0.5) ## anything with a point, decimal that is attached to a number is a floating point number
print(0.000000000000000000003) # same thing w/ this one.
print(5) # this is a integer.
print(3e24) # a float, but w/ the e -> scientific notation.
print(3.e-24)

#text below is a seperation of different strings, to enable quotes on a particular string, use
# \"text here\"" or '"blah"' !!
print("This is a string!!", "The text on the right should show ->", 'My name is "Monty Python"', sep=" ")
# apostrophes, require the \ escape button, this can be used as well for new line \n
print("How\'s the weather up there")
# if you dont wanna use x2 quotes then make sure you also use \ w/ apostrophes
print('How\'s the weather up there')

#Booleans!! I really do feel like making an input yes/no adventure game, ex:
# if player inputs false to a True/False Question they die, inputs true = go forward.
#python would ask -> is this true according to the question, if it is (as representated by
# the > and < sign) then it will be printed out. 1 -> true 0 -> false

print(True > False) # Should print out True
print(True < False) # should print out false. THESE TWO ARE CASE SENSITIVE!!

#GOAL: FIND BINARY OF DECIMAL VALUE 1011. Subtract Method
print(2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**9, sep=",")
print(1011-512, 499-256, 243-128, 115-64, 51-32, 19-16, 3-2, 1-1) ## now make a binary from these numbers
# PRINT -> TRUE if number subtracted with the 2nth has a result, if not skip and put 0.
print(1111110011)
print("The Binary number of 1011 is 1111110011")
print(512+256+128+64+32+16+2+1)

#GOAL: FIND DECIMAL VALUE OF BINARY 1011
print(1011, "RIGHT to LEFT, each number = 2nth power", )
print(2**3, 2**2, 2**1, 2**0, "\n 1= 2^3, 0=2^2, 1=2^1, 1=2^0") #Take these numbers and multiply each number 1011
print(2**3, 0, 2**1, 2**0,"=", 8+2+1) #Prints out a number b/c it is true =1.
print("The decimal value for binary 1011 = 11.")

