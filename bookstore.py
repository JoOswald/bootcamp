# This program creates a bookstore database and allows a user to make amendments to the database.
import sqlite3
db = sqlite3.connect('ebookstore')
cursor = db.cursor()

# For ease of use, this function allows the user to search by ID, title or author to see what 
# information is currently held in the database 
def view_books():
    check_criteria = input("What would you like to search by? (Author, Title, ID, Show All):  ").lower()
    if check_criteria == 'id':
        id_check = int(input('Enter the ID of the book you would like to search: '))
        # will only run if a valid ID is entered
        if id_exists(id_check):
            cursor.execute('''SELECT * FROM books WHERE id = ?''', (id_check,))
            book_query_list = cursor.fetchall()
            for books in book_query_list:
                print(f"ID: {books[0]} \tTitle: {books[1]} \tAuthor: {books[2]} \tQuantity: {books[3]}")

    elif check_criteria == 'author':
        author_check = input('Enter the author to search:  ')
        # will only run if a valid author is selected
        if author_exists(author_check):
            cursor.execute('''SELECT * FROM books WHERE author = ?''', (author_check,))
            book_query_list = cursor.fetchall()
            for books in book_query_list:
                print(f"ID: {books[0]} \tTitle: {books[1]} \tAuthor: {books[2]} \tQuantity: {books[3]}")
        
    elif check_criteria == 'title':
        title_check = input('Enter the title to search:  ')
        # will only run if a valid title is entered
        if title_exists(title_check):
            cursor.execute('''SELECT * FROM books WHERE title = ?''', (title_check,))
            book_query_list = cursor.fetchall()
            for books in book_query_list:
                print(f"ID: {books[0]} \tTitle: {books[1]} \tAuthor: {books[2]} \tQuantity: {books[3]}")

    elif check_criteria == 'show all':
        cursor.execute('''SELECT * FROM books''')
        book_query_list = cursor.fetchall()
        for books in book_query_list:
            print(f"\nID: {books[0]} \nTitle: {books[1]} \nAuthor: {books[2]} \nQuantity: {books[3]}\n---------------------")

    else:
        print('Search term not recognised.')  

# function to create a new, unique id number
def new_id():
    cursor.lastrowid + 1

# function to check that the id entered exists in the database
def id_exists(id_selected):
    cursor.execute('''SELECT id FROM books''')
    id_in_use = cursor.fetchall()
    # returns a tuple so make a list of the first element of each tuple (integer)
    id_list = []
    for ids in id_in_use:
        id_list.append(ids[0])
    if id_selected in id_list:
        return True
    else:
        print('That ID is not currently in use')
        return False

# function to check that author input matches an author in the database
def author_exists(author_selected):
    cursor.execute('''SELECT author FROM books''')
    authors_in_use = cursor.fetchall()
    author_list = []
    for authors in authors_in_use:
        author_list.append(authors[0].lower())
    if author_selected.lower() in author_list:
        return True
    else:
        print('Author not recognised')
        return False

# function to check that title input matches a title in the database
def title_exists(title_selected):
    cursor.execute('''SELECT title FROM books''')
    titles_in_use = cursor.fetchall()
    title_list = []
    for titles in titles_in_use:
        title_list.append(titles[0].lower())
    if title_selected.lower() in title_list:
        return True
    else:
        print('Title not recognised')
        return False

# Function to add a book to the books database
def add_book():
    id = new_id()
    title = input("Enter the book title:  ")
    author = input("Enter the author of the book:  ")
    qty = int(input("Enter the quantity:  "))

    cursor.execute('''INSERT INTO books (id, title, author, qty) VALUES(?,?,?,?)''', (id, title, author, qty))
    print("New book added")
    db.commit()

# function to update an existing record
def update_book():
    id_select = int(input("Please enter the ID of the book you would like to edit: "))
    # will only run if a valid ID is entered
    if id_exists(id_select):
        cursor.execute('''SELECT * FROM books WHERE id = ?''', (id_select,))
        book_info = cursor.fetchall()
        book_info = book_info[0]
        print(f"ID: {book_info[0]} \tTitle: {book_info[1]} \tAuthor: {book_info[2]} \tQuantity: {book_info[3]}")
        edit_choice = input("What aspect would you like to edit? (Title, Author, Qty)  ").lower()
        if edit_choice == 'title':
            new_title = input("Please enter the new title:  ")
            cursor.execute('''UPDATE books SET title = ? WHERE id = ?''', (new_title, id_select))
            print("Entry updated")
        elif edit_choice == 'author':
            new_author = input('Please enter the revised author name:  ')
            cursor.execute('''UPDATE books SET author = ? WHERE id = ?''', (new_author, id_select))
            print("Entry updated")
        elif edit_choice == 'qty':
            new_qty = int(input("Please enter the revised quantity: "))
            cursor.execute('''UPDATE books SET qty = ? WHERE id = ?''', (new_qty, id_select))
            print("Entry updated")
        else:
            print('Request not recognised')
        db.commit()
    
# Function to delete a book from the database
def delete_book():
    id_select = int(input("Please enter the ID of the book you would like to delete: "))
    if id_exists(id_select):
        cursor.execute('''SELECT * FROM books WHERE id = ?''', (id_select,))
        book_info = cursor.fetchall()
        book_info = book_info[0]
        print(f"ID: {book_info[0]} \tTitle: {book_info[1]} \tAuthor: {book_info[2]} \tQuantity: {book_info[3]}")
        check_delete = input('Are you sure you want to delete this entry? (Y/N)  ')
        if check_delete.lower() == 'y':
            cursor.execute('''DELETE FROM books WHERE id = ?''', (id_select,))
            print('Entry deleted')
            db.commit()

# create the books table 
cursor.execute('''CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, 
                    author TEXT, qty INTEGER)''')
db.commit()

# add the first line to the database as per the instructions
id1 = 3001
title1 = 'A Tale of Two Cities'
author1 = 'Charles Dickens'
qty1 = 30
cursor.execute('''INSERT INTO books (id, title, author, qty) VALUES (?,?,?,?)''', (id1, title1, author1, qty1))
db.commit()

# other books were added using the add book function 

while True:
    cursor.execute('''SELECT * FROM books''')
    book_query_list = cursor.fetchall()
    for books in book_query_list:
        print(f"\nID: {books[0]} \nTitle: {books[1]} \nAuthor: {books[2]} \nQuantity: {books[3]}\n---------------------")
    user_choice = int(input('''
Welcome to the ebookstore database. 
Please choose an option:
1.  Enter a new book
2.  Update a book already on the system
3.  Delete a book from the database
4.  Search books
0.  Exit
Options 1, 2 and 3 require the book ID number.  Use Search books to find this if not known  '''))

    if user_choice == 1:
        add_book()
    elif user_choice == 2:
        update_book()
    elif user_choice == 3:
        delete_book()
    elif user_choice == 4:
        view_books()
    elif user_choice == 0:
        print('Goodbye')
        break
    else:
        print('Invalid choice, please try again')