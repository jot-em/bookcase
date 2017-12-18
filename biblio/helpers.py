def helper_numbered_books_dict(books):
	book_dict = {}
	i = 1
	for el in books:
		book_dict[i] = el
		i += 1
	return book_dict