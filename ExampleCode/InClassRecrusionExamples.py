

def loop_factorial(whole):
    answer = 1
    while(whole  > 1):
        answer *= whole
        whole -= 1

    return answer

print("Testing loop factorial", loop_factorial(5))
print("Testing loop factorial", loop_factorial(4))

def factorial(whole):
    if whole < 2: return 1
    return whole * factorial(whole -1)


#print("Testing recursive factorial", factorial(5))
#print("Testing recursive factorial", factorial(4))


def sum(lst):
    #base case
    if not lst: return 0
    #recursive 
    return lst[0] + sum(lst[1:])


print("testing sum", sum([5,4,1]))
print("testing sum", sum([1,1,1, 1]))