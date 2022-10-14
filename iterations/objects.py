"""Define the first out of three ways to create child objects."""


class Child:
    """The child stores all of the details about itself."""

    def __init__(self, name, balance):
        """Initialize the Child object."""
        self.name = name
        self.balance = round(float(balance), 2)
        if self.balance >= 50.00:
            self.bonus = True
        else:
            self.bonus = False


if __name__ == '__main__':
    import unittest

    child_1 = [Child("John", 1500), ["John", 1500.00, True]]
    child_2 = [Child("Nathaniel", 50), ["Nathaniel", 50.00, True]]
    child_3 = [Child("Johnathan", 49.99), ["Johnathan", 49.99, False]]
    child_4 = [Child("Ricky", 49.999), ["Ricky", 50.00, True]]
    child_5 = [Child("Eliza", 49.9944444444445), ["Eliza", 49.99, False]]
    children = [child_1, child_2, child_3, child_4, child_5]

    class SimpleTest(unittest.TestCase):
        """Run tests on the Child object."""

        def test_children(self):
            """Test that the predefined children have the correct values."""
            for child in children:
                self.assertEqual(child[0].name, child[1][0])
                self.assertEqual(child[0].balance, child[1][1])
                self.assertEqual(child[0].bonus, child[1][2])

    unittest.main()
