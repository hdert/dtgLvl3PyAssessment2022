"""Define the third out of three ways to create child objects."""


class Child:
    """The child stores all of the details about itself."""

    def __init__(self, name: str, balance: float) -> None:
        """Initialize the Child object."""
        self.name = str(name)
        self._balance = round(float(balance), 2)

    def bonus(self) -> str:
        """Return the bonus state as an emoji so it can be used in the UI."""
        if self._balance >= 50.00:
            return "✅"
        return "❌"

    def deduct_balance(self, deduction_amount: float) -> None:
        """Deduct balance for object."""
        # Even if deduction amount is 0.001 greater than self._balance, the
        # last round operation in else should bring the total to 0, which is
        # valid.
        if round(float(deduction_amount), 2) > self._balance:
            raise ValueError("Deduction Amount is greater than balance.")
        else:
            # The round() wraps around the whole statement because of a
            # hardware limitation where 50 - 49.99 = 0.00999999999999801
            # instead of 50 - 49.99 = 0.01.
            self._balance = round(self._balance - float(deduction_amount), 2)

    def set_balance(self, new_balance: float) -> None:
        """Set balance for object."""
        self._balance = round(float(new_balance), 2)

    def get_balance(self) -> float:
        """Get the balance of the object."""
        return self._balance


if __name__ == '__main__':
    import unittest

    child_1 = [Child("Nicky", 1500), ["Nicky", 1500.00, "✅"]]
    child_2 = [Child("Ricky", 50), ["Ricky", 50.00, "✅"]]
    child_3 = [Child("Dicky", 49.99), ["Dicky", 49.99, "❌"]]
    child_4 = [Child("Dawn", 49.999), ["Dawn", 50.00, "✅"]]
    child_5 = [Child("Angelica", 49.9944444444445), ["Angelica", 49.99, "❌"]]
    child_6 = [Child("Eliza", 0), ["Eliza", 0, "❌"]]
    children = [child_1, child_2, child_3, child_4, child_5, child_6]

    class SimpleTest(unittest.TestCase):
        """Run tests on the Child object."""

        def test_children(self):
            """Test that the predefined children have the correct values."""
            for child in children:
                self.assertEqual(child[0].name, child[1][0])
                self.assertEqual(child[0].get_balance(), child[1][1])
                self.assertEqual(child[0].bonus(), child[1][2])

        def test_modify_children(self):
            """Test modification of the children objects."""
            for child in children:
                child[0].name = "L" + child[0].name[1:]
                child[1][0] = "L" + child[1][0][1:]
                self.assertEqual(child[0].name, child[1][0])
                child[0].deduct_balance(-50)
                child[1][1] += 50
                self.assertEqual(child[0].get_balance(), round(child[1][1], 5))
                self.assertEqual(child[0].bonus(), "✅")
                child[0].deduct_balance(50.001)
                child[1][1] -= 50
                self.assertEqual(child[0].get_balance(), round(child[1][1], 5))
                self.assertEqual(child[0].bonus(), child[1][2])
                child[0].set_balance(49.99)
                self.assertEqual(child[0].get_balance(), 49.99)
                self.assertEqual(child[0].bonus(), "❌")

    unittest.main()
