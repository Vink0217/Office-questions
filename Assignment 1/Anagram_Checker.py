'''
Q5) Anagram Checker 
Write a function to check if two strings are anagrams of each other. 
'''
first_string = str(input("Enter String: "))
first_string_strip = first_string.replace(" ","")
second_string = str(input("Enter String: "))
second_string_strip = second_string.replace(" ","")
first_array = []
second_array = []
for i in first_string_strip:
    first_array.append(i)

for j in second_string_strip:
    second_array.append(j)

if sorted(second_array) == sorted(first_array):
    print("Anangram")
else:
    print("Not anagram")    
