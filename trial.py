class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False


class Trie:
    def __init__(self):
        self.root=TrieNode()



    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        self.isEnd=True


    def search(self, word):
        node=self.root 
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.isEnd


    def startsWith(self, prefix):
        node=self.root 
        for char in word:
            if char not in node.children:
                return False 
            node=node.children[char]
        return True


    def delete(self, word):

        def recursive(node, word, i):

            if len(word)==i:
                if not node.isEnd:
                    return False
                node.isEnd=False
                return len(node.children)==0

            if word[i] not in node.children:
                return False

            need_delete = recursive(node.children[word[i]], word, i+1)

            if need_delete:
                node.children.pop(word[i])
                return len(node.children)==0

            return False

        recursive(root, word, 0)