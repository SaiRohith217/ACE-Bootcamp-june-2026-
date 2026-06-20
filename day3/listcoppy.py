'''import copy
list = [
    [18,66],
    [53,12],
    [14,15]
]
list1= copy.copy(list)
list1[0][0]= 100
list2 = copy.deepcopy(list)
print("Original list:", list)
print("Shallow copy:", list1)


list2[0][0]= 20
print("Deep copy:", list2)'''


list3 = [[0]*3 for _ in range(3)]

list3[0][0]= 5
print("List3:", list3)

