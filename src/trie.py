class Trie:
    def __init__(self):
        self.head = Node("")

    def save(self, string):
        length = len(string)
        current = self.head

        current.getLength().append(length)

        for c in string: 
            next = current.nextNode(c)
            if next == None:
                next = Node(c)
                current.getNext()[c] = next
            
            next.getLength().append(length)
            current = next

class Node:
    def __init__(self, key):
        self.key = key
        self.next = {}
        self.length = []

    def nextNode(self, key):
        if key in self.next: 
            return self.next[key]

        return None

    def getLength(self):
        return self.length

    def getKey(self):
        return self.key

    def getNext(self):
        return self.next        

    