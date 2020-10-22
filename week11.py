# %%

def selection_sort(L):
    L2 = {}
    for k, v in list(L.items()):
        current_min = k
        value_min = v
        for k2, v2 in list(L.items())[1:]:
            if current_min > k2:
                current_min = k2
                value_min = v2
        # print(current_min)
        # L2[current_min] = value_min
        # L.pop(current_min)

        keys_list[i], keys_list[current_min] = keys_list[current_min], keys_list[i]
        # L2[keys_list[i]] = L[keys_list[i]]
    return L2


# L=[5,23,65,34,554,76,-45,65,62,664,3,0,323,54,5]
# print(selection_sort(L))


persons = {"Rodrigo": 37, "Marisa": 39, "Guilherme": 7, "Leonardo": 40,
           "Fernanda": 38, "Lauro": 63, "Valdeci": 66, "Matheus": 6, "Marcos": 40, "Tony": 28}
print(selection_sort(persons))

# %%
a_dictionary = {"a": 1, "b": 2, "c": 3}
keys_list = list(a_dictionary)
print(keys_list)
key = keys_list[1]
print(key)


# %%
L = [5, 23, 65, 34, 554, 76, -45, 65, 62, 664, 3, 0, 323, 54, 5]
print(L.sort())

# %%
# Selection sort


def selection_sort(L):
    N = len(L)
    for i in range(N):
        current_min = i
        for j in range(i + 1, N):
            if L[current_min] > L[j]:
                current_min = j  # updates current_min
        L[i], L[current_min] = L[current_min], L[i]
    return L


L = [5, 23, 65, 34, 554, 76, -45, 65, 62, 664, 3, 0, 323, 54, 5]
print(selection_sort(L))

# %%
# import collections

# d = {2:3, 1:89, 4:5, 3:0}

# Lordered = collections.OrderedDict(sorted(d.items()))


def selection_sort(L):
    keys_list = list(L)
    N = len(keys_list)
    L2 = {}
    for i in range(N):
        current_min = i
        for j in range(i + 1, N):
            if keys_list[current_min] > keys_list[j]:
                current_min = j  # updates current_min
        # print(current_min, keys_list[current_min])
        keys_list[i], keys_list[current_min] = keys_list[current_min], keys_list[i]
        # print(i, keys_list[i])
        L2[keys_list[i]] = L[keys_list[i]]
    return L2


# L=[5,23,65,34,554,76,-45,65,62,664,3,0,323,54,5]
# print(selection_sort(L))


persons = {"Rodrigo": 37, "Marisa": 39, "Guilherme": 7, "Leonardo": 40,
           "Fernanda": 38, "Lauro": 63, "Valdeci": 66, "Matheus": 6, "Marcos": 40, "Tony": 28}
print(selection_sort(persons))

# %%


def sort_dict(dic, sortbyK=True):
    dic_ret = {}
    # sortbyK = False
    while len(dic) > 0:

        k, v = list(dic.items())[0]
        k_min = k
        v_min = v
        dic.pop(k)
        dic2 = dic.copy()

        while len(dic2) > 0:
            k2, v2 = list(dic2.items())[0]
            dic2.pop(k2)
            if sortbyK:
                if k_min > k2:
                    k_min = k2
                    v_min = v2
            else:
                if v_min > v2:
                    k_min = k2
                    v_min = v2
        dic_ret[k_min] = v_min
        if k != k_min:
            dic[k] = v
    return dic_ret


dic = {"Rodrigo": 37, "Marisa": 39, "Guilherme": 7, "Leonardo": 40,
       "Fernanda": 38, "Lauro": 63, "Valdeci": 66, "Matheus": 6, "Marcos": 40, "Tony": 28}

print(sort_dict(dic, False))
