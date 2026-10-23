
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("contacts.json")


def load_contacts():
    if not DATA_FILE.exists():
        return []

    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise ValueError("Contacts data must be a list.")
        return data
    except (json.JSONDecodeError, ValueError) as error:
        raise RuntimeError(f"Cannot load contacts: {error}") from error


def save_contacts(contacts):
    DATA_FILE.write_text(
        json.dumps(contacts, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    if not name or not phone:
        print("Name and phone are required.")
        return

    if any(c["phone"] == phone for c in contacts):
        print("This phone number already exists.")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added.")


def list_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(
            f"{index}. {contact['name']} | "
            f"{contact['phone']} | {contact['email']}"
        )


def search_contact(contacts):
    query = input("Search name or phone: ").strip().lower()
    matches = [
        c for c in contacts
        if query in c["name"].lower() or query in c["phone"].lower()
    ]

    list_contacts(matches)


def edit_contact(contacts):
    phone = input("Phone number of contact to edit: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            name = input(f"New name [{contact['name']}]: ").strip()
            email = input(f"New email [{contact['email']}]: ").strip()

            if name:
                contact["name"] = name
            if email:
                contact["email"] = email

            save_contacts(contacts)
            print("Contact updated.")
            return

    print("Contact not found.")


def delete_contact(contacts):
    phone = input("Phone number to delete: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted.")
            return

    print("Contact not found.")


def main():
    try:
        contacts = load_contacts()
    except RuntimeError as error:
        print(error)
        return

    actions = {
        "1": add_contact,
        "2": list_contacts,
        "3": search_contact,
        "4": edit_contact,
        "5": delete_contact,
    }

    while True:
        print("\n=== Contact Book ===")
        print("1. Add  2. List  3. Search")
        print("4. Edit 5. Delete 0. Exit")

        choice = input("Choose: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        action = actions.get(choice)

        if action is None:
            print("Invalid choice.")
            continue

        action(contacts)


if __name__ == "__main__":
    main()
