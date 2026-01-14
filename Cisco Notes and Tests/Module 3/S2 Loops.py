## 1/11/26 oh my god looping!! hooray its roller coaster time!!
# main methods of loops and stuff that will be used, infinite loops (enter/exit), skip loops, and most important
# while and for loops :DD

### Looping w/ [while]

# a slight similarity w/ if?  if condition_true -> execute command only once, while [condition] -> execute in block + loop?

# while keeps repeating anything that is in execution. this is called [loop's body] in the while loop.

# just like with if and else, each have their own block that orders can be nested in. be aware to try and exit it b/c
# it'll run infinitly.

# here's an infinite loop

#while True:
    #print("looping WEEEEEEEEEEEEE") # as long as the condition is true for the while function, it'll keep printing forever.

##### LAB -> Guess the Secret Number.
# complete the code w/ the following objectives -> use awhile loop for an integer number, check whether true or false and then it'll exit itself.

print(
"""
+=================+
| bruh bruh bruh |
+=================+
"""
)

secret_number =777
# we love gambling???!!!!!! idk why but i feel like adding an additonal modifer to like make but uhhh this isn't godot lol

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# jackpot_of_century = int(input("""
# +========================================================================================+
# | Alright! It's time to start guessing, enter that number and hope it's the right one!! |
# +========================================================================================+
#                             """))
counter = 50

# while jackpot_of_century != 777 or counter == 50:
#    print("try again, the infinite tunnel seems to expand evermore....")
#    jackpot_of_century = int(input("Maybe the tunnel will cease to exist when you guess the secret number ;)"))
#    counter += 1
#    print("This is your", counter,"th time.")
#    if counter == 5:
#            print("""
#            +================================+
#            | uhhh would you like a hint?? |
#            +================================+
#            """)
#    elif counter == 20:
#            print("""
#            +================================+
#            | ... okay, range is near 700-800|
 #           +================================+
 #           """)
 #   elif counter == 40:
 #           print("""
 #           +================================+
 #           | ... okay, range is near 770-780|
 #            +================================+
 #           """)
 #   else:
 #       if counter == 50:
  #          print("Unforunately, you might be stuck in this damn tunnel if somehow you didn't get it :(")
  #          break

#if jackpot_of_century == 777:
#    print("congrats the tunnel is now collapsing!")

##### looping code w/ for.

# this essentially counts the loops of each "turn" i was literally just doing that on line 50, but it seems that
# probably the counter strat i was using is a bit too idk? not efficient?
# basically, come back to that code later and redo it :)

### The special loop -> [FOR] and i think [RANGE] too.

i = 0 # small note, to get a different starting point, put this into the for block, like i += 2,
for i in range(2): # this keeps going and prints until it hits 10, which instant exit rather than print(10), you'll need to
    print("The current number is:", i) # put range(11) for that one.

# in -> goes and looks at the box, then goes into the box, the capacity of a box, say it had 10 slots, is what it'll look for.
# then it'll print it all out. or rather fill in those boxes, the last number is excluded.
# pass itself -> empty instruction, just like print it needs something in the for block to execute.
# ONLY INTEGERS WHOLE NMUMBERS.
for i in range(1, 1): # instead of putting it into the function, rather just include another argument: 2nd number.
    print("you can do this btw", i , "times")

### a third number can be added, and its the increment, like +2 each time.
for i in range(0, 105, 25):
    print("oh my goodness is that a x25 multiplier??", "current nummber is", i)

##### LAB -> Essentials of for loop - counting mississippily

import time #holy this might be the most important thing, cause all this time i was trying to figure out how the hell
# i could shut down the damn file w/o having to press the button all the time and
# as well as make the console have a dedicated countdown timer.
#for i in range(1, 6):
 #   print(i, "Mississippi")
 #   if i == 5:
  #      print("Ready or not, here I come!")
  #  time.sleep(1) # this basically makes the range go one at a time instead of instant.

#### Break and Continue statements

# what are they? Special Instructions + Keywords, syntatic candy? to simplify? uhh, i'll get it eventually.
# break ends the loop and continue starts the loop, kind of like a skip button?

## Break -> Exits the loop immediately, and if there are other functions below, it'll keep going down.
## Continue -> Makes python act like it's the end of the body for that SPECIFIC number, starts next turn.

### LAB -> Break Statement Stuck in a loop.

#animal_spooky = print("chupacabra")

#while animal_spooky != "chupacabra":
  #  animal_spooky = input("try again, wrong animal")
  #  if animal_spooky == "chupacabra":
 #       break
# if i wanted to, i could give hints + add a counter for this to make it so if idk counter >= 25, animal feature = hint.

# if animal_spooky == "chupacabra":
print("Hooray! you guessed chupacabra, the loop has now been broken.")

### LAB -> The continue statement - the Ugly Vowel Eater.
# im not going to lie, continue statement makes me a bit confused. the basic idea = skip button and move on, but when its in a
# while loop that's where its like idk if its actually having an effect.

## design a for lopp, if-elif-else + continue statement all together.

#Vowel_Extraction = input("Please enter any word.")
number = 0

for number in range(1,13): # actual test b/c idk what im doing wrong, real test below
    if number == 5 or number == 6 or number == 7: # if these conditions are satisfied -> SKIPPED. everything else printed.
        continue
    else:
        print(number, end=" ")

# this was originally suppsoed to be an input statement but i got so confused that i decided to remove it.
Vowel_Extraction = "\nbees"

#for letter in Vowel_Extraction: # okay, i see what i did wrong, ive been doing Vowel Extraction -> WHOLE word and not
#    Vowel_Extraction = Vowel_Extraction.upper() # the individual letters, oh my god AAGHRSURGSH.
 #   if letter == "e" or letter == "a" or letter == "i" or letter == "o" or letter == "u":
 #       continue
#    elif letter == letter.upper():
 #       continue
  #  elif letter != "e" or letter != "a" or letter != "i" or letter != "o" or letter != "u":
   #     letter = letter.upper()
#        print(letter, end=" ")
#    else:
#        print("Vowel lmao", end=" ")

### LAB -> Pretty Vowel Eater!
# Slightly same thing as before, but a new string is added -> word_without_Vowels. Any result w/o
# vowels will now be printed and assigned?

print("seperation")
word_without_Vowels = ""
Vowel_Extraction2 = "Gregory"

# mm, the empty variable is now tripping me out for some reason?
for letter in Vowel_Extraction2:
    word_without_Vowels = letter # bro i keep putting these two lines inside the if/elif/else statements, they need to be outside
    word_without_Vowels = word_without_Vowels.upper() # of the statements ohh fkafiwaguhgfdbafh
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    elif letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        continue
    elif letter != "a" or letter != "e" or letter != "i" or letter != "o" or letter != "u":
        print(word_without_Vowels, end="")
        time.sleep(0.5)
    else:
        print("did something happen? lol")










