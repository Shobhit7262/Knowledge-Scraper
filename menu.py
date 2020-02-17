from app import books

def print_all_books():
    for book in books:
        print(book)

def best_books(n):
    best_books_list = sorted(books , key=lambda x : x.star_rating * -1)[:n]
    for book in best_books_list:
        print(book)


def print_cheapest_book(n):
    cheapest_books = sorted(books , key=lambda x : x.price)[:n]
    for book in cheapest_books:
        print(book)

books_generator = (x for x in books)


def availability():
    print(next(books_generator))


def menu():
    user_input = input("""
    enter one of the following choice 
    
    a - to look at all books
    b - to look at best books 
    c - to look at cheap books
    n - to look at next available book
    q - to exit
    
    here : """)
    while user_input != "q":
        if user_input == "a":
            print_all_books()
        elif user_input == "b":
            num = int(input("enter the number of books : "))
            best_books(num)
        elif user_input == "c":
            num = int(input("enter the number of books : "))
            print_cheapest_book(num)
        elif user_input == "n":
            availability()
        else :
            print("Invalid C   hoice")
        user_input = input("""
             enter one of the following choice 
                
                a - to look at all books
                b - to look at best books 
                c - to look at cheap books
                n - to look at next available book
                q - to exit
                
                here : """)


menu()