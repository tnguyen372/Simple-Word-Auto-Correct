# Overview
A simple python program to practice NLTK and python which takes in a word from user input and checks if the word exists in the vocabulary bank. The vocabulary bank is
created by finding all the unique words in the NLTK brown subcorpus 'ca01' dataset. If the word does not exist in the bank, it will output the top 5 closest words to the user's input determined by Levenshtein distance as well as the probability of each word in the corpus.

# Libraries used
- NLTK
- Levenshtein Python C extension module
