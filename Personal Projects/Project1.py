# 1/11/26, I'll probably make a detailed plan on what this one will be later here.
# this is supposed to be a CYOA, choose your own adventure game. i really need to plan this out, including dialogue lol.
# im really thinking of that one doom mod that was related to house of leaves and stanley parable.

import time
starter_time = 6

while starter_time != 0:
    print(starter_time, "seconds left.")
    starter_time -= 1
    time.sleep(1)
    if starter_time == 5:
        start_of_adventure = input("The hallway opens and closes. Do you want to enter? Type Yes/No")

timer_seconds_left = 5

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

if start_of_adventure == "Yes":
    print("bruh")
    print("d1")
    print("d2")
    time.sleep(1)
