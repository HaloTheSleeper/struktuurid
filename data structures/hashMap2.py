class HashTable():
    def __init__(self, size) -> None:
        self.size = size
        self.buckets = [[] for _ in range(self.size)]
        
    def hash_key(self, key):
        return hash(key) % self.size
        
    def set_value(self, key, value):
        hash = self.hash_key(key)
        
        found = False
        for i, kv in enumerate(self.buckets[hash]):
            k, v = kv
            
            if k == key:
                self.buckets[hash][i] = (key, value)
                found = True 
                break
        
        if not found:
            self.buckets[hash].append((key, value))
            
    def print_table(self):
        print(self.buckets)

    
hTable = HashTable(10)
    
hTable.set_value("Kaidi", 48)
hTable.set_value("Arti", 18)
hTable.set_value("Arti", 30)
hTable.set_value("Jaanus", 19)

hTable.print_table()
