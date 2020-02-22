class Library:
	def __init__(self, books):
		# store books in an array
		self.books = []
		for b in books:
			self.books.append(b)

		# a cache of books, where the map's keys are the book titles
		self.__bookLookupTitleCache = {}

	def findBookByTitle(self, title):
		#the caller does not know about the internal storing or caching mechanism

		#if the book is cached, just return the cached value
		if title in self.__bookLookupTitleCache:
			return self.__bookLookupTitleCache[title]

		foundBook = None

		#look for the book in the list of books
		for b in self.books:
			if b.title == title:
				foundBook = b
				break

		#book not found
		if foundBook is None:
			return None

		#add book to cache
		self.__bookLookupTitleCache[foundBook.title] = foundBook
		return foundBook

class Book:
	def __init__(self, title, contents):
		self.title = title
		self.contents = contents
