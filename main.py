from database_function import *

def view_contacts () :  
    contacts = get_records()

    print('')

    for contact in contacts:
        print('-' * 20)
        print('ID: ', str(contact[0]))
        print('Name:   ', contact[1])
        print('Number: ', str(contact[2]))
        print('-' * 20)
        print('')
    main()

def add_contact () :
    print('')
    name = input('Enter name of the contact: ')
    number = input('Enter phone number of the contact: ')
    print('')

    insert_contact(name, int(number))

    main()

def edit_contact () :
    print('')
    id = input('Enter id of the contact you want to delete: ')
    name = input('Enter new name of the contact: ')
    number = input('Enter new number of the contact: ')

    update_contact(id, name, number)
    main()

    

def delete_contact_func () :
    print(' ')
    id = int(input('Enter id of the contact you want to delete: '))
    delete_contact(id)

    main()

def main () :
    menu = '''
1. View all contacts.
2. Add a contact.
3. Delete a contact.
4. Edit a contact.
5. Exit
    '''
    print('-' * 20, 'Menu', '-' * 20)
    print(menu)
    print('-' * 40)
    print('')
    option = int(input('> '))

    if option == 1:
        view_contacts()
    elif option == 2:
        add_contact()
    elif option == 3:
        delete_contact_func()
    elif option == 4:
        edit_contact()
    elif option == 5:
        exit()


main()