class Trie:
    def __init__(self):
        self.head = Node("")

    def save(self, string: str):
        length: int = len(string)
        current: Node = self.head

        current.length.append(length)

        for c in string: 
            next = current.nextNode(c)
            if next == None:
                next = Node(c)
                current.next[c] = next
            
            next.length.append(length)
            current = next
        
    def find(self, string):
        current = self.head
        for c in string:
            if current == None: break
            current = current.nextNode(c)
            
        return current

class Node:
    def __init__(self, key):
        self.key = key
        self.next = {}
        self.length = []

    def nextNode(self, key):
        if key in self.next: 
            return self.next[key]

        return None        

    