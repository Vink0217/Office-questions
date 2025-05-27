'''
Q2) Number to Words Converter 
Convert a number (e.g., 123) into its word form ("one hundred twenty-three"). 
'''
i = int(input("Enter a number to convert: "))
def number_to_words(i):
    single_digit = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    less_than_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if i < 10:
        return single_digit[i - 1]
    elif i < 20:
        return less_than_twenty[i - 10]
    elif i < 100:
        return tens[i // 10 - 2] + ("" if i % 10 == 0 else "-" + single_digit[i % 10 - 1])
    elif i < 1000:
        return single_digit[i // 100 - 1] + " hundred" + ("" if i % 100 == 0 else " and " + number_to_words(i % 100))


print(number_to_words(i))
