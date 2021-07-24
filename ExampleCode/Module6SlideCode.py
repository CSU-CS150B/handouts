import csv
from collections import namedtuple

machete = [4, 5, 2, 3,  6, 7, 8, 9]
machete_names = ["A New Hope", "The Empire Strikes Back", "Attack of  the Clones",
                 "Revenge of the Sith", "Return  of the Jedi", "The Force Awakens",
                 "The Last Jedi",  "The Rise of Skywalker"]

print("Star Wars {episode}: {title}".format(title=machete_names[2], episode=machete[2]))

glacier_size = [0.53, 0.34, 0.59, 0.2, 0.28, 0.13, 0.25, 5.5, 3.25, 0.84, 0.5, 0.75]
missing_glaciers = [0.19, 0.04, 0.08, 0.29, 0.22, 0.07, 0.12]

print(min(glacier_size)) # 0.13
print(max(glacier_size)) #  5.5
print(glacier_size.index(5.5)) #7
glacier_size[7] = "Five.Five"
print(glacier_size[7]) #  Five.Five

combined = glacier_size[7:9] +  missing_glaciers[0:3]
print(combined) # ["Five.Five", 3.25, 0.19, 0.04, 0.08]


unique = set([1, 1, 2, 2, 3, 3])
print(unique) # {1, 2, 3}

unique2 =  {1, 2, 97, 98, 99}
print(unique2) #{1, 2, 99, 97, 98}
unique.update(unique2)
print(unique) # {1, 2, 3, 99, 97, 98}

fixed = (1, 2, 3)
print(fixed)
print(fixed[1])
#fixed[1] = 10 #ERROR!

coords = namedtuple("Coordinates", ["Latitude", "Longitude"])

foco = coords("40.5853° N", "105.0844° W")
print(foco) # Coordinates(Latitude='40.5853° N', Longitude='105.0844° W')
print(foco.Latitude) # 40.5853° N

glaciers = [0.19, 0.04, 0.08, 0.29, 0.22, 0.07, 0.12]

index =  0
while index < len(glaciers):
    print(glaciers[index], end =' ')
    index += 1

for size in glaciers:
    print(size,  end=' ')

#



def simple_cipher(msg, shift):
    encrypt = ''
    for char in msg:
        encrypt += chr(ord(char)+shift)
    return encrypt

# pre - history, lists of plain text messages
# pre - key is the amount we want shift
# post - returns list of encrypted messages for each msg in history
def secure_message(history, key):
    encrypted = []
    for msg in history:
        encrypted.append(simple_cipher(msg, key))
    return tuple(encrypted)

def secure_messenger():
    person1 = ""
    person2 = ""
    history = []
    while check_exit(person1) and check_exit(person2):
        person1 = get_msg("Person1")
        history.append(person1)
        person2 = get_msg("Person2")
        history.append(person2)
    secured_message = secure_message(history, 5)
    print(secured_message)
    unsecure_message = secure_message(secured_message, -5)
    print(unsecure_message)

def get_msg(identity):
    return input("{}: What would you like to say? ".format(identity))



def check_exit(person):
    return person != "bye" and person != "goodbye"



print(simple_cipher("TEST: Ada", 2))
print(simple_cipher("TEST: AAAaaaBbBbCDE", 5))

test_History = ("Person1: Hello", "Person2: Howdy", "Person1: What them sports?",
                "Person2: I hear they are all over.")

print(secure_message(test_History, 2))
print(secure_message(test_History, 0) == test_History)

secure_messenger()

print()
print()

#### Files and CSV

f = open("simple.txt")
content = f.read()
f.close()
print(content)

f = open("simple.txt")
contents = f.readlines()
f.close()


print()
record = False
for line in contents:
    if line.strip() == "Legend of Korra":
        record = True
    if record:
        print(line.strip())

# Use with statement to guarantee file closure
with open("mobs.csv") as csvfile:
    mobs = csv.reader(csvfile)

    for mob in mobs:
        print(mob) #list including the header! (just a line)

print()
print()

mob = namedtuple("MOB", ["name", "hp", "ac", "initiative"])

def  mob_reader(filename, name):
    moblist = []
    with open(filename)  as  csvfile:
        mobs2 = csv.reader(csvfile)
        first = True
        for mob_line in mobs2:
            if first:
                first = False
                continue #  skip to start of loop
            if len(mob_line) >= 4:
                moblist.append(mob(mob_line[0], mob_line[1], mob_line[2],mob_line[3]))

    return moblist


def readpoem(filename):
    with open(filename)  as f:
        poem = f.read()
        return poem

print(mob_reader("mobs.csv", "zombie"))
print(readpoem("poem.txt"))

import csv

def read_poem(filename):
    with open(filename) as f:
        contents = f.readlines()

        for line in contents:
            print(line, end='')
#read_poem("poem.txt")

# pre - filename that is a CSV with the mobs name in the first location
# pre - mob_name the name of the mob I am looking for, return all references
# post: return a list of mobs that match mob_name
def mob_reader(filename, mob_name):
    mob_list = []
    with open(filename) as csvreader:
        lines = csv.reader(csvreader)
        for line in lines:
            if line[0] == mob_name:
                mob_list.append(line)
    return mob_list



def monster_horde(type_of_monster):
    monsters = mob_reader("mobs.csv", type_of_monster)
    init = 0
    first_mob = None
    for monster in monsters:
        if int(monster[3]) > init:
            init = int(monster[3])
            first_mob = monster
    print(first_mob)

monster_horde("skeleton")