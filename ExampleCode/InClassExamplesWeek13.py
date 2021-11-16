
lst = [12, 22, 13, 12, 15, 42, 21, 19]
new_list = []
for val in lst: 
    if val % 2 == 0:
        new_list.append(val)

print(new_list)
tmp = [i for i in new_list if i % 2 == 0]
print(tmp)

lst = [["A-", "14.23"],
    ["just B", "12.12"],
    ["A+", "16.00"],
    ["A", "15.00"],
    ["F", "0"]]

tmp2 = [float(ls[1]) for ls in lst if "A" in ls[0]]
print(tmp2)
# the new list built would return
#[14.23, 16.00, 15.00]
### use List Comprehensions! 
### hint in operator helps
