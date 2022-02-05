# In class activities


# Activity one: conditional statement

def age_check(age):
    return age >= 21 # replace false with your conditional statement. This can be *one line* don't over think

print(age_check(20)) # should print False
print(age_check(21)) # should print True
print(age_check(22)) # should print True


def age_check_by_region(age, region):
    confirm = "Unknown Region, Not OK"
    if region == "USA":
        if age >= 21: confirm = "OK"
        else: confirm = "NOT OK"
    elif region == "EURO":
        if age >= 18: confirm = "OK"
        else: confirm = "NOT OK"
    
    # write an if check, that will 
    # set the value of confirm 
    # based on the values expected below
    # will require a nested if statement, or an additional function


    return confirm 


print(age_check_by_region(21, "USA")) # prints  "OK"
print(age_check_by_region(20, "USA"))  # prints  "NOT OK"
print(age_check_by_region(21, "EURO"))  # prints  "OK"
print(age_check_by_region(18, "EURO"))  # prints  "OK"
print(age_check_by_region(17, "EURO"))  # prints  "NOT OK"
# if anything else is passed into region, it will return "Unknown Region, Not OK"
print(age_check_by_region(32, "YOLO"))
