class FixedSizeList:
    items = []
    max_size = 5

    def __init__(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
        else:
            self.items.pop(0)
            self.items.append(item)

    @classmethod
    def get_items(cls):
        return cls.items
a = FixedSizeList('a')
b = FixedSizeList('b')
c = FixedSizeList('c')
d = FixedSizeList('d')
e = FixedSizeList('e')
f = FixedSizeList('f')
print(FixedSizeList.get_items()) # [b, c, d, e, f]
