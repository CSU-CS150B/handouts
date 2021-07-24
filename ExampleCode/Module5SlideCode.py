
val = 5
val **= 2

val = 5 ** 2
print(val)

val = 5 // 2
print(val)

val  = 5.0  // 2
print(val)

print(ord('a'))
print(chr(97))

print(chr(ord('A' ) +2))


# let's code
def obfuscate(number):
    new_number = number
    new_number **= 2
    new_number = (new_number % 25) + 1
    return new_number

#print("TEST: {} -> {}".format(5, obfuscate(5)))
#print("TEST: {} -> {}".format(42, obfuscate(42)))
#print("TEST: {} -> {}".format(3, obfuscate(3)))
#print("TEST: {} -> {}".format(1919198, obfuscate(1919198)))

def simple_cipher(msg, shift):
    index = 0
    encrypted = ""
    while index < len(msg):
        encrypted += chr(ord(msg[index])+shift)
        index += 1
    return encrypted

def my_cipher_game():
    msg = input("What message would you like to encrypt? ")
    shift = int(input("What is your key? "))
    action = input("Do you wish to encrypt or decrypt (e/d)? ")[0]
    shift = obfuscate(shift)
    if action == 'd':
        shift *= -1
    encrypted = simple_cipher(msg, shift)
    print("Your encrypted message is...\n{}".format(encrypted))


my_cipher_game()



print(simple_cipher("Ada", 2))



### Branching Slides


val = 100 <= 10 * 10
print(val)


val = int(input("Number of puppies? "))
if val < 100 and val * 2 > 50:
    print("That's a start")
else:
    print("Need more puppies")


friend = input("What is better?")
if friend == "Cat" or friend == "Dog":
    print("they  are all good!")
else:
    print("A what now?")


favorite_companion = input("Who is your favorite companion? ")
favorite_companion2 = input("Who is the clever one? ")
if (favorite_companion == "Amy" or favorite_companion == "Martha") and favorite_companion2 == "Clara":
    print("they  are all good!")
else:
    print("Did you forget Clara?")


doc = 13
companion = "Clara" if doc == 12 else "Yasmin"
print(companion)  # prints Yasmin

#pre - only checking to see if one wins
def check_single(one, two):
    if (one == "Rock" or one=="rock") and (two == "Scissors" or two == "scissors"):
        return True
    if (one == "Scissors" or one == "scissors") and (two == "Paper" or two=="paper"):
        return True
    if (one == "Paper" or one == "paper") and (two == "Rock" or two == "rock"):
        return True
    return False

def get_choice():
    return input("Rock, Paper, or Scissors? ")

def rock_paper_scissors():
    end_game = False
    while not end_game:
        player1 = get_choice()
        player2 = get_choice()
        if check_single(player1, player2) :
            print("Player 1 wins")
            end_game = True
        elif check_single(player2, player1):
            print("Player 2 wins")
            end_game = True
        else:
            print("No one wins, try again.")

rock_paper_scissors()

#print("Test: Rock vs Scissors: {}".format(check_single("Rock", "Scissors")))
#print("Test: Scissors vs rock: Expected False, Answer: {}".format(
 #   check_single("Scissors", "rock")))
