"""Contact Book Management System
    This system allows you to manage your contacts efficiently.
    You Can add, read, update, and delete contacts.
"""


class ContactBook:
    """Contact Book Management System
    """
    def __init__(self):
        self.data = {}
        self.id_list = set()

    def add(self, id_: str, name: str, phone: str, gmail: str) -> None:
        """Add a new contact to the contact book.

        Args:
            id_ : The ID of the contact.
            name : The name of the contact.
            phone : The phone number of the contact.
            gmail : The Gmail address of the contact.
        """
        self.data[id_] = {'name': name, 'phone': phone, 'gmail': gmail}
        self.id_list.add(id_)
        print(f"Added contact {name} with ID {id_}")

    def read(self, id_: int = None) -> None:
        """Read a contact from the contact book.

        Args:
            id_ (optional): The ID of the contact to read. Defaults to None.
        """

        if id_:
            print(f"id = {id_}: ", self.data.get(id_, "Contact not found"))
        else:
            for ind in self.id_list:
                print(f"id = {ind}: ", self.data[ind])
                print('-' * 50)

    def delete(self, id_: int) -> None:
        """Delete a contact from the contact book.

        Args:
            id_ : The ID of the contact to delete.
        """

        x = self.data.pop(id_, "Contact not found")
        print(f"Deleted contact: {x}")
        self.id_list.discard(id_)

    def update(self, id_: int, name: str = None, phone: str = None, gmail: str = None) -> None:
        """Update a contact in the contact book.

        Args:
            id_ : The ID of the contact to update.
            name (optional): The new name of the contact. Defaults to None.
            phone (optional): The new phone number of the contact. Defaults to None.
            gmail (optional): The new Gmail address of the contact. Defaults to None.
        """
        if id_ in self.id_list:
            if name:
                self.data[id_]['name'] = name
            if phone:
                self.data[id_]['phone'] = phone
            if gmail:
                self.data[id_]['gmail'] = gmail
            print("Contact updated successfully.")

        else:
            print("Contact not found")


space = "-" * 50


if __name__ == "__main__":
    contact = ContactBook()
    while True:
        print(space)
        input_user = input("Enter command: (1.add, 2.read, 3.update, 4.delete, q.exit): ")

        if input_user == 'q':
            print("Exiting the Contact Book System.")
            break

        elif input_user == '1':
            id_input = input("Enter id: ")
            name_input = input("Enter name: ")
            phone_input = input("Enter phone: ")
            gmail_input = input("Enter gmail: ")
            contact.add(id_=id_input, name=name_input, phone=phone_input, gmail=gmail_input)
        
        elif input_user == '2':
            id_input = input("Enter id (blank = Read All ContactBook): ")
            print(space)
            contact.read(id_=id_input)

        elif input_user == '3':
            id_input = input("Enter id: ")
            name_input = input("Enter new name (blank = no change): ")
            phone_input = input("Enter new phone (blank = no change): ")
            gmail_input = input("Enter new gmail (blank = no change): ")
            contact.update(id_=id_input, name=name_input, phone=phone_input, gmail=gmail_input)

        elif input_user == '4':
            id_input = input("Enter id: ")
            contact.delete(id_=id_input)