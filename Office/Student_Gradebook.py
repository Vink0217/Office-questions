'''
Q11) Student Gradebook 
Store student names and marks in a dictionary. Allow user to query by name to get marks. 
'''
GradeBook = {"Adam":80,
             "Eve":60,
             "Aditya":68,
             "Vinayak":100,
             "Ahmed":99}

name = str(input("Enter Name of the student whose marks you want: "))
print(GradeBook[name])