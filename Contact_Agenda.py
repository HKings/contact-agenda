# -------- Contact Agenda --------
# 1. Add a new contact (Name, phone, email) / category (family, friens, work)
# 2. Search contact by name
# 3. Contacts list
# 4. Edit contacts
# 5. Check contacts 
# 6. Remove contacts
# 7. Delete all contacts
# 8. Exit

contacts = []

def show_menu():
    print("\n-- Welcome to Agenda of Tomorrow --")
    print("1.Add a new contact")
    print("2.Search contact by name")
    print("3.Contacts list")
    print("4.Edit contacts")
    print("5.Check contacts")
    print("6.Remove contacts")
    print("7.Delete all contacts")
    print("8.Exit")


# Add a new contact 
def add_new_contact():

    # List of possible categories
    category = ["Family", "Friends", "Work"]

     # Validate name
    while True:
        contact_name = input("Type the name of contact: ").strip() # The strip() is here to remove leading and trailing whitespace
        if not contact_name: # If the name is empty
            print("Name cannot be empty!")
        elif contact_name.isdigit(): # If the name is just numbers
            print("Name cannot be only numbers!")
        elif len(contact_name) < 2: # If the name is too short
            print("Name must have at least 2 characters!")
        else:
            break

     # Validate phone
    while True: # Request only numbers for the contact_phone
        contact_phone = input("Type the number phone: ").strip()
        if not contact_phone: # If the phone is empty
            print("Phone number cannot be empty!")
        elif not contact_phone.isdigit(): # If the phone is not just numbers
            print("Please enter only numbers!")
        elif len(contact_phone) < 5: # If the phone is too short
            print("Phone number must have at least 5 digits!")
        else:
            break

     # Validate email
    while True:
        contact_email = input("Type the email: ").strip()
        if not contact_email: # If the email is empty
            print("Email cannot be empty!")
        elif "@" not in contact_email or "." not in contact_email: # If email doesn´t have "@" and "." on their format
            print("Please enter a valid email format (exemple@domain.com)")
        elif contact_email.isdigit(): # If the email is just numbers
            print("Email cannot be only numbers!")
            continue
        else:
            break

    # Show possible categories
    print("\nChoose a category:")
    for i, catego in enumerate(category, 1):
        print(f"{i}. {catego}")

    # Aask to user to choose
    while True:
        try:
            option = int(input("Select category (1-3): "))
            if 1 <= option <= 3:
                chosen_category = category[option - 1]
                break
            else:
                print("Please choose between 1-3")
        except ValueError:
            print("Please enter a valid number")

    # Contact with category
    
    contact = f"Name: {contact_name} | Phone: {contact_phone} | email: {contact_email} | Category: {chosen_category}"
    contacts.append(contact)

    print(f"Contact {contact_name} added successfully with category {chosen_category}")


# Search contact by name
def search_contact():
    search = input("Type the name of contact (or type 0 to cancel): ")

    if search == 0:
        print("Operation canceled!")
        return

    # List for the results found
    result = []

    for contact in contacts:
        name_part = contact.split(" | ")[0] # split(" | ") divide the string into list, and get teh index [0] = Name: {contact_name}
        name = name_part.replace("Name: ", "") # remove the name to " "

        if search.lower() in name.lower():
            result.append(contact)

    if result:
        print("\nContacts found: ")
        for contact in result:
            print(f"{contact}")

    else:
        print("No contacts found with that name!")


def contacts_list():
    if contacts:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact}")

    else:
        print("No contacts!")


