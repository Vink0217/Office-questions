'''
Q14) CSV Reader 
Read a CSV file containing student marks and print names of students scoring above 75%. 
'''
import csv
file_path = r'Output Files\Marks.csv'
Above_75 = []
with open(file_path, 'r', newline='') as csvfile:
    Read_List = csv.DictReader(csvfile)
    for row in Read_List:
        if int(row['Marks']) > 75:
            Above_75.append(row['Name'])

print(f"Students scoring above 75%: {Above_75}")

