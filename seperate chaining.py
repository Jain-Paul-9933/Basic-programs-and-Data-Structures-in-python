class Hash:
    def __init__(self):
        self.size = 10
        self.arr = [[] for i in range(self.size)]

    def hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        hash_value = h % self.size
        return hash_value

    def __setitem__(self, key, value):
        h = self.hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


hash = Hash()
hash['march 6'] = 130
hash['march 8'] = 50
hash['march 2'] = 50
hash['march 17'] = 120
print(hash['march 17'])
del hash['march 17']
print(hash.arr)
