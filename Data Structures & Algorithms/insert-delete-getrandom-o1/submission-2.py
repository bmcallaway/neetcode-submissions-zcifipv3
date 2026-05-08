class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.numMap[val] = len(self.numMap)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False 
        idx = self.numMap[val]
        lastIdx = len(self.values) - 1
        lastVal = self.values[lastIdx]
        self.numMap[lastVal] =  idx
        del self.numMap[val]
        self.values[idx], self.values[lastIdx] = self.values[lastIdx], self.values[idx]
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()