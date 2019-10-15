class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        from collections import defaultdict

        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = '.'

        for word in strs:
            t = trie
            for c in word:
                t = t[c]
            t = t[END]

        result = ''
        while len(trie) == 1:
            k, v = list(trie.items())[0]
            if k != END:
                result += k
            trie = trie[k]
        return result