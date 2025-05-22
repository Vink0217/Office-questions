'''
Q12) Read and Count Words 
Read a text file and count total words, lines, and characters. 
'''

file_path = 'Output Files\Sample.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()  
    text = ''.join(lines)       
    line_count = len(lines)
    word_count = len(text.split())
    char_count = len(text)
    print(f"Total Lines: {line_count}, Total Words: {word_count}, Total Characters: {char_count}")
