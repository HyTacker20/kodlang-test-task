my_list = [4, 0, 5, 0, 3, 0, 0, 5]

print(my_list)
print("List lenght - " + str(len(my_list)))

for n in my_list:
    if n == 0:
        my_list.append(n)
        my_list.remove(n)

print(my_list)
print("List lenght - " + str(len(my_list)))