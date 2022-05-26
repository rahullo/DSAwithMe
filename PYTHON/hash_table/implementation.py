class Hash_table():
    def __init__(self, size):
        self.size = size
        self.data = [None]*self.size

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash+ord(key[i]) * i) % self.size
        return hash

    def set(self, key, value): 
        hash = self._hash(key) 
        print(hash)
        if not self.data[hash]: 
            self.data[hash] = [[key,value]]
        else: 
            self.data[hash].append([key, value])

    def get(self, key):
        hash = self._hash(key)
        return self.data[hash]
        

    

new_hash = Hash_table(100)
print(new_hash._hash('rahul'))
print(new_hash._hash('lohra'))
new_hash.set('one', 1)
new_hash.set('two', 2)
new_hash.set('three', 3)
new_hash.set('four', 4)

print(new_hash)

print(new_hash.get('two'))


