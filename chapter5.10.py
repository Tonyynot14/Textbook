students = int(input("How many students do you have?"))
highest = 0
secondhighest = 0
for i in range(students):
    score = int(input("What are the scores for the test?"))
    if score > highest:
        secondhighest=highest
        highest = score

print("The highest test score was", highest, "\nThe second highest was",secondhighest )
