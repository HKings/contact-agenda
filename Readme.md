# Contact Agenda

Hi there, this simple program is a **command-line contact management system** built in Python that helps you organize and manage your personal contacts efficiently. Whether you need to store family, friends, or work contacts, this application provides all the essential features you need in a clean, user-friendly interface.

## Features

- **Add New Contacts**: Store contact information with name, phone, email, and category
- **Smart Search**: Find contacts by name with partial matching
- **Contact Categories**: Organize contacts into Family, Friends, or Work categories
- **Edit Existing Contacts**: Update any contact information easily
- **Advanced Search**: Search contacts by any keyword across all fields
- **Contact Management**: View all contacts in a numbered list
- **Safe Deletion**: Remove individual contacts or clear the entire list
- **Input Validation**: Robust validation for names, phone numbers, and emails

## Why This Project?

This project was created to demonstrate:

- **Clean Code Practices**: Well-structured functions with single responsibilities
- **User Input Validation**: Comprehensive error handling and data validation
- **Interactive CLI Design**: Intuitive menu-driven interface
- **Data Management**: Efficient list operations and string manipulation
- **Python Fundamentals**: Loops, conditionals, functions, and error handling

## Prerequisites

- Python 3.6 or higher
- No external libraries required (uses only built-in Python modules)

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/HKings/contact-agenda.git
   cd contact-agenda
   ```

2. **Run the program**:
   ```bash
   python contact_agenda.py
   ```

3. **Follow the interactive menu** to manage your contacts!

## Usage Example

```
-- Welcome to Agenda of Tomorrow --
1. Add a new contact
2. Search contact by name
3. Contacts list
4. Edit contacts
5. Check contacts
6. Remove contacts
7. Delete all contacts
8. Exit

Type an option below: 1
Type the name of contact: João Silva
Type the number phone: 1234567890
Type the email: john.s@email.com

Choose a category:
1. Family
2. Friends
3. Work
Select category (1-3): 2

Contact João Silva added successfully with category Friends
```

## Project Structure

```
contact-agenda/
│
├── contact_agenda.py          # Main program file
├── README.md                  # Project documentation
```

## Menu Options

| Option | Feature | Description |
|--------|---------|-------------|
| 1 | Add Contact | Create a new contact with full validation |
| 2 | Search by Name | Find contacts using partial name matching |
| 3 | List Contacts | Display all contacts in numbered format |
| 4 | Edit Contact | Modify existing contact information |
| 5 | Check Contacts | Search contacts by any keyword |
| 6 | Remove Contact | Delete a single contact from the list |
| 7 | Delete All | Clear the entire contact list |
| 8 | Exit | Close the program |

## Key Features Explained

### Input Validation
- **Names**: Must be at least 2 characters, cannot be empty or just numbers
- **Phone Numbers**: Must contain only digits and be at least 5 digits long
- **Emails**: Must contain "@" and "." symbols with proper formatting

### Category System
Contacts are organized into three categories:
- **Family**: Personal family contacts
- **Friends**: Social connections
- **Work**: Professional contacts

### Search Functionality
- **Name Search**: Find contacts by partial name matching (case-insensitive)
- **Keyword Search**: Search across all contact fields for any term

## Future Enhancements

- Data persistence (save/load from file)
- Export contacts to CSV/JSON
- Contact backup and restore
- Advanced search filters
- Contact photo support
- Birthday reminders
- Integration with external APIs

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Hamilton P C Reis**
- GitHub: [@HKings](https://github.com/HKings)
- Email: hamiltonpcreis.eng@gmail.com

## Acknowledgments

- Built with Python's built-in modules
- Inspired by the need for simple, efficient contact management
- Thanks to the Python community for excellent documentation

**If you found this project helpful, please consider giving it a star!** ⭐