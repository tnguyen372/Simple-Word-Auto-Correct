from nltk.corpus import brown
from Levenshtein import distance as lev
import operator
## 
# For the purpose of this program, I considered a word to be a string of characters separated by whitespace.
# Even if the word contained punctuation, that entire string of characters would be considered a word until it
# was separated by whitespace character to denote a new word.
#
# In the future, I will implement a regexes for added complexity to discard punctuation and not consider strings containing 
# punctuation as one word. Right now, this will serve as an exercise to get accustomed to using nltk and python in general.
##

# Get a corpus from the brown corpus group. In this case I chose the first one (ca01)
brown_corpus = brown.words('ca01')
# Determine the total number of words in the brown corpus
total_num_words = len(brown_corpus)

# Find all unique words in the brown corpus and store it in a set
unique_words = set(brown_corpus)

# Use the set of unique words to build up a vocabulary dictionary containing word and word probability key value pairs
vocabulary = {}
for word in unique_words:
  # Determine the frequency of each vocabulary word
  frequency = brown_corpus.count(word)

  # Determine the relative frequency (probability) of the word and store the word and its probability as key value pair in a dictionary
  word_probability = frequency / total_num_words
  vocabulary[word] = word_probability

# Get user input to check if it exists in the vocabulary
user_word = input("Enter a word: ")
# If user input exists in the vocabulary dictionary, display to user that their word is a valid word
if vocabulary.get(user_word, -1) != -1:
  print(user_word, "is a complete and correct word in English.")
# Otherwise find the similarity between user input and each vocabulary word based on Levenshtein distance
else:
  # Store each vocabulary word and its levenshtein distance as key value pairs in another dictionary
  min_edit_dist_dict = {}
  for word_to_compare in vocabulary:
    min_edit_distance = lev(word_to_compare, user_word)
    # If the minimum edit distance is 5 or less store it into the min edit distance dictionary
    # Don't bother storing words with minimum edit distance of 6 or higher to reduce number of computations
    if (min_edit_distance < 6):
      min_edit_dist_dict[word_to_compare] = min_edit_distance
  
  # Sort the min edit dist dictionary by ascending order then grab the first 5 values to display as output
  sorted_dist_dictionary = dict(sorted(min_edit_dist_dict.items(), key=operator.itemgetter(1)))
  closest_words_list = list(sorted_dist_dictionary.keys())[:5]
  
  # Print the closest 5 words to the user input determined by Levenshtein distance and their respective probability
  print(user_word, "is not a recognized word. Did you mean to type in one of these words?")
  for i in range(5):
    closest_word = closest_words_list[i]
    print(i + 1, ".", closest_word, "- Probability:", vocabulary.get(closest_word))
    
