# main_with_json.py
import json

with open('config.json', 'r') as f:
    config = json.load(f)

ngrams_num  = config['DEFAULT']['NUM_OF_NGRAMS'] # read the number of ngrams

# should make the following code generic for variable number of languages
lang1_vect_file = config['DEFAULT']["LANGUAGE1_VECTOR_FILE"]
lang1_descriptiion = config['DEFAULT']["LANGUAGE1_DESCRIPTION"]
lang1_suffix = config['DEFAULT']["LANGUAGE1_SUFFIX"]
