# loop demo

#while True:
 #   print("infinite loop, breaks computer")

from random import random

i = 0
while i < 10:
    print(i)
    i += 1  # increment i

check = '-'
while check != 'y':
    print("I want to build a snowman.")
    check = input("Do you want to build a snowman? ")[0]


i = 10
answer = ""
while i > 0:
    answer += "{},".format(i)
    i -= 1
print(answer[:-1])

## let's code


def run_earnings(months, budget, cost):
    earnings = 0
    while months > 0:
        change = get_change()
        earnings += earnings * change
        print("DEBUG<run_earnings>: cost:{}, earnings:{}".format(cost, earnings))
        if budget >= cost:
            budget -= cost
            earnings += cost
        cost *= 1 + change  # there is an error in how i do this! maybe look up how to do it?
        months -= 1
    return earnings


def lets_play():
    budget = float(input("Enter a starting budget: "))
    cost = float(input("Cost of item: "))
    months = int(input("Enter a number of months to run: "))
    earnings = run_earnings(months, budget, cost)
    print("DEBUG budget: {} and earnings: {}".format(budget, earnings))


def get_change():
    return random.random() * random.randint(-1, 1)


# try running each method individually, so you can  test it with set values

lets_play()