## Variables!!! :DDDDDDDDDD, I used probably like one variable in section 3
# some variables include, variables are also kinda like storing it in a box, which then you would use later
# you'd pull it out using a print command
import math

gotcha = 2 + 2
print(gotcha)

roundednumber5 = 500 / 25 # This stores value into rounded number 5, that value is the result of 500/25
print(roundednumber5)

print(roundednumber5 + gotcha) # should print 24. if it doesn't then uhhh something wrong.

# Variables consist of two parts -> value & name
# roundednumber5 is one variable, other such variables in other languages work as well,
# no spaces allowed, and must begin with a letter, symbols, numbers will not work.

inches3rd = 2+3
# 3inches = 2+3 ## THIS will show up as invalid.

print(inches3rd)

## There's keywords such as False, True, elif, def, etc. Try not to use them for names/variables.
# it probably would show up as invalid. OR cannot be assigned.

# False = 2 + 2 -> INVALID
myFalse = 300/60
print(myFalse)

## Some variable declarations below. BTW, MAKE sure to always be accurate w/ variable names, or error/invalid will appear.
# ex -> if instanceguh was printed w/ capital I, console will print a nameError and redirect to a similar name.
instanceguh = 250
instanceguh = instanceguh / 2
accbal = 78
accname = "DashedTony"
print(instanceguh, accbal, accname)
print("The current balance of", accname, "is:", instanceguh-accbal,)

reloadedinstanceguh = instanceguh - accbal
great3 = "two twenty"
# + operator can combine both variables and strings i.e "The Current Balance of".
print("bro is in negatives, the total is:" + great3)
# after some testing, the print above can only actually print variables that has strings stored in them
# if tried storing anything but strings, as in numbers,integrals, etc, and it will throw an error message.

# print("negative debt, total: " + reloadedinstanceguh)
## will print out -> "can only concatenate str ( not "float") to str. no floats/integrals allowed
# when using the + operator. A way to bypass this would be to just use the comma.

print("guh guh total: ", reloadedinstanceguh)

print((9+16) ** 0.5) #square root.

# LAB Variables Section!
# John -> 3 apples, Mary -> 5 Apples, Adam -> 6 Apples.

john = 3
mary = 5
adam = 6

total_apples = john + mary + adam

print("Apples:", john, mary, adam)
print("The Total amount of apples that John, Mary, Adam gathered is:", total_apples)

# Lab1 Experimentation
# Use + Operator. -> can only be strings, so "blah blah" for ex.
TotalStatement = "Currently the total amount of apples as of this moment is:"
total_apples2 = "14" # can't store integers/floats in variables.
print(TotalStatement + total_apples2)

# String + Integer.
eatthatapple = "You currently have this many apples:"
print(eatthatapple, total_apples,  "\nWhere did these extra apples come from?: ", total_apples+total_apples,)

