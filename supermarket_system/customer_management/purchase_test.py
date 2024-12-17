import unittest
from unittest.mock import patch
import sys
import os
sys.path.append('../../')
from supermarket_system.customer_management.purchase_management import purchase
from supermarket_system.customer_management.records_management import record
from supermarket_system.product_management.sales_management import sales
from supermarket_system.product_management.warehouse_management import warehouse

class TestPurchase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Setup resources shared across all test cases."""
        cls.record = record()
        cls.product = warehouse()
        cls.product.add_product("001", "Apple", "Fruit", 2.5, "2024-11-26", 100)
        cls.sales = sales(cls.product)
        cls.membership = "CUST123"
        print("TestPurchase: SetupClass executed.")

    @classmethod
    def tearDownClass(cls):
        """Clean up resources shared across all test cases."""
        del cls.record
        del cls.sales
        del cls.product
        print("TestPurchase: TearDownClass executed.")

    def setUp(self):
        """Setup resources for each test case."""
        self.purchase = purchase(self.membership, self.record)
        self.sales.add_newproduct("001", 10, 5)
        print("TestPurchase: Setup executed.")

    def tearDown(self):
        """Clean up resources after each test case."""
        del self.purchase
        print("TestPurchase: TearDown executed.")
    
    @patch("builtins.input", side_effect=["A", "001", "2", "D", "001", "1", "exit"])
    def test_add_and_remove_from_cart(self, mock_input):
        """Test adding and removing items from the cart."""
        # Simulate adding and then removing items from the cart
        self.purchase.choose(self.membership, self.sales)
        
        # Assertions after add and remove
        # Check the cart contents
        self.assertEqual(len(self.purchase.purchases), 1, "Cart should still contain 1 item.")
        self.assertEqual(self.purchase.purchases[0]["name"], "Apple", "The item name should be 'Apple'.")
        self.assertEqual(self.purchase.purchases[0]["quantity"], 1, "The quantity should be 1 after removing 1.")
        self.assertEqual(self.purchase.purchases[0]["price"], 5, "The price should still be 5.")
        
        # Check the sales shelf stock
        self.assertEqual(self.sales.shelves["001"]["quantity"], 9, "Sales shelf should reflect restocked item after removal.")

    @patch("builtins.input", side_effect=["A", "001", "2", "exit"])
    def test_checkout(self, mock_input):
        """Test the checkout process."""
        
        # Simulate adding items to the cart
        self.purchase.choose(self.membership, self.sales)
        
        # Simulate checkout
        result = self.purchase.checkout()
        

        
        # Check if purchases are cleared after checkout
        self.assertEqual(len(self.purchase.purchases), 0, "Cart should be empty after checkout.")
    
        # Check the record has been added correctly
        self.assertEqual(len(self.record.history), 1, "Record should be added to the system.")
        record_entry = self.record.history.get(self.membership, [])

        self.assertEqual( [ record["total_price"] for record in record_entry], [10], "Total price in the record should match the checkout total.")
        self.assertEqual( [ record["profit"] for record in record_entry], [5], "Profit in the record should match the profit made.")
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPurchase)
    unittest.TextTestRunner(verbosity=2).run(suite)

run_tests()
