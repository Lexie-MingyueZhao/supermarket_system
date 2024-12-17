class purchase():
    """
    Represents a customer's purchase process, including adding/removing items from the cart, 
    displaying available items, and completing the checkout.

    Attributes:
        purchases (list): A list of dictionaries representing the items in the cart. 
                          Each item includes its name, price, quantity, and purchase price.
        customerId (str): The ID of the customer (membership identifier).
        record (object): A record-keeping object for storing purchase transactions.

    Methods:
        __init__(self, membership, record):
            Initializes the purchase object with customer membership and record-keeping system.

        display(self, sales):
            Displays the available items in the sales shelves using the sales object.

        choose(self, membership, sales):
            Allows the customer to add or remove items from the cart. 
            Updates the sales shelf quantities accordingly.

        checkout(self):
            Completes the checkout process, calculates the total price, 
            logs the transaction in the record system, and computes the profit.
    """
    def __init__(self,membership,record):
        self.purchases=[]
        self.customerId = membership
        self.record = record
    def display(self,sales):
        sales.display()
    def choose(self,membership,sales):
        while(True):
            sales.display()
            a = input("Do you want to add(A) to or delete(D) some goods from your cart?(or 'exit' to stop)")
            if a.lower() == 'exit':
                print("Exiting the add-to-cart process.")
                break
            
            else:
                if a=="A":
                    productId = input ("Enter the product id to add to your cart:")
                    if  productId not in sales.shelves:
                        print("Sorry, the product code is not valid.")
                        continue
                    else:
                        quantity = int(input(f"Enter the quantity for {sales.shelves[productId]['name']}: "))
                        if sales.shelves[productId]["quantity"] < quantity:
                            print("Sorry, insufficient stock on the shelf.")
                        else:
                            self.purchases.append({
                                "name": sales.shelves[productId]["name"],
                                "price": sales.shelves[productId]["sprice"],
                                "quantity": quantity,
                                 "pprice" : sales.shelves[productId]["pprice"]
                            })
                            sales.shelves[productId]["quantity"] -= quantity
                            print(f"{quantity} x {sales.shelves[productId]['name']} added to your cart.")
                elif a=="D":
                    if not self.purchases:
                        print("There are no gooods in your cart, add some first please")
                    else:
                        productId = input ("Enter the product id to remove from your cart:")
                        if productId in sales.shelves:
                            for item in self.purchases:
                                #print(item["name"] == sales.shelves[productId]["name"])
                                if item["name"] == sales.shelves[productId]["name"]:
                                    quantity = int(input(f"Enter the quantity for {sales.shelves[productId]['name']}: "))
                                    if item["quantity"] >= quantity:
                                        item["quantity"] -= quantity
                                        sales.shelves[productId]["quantity"] += quantity
                                        print(f"{quantity} x {sales.shelves[productId]['name']} remove from your cart.")
                                        break
                                        if item["quantity"] == 0:
                                            del item[productId]
                                            print(f"{sales.shelves[productId]['name']} remove from your cart.")
                                            break
                                    else:
                                        print(" the quantity is outweight")
                                        break
                                else:
                                    print("The id is wrong")
                            else:
                                print("The id is wrong")
                        else:
                            print("There is no that goods in your cart ")
                else:   
                    print("Please enter A, D or exit")

                
    
    
                    
    
    def checkout(self):
         if not self.purchases:
            return "Your cart is empty"
        
         total_price = 0
         profit = 0
         cal_q = {}
         print("Items in your cart:")
         for item in self.purchases:
             total_price += item["price"] * item["quantity"]
             profit += (item["price"]-item["pprice"]) * item["quantity"]
             print(f"{item['name']} - Quantity: {item['quantity']}, Price: {item['price']}, Total: {item['price'] * item['quantity']}")
             if item['name'] not in cal_q:
                 cal_q[item['name']] = item['quantity']
             else:
                 cal_q[item['name']] += item['quantity']
         print(f"Total Price: {total_price}")

         self.record.add_record(self.customerId, self.purchases, total_price, profit,cal_q)
        
         self.customers = []