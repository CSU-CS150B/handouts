

def myfun(lst):
    small = min(lst)
    large = max(lst)
    avg = sum(lst) / len(lst)
    return "Max: {}, Min:{}, Avg:{}".format(small, large, avg)

print(myfun([10, 20, 128, 74]))
print(myfun([1, 20, 120, 70]))
