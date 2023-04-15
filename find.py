my_array = [1, 2, 3, 4, 5]
my_search_item = 4

for i in range(len(my_array)):
    if my_array[i] == my_search_item:
        print("Element found at position", i, ":", my_array[i])
        break
else:
    print("Element not found")


