"""
----------------------------------------------------
asgn09.py
Holds functions for assignment 9.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-03-22"
----------------------------------------------------
"""
from word import Word

def insert_words(file_variable, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a HashSet.
    -------------------------------------------------------
    Preconditions:
        file_variable - the already open file containing data to evaluate (file)
        hash_set - the HashSet to insert the words into (HashSet)
    Postconditions:
        Each Word object in hash_set contains the number of comparisons
        required to insert that Word object from file_variable into hash_set.
    -------------------------------------------------------
    """
    for line in file_variable:
        line = line.strip().split()
        for word in line:
            if word.isalpha():
                obj = Word(word.lower())
                hash_set.insert(obj)

def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    -------------------------------------------------------
    Preconditions:
        hash_set - a hash set of Word objects (HashSet)
    Postconditions:
        returns
        total - the total of all comparison fields in the HashSet
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total = 0
    max_word = Word("temp")
    for word in hash_set:
        total += word.comparisons
        if word.comparisons > max_word.comparisons:
            max_word = word
    return total, max_word
