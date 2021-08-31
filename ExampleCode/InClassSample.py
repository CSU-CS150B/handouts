
def longerFunc(person, adj, code):
    print("Hello " + person)
    print("Cryptography is the " + adj)
    code = code + code / 2
    print("The hidden number is: ", int(code))

longerFunc("Valentine", "bombe", 10.0)
print()
print()

###
# computer = "Bombe Machine"  # assignment of string to variable
# code = 10  # whole number - called "int"
# formula = (code * 3/2) - 2.1
# print("The code to the " + computer + " is ", formula)
