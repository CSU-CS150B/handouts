

def number_generator(start, end = 10, step = 1):
    lst = []
    while start < end:
        lst.append(start)
        start += step
    return tuple(lst)

print(number_generator(5, 10, 1)) # (5, 6, 7, 8, 9)
print(number_generator(2)) # (2, 3, 4, 5, 6, 7, 8, 9)
# print(number_generator()) # does not run

print(number_generator(2, step=2)) # (2, 4, 6, 8)
print(number_generator(5, end=7))  # (5, 6)

# quest is to sort the list
def sort_list(unsorted, result=None, sorter=max):
    # base case - simplest case
    if result is None:
       result =  []
       unsorted = unsorted.copy()
    if len(unsorted) < 1:
        return result
    val = sorter(unsorted)
    result.append(val)
    unsorted.remove(val)
    return sort_list(unsorted, result=result, sorter=sorter)

zelda_lst =  ["Princess Zelda", "Ganon", "Link", "Impa", "Epona"]
print(sort_list(zelda_lst))
print(sort_list(zelda_lst, sorter=min))

def print_hello(*args):
    for arg in sorted(args):
        print("Hello {}".format(arg), end=', ')

print_hello("Hook",  "Wendy", "John", "Peter") # Hello Hook, Hello John, Hello Peter, Hello Wendy,
my_func = print_hello
my_func("Hook",  "Wendy", "John", "Peter") # Hello Hook, Hello John, Hello Peter, Hello Wendy,

print()
# lets code

def no_change(value):
    return value

def mul(value):
    #print("TEST<mul({})>".format(value))
    return value * value


# take a list of values, sum it up, and return the list modified by the function
def sum_it(lst, func=no_change, result=0, result_lst=None):
    if result_lst is None:
        result_lst = []
    # base case
    if len(lst) < 1:
        return result, result_lst
    if type(lst[0]) is list:
        val, rtn_lst = sum_it(lst[0],func=func)
        result_lst += rtn_lst
    else:
        val = func(lst[0])
        result_lst.append(val)
    result += val
    return sum_it(lst[1:], func=func, result=result,
                  result_lst=result_lst)

print("TEST", sum_it([-5, 1, [2, [[[-2]]]], -1], mul))


## to take a list of values, and sum-up that list
def sum_it_value(lst, func=no_change):
    # base case?
    if len(lst) < 1:
        return 0
    if type(lst[0]) is list:
        return sum_it_value(lst[0], func=func) + sum_it_value(lst[1:], func=func)
    return func(lst[0]) + sum_it_value(lst[1:], func=func)
