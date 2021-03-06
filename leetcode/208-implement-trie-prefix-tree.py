class TrieNode:
    def __init__(self):
        self.is_end_of_word = False
        self.children = {} # Key is character, value is node itself


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    # Time: O(L) Where L is length of word we insert
    # Space: O(L)
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    # Time: O(L) Where L is length of word are searching for.
    # Space: O(1)
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_of_word

    # Time: O(L) Where L is length of word are searching for.
    # Space: O(1)
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)