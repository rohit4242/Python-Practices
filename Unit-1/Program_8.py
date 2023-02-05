# Write a Python Program to input marks of 4 subjects and
# display Total, Percentage, Result and Grade. If student is fail
# (<40) in any subject then Result should be displayed as “FAIL”
# and Grade should be displayed as “With Held**”

def Calculate_Result(marks):
    for i in marks:
        if i < 40:
            return sum(marks), sum(marks)/4, "FAIL", "With Held"

    total = sum(marks)
    percentage = total / 4
    if percentage >= 80:
        grade = 'A+'
    elif percentage >= 70:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    else:
        grade = 'D'
    return total, percentage, "PASS", grade


marks = []

for i in range(4):
    marks.append(float(input(f'Enter Marks Of Subject {i+1}: ')))


total, percentage, result, grade = Calculate_Result(marks)

print("Total Marks is: ", total)
print("Percentage is: ", percentage)
print("Result : ", result)
print("Your Grade is: ", grade)
