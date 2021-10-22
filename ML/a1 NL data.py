import re
import collections

def process(line):
	print(line)

f = open("natural-language-data.txt")
for line in f:
	#process(line)
	pass

# multiprocessing
# import multiprocessing as mp
# pool = mp.Pool(2)
# jobs = []

# f = open("natural-language-data.txt")
# for line in f:
# 	jobs.append(
# 		pool.apply_async(process, (line))) #process - func, arg is line


# for job in jobs:
# 	job.get()

# pool.close()

# # 1.3 Split the text into individual words with regular expression
corpus = ("Andy is a data scientist. Andy's boss, Megan, was looking for him, but Andy was out to lunch. Megan texted Andy, How's the deadline coming along?'")
# Simply splitting the sentence with spaces
print("corpus.split(): ", corpus.split())

# Taking out punctuation
punctuation = ".',?"  # what is the universe of punctuation? How do we handle 's?
for p in punctuation:
    corpus = corpus.replace(p, '')

# print(corpus.split())

# Regex
word_regex = r'\W+'  # a raw str: one or more (+) non-word characters (\W) r'\W+'
# corpus.split()
# re.split(word_regex, corpus)

split_corpus = re.split(word_regex, corpus)
# print(split_corpus)

# a better regex
# word character + zero or more word characters or 's + word character
# OR
# just a word character
# import re
# \w - small -> word
word_regex_improved = r"(\w[\w']*\w|\w)"
word_matcher = re.compile(word_regex_improved)
# print(word_matcher.findall(corpus))


# 1.4 Converting words into lists of lower case tokens

def split_into_words(line):
    word_regex_improved = r"(\w[\w']*\w|\w)"
    word_matcher = re.compile(word_regex_improved)
    return word_matcher.findall(line)

processed_corpus = []

with open("natural-language-data.txt") as f:
    # to handle large text files, we use the file as an iterator
    for line in f:
        processed_corpus.extend(split_into_words(line))

processed_corpus = [w.lower() for w in processed_corpus]


print(processed_corpus)


# # 1.5 Removing uncommon words and stop words

# Before stop word removal
word_counts = collections.Counter(processed_corpus)
print(word_counts)

# Define some stop words
stop_words = {
    'ourselves', 'hers', 'between', 'yourself', 'but', 'again',
    'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they',
    'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into',
    'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as',
    'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we',
    'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more',
    'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above',
    'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any',
    'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does',
    'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can',
    'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where',
    'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't',
    'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how',
    'further', 'was', 'here', 'than'}

# find least common elements
uncommon_words = word_counts.most_common()[:-10:-1]
# [w for w in processed_corpus if not in stop_words]
# [w for w in processed_corpus if not in uncommon_words]

processed_corpus = [w for w in processed_corpus if w not in stop_words]
processed_corpus = [w for w in processed_corpus if w not in uncommon_words]
print(processed_corpus)