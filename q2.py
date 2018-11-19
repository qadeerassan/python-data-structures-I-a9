"""
----------------------------------------------------
q2.py
Tests insert_words and comparison_total with 
hash_set_sorted.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-03-22"
----------------------------------------------------
"""
from asgn09 import insert_words, comparison_total
from hash_set_sorted import HashSet

file_variable = open("gibbon.txt", "r")
hash_set = HashSet(20)

insert_words(file_variable, hash_set)
total, max_word = comparison_total(hash_set)

print("Total Comparisons: {:,d}".format(total))
print("Word with maximum comparisons '{}': {:,d}".format(max_word.word, max_word.comparisons))