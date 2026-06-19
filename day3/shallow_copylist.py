my_list = [1, 2, 3, 4, 5]
shallow_list = my_list.copy()  
shallow_list[3] = 56
print("Original list:", my_list)
print("Shallow copy:", shallow_list)
