import unittest
from logica import FinanceManager, Movement, Category


class TestCategory(unittest.TestCase):

    def test_create_category(self):
        cat = Category("Food")
        self.assertEqual(cat.name, "Food")

    def test_str_category(self):
        cat = Category("Transport")
        self.assertEqual(str(cat), "Transport")


class TestManagerCategories(unittest.TestCase):

    def setUp(self):
        self.manager = FinanceManager()

    def test_add_category(self):
        self.manager.add_category("Health")
        self.assertIn("Health", self.manager.get_categories())

    def test_get_categories_empty(self):
        self.assertEqual(self.manager.get_categories(), [])

    def test_add_multiple_categories(self):
        self.manager.add_category("Food")
        self.manager.add_category("Work")
        self.assertEqual(len(self.manager.get_categories()), 2)


class TestManagerMovements(unittest.TestCase):

    def setUp(self):
        self.manager = FinanceManager()
        self.manager.add_category("Work")
        self.manager.add_category("Food")

    def test_add_income(self):
        self.manager.add_movement("Salary", 1000.0, "Work", "Income")
        movements = self.manager.get_movements()
        self.assertEqual(len(movements), 1)
        self.assertEqual(movements[0].type, "Income")

    def test_add_expense(self):
        self.manager.add_movement("Lunch", 50.0, "Food", "Expense")
        movements = self.manager.get_movements()
        self.assertEqual(movements[0].title, "Lunch")

    def test_calculate_positive_balance(self):
        self.manager.add_movement("Salary", 1000.0, "Work", "Income")
        self.manager.add_movement("Lunch", 200.0, "Food", "Expense")
        self.assertEqual(self.manager.calculate_balance(), 800.0)

    def test_calculate_empty_balance(self):
        self.assertEqual(self.manager.calculate_balance(), 0.0)

    def test_movement_has_date(self):
        self.manager.add_movement("Salary", 1000.0, "Work", "Income")
        movement = self.manager.get_movements()[0]
        self.assertIsNotNone(movement.date)


if __name__ == "__main__":
    unittest.main()