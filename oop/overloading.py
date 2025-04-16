class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        match key:
            case "title":
                return self.title
            case "author":
                return self.author
            case "num_pages":
                return self.num_pages
            case _:
                return f"Key {key} was not found"


book1 = Book("Code", "C. Petzold", 480)
book2 = Book("Structured Computer Organization", "A.S. Tanenbaum", 801)
book3 = Book("Grokking Algorithms", "A.Y Bhargava", 256)
book4 = Book("Code", "C. Petzold", 480)

books = [book1, book2, book3]

for book in books:
    print(book)

print(book1 == book4)
print(book2 < book3)
print(book2 > book3)
print(book1 + book3)
print("Code" in book1)
print(book1["title"])
print(book1["author"])
print(book1["num_pages"])
print(book1["audio"])
