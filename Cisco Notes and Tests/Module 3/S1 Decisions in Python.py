# It's that time again. Back on it. 1/5/26 Actually doing it this time.
from selectors import SelectSelector

# depending on the code written -> always a true/false answer. no inbetween like unsure/letmethink. but this techniqually depends on operators.

# == -> "Equality Operator" is this equal to each other.

blingvar = 2
secondvar = 3
thirdvar = 3

print(blingvar == secondvar) # when this code is typed out -> python is going to ask is 1st var = to 2ndvar. which pops up as false.
print(thirdvar == secondvar) # this shows up as true b/c of both variables are the same. but what about an inputted varible?

# inputtedvar = input("type 1st variable")
# inputted2ndvar = input("type 2nd variable")
# print(inputtedvar == inputted2ndvar) # depending on what you typed here, it will show up as true if both variables are the same.

### 3.1.3 Exercises portion w/ thoughts. after like 4 months of not doing python, need a refresher.

print(2 == 2) # this is saying -> is 2 equal to 2. true.
print(2 == 2.) # the small dot is usually a period, a decimal. so its a float -> 2 == 2.0 -> false?
# **2.0 = integer. it's still the same, slightly forgot about it.
print(1 == 2) # 1 is not equal to 2 so false.

### Operators Section
# Equality Operator -> ==
var = 2
var == 0 # -> no answer b/c nothing is stored in var.

# Inequality Operator = != -> Not equal to. i've seen this before like on random forums/posts and stuff.

beegvar = 0
print("This should show up as", beegvar != 0) #false b/c 0 is equal to 0.

beegvar2 = 1
print("This should show up as:", beegvar2 != 0) #remember the variables. b/c it'll show up w/ a diff answer if its not the right one.

# Comparison Operator = > -> Greater than. Strict.

print(beegvar > beegvar2)# should print out as false. cause 0 is not greater than 1.

# Comparison Operator = >= -> Greater than or equal to. Non-Strict.

# now, it would be like idk integers -> 4 >= 5 -> is 4 greater than or equal to 5 -> false. now add decimals to it.

secondhandmovement = 4.5
thirdhandmovement = 5

print(secondhandmovement > thirdhandmovement) # false.

# Comparison Operator = < & <= -> less than and less than or equal to.
# < strict while <= nonstrict? what does that mean? i searched it up apprently -> enforce data types. strings are not equal to a number

#ex.
bang = 3
bang4 = "3"
# print(bang + bang4) # show up as an error.

# back to < and <=
mph_1st = 60
mph_2nd = 60
mph_example = 60

print("mph value is:", mph_1st < mph_2nd) # absolute strict, if number are same = false. why? b/c 60 is not < 60.
print("mph value is:", mph_1st <= mph_example) # if number = same then still true, b/c of the equal to operator.

### Answers and their usefulness.

# variables that get used w/ integers like for ex. a final value -> 2+2 = 4. can be used later as long as that variable had an
# integer in it.

## priority list.
# operators such as 1st: addtion, subtraction, 2nd:exponents, 3rd: multiplication, div, longdiv, percentage, are on the top 3 priority, might be best
# to make an actual table out of it.
# 4th -> + and - = binary.

# all of the new comparison operators -> <, <=, >, >= are 5th, and 6th are == and !=.

### Scenario LAB. Q&A.

# Use comparison operators provided and n as input and print true/false for output.

# n = int(input("Please input a number!"))
# print("The number of this n is:", n)

#onehundred = 100
#testn = int(input("What number would you like to input?"))
#print("The inputted number is:", testn, "then it is", testn >= onehundred)

### Conditions/Conditional execution.

# oh boy if then statements?? :DDD

# Special instruction -> conditional instruction: what does it do?
    # if true_or_not -> if true then go here, if not, go to a different pathway.
    # basically python is now given an option to do something if that something matches the criteria of true.

## test -> sheep >= 170

sheeptotal_counter = 165
if sheeptotal_counter >= 170:
    print("The current total of sheep on the barn is", sheeptotal_counter) # since the sheep total < 170, no print shall happen.
print("bah bah im a sheep")
# also note, the if function is a whole block, if i were to say another function out side of it then it'll still run.

bread_counter = 46
if bread_counter >= 50:
    print("wow that's alot of bread")
else:
    print("mmm, maybe you need more to donate?")
    print("get more bread bro.")
# if -> thing = or >= integer then -> print(1st statement), else? -> print(2nd statement).
# in short -> if criteria is not met then it does something else.
# also remember -> colons, both the if statement and else statement needs colons. think of the if + else they both of blocks
# as well as their own branches, so i can put more print statemetns in them.

