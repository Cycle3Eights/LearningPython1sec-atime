# remember math? kinda like that, arithmetic operators will be used.
print(2+2)

#python can be used as a calculator... although you could probably just get away with
#searching the answers online anyways or using a physical/digital one.

# all basic operators are as follows

#addition
print(2+3)
#subtraction
print(2-5)
#multiplcation
print(3*3, 3*3., "If number with a decimal point, then it becomes a float.")
#division -> this becomes a float, usually in long divison, depending on the number, you would have
# to continue dividing until it has been solved/repeating decimal.
print(6/3, 7/3, 2/2, "Always a Float when using division.")
#exponents, also try doing spaces = make it more need/readable
print(2 ** 3, "This should print out as 8, or 2^3.")
# Integer Division/Floor Divison -> This allows the results to become an integer instead of a float
# Which means always rounded. ROUNDING GOES TO THE LESSER INTEGER
## Keep in mind = dividing by 0 is undefined, same thing in python, and same thing on ti84 calculator.
print(6 // 3, 9 // 3, "Rounded Integer UNLESS, numbers in either positions have a decimal point. Then it's a float.", 7 // 3.)
print(6 // 4, 6. // 4, 6/4, "3rd number = 1.5, why? not integer divison, thus will not be rounded")

# Integer Division/Floor Division Continued.
print(-6 // 4, 6 // 4, "Note: Rounding goes to lesser integer value, thus -1.5 closer to 2. Rounded to -2 that way.")
print(5 / 4, -5 // 4, 5 // 4, "Negative numbers vs positive numbers can be a bit different.")
print(-6 // 4, -7 // 4, -8 // 4)
print(-6 / 4, -7 / 4, -8 / 4)

## REAL QUICK -> BRAIN CONFUSED ON INTEGER VALUES. WHY? -6 divded by 4 = -1.25.
## My brain immedietly tells me to round down to -1 but python rounds up to -2?
## In this case, -1.25 lesser integer = -2, ignore the .25 at all??

## FIGURED IT OUT, GO LEARN WHAT THE HELL FLOOR & CEILING IS IN MATH.
## IF NUMBER = -1.25, for negatives, DOWN is FLOOR, UP is CEILING. THUS = -1 and -2 in between!
## Python will round it out to the LESSER NUMBER. FOR NEGATIVES, THIS IS GOING TOWARDS -2!
## IF DECIMALS USE A NUMBER LINE/FIND WHERE THE NUMBER SITS AT.
## Which would make -1.25 go DOWN b/c of floor division.

# Some few problems to practice.
print(6 / 4, 6 // 4, "Floor Divison/Integer Division, 6 // 4 = 1.25, 1 & 2 are at it sides, thus =1")
print( 7 /3,  7 // 3, "7 // 3 should be 2.")
print(-6 / 4, -6 // 4, "Negatives are a bit tricky, remember: -1.5 is in between -1 and 2, GO DOWN FLOOR, so -2 is answer.")

## Always remember with Integer Division/Floor Division -> The # will be rounded LESSER than the Original
## Positive numbers such as 2.3, will be rounded down to 2 in python
## Negative Numbers such as -5.6 will go DOWN to negatives, so -6 in python.

print(5.6 /3, 5.6 //3, -5.6 // 3)

# Onto the Next. Remainder(Modulo in order languages).
print( 14 % 4)
       # 14/4 -> 4x3 = 12, then 14 -12 = 2. 2 Will be the result as thats the operator being used.
print( 12 % 4.5, "I technically could just get 2.67 then round it up to be 3 lol")
# This is solved by, -> 12 // 4.5, 12 / 4.5 = 2.67, FLOOR -> Down to 2.0. Multiply the 2 by 4.5,
# usually the right half is used in the multiplying section. 2.0 * 4.5 = 9, now just subtract this
# with the left half 12 - 9.0 = 3.0

## Rules with this, remember if you want to write it out, the steps are as follows.
# 1.Remember Integral Division/ Floor Division, the number that is left from this is a quotient.
# 2. Multiply the quotient from Floor Division with the number of the divisor of original problem.
# 3. Take the result from 2. and subtract that result with the dividend of the Original Problem.

# Extra? More Information on subtraction:
# Subtraction usually means - sign, but now it also means: Change sign of a number.
# There are two operators that are under the subtraction operator.
# unary (think uno in spanish or one, ex: +2) and binary operators (the usual 2+2, x+y, require 2 numbers/letters/etc)

print(+2, "This is apprently unary operator?")

#Operators and Priorities!
# Think like PEMDAS. Python uses hierarchy of Priorties, * is higher than + so it will be read first.
print(2 + 3 * 5, "If it works out, A: 17. Why? 3*5 = 15 + 2 = 17. Python will read left from right")
## LEFT SIDE BINDING ASIDE FROM EXPONENTS? LEFT TO RIGHT.
## Just a test, of the priorities, the remainder % read first then
print( 2 + 9 % 3)
print(9 % 3, 9 // 3, 3 * 3, 9 - 9, "% remainder, 1.floordiv, 2.res * divisor, 3.resultdiv - dividend.")

# Exponents read right to left
print(2 ** 2 ** 3, "2^3 -> 2^8 = 256, if I were to write it down, 2^(2^3)")
#predict, -3 ** 2 = positive 9, -3 * -3
# -2 ** 3 = negative 8. -2 * -2 = 4 * -2  = -8
# 9, but since the problem is like -(3**2) then its negative -9.

print(-3 **2, -2 **3, -(3**2), )
# 2nd and 3rd print predict was right, 1st predict was not. I wonder why?
# -3 ^ 2 so -3 * -3 = 9, was my thought process, but python is negative 9, while google encased the number
# google's interpretation of -3 **2 -> -(3**2) = -9.
#TURNS OUT I DO NOT KNOW HOW TO DO MY ORDER OF OPERATIONS.
# Just remember, the -3 ** 2 can be read as (-1)(3**2) this will lead to -9, as shown by google, python and other threads online.


## AS OF MODULE 2 PRIORITES, Highest 1 to lowest 4.
# 1. Operator Exponents -> **
# 2. Operator + & -, UNARY
# 3. Operators * (Multiply), / Divide, // Integer Division Or Floor Division, % Remainder
# 4. Operator + & - binary.

## PRACTICE PROBLEMS!!!
# Predict -> 2*3 % 5 REMEMBER BINDING DIRECTION ALWAYS LEFT. BOTH OF THESE ARE SAME PRIORITY.
# 2 * 3 = 6 % 5. 1. 6 // 5 -> 1.2 or 1, 1 * 5 = 5, 5 - 6 = -1??? remainder = whatever is left
# IDK why i keep making this hard on myself 1 is left over.
# the divisor first then subtract the result off of 1*5 = 5.
print( 2 * 3, 6 % 5)
print(2 *3 % 5, "If done right from left, 3 % 5 = 0, then 0 * 2 = 0. so remember left to right.")
print(14 % 4)

# Practice on Operators and Parentheses.
print((5 * ((25 %13)+100) / (2*13)) // 2, "Prints out 10.")
# First off, parenthesis first, 25 % 13 = 12 and 2 * 13 = 26
print(25 % 13, 25 // 13, 1 * 13, 25 - 13)
print( 2 * 13)
# Expression should now read as follows ((5 * (12 + 100) / 26 // 2)
# Next -> 12 + 100 = 112, then 26 // 2 = 13
print(26 // 2)
# Now read as ((5 * 112 / 13))
print(5 * 112 / 13, 5 * 112,560 / 13,)

## A redo of the problem from expression ((5 * 112 / 26 // 2), ALL operators are on the same lvl of bind.
# Now a left to right.
print(5 * 112,560 / 26,21.5 // 2)
resultbruh = 560 / 26 ## im ngl i did not want to type out all of those decimals, round it to 21.5 though.
print(resultbruh // 2)

## Section 3 Quiz for Operators. Be sure to remember those rules + PREDICT first then look at answer.
# Q1: ((2**4), (2*4.), (2*4))
    #A: 2^4 = 2*2*2*2 = 16, 2*4. = 8.0 (becomes a float.), 2*4 = 8 (no decimal, just number integer).
    #A1: This is read as -> 16, 8.0, 8 W/O COMMAs, if you would add it -> sep=",
print((2 ** 4 ), (2 * 4.), (2 * 4 ))
print((2 ** 4 ), (2 * 4.), (2 * 4 ),sep=",") #To add commas, sep=","

# Q2: print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
    #A2: -2 / 4 = -0.5, 2 / 4= 0.5, 2 // 4 = 0 (remember floor div). -2 // 4 = -1 (going down one floor.)
    #A2: This is read as: -0.5 0.5 0 -1
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

# Q3:print((2 % -4), (2 % 4), (2 ** 3 ** 2))
    #A3: 2 % -4 = 0 remainder is 0 b4 decimal.
    #A3: (2 % 4) -> 2 // 4 = 0, 0 * 4 = 0, 2 - 0 = 2 ???
    #A3: 2 ** 3 ** 2, 3 ** 2 = 9, 2 ** 9 = 512
    #A3: This is read as: 0 2 512 ????
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
 # Explaination for 2 % -4 ->  2 // -4 = -0.5 -> -1 floor down, -1 * -4 = 4, 2 -4 = -2
print( 2 // -4, -1 * -4, 2 - 4, "explaination for (2 % -4)")

print(1/4)