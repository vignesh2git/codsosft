#  Contact Book Application


contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print(f" Contact '{name}' added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print(" No contacts available.")
        return
    print("\n Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")

# Function to search a contact by name or phone
def search_contact():
    term = input("Enter name or phone to search: ").lower()
    found = [c for c in contacts if term in c['name'].lower() or term in c['phone']]
    if found:
        print("\n Search Results:")
        for contact in found:
            print(f"{contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
    else:
        print(" No matching contact found.")

# Function to update a contact
def update_contact():
    view_contacts()
    try:
        idx = int(input("Enter the contact number to update: ")) - 1
        if 0 <= idx < len(contacts):
            contact = contacts[idx]
            print(f"Updating contact: {contact['name']}")
            contact['name'] = input("Enter new name: ") or contact['name']
            contact['phone'] = input("Enter new phone: ") or contact['phone']
            contact['email'] = input("Enter new email: ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            print(f" Contact '{contact['name']}' updated successfully!")
        else:
            print(" Invalid contact number.")
    except ValueError:
        print(" Please enter a valid number.")

# Function to delete a contact
def delete_contact():
    view_contacts()
    try:
        idx = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            removed = contacts.pop(idx)
            print(f" Contact '{removed['name']}' deleted successfully!")
        else:
            print(" Invalid contact number.")
    except ValueError:
        print(" Please enter a valid number.")


def main():
    while True:
        print("\n=====  Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print(" Exiting Contact Book. Goodbye!")
            break
        else:
            print(" Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()