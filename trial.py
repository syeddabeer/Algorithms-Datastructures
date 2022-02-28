from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand, groupSize):
        hand.sort()
        n=len(hand)
        frequency=defaultdict(int)

        for i in hand:
            frequency[i] = frequency.get(i,0)+1

            # {1:1, 2:2, 3:2, 4:1, 6:1, 7:1, 8:1}

        for i in range(n):
            if frequency[hand[i]]!=0:
                for j in range(hand[i], hand[i]+groupSize):
                    if frequency[j]==0:
                        return False
                    frequency-=1
        return True
        

"""
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.
"""