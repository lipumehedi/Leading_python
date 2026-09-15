class Phonebook:
    def __init__(self):
        self.contacts = {}  

    def view_contact(self, name):
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
        else:
            print("Contact not found")

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Added {name}")

    def update_contact(self, name, new_number):
        if name in self.contacts:
            self.contacts[name] = new_number
            print(f"Updated {name}")
        else:
            print("Contact not found")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted {name}")
        else:
            print("Contact not found")



pb = Phonebook()

while True:
    print("\n--- Phonebook Menu ---")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
   

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Number: ")
        pb.add_contact(name, number)

    elif choice == "2":
        name = input("Name: ")
        pb.view_contact(name)

    elif choice == "3":
        name = input("Name: ")
        new_number = input("New Number: ")
        pb.update_contact(name, new_number)

    elif choice == "4":
        name = input("Name: ")
        pb.delete_contact(name)
        break

    else:
        print("Invalid choice")
