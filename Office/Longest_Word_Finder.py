'''
Q7) Longest Word Finder 
Given a sentence, find and print the longest word. 
'''
string_input = str(input("Enter String: "))
word = string_input.split()
longest_word = max(word, key=len)    
print(longest_word)