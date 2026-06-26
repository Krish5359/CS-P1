fake_names = {
    "John Smith": "James Brown",
    "Sarah Johnson": "Emily Davis",
    "Dr. Adams": "Dr. Cooper",
    "Dr. Williams": "Dr. Mitchell"
}

def get_fake_name(real_name):
    if real_name in fake_names:
        return fake_names[real_name]
    return "[UNKNOWN]"

print(get_fake_name("John Smith"))
print(get_fake_name("Dr. Adams"))

import random

first_names = ["James", "Emily", "Robert", "Sophia", "William"]
last_names = ["Brown", "Davis", "Wilson", "Taylor", "Anderson"]

def generate_fake_name():
    first = random.choice(first_names)
    last = random.choice(last_names)
    return first + " " + last

print(generate_fake_name())
print(generate_fake_name())
print(generate_fake_name())

def replace_patient_name(note, real_name):
    fake = generate_fake_name()
    note = note.replace(real_name, fake)
    return note

note = "Patient Name: John Smith has Parkinson's disease."

print("ORIGINAL:")
print(note)

print("PSEUDONYMIZED:")
print(replace_patient_name(note, "John Smith"))
doctor_names = ["Dr. Cooper", "Dr. Mitchell", "Dr. Harris", "Dr. Parker"]

def replace_doctor_name(note, real_doctor):
    fake_doctor = random.choice(doctor_names)
    note = note.replace(real_doctor, fake_doctor)
    return note

note2 = "Doctor Name: Dr. Adams treated the patient today."

print("ORIGINAL:")
print(note2)

print("PSEUDONYMIZED:")
print(replace_doctor_name(note2, "Dr. Adams"))

note3 = "Patient Name: John Smith has high blood pressure."
note4 = "Patient Name: Sarah Johnson has diabetes."

print("PATIENT 1 ORIGINAL:")
print(note3)
print("PATIENT 1 PSEUDONYMIZED:")
print(replace_patient_name(note3, "John Smith"))

print("PATIENT 2 ORIGINAL:")
print(note4)
print("PATIENT 2 PSEUDONYMIZED:")
print(replace_patient_name(note4, "Sarah Johnson"))

name_mapping = {}

def store_mapping(real_name):
    fake = generate_fake_name()
    name_mapping[real_name] = fake
    return fake

store_mapping("John Smith")
store_mapping("Sarah Johnson")
store_mapping("Dr. Adams")

print("NAME MAPPINGS:")
for real, fake in name_mapping.items():
    print(real, "->", fake)

    def reverse_mapping(note):
    for real, fake in name_mapping.items():
        note = note.replace(fake, real)
    return note

pseudonymized_note = "Patient James Brown has Parkinson's disease."

print("PSEUDONYMIZED:")
print(pseudonymized_note)

print("RESTORED:")
print(reverse_mapping(pseudonymized_note))