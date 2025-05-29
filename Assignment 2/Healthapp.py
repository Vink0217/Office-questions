'''
2. Hospital Management System 
Build a system to: 
Register patients 
Assign doctors 
Track appointments and prescriptions 
Generate daily reports 
Concepts: Classes for Patient, Doctor, Appointment, file I/O, date/time 
'''

class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

patients = []
doctors = []
appointments = []

def savetofile(data):
    with open ("file.txt", "a") as file:
        file.write(data +"\n")

def register_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    while True: 
        gender = input("Enter patient gender: ").strip().upper()
        if gender.isalpha():
            break
        else:
            print("Invalid Entry")
    patient = Patient(name, age, gender)
    patients.append(patient)
    savetofile(f"Patient Registered: {name}, Age: {age}, Gender: {gender}")
    print("Patient registered successfully.\n")

def assign_doctor():
    name = input("Enter doctor name: ")
    specialty = input("Enter doctors specialty: ")
    doctor = Doctor(name, specialty)
    doctors.append(doctor)
    savetofile(f"Doctor name: {name}, Specialty: {specialty}")
    print("Doctor assigned successfully.\n")

def book_appointment():

    print("Available Patients:")
    for i, patient in enumerate(patients, start= 1):
        print(f"{i}. {patient.name}")

    patientno = int(input("Select patient: ")) -1

    print("Available Doctors:")
    for i, doctor in enumerate(doctors, start=1):
        print(f"{i}. {doctor.name} - {doctor.specialty}")

    doctorno = int(input("Select doctor: "))-1

    date = input("Enter date (YYYY-MM-DD): ")
    time = input("Enter time (HH:MM AM/PM): ")
    appointment = Appointment(patients[patientno], doctors[doctorno], date, time)
    appointments.append(appointment)
    savetofile(f" Patient : {patients[patientno].name}, Doctor : {doctors[doctorno].name}, Date: {date}, Time: {time}")
    print("Appointment successfull.\n")

def generate_daily_report():
    date = input("Enter date (YYYY-MM-DD): ")
    print(f"Daily Report for {date}")
    found = False
    for appt in appointments:
        if appt.date == date:
            print(f"Patient: {appt.patient.name}, Doctor: {appt.doctor.name}, Time: {appt.time}")
            savetofile(f"Patient: {appt.patient.name}, Doctor: {appt.doctor.name}, Date: {date}, Time: {appt.time}")
            found = True
    if not found:
        print("No appointments found for the given date.\n")

def healthapp():
    while True:
        print("1. Register Patient")
        print("2. Assign Doctor")
        print("3. Book Appointment")
        print("4. Generate Daily Report")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            register_patient()
        elif choice == "2":
            assign_doctor()
        elif choice == "3":
            book_appointment()
        elif choice == "4":
            generate_daily_report()
        elif choice == "5":
            print("Bye")
            break
        else:
            print("Invalid choice, please try again.")

healthapp()
