class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]
        
    def hash_function(self, key):
        return hash(key) % self.size
    
    def set_value(self, key, value):
        index = self.hash_function(key)
        found = False
        for i, kv in enumerate(self.buckets[index]):
            k, v = kv
            if key == k:
                self.buckets[index][i] = (key, value)
                found = True
                break
        if not found:
            self.buckets[index].append((key, value))
    
    def get_value(self, key):
        index = self.hash_function(key)
        for k, v in self.buckets[index]:
            if key == k:
                return v
        return None
    
    def print_table(self):
        i = 0
        while i < len(self.buckets):
            print(self.buckets[i])
            i += 1
    
hTable = HashTable(10)
    
hTable.set_value(1, 10)
hTable.set_value(11, 5)

hTable.set_value(2, 8)

hTable.print_table()
