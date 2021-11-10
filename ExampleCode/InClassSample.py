import csv

lst = []

with open("mobs.csv") as csvfile:
    mobs = csv.reader(csvfile)
    print(mobs)

    for row in mobs:
        lst.append(row)
#        print(mob) #list including the header! (just a line)

filtered = []
for row in lst:
    if 'zombie' in row:
        filtered.append(float(row[1]))

print(sum(filtered)/len(filtered))


dct = {'val1':10, 'val2':30}

for val,value in  dct.items():
    print(val,value)


def myfunc(val = 10):
    print("this is my function")
    return val * 10 # ok silly

def myfunc2():
    print("this is the first  one ")
    print(myfunc(12))

myfunc2()