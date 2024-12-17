import unittest
import unittest
import sys
sys.path.append('../../')
from supermarket_system.product_management.warehouse_management import warehouse


class TestWarehouse(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        print("Setting up TestWarehouse Class...")
        cls.warehouse = warehouse()

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestWarehouse Class...")
        del cls.warehouse

    def setUp(self):
        print("Setting up for a test...")
        self.warehouse = warehouse()
        self.warehouse.add_product("001", "Milk", "Dairy", 2.5, "2024-11-26", 100)

    def tearDown(self):
        print("Tearing down after a test...")
        del self.warehouse

    def test_add_product(self):
        self.warehouse.add_product("002", "Bread", "Bakery", 3.0, "2024-11-27", 50)
        self.assertIn("002", self.warehouse.products)
        self.assertEqual(self.warehouse.products["002"]["quantity"], 50)
        self.assertEqual(self.warehouse.products["002"]["name"], "Bread")
        self.assertEqual(len(self.warehouse.products), 2)

    def test_remove_product(self):
        self.warehouse.remove_product("001", 50)
        self.assertEqual(self.warehouse.products["001"]["quantity"], 50)

        self.warehouse.remove_product("001", 50)
        self.assertNotIn("001", self.warehouse.products)

        #with self.assertLogs(level='WARNING') as log:
         #   self.warehouse.remove_product("002", 10)  # Attempt to remove non-existent product
          #  self.assertIn("There is no this product", log.output[0])

    def test_display(self):
        self.warehouse.add_product("002", "Eggs", "Dairy", 5.0, "2024-11-27", 200)
        self.warehouse.display()
        self.assertIn("001", self.warehouse.products)
        self.assertIn("002", self.warehouse.products)


def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWarehouse)
    unittest.TextTestRunner(verbosity=2).run(suite)

run_tests()