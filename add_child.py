"""The first of three implementations of the adding children ability."""
from tkinter import Tk, ttk, StringVar, IntVar, Label, messagebox
import pickle

# Initialize Tk window, frames, widgets, and Tk Variables

root = Tk()
root.title("Clothing Allowance Tracker")

# Frames

main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0)

# Information frame

info_frame = ttk.Frame(main_frame)
info_frame.grid(row=0, column=0, padx=0, pady=10)

# Action select frame

selection_frame = ttk.Frame(main_frame)
selection_frame.grid(row=1, column=0)

# Entry and confirmation frame

input_frame = ttk.Frame(main_frame)
input_frame.grid(row=2, column=0, padx=0, pady=10)

# Entry and Confirmation Frame Variables

value_entry_variable = StringVar()
value_entry_variable.set("0.00")

value_entry_button_variable = StringVar()
value_entry_button_variable.set("Deduct Allowance")

user_message_box_text_variable = StringVar()
user_message_box_text_variable.set("")

# Action Select Frame Variables

deduct_change_radio_button_result = IntVar()
deduct_change_radio_button_result.set(0)

child_select_radio_button_result = IntVar()


def change_value_entry_button_text() -> None:
    """Set the value_entry_button text to the correct verb."""
    value_entry_button_variable.set("Deduct Allowance" if (
        deduct_change_radio_button_result.get() == 0) else "Set Allowance")


def handle_user_input() -> None:
    """Handle user input."""
    child_number = child_select_radio_button_result.get()
    value = value_entry_variable.get()

    if deduct_change_radio_button_result.get() == 0:
        child_list[child_number].deduct_balance(value)
    else:
        child_list[child_number].set_balance(value)


def show_user_message(message: str, error: bool = False) -> None:
    """Show the user a message in the GUI."""
    if error is True:
        messagebox.showerror("Error!", message)
    else:
        user_message_box_text_variable.set(message)


def show_add_child_prompt() -> None:
    """Show the child creation widgets."""
    TemplateChild()


# Information Frame Contents

add_child_button = ttk.Button(info_frame,
                              text="Add Child",
                              command=show_add_child_prompt)
add_child_button.grid(row=1, column=0, columnspan=999, pady=(0, 20))

# Action Select Frame Contents

deduct_change_label = ttk.Label(selection_frame,
                                text="Deduct or Change Allowance",
                                font="bold")
deduct_change_label.grid(row=0, column=0)

deduct_radio_button = ttk.Radiobutton(
    selection_frame,
    text="Deduct Allowance",
    variable=deduct_change_radio_button_result,
    value=0,
    command=change_value_entry_button_text)
deduct_radio_button.grid(row=1, column=0)

reset_radio_button = ttk.Radiobutton(
    selection_frame,
    text="Reset Allowance",
    variable=deduct_change_radio_button_result,
    value=1,
    command=change_value_entry_button_text)
reset_radio_button.grid(row=2, column=0)

select_child_label = ttk.Label(selection_frame,
                               text="Select Child",
                               font="bold")
select_child_label.grid(row=3, column=0)

# Entry and Confirmation Frame Contents

value_entry = ttk.Entry(input_frame, textvariable=value_entry_variable)
value_entry.grid(row=0, column=0)

value_entry_button = ttk.Button(input_frame,
                                textvariable=value_entry_button_variable,
                                command=handle_user_input)
value_entry_button.grid(row=1, column=0, padx=0, pady=10)

user_message_box = Label(input_frame,
                         textvariable=user_message_box_text_variable,
                         bg="darkblue",
                         fg="white",
                         font=("default", 8))
user_message_box.grid(row=2, column=0, padx=5, pady=5)

# Add global configuration to all widgets


def configure_global(frame: ttk.Frame | Tk) -> None:
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
            widget.grid(sticky="N")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)


def calculate_minsize() -> None:
    """Calculate the minimum size of the window to show all UI components."""
    return
    min_width = 175
    min_height = 370
    max_name_height = 0

    for child in child_list:
        min_width += max(child._balance_label_widget.winfo_reqwidth(),
                         child._balance_widget.winfo_reqwidth(),
                         child._name_widget.winfo_reqwidth())
        min_height += child._child_selection_radio_button.winfo_reqheight()
        if child._name_widget.winfo_reqheight() > max_name_height:
            max_name_height = child._name_widget.winfo_reqheight()

    if deduct_change_label.winfo_reqwidth() > min_width:
        min_width = deduct_change_label.winfo_reqwidth() + 20

    min_height += max_name_height

    root.minsize(min_width, min_height)
    root.geometry(f"{min_width}x{min_height}")


