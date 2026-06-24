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