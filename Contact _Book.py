import json
import os

file_name = "../contact_data.json"

def load_data():
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

def add_contact(data):
    print("\nAdd New Contact")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    data.append(contact)
    save_data(data)
    print("Contact saved.\n")

def view_contacts(data):
    print("\nSaved Contacts:")
    if len(data) == 0:
        print("No contacts found.\n")
        return

    for i in range(len(data)):
        print(f"{i+1}. {data[i]['name']} - {data[i]['phone']}")
    print()

def search_contact(data):
    search = input("Enter name or phone to search: ").lower()
    found = False

    for contact in data:
        if search in contact["name"].lower() or search in contact["phone"]:
            print("\nContact Details:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            print()
            found = True

    if not found:
        print("Contact not found.\n")

def update_contact(data):
    name = input("Enter contact name to update: ").lower()

    for contact in data:
        if contact["name"].lower() == name:
            print("Press enter to keep old value.")

            new_phone = input("New Phone (" + contact["phone"] + "): ")
            new_email = input("New Email (" + contact["email"] + "): ")
            new_address = input("New Address (" + contact["address"] + "): ")

            if new_phone != "":
                contact["phone"] = new_phone
            if new_email != "":
                contact["email"] = new_email
            if new_address != "":
                contact["address"] = new_address

            save_data(data)
            print("Contact updated.\n")
            return

    print("Contact not found.\n")

def delete_contact(data):
    name = input("Enter contact name to delete: ").lower()

    for contact in data:
        if contact["name"].lower() == name:
            data.remove(contact)
            save_data(data)
            print("Contact deleted.\n")
            return

    print("Contact not found.\n")

def menu():
    data = load_data()

    while True:
        print("---- Contact Book ----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_contact(data)
        elif choice == "2":
            view_contacts(data)
        elif choice == "3":
            search_contact(data)
        elif choice == "4":
            update_contact(data)
        elif choice == "5":
            delete_contact(data)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice\n")

menu()