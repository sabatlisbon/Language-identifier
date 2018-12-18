import sys
import codecs
import string
import re
from collections import Counter
import nltk
from nltk import bigrams
from nltk import trigrams

#Build multiused definitions

# translator to remove punctuations - defined globally to avoid being complied each time
translator = str.maketrans('', '', string.punctuation)

# bleach_string removes symbols, puncuiations, numbers and double spacing
def bleach_string (input_string) :
    input_string = input_string.translate(translator) # remove punctuation
    input_string = re.sub(r'[^\w]', ' ', input_string) # Remove symbols and numbers
    input_string = re.sub(r'[0-9]|\n|\r', '', input_string) # Remove symbols and numbers
    input_string = input_string.strip() # remove trailing and leading spaces
    input_string = " ".join(input_string.split()) # remove double spaces
    return input_string

# get the string / readfile
with codecs.open('teste.txt', 'r', 'ISO8859-1') as file_object:
    lines = file_object.readlines()

ngrams1 = Counter()
ngrams2 = Counter()
ngrams3 = Counter()

for line in lines :
    #print("Original: " + line, end="")
    line = bleach_string(line)
    #print("Bleached: " + str(line))
    if line == '' :
        next # process next line

    for word in line.split(" ") : 
        # compute ngrams 1
        ngrams1 = ngrams1 + Counter(list(word))

        # compute grams 2
        ngrams2 = ngrams2 + Counter(bigrams(word))

        # compute grams 3
        ngrams3 = ngrams3 + Counter(trigrams(word))
    
#ngrams1[' '] = 0

# roll over the string feeding the hash table with histagram

# print("###########################################")
# print (ngrams1)
# print("###########################################")
# print (ngrams2)
# print("###########################################")
# print (ngrams3)
# print("###########################################")
# print("Resulting in the vector")


Final_Vector = ngrams1.most_common(300) + ngrams2.most_common(300) + ngrams3.most_common(300) 
b = {}
i=0
for item in Final_Vector :  
    index = ''.join(map(str,item[0]))
    #print (index)
    b[index] = Final_Vector[i][1]
    i += 1

Final_Vector = Counter(b)
Final_Vector = Final_Vector.most_common(300)
Output_Vector = []
i = 0
for ngram in Final_Vector :
    Output_Vector.append(ngram[0])
    i +=1

print (Output_Vector)
# how to Sort this by th number
# for i in range(0,len(Output_Vector)) : print(Output_Vector[i])
