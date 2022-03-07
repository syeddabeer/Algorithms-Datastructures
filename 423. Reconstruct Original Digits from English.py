class Solution:
	def originalDigits(self, s):
		# building hashmap letter -> its frequency
        count = collections.Counter(s)
        
        # building hashmap digit -> its frequency 
        out = {}
        # letter "z" is present only in "zero"
        out["0"] = count["z"]
        # letter "w" is present only in "two"
        out["2"] = count["w"]
        # letter "u" is present only in "four"
        out["4"] = count["u"]
        # letter "x" is present only in "six"
        out["6"] = count["x"]
        # letter "g" is present only in "eight"
        out["8"] = count["g"]
        # letter "h" is present only in "three" and "eight"
        out["3"] = count["h"] - out["8"]     # count("h") - count("g")
        # letter "f" is present only in "five" and "four"
        out["5"] = count["f"] - out["4"]
        # letter "s" is present only in "seven" and "six"
        out["7"] = count["s"] - out["6"]
        # letter "i" is present in "nine", "five", "six", and "eight"
        out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
        # letter "n" is present in "one", "nine", and "seven"
        out["1"] = count["n"] - out["7"] - 2 * out["9"]

        # building output string
        output = [key * out[key] for key in sorted(out.keys())]
        return "".join(output)



"""
Logic:
Hence the idea is to look for something unique. One could notice that all even numbers contain each a unique letter :
Letter "z" is present only in "zero".
Letter "w" is present only in "two".
Letter "u" is present only in "four".
Letter "x" is present only in "six".
Letter "g" is present only in "eight".
Hence there is a good way to count even numbers.
That is actually the key how to count 3s, 5s and 7s since some letters are present only in one odd and one even number (and all even numbers has already been counted) :
Letter "h" is present only in "three" and "eight".
Letter "f" is present only in "five" and "four".
Letter "s" is present only in "seven" and "six".
Now one needs to count 9s and 1s only, and the logic is basically the same :
Letter "i" is present in "nine", "five", "six", and "eight".
Letter "n" is present in "one", "seven", and "nine".
"""

"""
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.
Example 1:
Input: s = "owoztneoer"
Output: "012"
Example 2:
Input: s = "fviefuro"
Output: "45"

"""