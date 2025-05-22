'''
Q1) Prime Number Generator 
Generate all prime numbers between two given numbers using a function. 
'''
first_number = int(input("Enter the first numeber: "))
second_number = int(input("Enter the second number: "))

def prime_number_finder(first_number, second_number):
    for i in range(first_number, second_number):
        is_prime=True
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
            
        if is_prime:
            print(i)

prime_number_finder(first_number, second_number)
