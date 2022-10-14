"""Define the second out of three ways to create child objects."""


class Child:
    """The child stores all of the details about itself."""

    def __init__(self, name, balance):
        """Initialize the Child object."""
        self.name = name
        self.balance = round(float(balance), 2)

    def bonus(self):
        """Return the bonus state as an emoji so it can be used in the UI."""
        if self.balance >= 50.00:
            return "✅"
        return "❌"


if __name__ == '__main__':
    import unittest

    child_1 = [Child("Nicky", 1500), ["Nicky", 1500.00, "✅"]]
    child_2 = [Child("Ricky", 50), ["Ricky", 50.00, "✅"]]
    child_3 = [Child("Dicky", 49.99), ["Dicky", 49.99, "❌"]]
    child_4 = [Child("Dawn", 49.999), ["Dawn", 50.00, "✅"]]
    child_5 = [Child("Eliza", 49.9944444444445), ["Eliza", 49.99, "❌"]]
    children = [child_1, child_2, child_3, child_4, child_5]

    class SimpleTest(unittest.TestCase):
        """Run tests on the Child object."""

        def test_children(self):
            """Test that the predefined children have the correct values."""
            for child in children:
                self.assertEqual(child[0].name, child[1][0])
                self.assertEqual(child[0].balance, child[1][1])
                self.assertEqual(child[0].bonus(), child[1][2])

        def test_modify_children(self):
            """Test modification of the children objects."""
            for child in children:
                child[0].name = "L" + child[0].name[1:]
                child[1][0] = "L" + child[1][0][1:]
                self.assertEqual(child[0].name, child[1][0])
                child[0].balance += 50
                child[1][1] += 50
                self.assertEqual(child[0].balance, child[1][1])
                self.assertEqual(child[0].bonus(), "✅")
                child[0].balance -= 50.00
                child[1][1] -= 50
                self.assertEqual(child[0].balance, child[1][1])
                self.assertEqual(child[0].bonus(), child[1][2])
                child[0].balance = 49.99
                self.assertEqual(child[0].balance, 49.99)
                self.assertEqual(child[0].bonus(), "❌")

    unittest.main()
