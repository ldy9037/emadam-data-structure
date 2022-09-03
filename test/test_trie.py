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
        self.assertEqual(node.key(), "")
        
        for char in string:
            node = node.nextNode(char)
            self.assertEqual(node.key, char)
            self.assertEqual(node.length, [6])
        
        string = "eme"
        trie.save(string)

        node = trie.head

        for index, char in enumerate(string):
            node = node.nextNode(char)
            self.assertEqual(node.key(), char)
            
            if index >= 2: self.assertEqual(node.length, [3])
            else: self.assertEqual(node.length, [6,3])
    
    def test_save(self):
        trie = Trie()

        string = "emadam"
        trie.save(string)

        string = "eme"
        trie.save(string)
        
        find_node = trie.find("emadam")
        self.assertEqual(find_node.length, [6])
        self.assertEqual(find_node.key, "m")
        self.assertEqual(find_node.next, {})

        find_node = trie.find("emadw")
        self.assertIsNone(find_node)

if __name__ == '__main__':
    unittest.main()