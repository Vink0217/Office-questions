'''
7. Email Automation Bot 
Take a list of email addresses and names 
Send personalized emails using SMTP (mock or real) 
Generate log for each email 
Concepts: smtplib, email, file reading, error handling, logging 
'''

import smtplib
import getpass

HOST = "smtp.gmail.com"
PORT = 587

FROM_EMAIL = "vvinayakvinod@gmail.com"
file_path = r"Assignment 2\InputOutput Files\gmail.txt"

PASSWORD = getpass.getpass("Enter App Password: ")

MESSAGE = """Subject: Test Email from Python

Hi,

This is a test email sent using Gmail SMTP with Python!

Regards,
Vinayak
"""

# Connect to Gmail SMTP server
with smtplib.SMTP(HOST, PORT) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    with open(file_path,'r') as txtfile:
        lines = txtfile.readlines()
        for line in lines:
            smtp.login(FROM_EMAIL, PASSWORD)
            smtp.sendmail(FROM_EMAIL, line, MESSAGE)

print("[+] Email sent successfully.")
