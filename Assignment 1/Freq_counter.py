'''
Q9) Frequency Counter 
Count the frequency of each word in a given paragraph. 
'''
paragraph = "This is a paragraph with multiple repeating words like with words repeating paragraph paragraph is a is a is a is a with words"
dictionary = {}

for word in paragraph.split():
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

print(dictionary)
