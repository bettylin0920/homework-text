import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
import string
string.punctuation = string.punctuation
# you can add one at a time
# filter out symbols (isalpha, isdigit, isalnum)
for symbol in string.punctuation:
    stopwords.add(symbol)
    stopwords.add("``")
    stopwords.add("''")
    stopwords.add("'s")
    stopwords.add("'ve")
    stopwords.add("n't")
    stopwords.add("'re")
    stopwords.add(",")
    stopwords.add("--")
    stopwords.add("'ll")
    stopwords.update(string.punctuation)
import csv

# or update a sequence into the set

# write your code here

#read sentences from file "Building_Global_Community.txt"
# normalize words (\'Word\' and \'word\' are considered as the same word)
text = open('building_global_community.txt').read().lower()
lines = [line.strip() for line in text.splitlines()]


list_length = len(lines) # Set this to the length of lines
# split sentences into words (split, or nltk word_tokenize from nltk)
from nltk import word_tokenize
for i in range(0,list_length):
    lines[i] = word_tokenize(lines[i])



#print (lines)  檢查


#filter out stopwords (stopwords from nltk)
len = []
for i in range(0,list_length):
    len = len + lines[i]
    #print (lowers.split(' '))  for test
    #print (words)  for test



#count the occurance of words (Counter)
from collections import Counter
data=[]
data=[word for word in len if word not in stopwords]


counter = Counter(data)
counter = counter.most_common()

print (counter)

with open('wordcounttest.csv', 'w') as csvfile:
    # set up header
    fieldnames = ['word', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for word, count in counter:
        writer.writerow({'word': word, 'count': count})
