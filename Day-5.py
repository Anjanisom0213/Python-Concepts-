contacts = {}

while True:
    print("\n1. Add Contact\n2. View All\n3. Search\n4. Delete\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Contact saved!")

    elif choice == '2':
        for name, phone in contacts.items():
            print(f"{name} : {phone}")

    elif choice == '3':
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name}'s phone: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Deleted successfully.")
        else:
            print("No such contact.")

    elif choice == '5':
        break
    else:
        print("Invalid choice.")

