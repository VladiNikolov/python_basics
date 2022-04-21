# book_title = input()
# count_books = 0
# book_is_found = False
# next_book = input()
#
# while next_book != "No More Books":
#     if next_book == book_title:
#         book_is_found = True
#         break
#     count_books += 1
#     next_book = input()
# if book_is_found:
#     print(f"You checked {count_books} books and found it.")
# else:
#     print(f"The book you search is not here!")
#     print(f"You checked {count_books} books.")
#
#
book_title = input()
count_book = 0
next_book = input()

while next_book != "No More Books":
    if next_book == book_title:
        next_book = book_title
        break
    count_book += 1
    next_book = input()
if next_book == book_title:
    print(f"You checked {count_book} books and found it."  )
else:
    print("The book you search is not here!")
    print(f"You checked {count_book} books.")