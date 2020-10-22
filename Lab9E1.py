# %%
import datetime

# %%


class Person():
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def getName(self):
        return self.Name

    def getAge(self):
        return self.Age

    def birthday(self):
        return str(self.Name) + " is " + str(self.Age)


class Employee(Person):
    def __init__(self, Id, Name, Age):
        Person.__init__(self, Name, Age)
        self.Id = Id
        self.RateBase = 7.5
        self.RateBaseInc = 2.5
        self.YearBreakeven = 21

    def getRateBase(self):
        return self.RateBase

    def getRateBaseInc(self):
        return self.RateBaseInc

    def getYearBreakeven(self):
        return self.YearBreakeven

    def getId(self):
        return self.Id

    def setRateBase(self, RateBase: float):
        self.RateBase = float(RateBase)

    def setRateBaseInc(self, RateBaseInc: float):
        self.RateBaseInc = float(RateBaseInc)

    def setYearBreakeven(self, YearBreakeven: int):
        self.YearBreakeven = int(YearBreakeven)

    def calculate_pay(self):
        payment = 0.0
        if self.getAge() < self.YearBreakeven:
            payment = self.RateBase * self.getAge()
        else:
            payment = (self.RateBase + self.RateBaseInc) * self.getAge()
        return payment


class SalesPerson(Employee):
    def __init__(self, Region, SalesTotal, Id, Name, Age):
        Employee.__init__(self, Id, Name, Age)
        self.Region = Region
        self.SalesTotal = SalesTotal

    def getRegion(self):
        return self.Region

    def getSalesTotal(self):
        return self.SalesTotal

    def Bonus(self):
        return self.getSalesTotal() * 0.5


print("-----------------------------------------------------")
p = Person("Guilherme", 27)
print("Person")
print("Name", p.getName())
print("Age", p.getAge())


print(p.birthday())

print("-----------------------------------------------------")
e = Employee(1, "Rodrigo", 21)
print("Employee")
print("Name", e.getName())
print("Age", e.getAge())
print("Id:", e.getId())

print(e.birthday())
print("Your Pay:", e.calculate_pay())
e.setRateBase(8)
e.setRateBaseInc(3)
print("Your Pay:", e.calculate_pay())


print("-----------------------------------------------------")
s = SalesPerson("AUS", 30000, 2, "Phoebe", 21)
print("SalesPerson")
print("Name", s.getName())
print("Age", s.getAge())
print("Id:", s.getId())
print("Region:", s.getRegion())
print("SalesTotal:", s.getSalesTotal())

print(s.birthday())
print("Your Pay:", s.calculate_pay())
s.setRateBase(8)
s.setRateBaseInc(3)
print("Your Pay:", s.calculate_pay())
print("Bonus:", s.Bonus())