# random math together.
treeman = 79.0
yummyapples = treeman / total_apples
print("Whatever this is lol:", (john * john) // mary - (adam * adam) / john + (mary * adam * john))

print("The Treeman decides to bless you with an abundance amount of apples...", treeman+ total_apples,  "seriously what will you do with this?? Make juice? Make apple pie? Or maybe a slushie?")
print("Someone like alot of it Total now: ", treeman / john )

## Shortcut Operators.
# There are many different types of shortcut operators, these two below just showcase x * 2 and x + 10.

#Powers of 2 & Addition.
applesofcentury = 100
applesofcentury = applesofcentury * 2
pearsofdays = 5
pearsofdays = pearsofdays + 10
print("Apples:", applesofcentury, "Pears:", pearsofdays)

# A more simplified way

applesofcentury *= 2 # could be read as applesofcentury = applesofcentury * 2, just make sure to assign it a number first!
pearsofdays += 10 # just like ^, 5 + 10 = 15, w/ this new variable its 15 + 10 = 25.
print("Two different fruits are", applesofcentury, pearsofdays) # took the above 100 * 2 down here, now its 200 * 2 = 400.

## Special Note On Shortcut Operators!!
# Variable op= expression (like strings, "hello" or integers: 5, 10.0, e12.)
# Be sure to store something in said variable, like gobble = 5 then doing gobble op= #here otherwise it will show up as not defined.
# Gobble = 5 -> Gobble += 5 shows up as 10 when printed as Gobble stores the number as 5 then pulled out again to add 5.
# ^ This also could be like Gobble = Gobble + 5, but shortened out.

Gobble = 25
Gobble *= 5 # Gobble + 5 basically
Gobble2 = "guh"
print("The amount of turkeys that are in stock are:",Gobble, Gobble2)

# LAB, Variables Converter, miles -> kilometers.
# One mile = 1.61 Kilometers.
# One Kilometer = 0.62 miles

miles = 5 #edit this and below
kilometers = 8.05

miles2km = miles * 1.61
km2miles = kilometers / 1.61

#basically edit around with the miles and kilometers variables above, this does not use input() though.
print(miles, "miles and now converted to kilometers", round(miles2km, 2), "kilometers")
print(kilometers, "kilometers and now converted to miles", round(km2miles, 2), "miles")

#Extra -> Temperature Fahrenheit to Celsius Convertor
#32 degrees Fahrenheit is equivalent to 0 degrees Celsius

ConversionFtoC = (100-32) * 5/9 # The First 32 is the only number that needs to be changed in this formula, only change that.
ConversionCtoF = (37.78 * 9/5) + 32 # Same thing with FtoC, just change the first number.
print("Current Celsius Temperature is:", round(ConversionFtoC, 2), "Celsius")
print("Current Fahrenheit Temperature is:", round(ConversionCtoF, 2), "Fahrenheit")


## Trying my own idea of User Input Conversion. if its input() will not be recognized and unable to be multiplied as string != integer
# instead do int(input()) so that python recognizes it as an integer input rather than a string input.
# Remove the # symbol then test it out. Still on Variables, and functions seem a bit complicated? idk maybe
    # maybe an if statement?
        #if input() or timewait(5) then
        #print() else
        #print("taking too long, end here")
# Definitely could come back here later to input a wait/end function so it doesn't go on indefinitely.
###currentmiles2km = int(input("Please input the amount of miles to convert to kilometers: "))
###currentkm2miles = int(input("Perfect! Now Please input the amount of kilometers to convert to miles: "))
###print("There is:", currentmiles2km, "miles and converting it to km is:", round(currentmiles2km * 1.61, 2), "kilometers", "There is also:", currentkm2miles, "kilometers and converting it to km is:", round(currentmiles2km * 0.62, 2), "miles")

# LAB: Operators and Expressions

#Test -> 3x^2
x = int(5)
print((3 * x) ** 2)
# 2nd Test: The Whole Polynomials (side note: for a short while i forgot what polynomial was, thought it was 4 sided polynomials
# 3x^3 - 2x^2 + 3x -1

Secondx = float(1) # Change this number here to solve polynomial
print("The Output for this polynomial is:",(3 * Secondx) ** 3 - (2 * Secondx) ** 2 + 3 * Secondx - 1)

# Extra test, assign variables to each polynomial that is listed above.
# The ones that need to be edited is represented as x input in polynomials.
ThreetoPower3 = 3 * 1 # Only edit the 2nd number
ThreetoPower3 **= 3 # Number assigned above^3
TwotoPower2 = 2 * 1 # Only edit the 2nd number.
TwotoPower2 **= 2 # Number assigned above ^2
Threetimesfloatnumber = 3
Threetimesfloatnumber *= 1 # Edit this number here.
print("The Output for the quadratic Polynomial is:", float(ThreetoPower3 - TwotoPower2 + Threetimesfloatnumber - 1))

### TLDR: BRO GOT STUNLOCKED FOR 30 MINUTES FIGURING OUT WHY THERE'S TWO DIFFERENT ANSWERS IF x IS ASSIGNED AS 1.
# Now after remembering how Order of Operations works: BOTH polynomials are giving a different answer, 25 vs 3. Why?
# 3 ** 3 = 27, 2 ** 2 = 4, 3 * 1 = 3, -> 27 - 4 = 23 + 3 = 26 - 1 = 25 FOR ABOVE
# 1 ** 3 = 1 * 3 = 3, 1 ** 2 = 1 * 2 = 2, 3 * 1 = 3,-> 3 - 2 = 1 + 3 = 4 - 1 = 3 FOR BELOW.

## Going off of 3x^2, ABOVE: Multiplies using the Stored Variable, so it's read as 3x3x3 = 27, while
## BELOW: Multiples Exponents first, so 1x1x1 THEN * 3 -> coefficient = 3

print("Now try getting the output for the polynomial while using these numbers: 0, 1, -1, -3")

Assign0 = float(0)
print("The Output for a polynomial that has the number 0 is:", (3 * Assign0 ** 3 - 2 * Assign0 ** 2 + 3 * Assign0 - 1))

Assign1 = float(1)
print("The Output for a polynomial that has the number 1 is:", (3 * Assign1 ** 3 - 2 * Assign1 ** 2 + 3 * Assign1 - 1))

Assignneg1 = float(-1)
print("The Output for a polynomial that has the number -1 is:", (3 * Assignneg1 ** 3 - 2 * Assignneg1 ** 2 + 3 * Assignneg1 - 1))

Assignneg3 = float(-3)
print("The Output for a polynomial that has the number -3 is:", (3 * Assignneg3 ** 3 - 2 * Assignneg3 ** 2 + 3 * Assignneg3 -1))

