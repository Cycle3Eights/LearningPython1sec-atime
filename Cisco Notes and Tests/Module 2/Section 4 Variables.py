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

# LAB, Variables Converter, miles -> kilometers.


