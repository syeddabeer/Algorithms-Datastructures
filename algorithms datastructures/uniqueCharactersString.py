#return the unique characters in a string

class uniqueCharacters:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        str_list = []
        str_string=""
        max_length = 0
        #for everycharacter in the string
        for x in s:
            if x in str_list:
                pass
            else:
                str_list.append(x)  # returns array of characters
                str_string+=x # returns string
                max_length = max(max_length, len(str_list))

        return max_length, str_list, str_string
    
a,b,c=uniqueCharacters().lengthOfLongestSubstring("abcabcbb")
print("Number of unique characters: ",a)
print("The unique characters: ",b)
print("The unique characters string: ",c)