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