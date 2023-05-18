class Adapter:
    def __init__(self, array):
        self.dictionary = {}
        for row in array:
            key = row[0]
            values = row[1:]
            self.dictionary[key] = values
array = [
    ["key1", "value1_1", "value1_2"],
    ["key2", "value2_1", "value2_2"],
    ["key3", "value3_1", "value3_2"]
]
adapter = Adapter(array)
dictionary = adapter.dictionary
print(dictionary)

