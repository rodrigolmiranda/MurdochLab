
"""
#def swap(x,y):
T=((10,'Q1'), (20,'Q2'), (50,'Q3'))
for i in T:
    print(i[1])
def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)

    return (min_n, max_n, unique_words)

print(get_data(((10,'Q1'), (20,'Q2'), (50,'Q3'))))


Write a Python program to find the second smallest number in a list



"""

#L = [6,3,2,6,3]
L = list(map(int, input("Enter the list numbers separated by space ").strip().split()))

Ln = []
for i in L:
    if (i not in Ln):
        Ln.append(i)
Ln.sort()
print(Ln[1])
