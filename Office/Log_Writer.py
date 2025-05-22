'''
Q13) Simple Log Writer 
Write logs to a file every time the script is run with timestamps. 
'''
import time
log_file = r"Output Files\log.txt"
Time_at_that_instance = time.strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"{Time_at_that_instance} - Script started\n"
with open(log_file, "a") as file:
    file.write(log_entry)

a=int(input("Enter Number: "))
if a % 2 ==0:
    print("Even")
else:
    print("Odd")    

Time_at_that_instance = time.strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"{Time_at_that_instance} - Script finished\n"

with open(log_file, "a") as file:
    file.write(log_entry)
