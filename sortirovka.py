def sort(array):
    sorted_array = []
    for i in range(len(array)):
        for j in range(i):
            if array[j] > array[j+1]:
                sorted_array.append(array[j])
                sorted_array.append(array[j+1])
                if j == len(array)-2: break
            else: break
    return sorted_array
