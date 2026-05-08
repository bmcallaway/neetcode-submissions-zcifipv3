class RandomizedSet:

    def __init__(self):
        self.vals = set()


    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        self.vals.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vals:
            return False
        self.vals.remove(val)
        return True

    def getRandom(self) -> int:
        newList = list(self.vals)
        idx = random.randint(0, len(self.vals) - 1)
        return newList[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()