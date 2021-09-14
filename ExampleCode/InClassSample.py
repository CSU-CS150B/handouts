
    
def simpleWhile(start, end):
    counter = 0
    while start < end:
        counter -= 1
        start += 1
    return counter


print(simpleWhile(12, 12))
print(simpleWhile(1, 0))
print(simpleWhile(0, 5))

#---
i = 0
while i < 10:
    print(i)
    i += 1  # increment i

check = '-'
while check != 'y':
    print("I want to build a snowman.")
    check = input("Do you want to build a snowman? ")[0]


i = 10
answer = ""
while i > 0:
    answer += "{},".format(i)
    i -= 1
print(answer)