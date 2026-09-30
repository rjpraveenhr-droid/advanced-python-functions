# Library Book Availability Checker

books = ["The Psychology of Money", "DNA", "The Truth in True Crime", "Narnia"]
copies = [5, 0, 3, 2]

# Pair book names with copy counts
book_data = dict(zip(books, copies))

print("Book availability:")
for book, count in book_data.items():
    if count > 0:
        print(book, "-", count, "copies available")

# Update late fees using map()
late_fees = [10, 20, 15, 25]

updated_fees = list(map(lambda fee: fee + 5, late_fees))

print("Updated late fees:", updated_fees)

# Combine books and updated fees using zip()
book_fees = list(zip(books, updated_fees))

print("Book late fees:")
for book, fee in book_fees:
    print(book, "-", fee)

# Check if a chosen book is unavailable
chosen_book = input("Enter the book you want: ")

if book_data[chosen_book] == 0:
    print("Book is unavailable!")
else:
    print("Book is available!")

print("Checking complete!")