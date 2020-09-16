"""
2. Write a program that will take the marks (for three assessments Quiz1 (20%), Quiz2(30% and Final(50%)) of all the students of a unit as input and stores all the detail in a list. Your program should have following features and constrains:
• Check the input validity
• Compute the total marks and letter grade. Use the Murdoch
university grade conversion table to calculate the letter grade.
• Keep taking the input unless a negative or zero is given as the
input for student ID
• Save the data in following format:
[st_ID, Q1_mark, Q2_mark, Final_mark, Total, Letter grade]
• Display the whole list.
A typical input output screenshot might be as follows:
Student ID:1001
Enter Q1: 20
Enter Q2: 25
Enter Final: 40
Student ID:1002
Enter Q1: 12
Enter Q2: 2.5
Enter Final: 45
Student ID:1003
Enter Q1: 20
Enter Q2: 30
Enter Final: 32
Student ID:0
[[1001, 20.0, 25.0, 40.0, 85.0, ‘HD’], [1002, 12.0, 2.5, 45.0, 59.5, ‘P’],
[1003, 20.0, 30.0, 32.0, 82.0, ‘D’]]
Note: This output format may not look the same as the format asked.
"""

s = 1
L = []
Lf = []
b = True


while(b):
    s = int(input("Student ID: "))
    if (s <= 0):
        break
    L.append(s)

    q1 = -1
    while not(q1 >= 0 and q1 <= 20):
        q1 = float(input("Enter Q1: "))
    L.append(q1)

    q2 = -1
    while not(q2 >= 0 and q2 <= 30):
        q2 = float(input("Enter Q2: "))
    L.append(q2)

    f = -1
    while not(f >= 0 and f <= 50):
        f = float(input("Enter Final: "))
    L.append(f)
    total = q1+q2+f
    lg = ""
    if (total >= 80):
        lg = "HD"
    elif( total >= 60):
        lg = "D"
    elif( total >= 50):
        lg = "P"
    else:
        lg = "N"

    L.append(total)
    L.append(lg)
    Lf.append(L)
    L = []

print(Lf)
