


#create a dictionary with some 'assignments' in it, 
my_grades =  {"a1": 3, "a2": 4, "p1": 0, "p3":"n/a"}

## print some out
print(my_grades["a1"])
print(my_grades["p1"])

# add another
my_grades["another"] = 10

# print all out
print(my_grades)

for assignment, grade in my_grades.items():
    print(assignment, grade)














def update_grade(grades):
    assignment = input("Which assignment do you want to update? ")
    grade = input("What grade would you like? ")
    grades[assignment] = grade

def run():
    grades = {}
    print("Welcome to the grade book.")
    action = input("what would you like to do? ")
    while(action != "exit") :
        if action == "update":
            update_grade(grades)
        if action == "print":
            print(grades)
        action = input("what would you like to do? ")

#run()





 