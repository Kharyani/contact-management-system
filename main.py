import json
import os

FILE_NAME = "contacts.json"

# Load contacts
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Generate ID
def generate_id(contacts):
    return len(contacts) + 1

# Add contact
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    city = input("Enter City: ")
    company = input("Enter Company: ")

    contact = {
        "id": generate_id(contacts),
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
        "company": company
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("✅ Contact added successfully!")

# View contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for c in contacts:
        print(f"\nID: {c['id']}")
        print(f"Name: {c['name']}")
        print(f"Phone: {c['phone']}")
        print(f"Email: {c['email']}")
        print(f"City: {c['city']}")
        print(f"Company: {c['company']}")

# Search contact
def search_contact(contacts):
    keyword = input("Enter name/email/phone to search: ").lower()

    found = False
    for c in contacts:
        if (keyword in c['name'].lower() or
            keyword in c['email'].lower() or
            keyword in c['phone']):
            print(f"\nFound: {c}")
            found = True

    if not found:
        print("No match found.")

# Filter contacts
def filter_contacts(contacts):
    choice = input("Filter by (1) City or (2) Company: ")

    if choice == "1":
        city = input("Enter city: ").lower()
        for c in contacts:
            if c['city'].lower() == city:
                print(c)

    elif choice == "2":
        company = input("Enter company: ").lower()
        for c in contacts:
            if c['company'].lower() == company:
                print(c)

# Update contact
def update_contact(contacts):
    cid = int(input("Enter ID to update: "))

    for c in contacts:
        if c['id'] == cid:
            c['name'] = input("New Name: ")
            c['phone'] = input("New Phone: ")
            c['email'] = input("New Email: ")
            c['city'] = input("New City: ")
            c['company'] = input("New Company: ")
            save_contacts(contacts)
            print("✅ Updated successfully!")
            return

    print("Contact not found.")

# Delete contact
def delete_contact(contacts):
    cid = int(input("Enter ID to delete: "))

    for c in contacts:
        if c['id'] == cid:
            contacts.remove(c)
            save_contacts(contacts)
            print("🗑 Deleted successfully!")
            return

    print("Contact not found.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Filter Contacts")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            filter_contacts(contacts)
        elif choice == "5":
            update_contact(contacts)
        elif choice == "6":
            delete_contact(contacts)
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()