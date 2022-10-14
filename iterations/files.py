"""The first of three implementations of the saving, and opening functions."""
from tkinter import Tk, ttk, StringVar, IntVar
from typing import Union, List

child_list: List = []

# Initialize Tk window, widgets, and Tk Variables

x_default = 325
y_default = 375

root = Tk()
root.title("Placeholder Text")
root.minsize(x_default, y_default)

root.geometry(f"{x_default}x{y_default}")

# Frames

main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0)

# Information frame

info_frame = ttk.Frame(main_frame)
info_frame.grid(row=0, column=0, padx=0, pady=10)

# Action select frame

selection_frame = ttk.Frame(main_frame)
selection_frame.grid(row=1, column=0, padx=0, pady=0)

# Entry and confirmation frame

input_frame = ttk.Frame(main_frame)
input_frame.grid(row=2, column=0, padx=0, pady=10)

# Action Select Frame Variables

deduct_change_radio_button_result = IntVar()
deduct_change_radio_button_result.set(0)

child_select_radio_button_result = IntVar()

# Action Select Frame Contents

deduct_change_label = ttk.Label(selection_frame,
                                text="Deduct or Change Allowance",
                                font="bold")
deduct_change_label.grid(row=0, column=0, padx=0, pady=0)

deduct_radio_button = ttk.Radiobutton(
    selection_frame,
    text="Deduct",
    variable=deduct_change_radio_button_result,
    value=0)
deduct_radio_button.grid(row=1, column=0, padx=0, pady=0)

reset_radio_button = ttk.Radiobutton(
    selection_frame,
    text="Reset/Change",
    variable=deduct_change_radio_button_result,
    value=1)
reset_radio_button.grid(row=2, column=0, padx=0, pady=0)

select_child_label = ttk.Label(selection_frame,
                               text="Select Child",
                               font="bold")
select_child_label.grid(row=3, column=0, padx=0, pady=0)

# Entry and Confirmation Frame Variables

value_entry_variable = StringVar()
value_entry_variable.set("0.00")

value_entry_button_variable = StringVar()
value_entry_button_variable.set("Deduct/Set Allowance [change]")

# Entry and Confirmation Frame Contents

value_entry = ttk.Entry(input_frame, textvariable=value_entry_variable)
value_entry.grid(row=0, column=0, padx=0, pady=0)

value_entry_button = ttk.Button(input_frame,
                                textvariable=value_entry_button_variable)
value_entry_button.grid(row=1, column=0, padx=0, pady=10)

# Add global configuration to all widgets


def configure_global(frame: Union[ttk.Frame, Tk]) -> None:
    """Configure global options for all widgets.

    Args:
        frame (Union[ttk.Frame, Tk]): The Frame or window to do operations on.

    """
    for widget in frame.winfo_children():
        if isinstance(widget, ttk.Frame):
            configure_global(widget)
        else:
            widget.grid_rowconfigure(0, weight=1)
            widget.grid_columnconfigure(0, weight=1)
            # widget.grid(padx=0, pady=0)
            widget.grid(sticky="N")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)


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

        self._frame = ttk.Frame(info_frame)
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

        self._child_selection_radio_button = ttk.Radiobutton(
            selection_frame,
            textvariable=self._name_variable,
            variable=child_select_radio_button_result,
            value=(len(child_list) - 1))
        self._child_selection_radio_button.grid(row=(3 + len(child_list)),
                                                column=0)

        for widget in self._frame.winfo_children():
            widget.grid(pady=5, padx=5)

        root.minsize(
            x_default +
            (((len(child_list) - 3) * 90) if len(child_list) > 3 else 0),
            y_default + ((len(child_list) - 1) * 16))

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


# Files


def get_saved_data() -> None:
    """Get saved object data from file."""
    children_file = open("children.csv", "r")
    children_list = children_file.readlines()

    for child in children_list:
        child_data = child.strip().split(",")
        Child(*child_data)

    children_file.close()


def save_data() -> None:
    """Save object data to file."""
    children_file = open("children.csv", "w")

    for child in child_list:
        children_file.write(f"{child.name},{child.get_balance()}\n")

    children_file.close()


if __name__ == '__main__':

    import unittest

    child_verification_list = [["Nicky", 1500.00, "✅"], ["Ricky", 50.00, "✅"],
                               ["Dicky", 49.99, "❌"], ["Dawn", 50.00, "✅"],
                               ["Angelica", 49.99, "❌"], ["Eliza", 0.00, "❌"],
                               ["Eliza", 0.00, "❌"], ["Eliza", 0.00, "❌"],
                               ["Eliza", 0.00, "❌"], ["Eliza", 0.00, "❌"],
                               ["Eliza", 0.00, "❌"], ["Eliza", 0.00, "❌"]]

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

    get_saved_data()

    configure_global(root)

    # Start the Tk window

    root.mainloop()

    unittest.main()
