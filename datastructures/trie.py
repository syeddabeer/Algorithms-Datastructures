class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word):
        node=self.root #initialize node iterator
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode() #insert char by char
            node=node.children[char]   #increment
        node.isEnd=True
        
    
    def search(self, word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]  #iterate when prior char is found in the trie
        return node.isEnd              # returns True if arrived at end
    
    def startsWith(self, prefix):
        node=self.root
        for char in prefix:
            if char not in node.children:
                return False
            node=node.children[char]
        return True
    
    def delete(self, word):
        def recursive(node, word, i):
            if i==len(word):
                if not node.isEnd: # word is not in trie
                    return False 
                node.isEnd=False # delete word via changing isEnd be False
                return len(node.children)==0
                
            if word[i] not in node.children: # word is not in trie
                return False
                
            need_delete = recursive(node.children[word[i]], word, i + 1)   #to iterate forward node.children[word[i]]
            
            if need_delete:
                node.children.pop(word[i])
                return len(node.children)==0
                
            return False
            
        recursive(self.root, word, 0)
  