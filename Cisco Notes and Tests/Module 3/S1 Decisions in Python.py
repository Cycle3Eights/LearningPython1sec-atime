# It's that time again. Back on it. 1/5/26 Actually doing it this time.

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

n = int(input("Please input a number!"))
print("The number of this n is:", n)

onehundred = 100
testn = int(input("What number would you like to input?"))
print("The inputted number is:", testn, "then it is", testn >= onehundred)

