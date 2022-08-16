import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src.trie import Trie, Node

class TrieTests(unittest.TestCase):

    def test_save(self):
        trie = Trie()

        string = "emadam"
        trie.save(string)
        
        node = trie.head
        self.assertEqual(node.getKey(), "")
        
        for char in string:
            node = node.nextNode(char)
            self.assertEqual(node.getKey(), char)
            self.assertEqual(node.getLength(), [6])
        
        string = "eme"
        trie.save(string)

        node = trie.head

        for index, char in enumerate(string):
            node = node.nextNode(char)
            self.assertEqual(node.getKey(), char)
            
            if index >= 2: self.assertEqual(node.getLength(), [3])
            else: self.assertEqual(node.getLength(), [6,3])
    
    def test_save(self):
        trie = Trie()

        string = "emadam"
        trie.save(string)

        string = "eme"
        trie.save(string)
        
        find_node = trie.find("emadam")
        self.assertEqual(find_node.getLength(), [6])
        self.assertEqual(find_node.getKey(), "m")
        self.assertEqual(find_node.getNext(), {})

        find_node = trie.find("emadw")
        self.assertIsNone(find_node)

if __name__ == '__main__':
    unittest.main()