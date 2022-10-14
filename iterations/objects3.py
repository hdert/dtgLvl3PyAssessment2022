"""Define the fourth :) out of three ways to create child objects."""
from tkinter import Tk, ttk, StringVar
from typing import List

root = Tk()
root.title("Placeholder Text")
root.minsize(350, 400)

root.geometry("350x400")


class Child:
    """The child stores all of the details about itself."""

    def __init__(self, name: str, balance: float) -> None:
        """Initialize the Child object."""
        self.name = str(name)
        self._balance = round(float(balance), 2)
        child_list.append(self)

        self._name_variable = StringVar()
        self._name_variable.set(self.name)

        self._balance_variable = StringVar()
        self._balance_variable.set(str(self._balance))

        self._bonus_variable = StringVar()
        self._bonus_variable.set(self.bonus())

        self._frame = ttk.Frame(root)
        self._frame.grid(row=0, column=(len(child_list) - 1), padx=0, pady=0)

        self._name_widget = ttk.Label(self._frame,
                                      textvariable=self._name_variable,
                                      font="bold")
        self._name_widget.grid(row=0, column=0)

        self._balance_label_widget = ttk.Label(self._frame,
                                               text="Account Balance:")
        self._balance_label_widget.grid(row=1, column=0)

        self._balance_widget = ttk.Label(self._frame,
                                         textvariable=self._balance_variable)
        self._balance_widget.grid(row=2, column=0)

        self._bonus_label = ttk.Label(self._frame, text="Bonus:")
        self._bonus_label.grid(row=3, column=0)

        self._bonus_widget = ttk.Label(self._frame,
                                       textvariable=self._bonus_variable)
        self._bonus_widget.grid(row=4, column=0)

        for widget in self._frame.winfo_children():
            widget.grid_rowconfigure(0, weight=1)
            widget.grid_columnconfigure(0, weight=1)
            widget.grid(sticky="N")
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)

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


child_list: List = []

if __name__ == '__main__':
    import unittest

    Child("Nicky", 1500)
    Child("Ricky", 50)
    Child("Dicky", 49.99)
    Child("Dawn", 49.999)
    Child("Angelica", 49.9944444444445)
    Child("Eliza", 0)

    child_verification_list = [["Nicky", 1500.00, "✅"], ["Ricky", 50.00, "✅"],
                               ["Dicky", 49.99, "❌"], ["Dawn", 50.00, "✅"],
                               ["Angelica", 49.99, "❌"], ["Eliza", 0.00, "❌"]]

    class SimpleTest(unittest.TestCase):
        """Run tests on the Child object."""

        def test_children(self):
            """Test that the predefined children have the correct values."""
            for i, child in enumerate(child_list):
                self.assertEqual(child.name, child_verification_list[i][0])
                self.assertEqual(child.get_balance(),
                                 child_verification_list[i][1])
                self.assertEqual(child.bonus(), child_verification_list[i][2])

        def test_modify_children(self):
            """Test modification of the children objects."""
            for i, child in enumerate(child_list):
                child.name = "L" + child.name[1:]
                child_verification_list[i][
                    0] = "L" + child_verification_list[i][0][1:]
                self.assertEqual(child.name, child_verification_list[i][0])
                child.deduct_balance(-50)
                child_verification_list[i][1] += 50
                self.assertEqual(child.get_balance(),
                                 round(child_verification_list[i][1], 5))
                self.assertEqual(child.bonus(), "✅")
                child.deduct_balance(50.001)
                child_verification_list[i][1] -= 50
                self.assertEqual(child.get_balance(),
                                 round(child_verification_list[i][1], 5))
                self.assertEqual(child.bonus(), child_verification_list[i][2])
                child.set_balance(49.99)
                self.assertEqual(child.get_balance(), 49.99)
                self.assertEqual(child.bonus(), "❌")

    root.mainloop()
    unittest.main()
