# Input: words = ["apple","pleas","please"], 
# puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
# Output: [0,1,3,2,0]
class Solution:
	def findNumOfValidWords(self, words, puzzles):
		SIZE = 26
		trie = [[0]*SIZE]
		count = [0]
		for word in words:
			word = sorted(set(word))
			if len(word) <= 7:
				node = 0
				for letter in word:
					i = ord(letter) - ord('a')
					if trie[node][i] == 0:
						trie.append([0]*SIZE)
						count.append(0)
						trie[node][i] = len(trie) - 1
					node = trie[node][i]
				count[node] += 1

		# search for valid words
		def dfs(node, has_first):
			total = count[node] if has_first else 0
			for letter in puzzle:
				i = ord(letter) - ord('a')
				if trie[node][i]:
					total+=dfs(trie[node][i], has_first or letter == puzzle[0])
			return total

		result=[]
		for puzzle in puzzles:
			result.append(dfs(0, False))
		return result


from collections import defaultdict

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        n = len(words)
        m = len(puzzles)
        
        freq = defaultdict(int)   # Hash the words in this dictionary
        
        for w in words:
            freq[tuple(sorted(list(set(w))))] += 1
        
        ans = [0]*m
        
        for i, w in enumerate(puzzles):
            puzzleSet = list(w)
			# Try all subsets of puzzles[i] because 2nd condition in question is word should be subset of puzzle
            for x in range(1 << (len(puzzleSet)-1)):  # Using the fact that length of puzzles[i] is 7 --> 64 iterations (2^6)
                puzzleSubSet = [w[0]]   # First letter should be included in the subset of puzzles[i]
                for c in puzzleSet[1:]:  # --> 6 iterations
                    if x & 1:    # Select the characters whose bit is set to 1
                        puzzleSubSet.append(c)
                    x = x >> 1  # Divide x by 2
                ans[i] += freq[tuple(sorted(puzzleSubSet))]   # Add answer of that subset for puzzles[i]
        return ans
# With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
# word contains the first letter of puzzle.
# For each letter in word, that letter is in puzzle.
# For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage", while
# invalid words are "beefed" (does not include 'a') and "based" (includes 's' which is not in the puzzle).
# Return an array answer, where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i].