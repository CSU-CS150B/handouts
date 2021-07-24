
def reverse_list(values):
    # base first!
    if len(values) < 1:
        return values
    return [values[-1]] + reverse_list(values[:-1])




def reverse_list_tail(values, reverse):
    # base first!
    if len(values) < 1:
        return reverse + values
    return  reverse_list_tail(values[:-1], reverse + [values[-1]])

def reverse_list_tail_start(values):
    return  reverse_list_tail(values, [])


def recursion_slide_code():
    twolength = ["a", "b"]
    reverse = [twolength[1], twolength[0]]
    print(reversed)

    ## reverse a list
    print(reverse_list(["Princess Zelda", "Ganon", "Link", "Epona", "Impa"]))

    print(reverse_list_tail_start(["Princess Zelda", "Ganon", "Link", "Epona", "Impa"]))


recursion_slide_code()

# sort values in a list

zelda_lst =  ["Princess Zelda", "Ganon", "Link", "Epona", "Impa"]

# quest is to sort the list
def sort_list_tail(unsorted, result, use_max):
    # base case - simplest case
    if len(unsorted) < 1:
        return result
    val = max(unsorted) if use_max else min(unsorted)
    result.append(val)
    unsorted.remove(val)
    return sort_list_tail(unsorted, result, use_max)

def sort_list_min(unsorted):
    #print("TEST<sort_list_min>", unsorted)
    return sort_list_tail(unsorted.copy(), [], False)

def sort_list_max(unsorted):
    #print("TEST<sort_list_max>", unsorted)
    return sort_list_tail(unsorted.copy(), [], True)

harder_list = [1, [3,5], 2, [15,13]]

print(sort_list_min(zelda_lst))
print(sort_list_max(zelda_lst))


### dictionary slide code

def dictionary_slides():
    authorized = {"Murdoch": ["Cut & Thrust", "Rapier Spear", "Rapier", "Combat Archery"],
                  "Valtaja": ["Cut & Thrust", "Rapier Spear", "Rapier"],
                  "Aegeon": ["Cut & Thrust", "Rapier Spear", "Rapier", "Armored Combat", "Great Weapons"],
                  "Felix": ["Armored Combat", "Great Weapons"]}

    print(authorized["Murdoch"]) # ['Cut & Thrust', 'Rapier Spear', 'Rapier', 'Combat Archery']
    authorized["Murdoch"].append("Armored Combat")
    print(authorized["Murdoch"]) # ['Cut & Thrust', 'Rapier Spear', 'Rapier', 'Combat Archery', 'Armored Combat']
    authorized["Miriam"] = ["Cut & Thrust","Great Weapons" ]
    print(authorized)

    for key, value in  authorized.items():
        print("{} is authorized in {}".format(key, value))


dictionary_slides()
print()
print()

# let's code
uh_database  = {"Murdoch": ["Cut & Thrust", "Rapier Spear", "Rapier", "Combat Archery"],
                "Valtaja": ["Cut & Thrust", "Rapier Spear", "Rapier"],
                "Aegeon":  ["Cut & Thrust", "Rapier Spear", "Rapier", "Armored Combat",
                            "Great Weapons"],
                "Felix":   ["Armored Combat", "Great Weapons"]}

def is_auth(db, name, style):
    if name not in db:
        return False
    return style in db[name]

def add_auth(db, name, style):
    if name not in db:
        db[name] = [style]
    else:
        if not is_auth(db, name, style):
            db[name].append(style)
    return name, db[name]

def remove_auth(db, name, style):
    if is_auth(db, name, style):
        db[name].remove(style)
        if len(db[name]) < 1:
           db.pop(name)
        else:
            return db[name]
    return None

def print_all(db):
    for k in sorted(db.keys()):
        print("{} is authorized in {}.".format(k, ", ".join(sorted(db[k]))))


print("TEST", add_auth(uh_database, "Miriam", "Rapier"))
print("TEST", add_auth(uh_database, "Miriam", "C&T"))
print("TEST", remove_auth(uh_database, "Miriam", "Rapier"))

print_all(uh_database)
