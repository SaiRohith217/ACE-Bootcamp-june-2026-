my_list = []

for method in dir(my_list):
    if callable(getattr(my_list, method)):
        print(method)