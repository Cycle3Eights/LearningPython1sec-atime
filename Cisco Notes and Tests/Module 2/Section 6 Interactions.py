## probably inputs, which makes me think of an input text game. sounds alr for a project in future.

## 8/25/25, possibly my most awaited section of module 2 :D
## INPUTS!! I like the input() function, i've used it in Section 3, 4, and 5 because in some cases I felt inputs > print
## Maybe as a small side project for the end of Module 2, make an input CYOA: Choose Your Own Adventure game?

# So far, things about the input statement that I've already known based off of prev sections/looking it up.
# input() is a function and will only be read in string form. To specify that you'd want python to read a number/float:

# float(input()) and int(input()), [[and be sure to store it as a variable]], if combined/pulled with a print statement.

# input() generally require a user to put feedback into to the console below.
# a user puts an answer and gets an output, a result w/ usually an accompaning print() statement.


# idk how to terminate after 30 seconds, so # for now.
# chickenamount = float(input("How much chicken legs would you like to eat? ")) ## if w/o float/int, will throw up an invalid.
# print("Great! Here is:", chickenamount, "chicken legs. Enjoy!")

## Prohibited Operations
# anything = int(input("enter a number")) -> W/O the int in front of the input it would show up as "userinput" ** 2.0, which
# for python rules is something that is not allowed.
# something = anything ** 2.0
# print(anything, "To the power of 2 is", something)

## To get around to solving this -> Type Casting, only works with input(), not with print.

# int() function -> converts to a integer, so 3, 6, 9. Apprently MAKE sure to enter a valid number? probably error after.
# float() function -> converts to a floating decimal, so 3.0, 6.0, 9.0.

# When the pythagorean theorem is being written out -> (a ** 2 + b ** 2) ** 0.5 -> square root in this case is 0.5.

print((2 ** 3 + 2 ** 3) ** 0.5 ) # if i was writing this down, c^2 being 0.5 is b/c when c^2 = 16, gotta get rid of the exponent.
# so sqrt it on both side, with when done would be c = 4. all answers would end up being a float in the console.

## String Operators
# Both the + and the * have an additional purpose. Based on past knowledge -> + should add both strings together
steak = "ILOVE"
steakloving = "STEAKFR!!"
print(steak + steakloving) # This is a Concatenation Operator. ONLY adds both strings. Basically glues them together or like
# w/ sticking together two small lego pieces. both variables in the whole argument must be a string cause it'll throw up invalid error.

print("\nYou really must love steak to be shouting:" + steak + " " + steakloving + ".") # Just add a " " with a gap to seperate variables
# that " " is called an Empty String.

# * = Replication Operator.
# As the name implies it multiplies a valid string for many x times.

print(steakloving * 5) # Usual Format -> String and a Integer and it will copynpaste the string for 5 times, no gaps though.

## Extra -> triangle time???
print(" " * 3 + "/" + " " + "\\")
print(" " * 2 + "/" +" " * 3 + "\\"  + "\n /" + " " * 5 + "\\" )
print("/" + "_" * 7 + "\\")
# Small note, in order to bypass the left side slash, cause that can be used with different other commands,
# put a double \\ instead.

# LAB Simple Input and Output
# Evaluate results of the given arithmetic operations -> Addition, Subtraction, Multiplication, Division.

# Float Value for two variables.
# I think I would need to use function or something to make it so result yields ERROR, if
# one of the variables are used to divide by 0.
#variableA = float(input("Enter a number between 1 to 100!"))
#variableB = float(input("Enter a 2nd number between 1 to 100!"))

#Prints in string quotations form, this only works with the String Operator: +.
#IF W/O String Operator, then use comma's instead.
# print("When adding both variables, the result is: " + str(variableA + variableB))
# print("Subtracting both variables yields a result of: " + str(variableA - variableB))
# print("Multiplying both variables gives: " + str(variableA * variableB))
# print("Dividing both variables gives: " + str(variableA / variableB))

## Turns out python will actually just stop me anyway if there's an input of 0: "ZeroDivisionError"

# LAB Operators and Expressions
# That is one division type looking problem that probably has an actual name. But it's 1/x+1/x+1/x+1/x+1/x+1, which probably
# would look better written down on paper or shown on website

# Keep in mind of the order of operators + hierarchy.

# I could technically just instead of using input statement, just use variable assignment + print instead.
#InputinX = float(input("It's division testing time, please input any number here: "))
#Yresult = 1/(InputinX + 1/(InputinX + 1/(InputinX + 1/InputinX)))
# print("Wacky Division should result: ", Yresult)

# LAB Operators and Expressions - 2
# Code and Evaluate end time based on the given input.

hours = int(input("Enter a number based on a specific hour: ")) #Hours -> 0 to 23.
minutes = int(input("Enter a number based on a specific minute: ")) #Minutes -> 0 to 59
duration = int(input("How long will this event last? Please give a specific amount of minutes: "))
#endtime = hours

# print("An event will start at: " + str(hours) + ":" + str(minutes) + " and will last for: " + str(duration) + " minutes.")
# print("Which means that this event should end at:", str(endtime))

#figuring out information for time
# 1440 minutes = 24 hours.
# try converting it into TOTAL minutes then convert it back into hours + minutes.
hour2minute = hours * 60
totalminutes2hours = minutes + hour2minute
durationaddedonminutes = totalminutes2hours + duration # total minutes
conversiontotal = int(durationaddedonminutes / 60)
conversiontoremainder = durationaddedonminutes % 60

print(totalminutes2hours, "total amount of minutes after duration is", durationaddedonminutes)
print("conversion test", conversiontotal, conversiontoremainder)
print("This event should be ending at:" + str(conversiontotal) + ":" + str(conversiontoremainder))