contacts = {
    "Amit": "9876543210",
    "Priya": "9123456789",
    "Rahul": "9988776655"
}

contacts["Neha"] = "9012345678"
contacts["Amit"] = "9000000000"

existing_contact = contacts.get("Priya", "Contact not found")
missing_contact = contacts.get("Suresh", "Contact not found")

print("Safe Lookup Results:")
print(f"Priya's Phone: {existing_contact}")
print(f"Suresh's Phone: {missing_contact}")
print()

print("Contact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
