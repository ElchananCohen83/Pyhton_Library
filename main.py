from library_operator import LibraryOperator
from library_manager import LibraryManager
from genre import Genre
from book import Book
from customer import Customer
from random import randint

operator = LibraryOperator(operator_last_name='Haviv', operator_first_name='Barak', operator_password='1234')

library = LibraryManager()

def main():
    #רשימת כל הספרים בספריה (לא קטלוג)
    #library.books_manager.print_instance_book()


    # קטלוג
    #library.books_manager.get_catalog_books()


    # חיפוש ספר
    #library.books_manager.book_search('אי האוצרות')


    # הוספת ספר
    #library.books_manager.add_book(Book(book_name='משנה תורה', author_name='רמב"ם', genre=Genre().documentary, publishing_year=1160, age_restriction=False, number_of_pages=850))


    # הסרת ספר = לא ניתן להסיר כאשר הספר בהשאלה
    #library.books_manager.delete_row_in_books(876)
    #ךהחליף שם


    # רשימת לקוחות
    #library.customer_manager.print_instance_customers()
    #להסיר את המילה אינסטנס


    # הוספת לקוח
    #library.customer_manager.add_customers(Customer(customer_last_name='גליקמן', customer_first_name='אליהו'))


    # הסרת לקוח
    # library.customer_manager.delete_customers(101)
    # library.customer_manager.delete_customers()


    # חיפוש לקוח
    #library.customer_manager.customers_search('כהנמן טל')


    # רשימת השאלות
    # library.lending_manager.print_instance_lending()


    # השאלת ספר = בדיקה מנוי לקוח וזמינות ספר, הוספת שורת השאלה, ועדכון בלקוח ובספר
    #library.lending_manager.add_lending_book(2, 1)
    #library.lending_manager.add_lending_book(2, 1)

    # החזרת ספר = הסרת השאלה ועדכון בלקוח ובספר
    #library.lending_manager.return_lending(158)

    #רשימת לקוחות והספרים בהשאלה פעילה
    #library.select_active_lending_details()
    pass

# while input('Enter full name:') != operator.first_name + ' ' + operator.last_name:
#     print('The name does not match the one registered in the system')
#
# while input('Enter password:') != operator.operator_password:
#     print('The password does not match the one registered in the system')

if __name__ == '__main__':
    main()


