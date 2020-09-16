"""
1. Given a sorted List, remove the duplicates in-place such that each
element appears only once and return the new length.
Example 1:
Given List1 = [1, 1, 2],
Your function should return length = 2, with the first two elements of
List1 being 1 and 2 respectively.
Example 2:
Given List2 = [0, 0,1, 1, 1, 2, 2, 3, 3, 4],
Your function should return length = 5, with the first five elements of
List2 being modified to 0, 1, 2, 3, and 4 respectively
"""

v = input("Type a list of values separated by space: ")
L = v.split()
Ln = []
for i in L:
    if (i not in Ln):
        Ln.append(i)
#print(Ln)
print ("lenght =", len(Ln))