# ShockingRotom 2021
# Parses strings from files and compares searching algorithms

import re
import time


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# Creates list with given file
def create_list(file):
    # Makes a list of all the lines in the given file
    with open(file) as f:
        line_list = f.readlines()
    word_list = []
    # Separates the lines into words creating a new list with all the words
    for i in line_list:
        word_list += (split_line(i))
    return word_list


# Function for linear search
def linear_search(file, list):
    # Gets the starting time to calculate the time it takes to complete this search
    start_time = time.time()
    print(" ")
    print("--- Linear search ---")
    print(" ")
    # Creates a var to keep track of the line number
    line_num = 0
    # Loops through all the lines in the given file
    for lines in open(file).readlines():
        # Adds to the line number each loop
        line_num += 1

        # Makes a words list with all the words on the current line
        words_list = split_line(lines)

        # Loops through the words list
        for word in words_list:
            i = 0
            # Loops through until it either finds the word in the dictionary list or it reaches the end of the list
            while i < len(list) and list[i] != word.upper():
                i += 1
            # If the loop reached the end of the list and didn't find the word print the word and line number
            if i == len(list):
                print(word + " on line " + str(line_num))

    # Calculates, prints and returns the end time
    end_time = time.time() - start_time
    print("File searched in " + str(end_time) + " seconds")
    return end_time


# Function for binary search
def binary_search(file, list):
    # Gets the starting time to calculate the time it takes to complete this search
    start_time = time.time()
    print(" ")
    print("--- Binary Search ---")
    print(" ")
    # Creates a var to keep track of the line number
    line_num = 0
    # Loops through all the lines in the given file
    for lines in open(file).readlines():
        # Adds to the line number each loop
        line_num += 1

        # Makes a words list with all the words on the current line
        words_list = split_line(lines)

        # Loops through the words list
        for word in words_list:
            # Sets the lower bound var to 0
            lower_bound = 0
            # Sets upper bound var to the length of list
            upper_bound = len(list) - 1
            # Sets found var to false
            found = False
            # Loops through until either lower bound > upper bound (ei searched entire list and didnt find word)
            # Or the word was found
            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2
                # Checks where the word is when compared to middle pos in the list and sets the upper bound/lower bound
                # Accordingly but if neither conditions are false it means we found the word
                if list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True
            # If the word was not found in the list print the word and line number
            if not found:
                print(word + " on line " + str(line_num))

    # Calculates, prints and returns the end time
    end_time = time.time() - start_time
    print("File searched in " + str(end_time) + " seconds")
    return end_time


# Creates a list of all the word in the dictionary
dictionary_list = create_list('dictionary.txt')

# Calls the search functions and returns the time it took to complete them
# (AliceInWonderLand200.txt can be swapped out for AliceInWonderLand.txt)
linear_time = linear_search('AliceInWonderLand200.txt', dictionary_list)
binary_time = binary_search('AliceInWonderLand200.txt', dictionary_list)

# Prints how much longer the binary search algorithm takes
print(" ")
print("The linear search algorithm took " + str((linear_time - binary_time) / binary_time) +
      " times longer than the binary search")