#nested if-else statements; my own wacky example.
# if trex_are_alive:
#   if weapons_are_around:
#       defend() # call function -> do this
#    else:
        #hide() # if does not match then do this
#else:
#    if flyingsharks_are_real: #now if trex isnt real then it'll move to the else function.
        #getinanddrive() # do all these functions if matched. also where did you get a car?
        #acclerate()
        #leavepremises()
#    else:
        #wakeup_dream()

## Cascading -> if-elif-else
# basically and order to check and if it doesnt work it'll go down until it works or to the last else statement.
chicken5 = 0

if chicken5 >= 5:
    print("hooray for 5 chickens")
elif chicken5 == 4:
    print(chicken5, "christmas trees")
elif chicken5 == 0: # okay figure out how to do this one later? make it so like its a certain range from 1 to 4.
    print("oh wow nothing")

# side note -> i could mnake it a bit more tighter w/o the use of indents liek this
if chicken5 >= 5: print("hooray for 5 chickens huzzah")
elif chicken5 == 4: print(chicken5, "christmas trees, christmass")
elif chicken5 == 0: print("oh wow nothing, fr? ")

# me personally i like my indents, so i'll probably not do this.

### the looping methods :)

# psudo code -> readable but unable to be executed, also thing about loops
# you set the function to read that specific integer -> exit(), so it'll keep looping over and over until it gets the right
# number.

### LAB -> Comparison Operators and conditional execution
# Spathiphyllum -> must match this exactly, if lowercase -> needs capital s, if something unrelated -> then say no.

# this was supposed to be an input but b/c idk how to break or end it b4 input like after 10 seconds, i set it as a stored variable.
thatdamnplantname = "Spathiphyllum"
if thatdamnplantname == "Spathiphyllum":
    print("Hooray! Spathipyllum is the best plant")
elif thatdamnplantname == "spathiphyllum":
    print("did you forget to capitalize Spathiphyllum?")
else: #oh and btw, you could do elif thatdamnplantname != "spath" or "Spath" and i think it still works, but else is fine.
    print("remember: Spathiphyllum not,", thatdamnplantname)

### LAB -> Essentials of if-else statement
# Writing a tax calculator, try to actually break this into chunks lol?
# This will be using cisco's given data, but adding on for the if-else function.

income = 85528 # float(input("Enter the annual income: "))

#if income < 85528:
 #   tax = income * 0.18 - 556.02
 #   if tax <= 0:
#        tax = 0.0
#else:
#    if income > 85528:
 #       surplus = income - 85528
#        tax = 14839.02 + surplus * 0.32

# tax = round(tax, 0) # if somehow income is above 855528 it'll not be stored in tax. the < operator takes it from
# 85528 to negative infinity.
print("The tax is:", "thalers")

### LAB -> if-elif-else statements. Leap year/ Common year

year = 2000

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    if year > 1582:
        if year != (year % 4): # -> figured out the asnwer, but, this is asking, if the year is not equal to
            print("common year") # year remainder by 4. but i never actually put 0 there
        elif year != (year % 100):
            print("leap year")
        elif year != (year % 400):
            print("common year")
        else:
            print("leap year")

### Section Quiz thoughts.
print(3 % 4)

x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
# small thoughts, new values for x,y,z are now there. but since 5,10,8, the values are now switched?
# so x value = 5, now its 8, switched with z and it's value is now 5.
# which explains on how x > z -> 8 > 5??
print((y - 5 ) == x)
# 10 - 5 -> 5 is equal to x. current x value is 8. which means this would be false as 5 != 8.

threebees = 10

if threebees == 10:
    print(threebees == 10)
if threebees > 5:
    print(threebees < 5)

if threebees < 10:
    print(threebees < 10)
else:
    print("bruh")
# right, i keep forgetting that the if functions are techniqually their own block.
# so, if -> else, if three < 10:  would not print out the if statement, so it goes down to else, which would print out bruh.

bees = 3
beeswood = 3.0

if bees == beeswood:
    print("three")
elif bees == beeswood:
    print("both are not the same?") # the if itself gets printed, but for elif statement -> instead of comparing numbers
else: # i think this is rather comparing the type, b/c 3 and 3.0 are not the same, one is an integer and one is a float
    print("knowledge check") # so this is asking -> is an integer the same as a float and i'd say no.

# else itself is never printed, why? b/c it is basically "otherwise", so if bees != beeswood then it would print i think.
# else is also the last thing that is printed, so i think it would also be discarded unless everything else above it
# cascade -> is not valid.
if bees != beeswood:
    print("threepeas")
else:
    print("knowledge check")