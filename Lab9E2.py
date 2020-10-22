# %%
import datetime
# %%


class person():
    def __init__(self, n, DoB):
        self.__DoB = DoB
        self.__name = n

    def getName(self):
        return self.__name

    def getDate(self):
        return self.__DoB

    def getFormattedDate(self):
        return self.__DoB.strftime('%d/%m/%Y')


class memberMU(person):  # inherits person
    def __init__(self, n, DoB, DoJoining):
        person.__init__(self, n, DoB)  # for super class
        self.DoJ = DoJoining


class studentMU(memberMU):
    def __init__(self, n, DoB, DoJoining, Major):
        memberMU.__init__(self, n, DoB, DoJoining)
        self.Major = Major

    def getMajor(self):
        return self.Major


ch = 1
listSt = {}
listStaff = {}
listVis = {}
while not ch == 0:
    print("1-Check-in student")
    print("2-Check-in staff")
    print("3-Check-in visitor")
    print("4-Display student")
    print("5-Display staff")
    print("6-Display visitor")
    print("7-Check-out student")
    print("8-Check-out staff")
    print("9-Check-out visitor")
    print("0-Exit")
    ch = int(input("Option: "))
    if ch == 1:
        n = input("Name:   ")
        dob = datetime.datetime.strptime(
            input("DoB(dd/mm/yyy):  "),  '%d/%m/%Y')
        doj = datetime.datetime.strptime(
            input("DoJ(dd/mm/yyy):  "),  '%d/%m/%Y')
        mjr = input("Major: ")
        tmpSt = studentMU(n, dob, doj, mjr)
        listSt[n] = tmpSt

    elif ch == 2:
        n = input("Name:   ")
        dob = datetime.datetime.strptime(
            input("DoB(dd/mm/yyy):  "),  '%d/%m/%Y')
        doj = datetime.datetime.strptime(
            input("DoJ(dd/mm/yyy):  "),  '%d/%m/%Y')
        tmpStaf = memberMU(n, dob, doj)
        listStaff[n] = tmpStaf

    elif ch == 3:
        n = input("Name:   ")
        dob = datetime.datetime.strptime(
            input("DoB(dd/mm/yyy):  "),  '%d/%m/%Y')

        tmpVis = person(n, dob)
        listVis[n] = tmpVis

    elif ch == 4:
        for i in listSt.keys():
            print("Name: ", listSt[i].getName(),
                  "DoB: ", listSt[i].getFormattedDate())

    elif ch == 5:
        for i in listStaff.keys():
            print("Name: ", listStaff[i].getName(),
                  "DoB: ", listStaff[i].getFormattedDate())
    elif ch == 6:
        for i in listVis.keys():
            print("Name: ", listVis[i].getName(),
                  "DoB: ", listVis[i].getFormattedDate())
    elif ch == 7:
        n = input("Name of the checkout student:   ")
        if n in listSt.keys():
            del listSt[n]
        else:
            print("Student " + n + " didn't do the check-in.")
    elif ch == 8:
        n = input("Name of the checkout Staff:   ")
        if n in listStaff.keys():
            del listStaff[n]
        else:
            print("Staff " + n + " didn't do the check-in.")
    elif ch == 9:
        n = input("Name of the checkout Visitor:   ")
        if n in listVis.keys():
            del listVis[n]
        else:
            print("Visitor " + n + " didn't do the check-in.")
    else:
        print("Number invalid, try again.")
print("END")
