searched_book = input()
books_counter = 0
book_is_found = False
next_book = input()

while next_book != 'No More Books': #while next_book != 'searched_book':
    if next_book == searched_book:
        book_is_found = True
        break
    books_counter += 1
    next_book = input()
if book_is_found:    #if book_if_found == True:
    print(f'You checked {books_counter} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {books_counter} books.')