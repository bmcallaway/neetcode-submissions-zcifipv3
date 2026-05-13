class Node:
    def __init__(self, key, val):
        self.prev: Node | None = None
        self.next: Node | None = None
        self.key = key
        self.val = val
        self.counter = 1
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodes = {}
        self.freqs = {}
        self.minFreq = 0
        left, right = Node(0, 0), Node(0, 0)
        left.next, right.prev = right, left
        self.freqs[1] = (left, right)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self.updateFreqs(node) 
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self.updateFreqs(node)
        else:
            node = Node(key, value)
            if len(self.nodes) == self.cap:
                self.removeLFU()
            self.add(node)
    
    def updateFreqs(self, node):
        left, right = self.freqs[self.minFreq]
        if node.prev == left and node.next == right:
            self.minFreq += 1
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        node.counter += 1
        if node.counter not in self.freqs:
            left, right = Node(0, 0), Node(0, 0)
            left.next, right.prev = right, left
            self.freqs[node.counter] = (left, right)
        right = self.freqs[node.counter][1]
        prev = right.prev
        prev.next, node.prev = node, prev
        node.next, right.prev = right, node

    def removeLFU(self):
        left, right = self.freqs[self.minFreq]
        removing = left.next
        left.next = removing.next
        removing.next.prev = left
        del self.nodes[removing.key]

    def add(self, node): #adds new node to nodes and freqs[1] right side of list
        self.minFreq = 1
        self.nodes[node.key] = node
        right = self.freqs[1][1]
        prev = right.prev
        prev.next = node
        node.prev = prev
        node.next = right
        right.prev = node
    

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)