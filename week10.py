# %%
import datetime

# %%


class Person():
    def __init__(self, DoB, Name):
        self.DoB = DoB
        self.Name = Name

    def getName(self):
        return self.Name

    def getDoB(self):
        return self.DoB


class NonMember(Person):
    def __init__(self, DoB, Name):
        Person.__init__(self, DoB, Name)


class MemberOfMU(Person):
    def __init__(self, Since, DoB, Name):
        Person.__init__(self, DoB, Name)
        self.Since = Since

    def getSince(self):
        return self.Since


class Staff(MemberOfMU):
    def __init__(self, Dept, Since, DoB, Name):
        MemberOfMU.__init__(self, since, DoB, Name)
        self.Dept = Dept

    def getDept(self):
        return self.Dept


class Student(MemberOfMU):
    def __init__(self, GPA, Since, DoB, Name):
        MemberOfMU.__init__(self, Since, DoB, Name)
        self.GPA = GPA

    def getGPA(self):
        return self.GPA


s = Student(123, datetime.date(2000, 1, 1),
            datetime.date(1983, 6, 9), "Rodrigo")
print("Name", s.getName())
print("GPA", s.getGPA())
print("Since:", s.getSince())
print("Day DOB: ", s.getDoB().day)
print("Month DOB: ", s.getDoB().month)
print("Year DOB: ", s.getDoB().year)

# %%

date_time_str = '29/06/2008'
date_time_obj = datetime.datetime.strptime(date_time_str, '%d/%m/%Y')
print(date_time_obj)
# print(          datetime.datetime.strptime("09/06/1983",  '%d/%m/%Y'))
print(date_time_obj.strftime('%d/%m/%Y'))
