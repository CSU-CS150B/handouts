



def update_grade(grades):
    assignment = input("Which assignment do you want to update? ")
    grade = input("What grade would you like? ")
    grades[assignment] = grade # maybe turn to 

def run():
    grades = {} # initialize dictionary
    print("Welcome to the grade book.")
    action = input("what would you like to do? ")
    while(action != "exit") :
        if action == "update":
            update_grade(grades)
        action = input("what would you like to do? ")

run()