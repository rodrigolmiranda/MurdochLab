# %%

import random


class square:
    def __init__(self, a):
        self.side = a

    def getArea(self):
        return self.side**2

    def __lt__(self, other):
        print("a")
        return self.side < other.side


print(1)
s1 = square(14)
print(2)
s2 = square(5)
print(3)
print(s1.getArea())
print(4)
print(s1 < s2)
print(5)
