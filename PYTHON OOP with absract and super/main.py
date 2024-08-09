from absuper import Product


class PhysicalProduct(Product):
    def __init__(self, name, base_price, shipping_cost, tax_rate):
        super().__init__(name, base_price)
        self.shipping_cost = shipping_cost
        self.tax_rate = tax_rate

    def calculate_total_price(self):
        tax = self.base_price * self.tax_rate
        total_price = self.base_price + tax + self.shipping_cost
        return total_price


class DigitalProduct(Product):
    def __init__(self, name, base_price, discount_rate):
        super().__init__(name, base_price)
        self.discount_rate = discount_rate

    def calculate_total_price(self):
        discount = self.base_price * self.discount_rate
        total_price = self.base_price - discount
        return total_price


if __name__ == "__main__":
    physical_product = PhysicalProduct(name="Laptop", base_price=1000, shipping_cost=50, tax_rate=0.1)
    digital_product = DigitalProduct(name="Ebook", base_price=50, discount_rate=0.2)

    print(f"Total price for {physical_product.name}: ${physical_product.calculate_total_price():.2f}")
    print(f"Total price for {digital_product.name}: ${digital_product.calculate_total_price():.2f}")