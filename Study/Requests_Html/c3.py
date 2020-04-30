class BookCollection:
    def __init__(self):
        self.data = ['《往事》','《只能》','《回味》']
    def __iter__(self):
        pass
    def __next__(self):
        pass
if __name__ == '__main__':
    books = BookCollection
    for book in books:
        print(book)