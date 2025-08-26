## comments, like the one you're seeing right now

#idk if i'd add any notes really. it's just the # comment command.
# the overuse of comments in previous sections 2-4 is like probably not good anyway lol.

# Comment Overview
# Comments must be clear, concise and straight to the point for readability and neatness(?).

#Comment Examples
burgers = "cheese"
cheese = "burger"
print(burgers + cheese) # the + operator combines both variables to print out str: "cheeseburger"

numberA = "float(5)" # keep in mind + operator does not work for float,integers, only strings
cheeseburgers = "Cheeseburgers"
print("I would like to eat", numberA, cheeseburgers)
print(numberA + cheeseburgers, sep="")

# Making a line of code invisible

tree = int(input("Please input how many trees you would like to receive:"))
# bakery = input("What type of cake would you want? Carrot Cake? Red Velvet Cake?")
# Having a comment b4 a line of code WILL make python NOT read it. If used later, be sure to remove the #.
print("Here you go:", tree, "trees")

# If somehow there's an error somewhere, then # would be useful towards figuring out the problem. CTRL + / Windows for quick-commenting
# Lines of code.

#LAB Comments
#This is post-edit off of the website. Which explains the actual variables, instead of leaving it as a letter.
# As well as converts seconds -> 3600(1hour) to an x amount of hours.
### <- from website itself.
number_of_hours = 3 # number of hours
seconds_in_a_hour = 3600 # number of seconds in 1 hour

print("Hours: ", number_of_hours, "Which when converted to seconds is:", seconds_in_a_hour * number_of_hours,) #prints hours which converts to seconds
#prints x hours then converts to seconds by multiplying 3600 * x hours.

### here we should also print "Goodbye", but a programmer didn't have time to write any code
#^ truly the 3 seconds of typing print("Goodbye" of all time
print("Goodbye")

### this is the end of the program that computes the number of seconds in 3 hour
hoursmultiple = 3 #Edit the number to your own choosing
secondsto1hour = 3600 # 3600 seconds = 1 hour

secondstohours = secondsto1hour * hoursmultiple # 3600 times 3 = 10800 seconds in 3 hours.
print("Currently you chose", hoursmultiple, "hours to be converted to seconds:", secondstohours, "seconds")

#Special note, not everything needs to be overcommented in a real program, but since this is practice, future me will thank
# himself later on what he's looking at.


