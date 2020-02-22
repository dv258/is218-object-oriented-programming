class Library:
	def __init__(self, books):
		self.books = []
		for b in books:
			self.books.append(b)

		self.__bookLookupTitleCache = {}

	def findBookByTitle(self, title):
		if title in self.__bookLookupTitleCache:
			return self.__bookLookupTitleCache[title]

		foundBook = None

		for b in self.books:
			if b.title == title:
				foundBook = b
				break

		if foundBook is None:
			return None

		self.__bookLookupTitleCache[foundBook.title] = foundBook
		return foundBook

class Book:
	def __init__(self, title, contents):
		self.title = title
		self.contents = contents
