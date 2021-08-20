## Expression and Functions Slides

computer = "Bombe Machine"  # assignment of string to variable
code = 10  # whole number - called "int"
formula = (code * 3 / 2) - 2.1  # now a floating point number
print("The code to the " + computer + " is ", end='')
print(formula)


def cipher_machine_code(computer, code):
    formula = (code * 3 / 2) - 2.1  # now a floating point number
    print("The code to the " + computer + " is ", end='')
    print(formula)


def get_real_code(code):
    return (code * 3 / 2) - 2.1


def print_machine_info(computer, code):
    print("The code to the " + computer + " is ", end='')
    print(get_real_code(code))


def use_formula(code):
    solve_cipher(get_real_code(code) * 10)


def solve_cipher(param):
    pass


# call the function twice
cipher_machine_code("Bombe Machine", 10)
cipher_machine_code("Colossus", 12)

## Strings and String Formatting 02-4

fname = "Howard"
mname = "Phillips"
longname = "of the Lovecraft"
length = len(fname)  # sets 2 to length!
finitial = fname[0]  # returns H, sets it to finitial
minitial = mname[0]  # returns P, sets it to minitial
lname = longname[7:]  # returns Lovecraft
print(finitial + minitial + lname)
print(finitial + "." + minitial + ". " + lname)
print(len(lname))

print(finitial + "." + minitial + ". " + lname + str(len(lname)))

combined = "{}.{}. {}".format(finitial, minitial, lname)
message = "{name} is {length} long".format(length=len(combined), name=combined)
print(message)

thirty_three = 1 / 3 * 100
print(str(thirty_three) + "%")
print("{:.2f}%".format(thirty_three))

print("|{:<30}|".format(combined))


#### let's program (final code)
def get_author_name(fname, mname, lname):
    fancy_name = "{first}.{middle}. {last}".format(last=lname[-5:],
                                                   first=fname[0],
                                                   middle=mname[0])
    return fancy_name


def get_percent_difficult(words, complex_words):
    complex = (complex_words / words) * 100
    return "{:.2f}%".format(complex)


def get_author_card(name, complexity):
    card_border = "+==============================+\n"
    card = card_border
    card += "|{name:<30}|\n".format(name=name)
    card += "|{:<30}|\n".format("Complexity Level: " + complexity)
    card += "|{:<30}|\n".format(" ")
    card += "|{:<30}|\n".format(" ")
    card += card_border[:-1]
    return card


name = get_author_name("Aidan", "Rayson", "LionHeart")
complex = get_percent_difficult(1000, 999)
print(get_author_card(name, complex))


## in class only code
coding = "Compiling is Automatic Coding"
short = coding[11:11]
print(len(short))

print(coding[:10])
