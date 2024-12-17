

import sys
import unittest
sys.path.append('../../')
from supermarket_system.product_management.sales_management import sales # type: ignore
from supermarket_system.product_management.warehouse_management import warehouse # type: ignore

class TestSales(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up TestSales Class...")
        cls.warehouse = warehouse()
        cls.sales = sales(cls.warehouse)

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestSales Class...")
        del cls.sales
        del cls.warehouse
    
    def setUp(self):
        print("Setting up for a test...")
        self.warehouse = warehouse()
        self.sales = sales(self.warehouse)
        self.warehouse.add_product("001", "Milk", "Dairy", 2.5, "2024-11-26", 100)
        self.warehouse.add_product("002", "Eggs", "Dairy", 5.0, "2024-11-27", 200)

    def tearDown(self):
        print("Tearing down after a test...")
        del self.sales
        del self.warehouse

    def test_add_newproduct(self):
        
        self.sales.add_newproduct("001", 50, 3.0)
        self.assertIn("001", self.sales.shelves)
        self.assertEqual(self.sales.shelves["001"]["quantity"], 50)
        self.assertEqual(self.sales.shelves["001"]["sprice"], 3.0)
        self.assertEqual(self.warehouse.products["001"]["quantity"], 50)

    def test_increase_quantity(self):
        self.sales.add_newproduct("001", 50, 3.0)
        self.sales.increase_quantity("001", 20)
        self.assertEqual(self.sales.shelves["001"]["quantity"], 70)
        self.assertEqual(self.warehouse.products["001"]["quantity"], 30)  # Reduced in warehouse

    def test_decrease_quantity(self):
        self.sales.add_newproduct("001", 50, 3.0)
        self.sales.decrease_quantity("001", 20)
        self.assertEqual(self.sales.shelves["001"]["quantity"], 30)
        self.assertEqual(self.warehouse.products["001"]["quantity"], 70)  # Returned to warehouse

    def test_change_price(self):
        self.sales.add_newproduct("001", 50, 3.0)
        self.sales.change_price("001", 4.0)
        self.assertEqual(self.sales.shelves["001"]["sprice"], 4.0)
        self.assertIn("001", self.sales.shelves)

    def test_display(self):
        self.sales.add_newproduct("001", 50, 3.0)
        self.sales.display()
        self.assertIn("001", self.sales.shelves)
        self.assertEqual(self.sales.shelves["001"]["name"], "Milk")
        self.assertEqual(self.sales.shelves["001"]["quantity"], 50)
        self.assertEqual(self.sales.shelves["001"]["sprice"], 3.0)




def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSales)
    unittest.TextTestRunner(verbosity=2).run(suite)

run_tests()

