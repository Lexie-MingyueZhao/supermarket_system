import datetime
class record():
    """
    A class to manage and track purchase records and analyze supermarket data.

    Attributes:
        history (dict): A dictionary where each key is a customer ID, and the value is a list of their purchase records.
        q (dict): A dictionary that keeps track of the quantities sold for each product.

    Methods:
        __init__(self):
            Initializes the record object with empty history and quantity trackers.

        add_record(self, customerId, items, totalprice, profit, cal):
            Adds a new purchase record for a customer and updates the product quantity tracker.

        get_history(self, customerId):
            Retrieves and prints the purchase history of a specific customer.

        get_total(self, customerId):
            Calculates and prints the total spending and number of purchases for a specific customer.

        supermarket_situation(self):
            Analyzes and prints supermarket statistics, including total visits, sales, profit, and the most popular product.
    """
    def __init__(self):
        self.history={}
        self.q ={}
    def add_record(self,customerId,items,totalprice,profit,cal):
        if customerId not in self.history:
            self.history[customerId]=[]

        purchase_details = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
            "items": items, 
            "total_price": totalprice,
            "status": "Paid",
             "profit" : profit
        }
        self.history[customerId].append(purchase_details)
        for key, item in cal.items():
            if key not in self.q:
                self.q[key] = item
            else:
                self.q[key] += item

    def get_history(self, customerId):
        #print(self.history)
        try:
            records = self.history.get(customerId, [])
            if not records:
                raise KeyError
        except KeyError:
            print("key Error")
        else:
            #print(records)
            print( [[record["date"], record["items"], record["total_price"],record["status"]] for record in records])

    def get_total(self,customerId):
        if customerId not in self.history:
            return 0
        total_spent = 0
        total_count=0
        for record in self.history[customerId]:
            total_spent += record['total_price']
            total_count += 1
        print(f"total count:{total_count},total spent: {total_spent}")

    def supermarket_situation(self):
        visits=0
        sale=0
        profit = 0
        max_q=0
        name = ""
        for key, records in self.history.items():
            visits += len(records)
            for record in records:
                sale += record["total_price"]
                profit += record["profit"]
        for id, item in self.q.items():
            if item > max_q:
                max_q = item
                name = id
        print(f"total visits: {visits},total sales:{sale}, total profit: {profit}, most popular product:{name} with quantity of {max_q}")
            