# Contact Book Management System

A simple command-line Contact Book application written in Python. This project allows you to efficiently manage your contacts with basic CRUD (Create, Read, Update, Delete) operations.

## Features
- Add new contacts with ID, name, phone, and Gmail address
- View all contacts or a specific contact by ID
- Update contact details (name, phone, Gmail)
- Delete contacts by ID
- Simple and interactive command-line interface

## Getting Started

### Prerequisites
- Python 3.x

### Running the Application
1. Clone or download this repository.
2. Navigate to the `src` directory:
   ```bash
   cd src
   ```
3. Run the main script:
   ```bash
   python main.py
   ```

### Usage
- When prompted, enter a command:
  - `1` to add a contact
  - `2` to read (view) contacts
  - `3` to update a contact
  - `4` to delete a contact
  - `q` to exit the application

Follow the on-screen instructions for each operation.

## Example
```
Enter command: (1.add, 2.read, 3.update, 4.delete, q.exit): 1
Enter id: 101
Enter name: Alice
Enter phone: 1234567890
Enter gmail: alice@gmail.com
Added contact Alice with ID 101
```

## License
This project is licensed under the MIT License.
