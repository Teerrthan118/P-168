class Bookshelf:
    def __init__(self,name,author,price,publishing_year):
        self.book_name = name
        self.author = author
        self.price = price
        self.publishing_year = publishing_year
    
    def add_book(self):
        print("Book Name: "+self.book_name)
        print("Author Name: "+self.author)
        print("Price: "+ str(self.price))
        print("Publishing Year: "+ str(self.publishing_year))
        print("Book Added")
    
    def years_since_published(self):
        years_ago_published = 2023 - self.publishing_year
        print("This book was published " + str(years_ago_published) + " years ago")

Book1 = Bookshelf("Harry Potter and the Philosopher's Stone","J.K. Rowling",1928,1997)
Book1.add_book()
Book1.years_since_published()

Book2 = Bookshelf("Diary of a Wimpy Kid","Jeff Kinney",700,2017)
Book2.add_book()
Book2.years_since_published()