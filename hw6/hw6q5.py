# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 6 Question 5


txt = initialization()      #a function which reads in the text file and stores  it in the string variable txt
txt_del= delete_punctuation(txt)   # a function which accepts the txt string and removes all punctuation
# txt_words is  a list of all of the words in the Gettysburg Address
txt_words = determine_number(txt_del)  # a function which accepts txt_del and returns a list and it's length (the number of words)
txt_unique_words = determine_unique_words(txt_words) # function whih eliminates repetitions
order_alphabetically(txt_unique_words) # a function which accepts the list of unique words and prints the list sorted
order_by_length (txt_unique_words) # a function which accepts the list of unique words, orders them by length, and prints out the list from the longest to the shortest with  hyphen after each word followed by its length.