class TemplateChild:
    """The templateChild is for creating a child."""

    def __init__(self) -> None:
        """Initialize the templateChild."""
        self._child_creation_frame = ttk.Frame(info_frame)
        self._child_creation_frame.grid(row=0, column=len(child_list))

        self._child_name_entry_label = ttk.Label(self._child_creation_frame,
                                                 text="Enter Name:")
        self._child_name_entry_label.grid(row=0, column=0, columnspan=2)

        self._child_name_entry_variable = StringVar()
        self._child_name_entry_variable.set("Name")
        self._child_name_entry = ttk.Entry(
            self._child_creation_frame,
            textvariable=self._child_name_entry_variable)
        self._child_name_entry.grid(row=1, column=0, columnspan=2, pady=(0, 5))

        self._child_allowance_entry_label = ttk.Label(
            self._child_creation_frame, text="Enter Allowance:")
        self._child_allowance_entry_label.grid(row=2, column=0, columnspan=2)

        self._child_allowance_entry_variable = StringVar()
        self._child_allowance_entry_variable.set("0.00")

        self._child_allowance_entry_widget = ttk.Entry(
            self._child_creation_frame,
            textvariable=self._child_allowance_entry_variable)
        self._child_allowance_entry_widget.grid(row=3,
                                                column=0,
                                                columnspan=2,
                                                pady=(0, 5))

        self._child_allowance_cancel_button = ttk.Button(
            self._child_creation_frame,
            text="Cancel",
            command=self.delete_template_child)
        self._child_allowance_cancel_button.grid(row=4, column=0)

        self._child_allowance_create_button = ttk.Button(
            self._child_creation_frame,
            text="Create",
            command=self.create_child)
        self._child_allowance_create_button.grid(row=4, column=1)

        configure_global(self._child_creation_frame)

        calculate_minsize()

    def create_child(self) -> None:
        """Create a child."""
        Child(self._child_name_entry_variable.get(), 0.0)
        deduct_change_radio_button_result.set(1)
        value_entry_variable.set(self._child_allowance_entry_variable.get())
        child_select_radio_button_result.set(len(child_list) - 1)
        self.delete_template_child()
        handle_user_input()

    def delete_template_child(self) -> None:
        """Delete the template child and widgets."""
        self._child_creation_frame.destroy()


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
        self._frame.grid(row=0, column=(len(child_list) - 1))

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

        calculate_minsize()

    def __getstate__(self):
        """Get the state of the instance for saving with pickle."""
        return {'name': self.name, '_balance': self._balance}

    def bonus(self) -> str:
        """Return the bonus state as an emoji so it can be used in the UI."""
        if self._balance >= 50.00:
            return "✅"
        return "❌"

    def deduct_balance(self, deduction_amount: float | str) -> None:
        """Deduct balance for object."""
        try:
            deduction_amount = round(float(deduction_amount), 2)
        except ValueError:
            show_user_message(
                "Value entered needs to be a number, e.g. 15.30, 50", True)
            return
        if abs(deduction_amount) > 999999:
            show_user_message(
                "Value entered too large, " +
                "please enter a value smaller than 1,000,000.", True)
            return
        if deduction_amount > self._balance:
            show_user_message(
                "Cannot deduct more money than is in the account!. " +
                "Please enter an amount smaller than the " +
                "current account balance.", True)
            return
        # The round() wraps around the whole statement because of a
        # hardware limitation where 50 - 49.99 = 0.00999999999999801
        # instead of 50 - 49.99 = 0.01.
        new_balance = round((self._balance - deduction_amount), 2)
        if new_balance > 999999:
            show_user_message(
                "Account value cannot be higher than 1,000,000. " +
                "Please enter a smaller amount")
            return
        self.set_balance(new_balance)

    def set_balance(self, new_balance: float | str) -> None:
        """Set balance for object."""
        try:
            new_balance = round(float(new_balance), 2)
        except ValueError:
            show_user_message(
                "Value entered needs to be a number, e.g. 15.30, 50", True)
            return
        if abs(new_balance) > 999999:
            show_user_message(
                "Value entered too large, " +
                "please enter value smaller than 1,000,000", True)
            return
        if new_balance < 0:
            show_user_message(
                "Value entered needs to be zero or higher, e.g. 0, 15.30, 100",
                True)
            return

        self._balance = new_balance
        self._balance_variable.set(str(self._balance))
        self._bonus_variable.set(self.bonus())

    def get_balance(self) -> float:
        """Get the balance of the object."""
        return self._balance


child_list: list[Child] = []

# Files


def get_saved_data() -> None:
    """Get saved object data from file."""
    with open("save_file.pickle", "rb") as children_file:
        children_list = pickle.load(children_file)

        for child in children_list:
            Child(child.name, child._balance)


def save_data() -> None:
    """Save object data to file."""
    with open("save_file.pickle", "wb") as children_file:
        pickle.dump(child_list, children_file)


if __name__ == '__main__':

    import unittest

    user_input_test_change_list: list[tuple[str | float, bool,
                                            float]] = [(1000000, False, 0),
                                                       (-1000000, False, 0),
                                                       (-1, True, 0),
                                                       (0, True, 0),
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
                    child_verification_list[i][1],
                    child_verification_list[i][2])
                self.assertEqual(child.name, child_verification_list[i][0])
                child.deduct_balance(-50)
                child_verification_list[i] = (
                    child_verification_list[i][0],
                    round(child_verification_list[i][1] + 50,
                          2), child_verification_list[i][2])
                self.assertEqual(child.get_balance(),
                                 round(child_verification_list[i][1], 5))
                self.assertEqual(child.bonus(), "✅")
                child.deduct_balance(50.001)
                child_verification_list[i] = (child_verification_list[i][0],
                                              child_verification_list[i][1] -
                                              50,
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

    get_saved_data()

    configure_global(root)

    # root.update()
    # root.minsize(root.winfo_width(), root.winfo_height())

    # Start the Tk window

    root.mainloop()

    unittest.main()
