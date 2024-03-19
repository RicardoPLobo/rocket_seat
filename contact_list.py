def add_contact(contacts):
    contact_name = input("Type new contact's name: ")
    contact_number = input("Type new contact's phone number: ")
    contact_email = input("Type new contact's email address: ")
    while True:
        contact_favorite = input("Set contact as favorite(Y/N): ").lower()
        if contact_favorite == "y" or contact_favorite == "yes":
            contact_favorite = True
            favorite = "✓"
            contacts.append({"name": contact_name, "number": contact_number, "email": contact_email, "favorite": contact_favorite})
            break
        elif contact_favorite == "n" or contact_favorite == "no":
            contact_favorite = False
            favorite = " "
            contacts.append({"name": contact_name, "number": contact_number, "email": contact_email, "favorite": contact_favorite})
            break
        else:
            print("Invalid answer.")
    print(f"\nNew contact added:\nName: {contact_name}\nPhone number: {contact_number}\nEmail address: {contact_email}\nFavorite [{favorite}]")

def show_contacts(contacts):
    print("\nList of contacts:")
    for contact in contacts:
        favorite = "✓" if contact["favorite"] == True else " "
        print("\nName: %s\nPhone Number: %s\nEmail address: %s\nFavorite [%s]" %(contact["name"], contact["number"], contact["email"], favorite))

def edit_contact(contacts):
    while True:
        choice = input("\nEnter the name of the contact you would like to edit (Or type '1' to cancel): ").capitalize()
        if choice == "1":
            return
        else:
            for contact in contacts:
                if choice == contact["name"]:
                    print("\nWhat would you like to edit?")
                    print("1. Name")
                    print("2. Phone Number")
                    print("3. Email address")
                    print("4. Cancel")
                    edit = input("Enter the number of your choice: ")
                    if edit == "1":
                        contact["name"] = input("\nEnter new name: ")
                        print("\nContact name updated to '%s'" %contact["name"])
                        return
                    elif edit == "2":
                        contact["number"] = input("\nEnter new phone number: ")
                        print("\nPhone number updated to '%s'" %contact["number"])
                        return
                    elif edit == "3":
                        contact["email"] = input("\nEnter new email address: ")
                        print("\nEmail address updated to '%s'" %contact["email"])
                        return
                    elif edit == "4":
                        return
            print("\nName not in contact list")

def set_unset_favorite(contacts):
    while True:
        choice = input("\nEnter the name of the contact you would like to set/unset favorite (Or type '1' to cancel): ").capitalize()
        if choice == "1":
            return
        else:
            for contact in contacts:
                if choice == contact["name"]:
                    if contact["favorite"] == False:
                        contact["favorite"] = True
                        print("\n'%s' set as favorite" %contact["name"])
                        return
                    else:
                        contact["favorite"] = False
                        print("\n'%s' unset as favorite" %contact["name"])
                        return
            print("\nName not in contact list")

def show_favorite_contacts(contacts):
    print("\nList of favorite contacts:")
    for contact in contacts:
        if contact["favorite"] == True:
            print("\nName: %s\nPhone number: %s\nEmail address: %s" %(contact["name"], contact["number"], contact["email"]))

def delete_contact(contacts):
    while True:
        choice = input("\nEnter the name of the contact you would like to delete (Or type '1' to cancel): ").capitalize()
        if choice == "1":
            return
        else:
            for contact in contacts:
                if choice == contact["name"]:
                    print("\nContact '%s' removed" %(contact["name"]))
                    contacts.remove(contact)
                    return
            print("\nName not in contact list")
                    

try:
    contacts = []
    while True:
        print("\nContacts menu: ")
        print("1. Add a contact")
        print("2. Show contact list")
        print("3. Edit a contact")
        print("4. Set/Unset contact as favorite")
        print("5. Show favorite contact list")
        print("6. Delete a contact")
        print("7. Leave")

        choice = input("\nType your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            show_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            set_unset_favorite(contacts)
        elif choice == "5":
            show_favorite_contacts(contacts)
        elif choice == "6":
            delete_contact(contacts)
        elif choice == "7":
            print("\nProgram finished.")
            break
        else:
            print("\nInvalid number.")
except KeyboardInterrupt:
    print("\nProgram canceled.")