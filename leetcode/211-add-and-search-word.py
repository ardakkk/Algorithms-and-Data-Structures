class WordNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = WordNode()
    # Time: O(L) Where L is length of word we are inserting
    # Space: O(L)
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = WordNode()
            node = node.children[char]

        node.is_end_of_word = True

    # Time: O(N) Where N is total number of Trie Nodes. This can happen if we receive a word that is all dots like "........."
    # Space: O(1)
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        self.res = False
        self.dfs(self.root, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.is_end_of_word:
                self.res = True
            return

        next_char = word[0]
        if next_char == ".":
            for child in node.children.values():
                self.dfs(child, word[1:])
        else:
            if next_char in node.children:
                self.dfs(node.children[next_char], word[1:])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)