class Trie:
    def __init__(self):
        self.head = Node("")

class Node:
    def __init__(self, key):
        self.key = key
        self.next = {}
        self.length = []

    def next(self, key):
        if key in self.next: 
            return self.next[key]

        return None
    
    