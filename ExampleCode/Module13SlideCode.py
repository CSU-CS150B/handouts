import csv
import random


def loops_slide_code():

    odds = []
    for val in [23, 12, 13, 16, 18, 2, 23, 0, 17, 20, 191, 10]:
        if val in odds:
            break
        if val % 2 == 1:
            odds.append(val)
    else:
        print("Found no duplicates!") # NOT printed!
    print(odds) # [23, 13]

    odds = []
    for val in [23, 12, 13, 16, 18, 2, 23, 0, 17, 20, 191, 10]:
        if val in odds:
            continue
        if val % 2 == 1:
            odds.append(val)
    print(odds) # [23, 13, 17, 191]

    numbers = [random.randint(1,6) for i in range(1,10)]
    print(numbers) # [6, 5, 2, 4, 2, 6, 1, 3, 4]

    odds = [i*-1 for i in numbers if i % 2 == 1]
    print(odds)# [-5, -1, -3]

loops_slide_code()

# let's code!


## this example was not used in the slides, but I have it here just as another example
def get_die_roles(count=1,sides=6):
    return [random.randint(1,sides) for i in range(0,count)]


def get_successes(rolls, dc):
    #return len([i for i in rolls if i >= dc]) + len([20 for i in rolls if i == 20]) - len([1 for i in rolls if i == 1])
    count = 0
    for roll in rolls:
        if roll == 20:
            count += 2
        elif roll == 1:
            count -= 2
        elif roll >= dc:
            count += 1
    return count


def challenge(dc, total_rolls=6, success_need=3, damage_risk=(2,6,0)):
    rolls = get_die_roles(total_rolls, 20)
    success_check = get_successes(rolls, dc) > success_need
    damage = sum(get_die_roles(damage_risk[0], damage_risk[1]))
    damage = damage * damage_risk[3] if success_need > success_check else damage
    return success_check, damage, rolls

print()
print()
# Let's Code - flower example
def reader(filename):
    headers = {}
    with open(filename) as csvreader:
        lines = [tuple(line) for line in csv.reader(csvreader)]
        for index, header in enumerate(lines[0]):
           # print("DEBUG<reader>: index:{} and header:{}".format(index,header))
            headers[header] = index
    return headers, tuple(lines[1:])

def categorize(data_list, category_index, *args):
    categories = {}
    lower_args = [arg.lower() for arg in args]
    for larg in lower_args:
        categories[larg] = [data for data in data_list if data[category_index].lower() == larg]
    categories["other"] = [data for data in data_list if data[category_index].lower() not in lower_args ]
    return categories

def build_stats(data, category_index, image_index, *args):
    categories = categorize(data, category_index, *args)
    pop_list = []
    for key,value in categories.items():
        if len(value) < 1:
            pop_list.append(key)
            continue  # skip empty categories
        categories[key] = {"average": len(value) / len(data),
                           "total" : len(value),
                           "plants" : value,
                           "no-image": [val for val in value if
                                        val[image_index].lower() == "n/a"]
                           }
    else:
        for key in pop_list:
            categories.pop(key)
    return categories

def run_stats():
    headers, data = reader("flowers.csv")
    stats = build_stats(data, headers["Category"], headers["Image"], "poisonous", "ok")
    print_stats(stats, headers["Common"], headers["Technical"])

def print_stats(stats, *args):
    for category,stat in stats.items():
        print("{}:".format(category).capitalize())
        print("Percent of Total: {}%".format(stat["average"]*100))
        print()
        for plant in sorted(stat["plants"]):
            for arg in args:
                print("{:<20}".format(plant[arg]), end='')
            print()
        print()




run_stats()
######## Recursion Slides


def binary_search(sorted_list, value, start=0, end=None):
    if end is None:
        end = len(sorted_list)
    if (end - start)+1 < 2:
        return -1
    ## get middle index!
    middle = (end+start) // 2 #notice //, why?
    if value == sorted_list[middle]:
        index = middle
    elif value < sorted_list[middle]:
        print("DEBUG <", value, sorted_list[middle])
        index = binary_search(sorted_list, value, start=0, end=middle)
    else:
        print("DEBUG else", value, sorted_list[middle])
        index = binary_search(sorted_list, value, start=middle+1, end=end)
    return index

def recursive_slide_code(): ## way to debug it!
    values = sorted([random.randint(0, 100) for i in range(0,10)])
    print(values)
    for index,value in enumerate(values):
        found = binary_search(values, value)
        print("Found {}, at index {} looking for {}: Valid? {}".format(values[found], found, value, values[found] == value))


recursive_slide_code()