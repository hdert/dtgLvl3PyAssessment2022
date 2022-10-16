"""A module with everything required for unittests."""
from add_child import *
import unittest

user_input_test_change_list: list[tuple[str | float, bool,
                                        float]] = [(1000000, False, 0),
                                                   (-1000000, False, 0),
                                                   (-1, True, 0), (0, True, 0),
                                                   ("string", False, 0),
                                                   (1, True, 1),
                                                   (999999, True, 999999),
                                                   (-999999, True, 0),
                                                   (-999999, False, 1),
                                                   (-1, False, 999999)]
user_input_test_reset_list: list[tuple[str | float,
                                       bool]] = [(1000000, False),
                                                 (-1000000, False),
                                                 (-1, False), (0, True),
                                                 ("string", False),
                                                 (999999, True),
                                                 (-999999, False)]

child_verification_list: list[tuple[str | int, float, str]] = [
    ("Nicky", 1500.00, "✅"), ("Ricky", 50.00, "✅"), ("Dicky", 49.99, "❌"),
    ("Dawn", 50.00, "✅"), ("Angelica", 49.99, "❌"), ("Eliza", 0.00, "❌"),
    ("Eliza", 0.00, "❌"), ("Eliza", 0.00, "❌"), ("Eliza", 0.00, "❌"),
    ("Eliza", 0.00, "❌"), ("Eliza", 0.00, "❌"), ("Eliza", 0.00, "❌"),
    ("Robert, and Bobby", 0.00, "❌"), ("DropTables", 0.00, "❌"),
    ("""Overflow,9999\nEliza""", 0.0, "❌"),
    ("""Overflow29999\nEliza""", 0.0, "❌"), ("999", 0.0, "❌")
]


class SimpleTest(unittest.TestCase):
    """Run tests on the Child object."""

    def test_children(self) -> None:
        """Test that the predefined children have the correct values."""
        for i, child in enumerate(child_list):
            self.assertEqual(child.name, child_verification_list[i][0])
            self.assertEqual(child.get_balance(),
                             child_verification_list[i][1])
            self.assertEqual(child.bonus(), child_verification_list[i][2])

    def test_modify_children(self) -> None:
        """Test modification of the children objects."""
        for i, child in enumerate(child_list):
            child.name = "L" + child.name[1:]
            child_verification_list[i] = (
                "L" + str(child_verification_list[i][0])[1:],
                child_verification_list[i][1], child_verification_list[i][2])
            self.assertEqual(child.name, child_verification_list[i][0])
            child.deduct_balance(-50)
            child_verification_list[i] = (child_verification_list[i][0],
                                          round(
                                              child_verification_list[i][1] +
                                              50, 2),
                                          child_verification_list[i][2])
            self.assertEqual(child.get_balance(),
                             round(child_verification_list[i][1], 5))
            self.assertEqual(child.bonus(), "✅")
            child.deduct_balance(50.001)
            child_verification_list[i] = (child_verification_list[i][0],
                                          child_verification_list[i][1] - 50,
                                          child_verification_list[i][2])
            self.assertEqual(child.get_balance(),
                             round(child_verification_list[i][1], 5))
            self.assertEqual(child.bonus(), child_verification_list[i][2])
            child.set_balance(49.99)
            self.assertEqual(child.get_balance(), 49.99)
            self.assertEqual(child.bonus(), "❌")

    def test_user_input_change(self) -> None:
        """Test user input deduct handling."""
        deduct_change_radio_button_result.set(0)
        selected_child = child_select_radio_button_result.get()
        for value in user_input_test_change_list:
            child_list[selected_child].set_balance(value[2])
            value_entry_variable.set(str(value[0]))
            handle_user_input()
            child_balance = child_list[selected_child].get_balance()
            if value[1] is True:
                self.assertEqual(value[2] - float(value[0]), child_balance)
            else:
                self.assertEqual(value[2], child_balance)
                if value[0] is float:
                    self.assertNotEqual(value[2] - float(value[0]),
                                        child_balance)

    def test_user_input_reset(self) -> None:
        """Test user input reset handling."""
        deduct_change_radio_button_result.set(1)
        selected_child = child_select_radio_button_result.get()
        for value in user_input_test_reset_list:
            child_list[selected_child].set_balance(999999)
            value_entry_variable.set(str(value[0]))
            handle_user_input()
            child_balance = child_list[selected_child].get_balance()
            if value[1] is True:
                self.assertEqual(value[0], child_balance)
            else:
                self.assertEqual(999999, child_balance)
                self.assertNotEqual(value[0], child_balance)


if __name__ == "__main__":

    get_saved_data()
    configure_global(root)
    unittest.main()
