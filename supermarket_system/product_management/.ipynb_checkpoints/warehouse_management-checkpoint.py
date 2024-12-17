class warehouse():
    def __init__(self):
        self.products={}
    def add_product(self,productId, productname, category, purchaseprice, entrydate, quantity):
        if productId in self.products:
            self.products[productId]["quantity"] += quantity
        else:
            self.products[productId]={
                "name": productname,
                "category": category,
                "pprice" : purchaseprice,
                "edate" : entrydate,
                "quantity" : quantity
            }
    def remove_product(self, productId, quantity):
        if productId in self.products and self.products[productId]["quantity"] >= quantity:
            self.products[productId]["quantity"] -= quantity
            if self.products[productId]["quantity"] == 0:
                del self.products[productId]
        else:
            print("There is no this product or the quantity is greater than the quantity in warehouse")
    def display(self):
        for id, product in self.products.items():
            print(id, product['name'], product['category'], product['pprice'], product['edate'], product['quantity'])

        
            