"""
3. [Continuation of question 2] Show the following statistics:
• Average, highest and lowest mark
• The ID of all the students who got the highest mark
• The ID of all the students who got the lowest mark
• Total number of students failed in the unit (assuming 50% is thepass mark)
"""
s = 1
L = []
Lf = []
b = True

###########
totalall = 0.0
high = 0.0
low = 100.0
totalfail = 0
LHigh = []
Llow = []
###########

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

    ###########
    totalall = totalall + total

    if (total == high):
        LHigh.append(s)
    elif (total > high):
        LHigh = []
        LHigh.append(s)

    if (total == low):
        Llow.append(s)
    elif (total < low):
        Llow = []
        Llow.append(s)

    high = max(high, total)
    low = min(low, total)

    ###########

    lg = ""
    if (total >= 80):
        lg = "HD"
    elif( total >= 60):
        lg = "D"
    elif( total >= 50):
        lg = "P"
    else:
        lg = "N"
        totalfail = totalfail + 1

    L.append(total)
    L.append(lg)
    Lf.append(L)
    L = []

print(Lf)

###########
print("Average", totalall / len(Lf))
print("Highest", high)
print("Lowest", low)
print("List of ID who got the highest mark", LHigh)
print("List of ID who got the lowest mark", Llow)
print("Total students failed", totalfail)
###########