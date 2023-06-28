class HashTable:
    def __init__(self):
        self.size = 10
        self.hashmap = [[] for _ in range(0, self.size)]
        print(self.hashmap)

    def hashing_function(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key

    def set(self, key, value):
        hash_key = self.hashing_function(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            slot[i] = ((key, value))
        else:
            slot.append((key, value))

    def get(self, key):
        hash_key = self.hashing_function(key)
        slot = self.hashmap[hash_key]
        for kv in slot:
            k, v = kv
            if key == k:
                return v
            else:
                raise KeyError("Does not exist")


h = HashTable()
h.set(10, 'value1')
h.set(20, 'value2')
h.set('key3', 'value3')
print(h.hashmap)
print(h.get(20))
# class MyHashMap:
#     def __init__(self, size):
#         # Define an array to store the hashmap
#         self.map = [None] * size
#         self.size = size

#     def hash(self, key):
#         return key % self.size

#     def put(self, key, value):
#         self.map[self.hash(key)] = value

#     def get(self, key):
#         return self.map[self.hash(key)]


# my_map = MyHashMap(10)
# my_map.put(2, "Hello")
# # print(my_map.get(2))
# # Get "Hello"
# my_map.put(14, "World")
# # print(my_map.get(2))
# print(my_map.map)
# # Get "World"
