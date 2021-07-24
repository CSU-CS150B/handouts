
#

def slide_examples():
    cast = ["Westley", "Buttercup", "Inigo Montoya", "Vizzini",
            "Fezzik", "Rugan", "Humperdinck"]

    cast.sort()
    cast2 = ["Westley", "Buttercup", "Inigo Montoya", "Vizzini",
                "Fezzik", "Rugan", "Humperdinck"]


    if cast == sorted(cast2):
        print("They are equal") # this does print!

    for actor in reversed(cast):
        print(actor)

    print(max(cast)) # Westley
    print(min(cast))

    for index, actor in enumerate(cast):
        print("{}: {}".format(index, actor))


# code along code


pb_cast = ["Westley", "Buttercup", "Inigo Montoya", "Vizzini",
        "Fezzik", "Rugan", "Humperdinck"]
pb_villains = ["Humperdinck", "Rugan", "Vizzini"]


# get a list of heroes sorted - from the cast
# given a list of villains and a list of cast members
# return a sorted list
def get_heroes(cast, villains):
    hero = cast.copy()
    for villain in villains:
        if villain in hero:
            hero.remove(villain)
    hero.sort()
    return hero

def get_grouped_casts(grouped_cast_list):
    heroes = grouped_cast_list[0]
    villains = grouped_cast_list[1]
    grouped_string = ""
    for i, hero in enumerate(heroes):
        villain = villains[i] if i < len(villains) else ""
        grouped_string += "{}: {:<20} {}\n".format(i+1, hero, villain)
    return grouped_string

def movie_analysis(cast, villains):
    heroes = get_heroes(cast, villains)
    combined = [heroes,villains]
    print(get_grouped_casts(combined))

movie_analysis(pb_cast, pb_villains)
#print("TEST", get_heroes(pb_cast, pb_villains))
#print("TEST", pb_cast, pb_villains)
#print("TEST", pb_cast, pb_villains)
