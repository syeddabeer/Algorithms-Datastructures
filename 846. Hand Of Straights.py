from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand, groupSize):
        hand.sort()
        n = len(hand)
        frequency = defaultdict(int)
        # count the frequency of each card
        for i in hand:
            frequency[i] = frequency.get(i,0) + 1
            
        #iterate the number of times = number of numbers in hand
        for i in range(n):
            if frequency[hand[i]]!=0:
                for j in range(hand[i], hand[i]+groupSize):
                    if frequency[j]==0:
                        return False
                    frequency[j] -= 1
        return True