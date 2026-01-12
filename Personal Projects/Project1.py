# 1/11/26, I'll probably make a detailed plan on what this one will be later here.
# this is supposed to be a CYOA, choose your own adventure game. i really need to plan this out, including dialogue lol.
# im really thinking of that one doom mod that was related to house of leaves and stanley parable.

import time


start_of_adventure = input("The hallway opens and closes. Do you want to enter? Type Yes/No")
timer_seconds_left = 5 # Eventually try and figure out how to do a timer + input as soon as console opens. but for now,

while timer_seconds_left != 0: # it'll wait until i put a response and then it'll start the countdown.
    print("You have", timer_seconds_left, "seconds left.")
    timer_seconds_left -= 1
    time.sleep(1)
    if timer_seconds_left == 0:
        print("testing")
        start_of_adventure =input("uhhh? did you mean yes or no?")


if start_of_adventure == "Yes":
    print("Great! as soon as you enter the hallway, you start to realize the door behind you starts... fading out of existence??")
elif start_of_adventure == "No":
    print("bye i guess lmao")
else:
    if start_of_adventure != "Yes" or "No":
        print("this should break")


for Starter_Story in range(3):
    print("blah blah", Starter_Story)
    time.sleep(1) # for future me, instead of adding time.sleep command AFTER EVERY SINGLE PRINT STATEMENT, i feel like
                    # there should be a way to pull print statements somehow. b/c i know time.sleep works sure but i
                    # like neatness and if i can somehow store it in a if statement or something i would but it
                    # only works in a for/while loop. Which if there was a strat that i know of I'd use it.