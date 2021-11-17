# keyword Recommendations without trie
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        list_ = []
        products.sort()
        for i, c in enumerate(searchWord):
            products = list(filter(lambda p: p[i] == c if len(p) > i else False, products))
            # products = [p for p in products if len(p) > i and p[i]==c ]
            list_.append(products[:3])
        return list_