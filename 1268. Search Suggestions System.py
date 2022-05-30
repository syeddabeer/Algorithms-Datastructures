#1268. Search Suggestions System

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True 
    
        
    def startingWith(self,prefix):
        node = self.root
        res = []
        for char in prefix:
            if char not in node.children:
                return res
            node = node.children[char]
        res = self.getWords(res,node,prefix)
        return res
        
    def getWords(self,res,node,prefix):
        if len(res) == 3:
            return res
        
        if node.isEnd == True:
            res.append(prefix)
            
        for child in node.children.keys():
           
            self.getWords(res,node.children[child],prefix + child )
        return res
                
          
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
     
        finalres = []
        t = Trie()
        
        for product in sorted(products):
            t.insert(product)
            
        for i in range(1,len(searchWord)+1):
            search = searchWord[0:i]
            finalres.append(t.startingWith(search))

        return finalres


"""
1268. Search Suggestions System
Medium

2321

139

Add to List

Share
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
 

Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
"""