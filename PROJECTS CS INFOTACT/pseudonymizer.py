import random

fake_names = {
    "John Smith": "James Brown",
    "Sarah Johnson": "Emily Davis",
    "Dr. Adams": "Dr. Cooper",
    "Dr. Williams": "Dr. Mitchell"
}

first_names = ["James", "Emily", "Robert", "Sophia", "William"]
last_names = ["Brown", "Davis", "Wilson", "Taylor", "Anderson"]
doctor_names = ["Dr. Cooper", "Dr. Mitchell", "Dr. Harris", "Dr. Parker"]
streets = ["Oak Street", "Maple Avenue", "Pine Road", "Elm Boulevard"]
cities = ["Springfield", "Riverside", "Fairview", "Georgetown"]
domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]

name_mapping = {}

def get_fake_name(real_name):
    if real_name in fake_names:
        return fake_names[real_name]
    return "[UNKNOWN]"

def generate_fake_name():
    first = random.choice(first_names)
    last = random.choice(last_names)
    return first + " " + last

def replace_patient_name(note, real_name):
    fake = generate_fake_name()
    note = note.replace(real_name, fake)
    return note

def replace_doctor_name(note, real_doctor):
    fake_doctor = random.choice(doctor_names)
    note = note.replace(real_doctor, fake_doctor)
    return note

def store_mapping(real_name):
    fake = generate_fake_name()
    name_mapping[real_name] = fake
    return fake

def reverse_mapping(note):
    for real, fake in name_mapping.items():
        note = note.replace(fake, real)
    return note

def generate_fake_address():
    number = random.randint(100, 999)
    street = random.choice(streets)
    city = random.choice(cities)
    return str(number) + " " + street + ", " + city

def generate_fake_phone():
    part1 = random.randint(100, 999)
    part2 = random.randint(100, 999)
    part3 = random.randint(1000, 9999)
    return str(part1) + "-" + str(part2) + "-" + str(part3)

def generate_fake_email():
    first = random.choice(first_names).lower()
    last = random.choice(last_names).lower()
    domain = random.choice(domains)
    return first + "." + last + "@" + domain

print(get_fake_name("John Smith"))
print(get_fake_name("Dr. Adams"))

print(generate_fake_name())
print(generate_fake_name())

note = "Patient Name: John Smith has Parkinson's disease."
print("ORIGINAL:") 
print(note)
print("PSEUDONYMIZED:")
print(replace_patient_name(note, "John Smith"))

note2 = "Doctor Name: Dr. Adams treated the patient today."
print("ORIGINAL:")
print(note2)
print("PSEUDONYMIZED:")
print(replace_doctor_name(note2, "Dr. Adams"))

note3 = "Patient Name: John Smith has high blood pressure."
note4 = "Patient Name: Sarah Johnson has diabetes."
print("PATIENT 1 PSEUDONYMIZED:")
print(replace_patient_name(note3, "John Smith"))
print("PATIENT 2 PSEUDONYMIZED:")
print(replace_patient_name(note4, "Sarah Johnson"))

store_mapping("John Smith")
store_mapping("Sarah Johnson")
store_mapping("Dr. Adams")
print("NAME MAPPINGS:")
for real, fake in name_mapping.items():
    print(real, "->", fake)

print("FAKE ADDRESS:")
print(generate_fake_address())

print("FAKE PHONE:")
print(generate_fake_phone())

print("FAKE EMAIL:")
print(generate_fake_email())

real_note = """
Patient Name: John Smith
Doctor Name: Dr. Adams
Diagnosis: Patient has Parkinson's disease.
"""

store_mapping("John Smith")
store_mapping("Dr. Adams")

pseudonymized = real_note
for real, fake in name_mapping.items():
    pseudonymized = pseudonymized.replace(real, fake)

print("ORIGINAL:")
print(real_note)

print("PSEUDONYMIZED:")
print(pseudonymized)

print("RESTORED:")
print(reverse_mapping(pseudonymized))