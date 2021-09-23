

# Write a line of code that returns true if one is “Rock”
# and two is “Scissors” (now finish the game)
def check_single(one, two):
    if "Rock" == one  and "Scissors" == two:
        return True
    elif "Scissors" == one and "Paper" == two:
        return True
    elif "Paper" == one  and "Rock" == two:
        return True
    return False







print("TESTING", check_single("Rock", "Scissors"),
      check_single("Rock", "Bomb"),
      check_single("Scissors", "Paper"),
      check_single("Paper", "Rock"))









favorite_companion = input("Who is your favorite companion? ")
favorite_companion2 = input("Who is the clever one? ")
if (favorite_companion == "Amy" or favorite_companion == "Martha") and favorite_companion2 == "Clara":
    print("they are all good!")
else:
    print("Did you forget Clara?")


def rock_paper_scissors():
    winner = False
    while not winner:
        player1 = input("Rock, Paper, or Scissors? ")
        player2 = input("Rock, Paper, or Scissors? ")
        p1_win = check_single(player1, player2)
        p2_win = check_single(player2, player1)
        ## todo

