'''
Q10) Character Counter 
Count how many times each character appears in a string (excluding spaces). 
'''
String_Input = 'It cant be free in this economy'
String_Input = String_Input.replace(' ','')
Count = {}
for char in String_Input:
  if char in Count:
      Count[char] += 1
  else:
      Count[char] = 1

print(Count)
