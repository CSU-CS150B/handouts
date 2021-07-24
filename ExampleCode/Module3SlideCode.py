import random


def get_happy(puppies):
    happy = False
    if puppies >= 100:
        happy = True
    return happy


def get_happy2(puppies):
    if puppies >= 100:
        happy = True
    else:
        happy = False
    return happy


# conditions are operations, so you can return the result
def get_happy3(puppies):
    return puppies >= 100


def broken_rogue(dice_roll):
    if dice_roll >= 10:
        if dice_roll > 15:
            print("Trap Disarmed!")
        else:
            print("Get the 10 foot pole...")
    elif dice_roll >= 5:
        print("As far as I am aware, no traps.")
    else:
        print("Found the trap!")


broken_rogue(10)
broken_rogue(16)
broken_rogue(5)
broken_rogue(1)


## let's code

def check_for_traps(dice_roll, difficulty, contains_trap):
    if dice_roll >= difficulty:
        return contains_trap
    elif dice_roll >= 5:
        return False
    else:
        return not contains_trap


def disarm_trap(dice_roll, difficulty, dmg_on_fail):
    if dice_roll >= difficulty:
        return 0
    if dice_roll > 1:
        return dmg_on_fail
    return dmg_on_fail * 2


def quest_actions():
    answer = input("Do you check for traps (y/n)? ")[0]  # just grab first character
    if answer == 'y':
        trap = check_for_traps(random.randint(1, 20), 15, True)
        if trap:
            run_found_trap()
        else:
            run_no_trap()
    else:
        dmg = disarm_trap(0, 15)
        print("There was a trap! You took {} damage.".format(dmg))

def run_no_trap():
    print("As far as you are aware, no traps.")
    proceed = input("Do you wish to proceed (y/n): ")[0]
    if proceed == 'y':
        dmg = disarm_trap(0, 15, 10)
        print("There was a trap! You took {} damage.".format(dmg))
    else:
        print("Smart, there was really a trap. Goodbye")

def run_found_trap():
    print("You found a trap!")
    disarm = input("Do you wish to disarm the trap (y/n)? ")[0]
    if disarm == 'y':
        dmg = disarm_trap(random.randint(1, 20), 12, 10)
        if dmg > 0:
            print("You fail to disarm the trap properly, taking {} damage.".format(dmg))
        else:
            print("You successfully disarm the trap. You made it!")





quest_actions()