# Edit a existing contact
def edit_contact():

    if not contacts:
        print("No contacts to edit!")
        return

    contacts_list()

    try:
        index = int(input("Type the index of contact to edit: ")) - 1


        if 0 <= index < len(contacts): # the index can't be less than 0 and higher than number of existing contacts
            print(f"\nEditing contact: {contacts[index]}") 

            # Request new data from user
            new_name = input("New name (or press Enter to keep current): ")

            while True:
                new_phone = input("New phone (or press Enter to keep current): ")
                if not new_phone:
                    break
                elif new_phone.isdigit():
                    break
                else:
                    print("Please enter only numbers!")

            new_email = input("New email (or press Enter to keep current): ")

            # Choosing new category
            categories = ["Family", "Friends", "Work"]
            print("Choose new category: ")

            for i, catego in enumerate(categories, 1): # Loop for to scroll through the list to enumerate the new categories
                print(f"{i}. {catego}") # Print the categories with index

            try:
                option = int(input(" Select category (1-3, or 0 to keep current): "))
                if 1 <= option <= 3:
                    new_category = categories[option - 1]
                else:
                    new_category = None # Keep the same category

            except ValueError:
                new_category = None

            
            # Use the actual data (If the user doesn't change the old data)
            old_contact = contacts[index]
            old_parts = old_contact.split(" | ")
            old_name = old_parts[0].replace("Name: ", "")
            old_phone = old_parts[1].replace("Phone: ", "")
            old_email = old_parts[2].replace("email: ", "")
            old_category = old_parts[3].replace("Category: ", "")

            # Use new data if provided, otherwise keep existing
            final_name = new_name if new_name else old_name
            final_phone = new_phone if new_phone else old_phone
            final_email = new_email if new_email else old_email
            final_category = new_category if new_category else old_category

            # Update contact
            update_contact = f"Name: {final_name} | Phone: {final_phone} | email: {final_email} | Category: {final_category}"

            # Update the list
            contacts[index] = update_contact

            print("Contact update successfully!")
            print(f"New contact: {update_contact}")

        else:
            print("Invalid index!")

    except ValueError:
        print("Please enter a valid number!")


def check_contacts():

    if not contacts:
        print("No contacts to check!")
        return

    check = input("Type the key-word: ") # Request the term from user

    # Search for contact containing the term
    result = [contact for contact in contacts if check.lower() in contact.lower()]
    if result:
        print("\nContact Found")

        for contact in result:
            print(f"-{contact}")
    
    else:
        print("No contact found with that term.")


def remove_contacts(): # Remove a single contact from the contact list

    # Check is list is empty
    if not contacts:
        print("No contacts to remove!")
        return

    contacts_list()
    print("\nType 0 to cancel.")

    while True:
        try:
            index = int(input("Type the index of contact to remove (0 to cancel):  ")) - 1

            if index == -1: # If the user type 0
                print("Operation canceled!")
                break

            if 0 <= index < len(contacts):
                remove = contacts.pop(index) # Delete just the contact chosen
                print(f"The contact {remove} was removed successfully!")
                break

            else:
                print("Invalid index!")

        except ValueError:
            print("Please enter a valid number!")


def delete_all_contacts(): # Remove all contacts from the contact list

    # Check if list is empty
    if not contacts:
        print("No contacts to delete!")
        return

    while True:
        delete_all = input("Are you sure you want to delete all the contact of the list? (yes/no):")

        if delete_all.lower() in ["yes", "y"]:
            contacts.clear()
            print("The contacts were deleted successfully.")
            break
        elif delete_all.lower() in ["no", "n"]:
            print("Process Canceled!")
            break
        else:
            print("Please enter 'yes' or 'no' only!")


# Main Loop
while True:
    show_menu()

    option = input("\n Type a option below: ").strip() # The strip() is here to remove leading and trailing whitespace

    if option == "1":
        add_new_contact()
    elif option == "2":
        search_contact()
    elif option == "3":
        contacts_list()
    elif option == "4":
        edit_contact()
    elif option == "5":
        check_contacts()
    elif option == "6":
        remove_contacts()
    elif option == "7":
        delete_all_contacts()
    elif option == "8":
        print("Leaving the program. See you soon!")
        break
    else:
        print("Invalid option! Please choose between 1-8.")