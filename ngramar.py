import sys
import codecs
import re

# get the string / readfile

contents = ""
with codecs.open('teste.txt', 'r', 'utf-8') as file_object:
    contents = file_object.read()

pattern = re.compile('([^\s\w]|_)+')
clean_contents = pattern.sub('', contents)
clean_contents = re.sub("\d+", "", clean_contents)
clean_contents = re.sub("[\t ]+", " ", clean_contents)
clean_contents = re.sub("\n+", "\n", clean_contents)

print(clean_contents)

# Clean the file (get rid of the pontuations and numbers, and of double spasing )

# create the file rollers

# Doubt should I normalize the string before o during rolling

# eliminate double spacing

# roll over the string feeding the hash table with histagram



# return vector