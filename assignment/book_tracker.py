
def dashboard():

    """Prints  
    ========================================
      📚  YOUR LIBRARY
    ========================================
    """

    print("=" * 40)
    print("  📚  YOUR LIBRARY ")
    print("=" * 40)





def show_menu():

    print()
    print("  What would you like to do? \n")
    print("  1) View books")
    print("  2) Add a book \n")
    print("  q) Quit \n")

    return(input("> ").strip().lower())
    

def estimate_reading_time(pages):
 
    #Estemates hours assuming 40 pages/hour rounded to 1 decimal place
    return(round(int(pages)/40, 1))


def add_book(Library):

    #gets input for title, auther, and pages    
    title = input("Book title: ").strip().title()
    author = input("Author: ").strip().title()
    pages = input("Page count: ")

    #calls estimate_reading_time by passing in pages
    hours = estimate_reading_time(pages)

    #Adds book info to a dictionary
    book = {
        "Title": title,
        "Author": author,
        "Pages": pages,
        "Hours": hours
    }

    #Adds book to list
    Library.append(book)


    #prints book's description
    print("\nBook added: \n")
    print(f"  '{title}' by {author} -- approx. {hours} hours to read")




def view_books(Library):
    if len(Library) == 0:
            print("Your library is empty. Add a book first!")
  
    else:

        for num in range(len(Library)):
            book = Library[num]
            print(f"{num + 1}. '{book["Title"]}' - {book["Author"]} ({book["Pages"]} pages - approx. {book["Hours"]} hours to read)")




def main():


    Library = []

    dashboard()


    while True:
        Choice = show_menu()

        if Choice == "1":
            view_books(Library)

        elif Choice == "2":
            add_book(Library)
        elif Choice == "q" or Choice == "quit" or Choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Sorry, that option isn't available.")

if __name__ == "__main__":
    main()