def dashboard():

    """Prints  
    ========================================
      📚  YOUR LIBRARY
    ========================================
    """

    print("=" * 40)
    print("  📚  YOUR LIBRARY ")
    print("=" * 40)


def estimate_reading_time(pages):
 
    #Estemates hours assuming 40 pages/hour rounded to 1 decimal place
    return(round(int(pages)/40, 1))


def add_book():

    #gets input for title, auther, and pages    
    title = input("Book title: ").strip().title()
    author = input("Author: ").strip().title()
    pages = input("Page count: ")

    #calls estimate_reading_time by passing in pages
    hours = estimate_reading_time(pages)

    #prints book's description
    print(f"'{title}' by {author} -- approx. {hours} hours to read")


def main():
    dashboard()
    add_book()


if __name__ == "__main__":
    main()