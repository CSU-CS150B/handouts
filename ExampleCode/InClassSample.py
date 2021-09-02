
# def longerFunc(person, adj, code):
#     print("Hello " + person)
#     print("Cryptography is the " + adj)
#     code = code + code / 2
#     print("The hidden number is: ", int(code))
#
# longerFunc("Valentine", "Bombe", 10.0)
# print()
# print()

###
def student_score(name, score):
    return "{},{:.2f}%".format(name, score*100)

print(student_score("Amy", 0.39399))