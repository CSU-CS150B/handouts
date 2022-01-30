## Inclass Activity

# Task 1: Write a function named nameFormat(first, last), that takes in two parameters
# it will then return a string in the format of "last, first"
# example:
# ```
#  name = nameFormat("Monica", "Rambeau")
#  print(name) # prints Rambeau, Monica 
# ```
# don't forget indents for your block of code under the def
def nameFormat(first, last):
    return last + ", " + first


## Task 2: Write a function called computeAverage, that takes in three values, and returns
# the average value. Remember the average value is (value1 + value2 + value3) / 3
def computeAverage(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3


### Task 3
## In the comments here, write a sentance lines explaining what this funciton does, and why a seperate function
#
#
#
def getGrade():
    return float(input("Enter a grade: "))

## Task 4 - Uncomment the line below tests() to make this program run, make sure to put values in zybooks!
def main():
    fname = input("What is your first name? ")
    lname = input("What is your last name? ")
    grade1 = getGrade()
    grade2 = getGrade()
    grade3 = getGrade()
    print(nameFormat(fname, lname) + " has an average grade of " + str(computeAverage(grade1, grade2, grade3)))


## A series of function calls to help test what you write above
## modify as you will
def tests():
    name = nameFormat("Monica", "Rambeau")
    print(name) # should print Rombeau, Monica
    name2 = nameFormat("Kitty", "Pryde")
    print(name2) # should print Pryde, Kitty
    marvelGrades = computeAverage(100, 80, 90)
    shadowcatGrades = computeAverage(70, 90, 100)
    print(marvelGrades) # should print  90.0
    print(shadowcatGrades) # should print 86.666667 (number of 66 may vary)

tests()
main()


## last thought - notice how this entire program, everything is inside a function, except the two calls to 'run'
# the program. This is what programming will start to look like!
