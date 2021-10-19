"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""
class Solution:
    def fullJustify(self, words, maxWidth):
        answer=[]
        w_iter, w_break=0, 0
        curlen = 0
        self.words=words
        
        while w_break<len(words):
            curlen += len(words[w_break])
            
            if curlen >= maxWidth:
                if curlen > maxWidth:
                    curlen -= (len(words[w_break]) + 1)
                    w_break -= 1
                
                answer.append(self.addWordsToResult(w_iter, w_break, 0 if w_break==len(words)-1 else (maxWidth-curlen)))
                curlen=0
                w_iter, w_break=w_break+1, w_break+1
                
            elif curlen<maxWidth:
                # considers one space after every word.
                curlen += 1
                
                #considers next word
                w_break += 1
        
        # this happens for the last line.
        # last line w_break is more than list length to come out of loop. index should be -1'd for accurate performance
        
        if curlen > 0:
            answer.append(self.addWordsToResult(w_iter, w_break-1, 0))
        
        last = answer[-1]
        extra= maxWidth - len(last)
        answer[-1] = last + (' '*extra)
        return answer
            
        
    def addWordsToResult(self, w_iter, w_break, sp_per_line):
        resultText=''
        # for last line, sp per line is zero. to overcome, we added statements involving -1 index.
        if w_iter==w_break:
            resultText += self.words[w_break] + (' '*sp_per_line)
            return resultText
        places=w_break-w_iter
        print(places)
        word_spacing, remaining = 1 + sp_per_line//places, sp_per_line%places
        while w_iter<=w_break: 
            resultText += self.words[w_iter]
            if w_iter < w_break:
                resultText += (' '*word_spacing)
            
            if remaining>0:
                resultText += ' '
                remaining -= 1
            
            w_iter += 1
        return resultText
            
prices1=["This", "is", "an", "example", "of", "text", "justification."]
print(Solution().fullJustify(prices1, 16))



