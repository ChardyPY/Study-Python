class Book:
    def __init__(self, pages, for_sale, price):
        self.pages = pages
        self.for_sale = for_sale
        self.price = price

    def openbook(self):
        print(f"The book page is {self.pages}")