"""A program to track clothing allowance."""
from tkinter import Tk, ttk, StringVar, IntVar, Label, messagebox
import pickle

# Initialize the Tk Window, Frames, Widgets, and Tk Variables

root = Tk()
root.title("Clothing Allowance Tracker")

GLOBAL_SAVE_FILE = "save_file.pickle"

# Frames

main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0)

# Information Frame

info_frame = ttk.Frame(main_frame)
info_frame.grid(row=0, column=0, padx=0, pady=10)

# Action Select Frame

selection_frame = ttk.Frame(main_frame)
selection_frame.grid(row=1, column=0)

# Entry and Confirmation Frame

input_frame = ttk.Frame(main_frame)
input_frame.grid(row=2, column=0, padx=0, pady=10)

# GUI Variables
# Entry and Confirmation Frame Variables

value_entry_variable = StringVar()
value_entry_variable.set("0.00")

value_entry_button_variable = StringVar()
value_entry_button_variable.set("Deduct Allowance")

user_message_box_text_variable = StringVar()
user_message_box_text_variable.set("")

# Action Select Frame Variables

action_select_radio_button_result = IntVar()
action_select_radio_button_result.set(0)

child_select_radio_button_result = IntVar()

# GUI Functions


def action_select_radio_button_handler() -> None:
    """Manipulate the GUI to make sense for the selected action.

    This functions is responsible for:
    - Changing the 'value_entry_button's text to fit the selected action.
    - Changing the value_entry placeholder and placeholder changing binds.
    - Disabling and enabling the value_entry Entry depending on selection.
    """
    selection = action_select_radio_button_result.get()
    list_of_placeholders = ["0.00", "Name", ""]
    if selection == 0:
        value_entry_button_variable.set("Deduct Allowance")
        value_entry.config(state="enabled")
        if value_entry_variable.get() in list_of_placeholders:
            value_entry_variable.set("")
            on_focus_out(value_entry, "0.00")
        value_entry.bind("<FocusIn>",
                         lambda x: on_focus_in(value_entry, "0.00"))
        value_entry.bind("<FocusOut>",
                         lambda x: on_focus_out(value_entry, "0.00"))
    elif selection == 1:
        value_entry_button_variable.set("Set Allowance")
        value_entry.config(state="enabled")
        if value_entry_variable.get() in list_of_placeholders:
            value_entry_variable.set("")
            on_focus_out(value_entry, "0.00")
        value_entry.bind("<FocusIn>",
                         lambda x: on_focus_in(value_entry, "0.00"))
        value_entry.bind("<FocusOut>",
                         lambda x: on_focus_out(value_entry, "0.00"))
    elif selection == 2:
        value_entry_button_variable.set("Change Name")
        value_entry.config(state="enabled")
        if value_entry_variable.get() in list_of_placeholders:
            value_entry_variable.set("")
            on_focus_out(value_entry, "Name")
        value_entry.bind("<FocusIn>",
                         lambda x: on_focus_in(value_entry, "Name"))
        value_entry.bind("<FocusOut>",
                         lambda x: on_focus_out(value_entry, "Name"))
    elif selection == 3:
        value_entry_button_variable.set("Delete Child")
        value_entry_variable.set("")
        value_entry.config(state="disabled")
        value_entry.unbind("<FocusIn>")
        value_entry.unbind("<FocusOut>")


def handle_user_input() -> None:
    """Process the user pressing the main button 'value_entry_button'."""
    child_number = child_select_radio_button_result.get()
    value = value_entry_variable.get()
    selection = action_select_radio_button_result.get()

    if selection == 0:
        child_list[child_number].deduct_balance(value)
        value_entry_variable.set("0.00")
    elif selection == 1:
        child_list[child_number].set_balance(value)
        value_entry_variable.set("0.00")
    elif selection == 2:
        child_list[child_number].set_name(value)
        value_entry_variable.set("Name")
    elif selection == 3:
        child_list[child_number].delete_child()


def show_user_message(message: str, error: bool = False) -> None:
    """Show the user a message in the GUI or as a popup depending on severity.

    Args:
        message (str): The message to show to the user.
        error (bool): Whether or not the message is an error.
            Defaults to False.

    """
    if error is True:
        messagebox.showerror("Error!", message)
    else:
        user_message_box_text_variable.set(message)
        set_size()


def on_focus_in(widget: ttk.Entry, placeholder: str) -> None:
    """Delete placeholder text, if it exists on focus of the specified widget.

    Args:
        widget (ttk.Entry): The entry widget to perform the operation on.
        placeholder (str): The placeholder text.
    """
    if widget.get() == placeholder:
        widget.delete("0", "end")


def on_focus_out(widget: ttk.Entry, placeholder: str) -> None:
    """Add placeholder text on unfocus, if the Entry widget has no contents.

    Args:
        widget (ttk.Entry): The entry widget to perform the operation on.
        placeholder (str): The placeholder text.
    """
    if widget.get() == "":
        widget.insert("0", placeholder)


# GUI Contents
# Action Select Frame Contents

deduct_change_label = ttk.Label(selection_frame,
                                text="Select Action",
                                font="bold")
deduct_change_label.grid(row=0, column=0, padx=10)

deduct_radio_button = ttk.Radiobutton(
    selection_frame,
    text="Deduct Allowance",
    variable=action_select_radio_button_result,
    value=0,
    command=action_select_radio_button_handler)
deduct_radio_button.grid(row=1, column=0)

reset_radio_button = ttk.Radiobutton(
    selection_frame,
    text="Reset Allowance",
    variable=action_select_radio_button_result,
    value=1,
    command=action_select_radio_button_handler)
reset_radio_button.grid(row=2, column=0)

name_change_radio_button = ttk.Radiobutton(
    selection_frame,
    text="Change Name",
    variable=action_select_radio_button_result,
    value=2,
    command=action_select_radio_button_handler)
name_change_radio_button.grid(row=3, column=0)

delete_child_radio_button = ttk.Radiobutton(
    selection_frame,
    text="Delete Child",
    variable=action_select_radio_button_result,
    value=3,
    command=action_select_radio_button_handler)
delete_child_radio_button.grid(row=4, column=0)

select_child_label = ttk.Label(selection_frame,
                               text="Select Child",
                               font="bold")
select_child_label.grid(row=5, column=0)

# Entry and Confirmation Frame Contents

value_entry = ttk.Entry(input_frame, textvariable=value_entry_variable)
value_entry.bind("<FocusIn>", lambda x: on_focus_in(value_entry, "0.00"))
value_entry.bind("<FocusOut>", lambda x: on_focus_out(value_entry, "0.00"))
value_entry.grid(row=0, column=0)

value_entry_button = ttk.Button(input_frame,
                                textvariable=value_entry_button_variable,
                                command=handle_user_input)
value_entry_button.grid(row=1, column=0, padx=0, pady=10)

user_message_box = Label(input_frame,
                         textvariable=user_message_box_text_variable,
                         bg="darkblue",
                         fg="white")
user_message_box.grid(row=2, column=0, padx=5, pady=5)

# Main Functions
# Saving and Loading Functions


def get_saved_data(save_file_location: str) -> None:
    """Get saved object data from file.

    Args:
        save_file_location (str): The location of the save file.
    """
    try:
        with open(save_file_location, "rb") as children_file:
            children_list = pickle.load(children_file)

            for child in children_list:
                Child(child._name, child._balance)
    except FileNotFoundError:
        # We pass as if the file doesn't exist, we will just start out with a
        # blank program with no kids. This is what we want as the program has
        # been started for the first time, as it doesn't have a save file.
        pass


def save_data(save_file_location: str) -> None:
    """Save object data to file.

    Args:
        save_file_location (str): The location of the save file.
    """
    with open(save_file_location, "wb") as children_file:
        pickle.dump(child_list, children_file)


# GUI Functions


def global_gui_configuration(frame: ttk.Frame | Tk) -> None:
    """Configure global options for all widgets.

    Args:
        frame (Union[ttk.Frame, Tk]): The Frame or window to do operations on.

    """
    for widget in frame.winfo_children():
        if isinstance(widget, ttk.Frame):
            global_gui_configuration(widget)
        else:
            widget.grid_rowconfigure(0, weight=1)
            widget.grid_columnconfigure(0, weight=1)
            widget.grid(sticky="N")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)


def set_size() -> None:
    """Set root.geometry to override user window resizing.

    This function calls minsize and maxsize with 0, to unset them. This means
    that the call to root.geometry() will reset the window height and width.
    It then gets the updated window size values and put them into variables
    for DRYness. It then sets those values as minsize and maxsize so the user
    cannot resize the window. This helps avoid user confusion when some window
    elements cannot be seen, or the window is resized to big.
    """
    root.minsize(0, 0)
    root.maxsize(0, 0)
    root.geometry("")
    root.update()

    size_x, size_y = root.winfo_width(), root.winfo_height()
    root.minsize(size_x, size_y)
    root.maxsize(size_x, size_y)


# User Input Checker


def check_if_valid_balance(new_balance: float | str) -> float | bool:
    """Check if value is valid as a balance.

    Args:
        new_balance (float): The value to check.
    Returns:
        new_balance if new_balance is a valid value, False otherwise.
    """
    try:
        new_balance = round(float(new_balance), 2)
    except ValueError:
        show_user_message("Value entered needs to be a number, e.g. 15.30, 50",
                          True)
        return False
    if abs(new_balance) > 999999:
        show_user_message(
            "Value entered too large, " +
            "please enter value smaller than 1,000,000", True)
        return False
    if new_balance < 0:
        show_user_message(
            "Value entered needs to be zero or higher, e.g. 0, 15.30, 100",
            True)
        return False

    return new_balance


# Main Function


def main() -> None:
    """Start the program."""
    get_saved_data(GLOBAL_SAVE_FILE)

    global_gui_configuration(root)

    root.mainloop()


# Classes


class TemplateChild:
    """A class that manages child creation, and it's GUI widgets."""

    def __init__(self) -> None:
        """Initialize the TemplateChild.

        This creates the widget's and variables required for the child
        creation GUI.
        """
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
        # The second passed argument of the on_focus functions is hardcoded as
        # you can't get the value from the StringVar as that changes.
        self._child_name_entry.bind(
            "<FocusIn>", lambda x: on_focus_in(self._child_name_entry, "Name"))
        self._child_name_entry.bind(
            "<FocusOut>",
            lambda x: on_focus_out(self._child_name_entry, "Name"))
        # We only want padding on the bottom here to separate the 'sections'.
        self._child_name_entry.grid(row=1, column=0, columnspan=2, pady=(0, 5))

        self._child_allowance_entry_label = ttk.Label(
            self._child_creation_frame, text="Enter Allowance:")
        self._child_allowance_entry_label.grid(row=2, column=0, columnspan=2)

        self._child_allowance_entry_variable = StringVar()
        self._child_allowance_entry_variable.set("0.00")

        self._child_allowance_entry = ttk.Entry(
            self._child_creation_frame,
            textvariable=self._child_allowance_entry_variable)
        # The second passed argument of the on_focus functions is hardcoded as
        # you can't get the value from the StringVar as that changes.
        self._child_allowance_entry.bind(
            "<FocusIn>",
            lambda x: on_focus_in(self._child_allowance_entry, "0.00"))
        self._child_allowance_entry.bind(
            "<FocusOut>",
            lambda x: on_focus_out(self._child_allowance_entry, "0.00"))
        # We only want padding on the bottom here to separate the 'sections'.
        self._child_allowance_entry.grid(row=3,
                                         column=0,
                                         columnspan=2,
                                         pady=(0, 5))

        self._child_allowance_cancel_button = ttk.Button(
            self._child_creation_frame,
            text="Cancel",
            command=self._delete_template_child)
        self._child_allowance_cancel_button.grid(row=4, column=0, padx=(10, 0))

        self._child_allowance_create_button = ttk.Button(
            self._child_creation_frame,
            text="Create",
            command=self._create_child)
        self._child_allowance_create_button.grid(row=4, column=1, padx=(0, 10))

        for widget in self._child_creation_frame.winfo_children():
            widget.grid_rowconfigure(0, weight=1)
            widget.grid_columnconfigure(0, weight=1)
            widget.grid(sticky="N", padx=5)

        add_child_button.config(state="disabled")

        set_size()

    def _create_child(self) -> None:
        """Create a child from the information given.

        This method checks if the child has valid attributes, then creates
        that child, saves the program, then deletes the TemplateChild.
        """
        new_child_balance = self._child_allowance_entry_variable.get()
        child_balance = check_if_valid_balance(new_child_balance)
        if child_balance is False:
            return
        Child(self._child_name_entry_variable.get(), child_balance)
        save_data(GLOBAL_SAVE_FILE)
        self._delete_template_child()
        set_size()

    def _delete_template_child(self) -> None:
        """Delete the template child and it's widgets."""
        self._child_creation_frame.destroy()

        add_child_button.config(state="normal")

        set_size()


# Information Frame Contents

add_child_button = ttk.Button(info_frame,
                              text="Add Child",
                              command=TemplateChild)
add_child_button.grid(row=1, column=0, columnspan=999, pady=(0, 20))


class Child:
    """The child stores all of the details about itself."""

    def __init__(self, name: str, balance: float) -> None:
        """Initialize the Child object.

        This initializes values and checks their validity. It then generates
        a widgets to show the child instance in the GUI based off of those
        values.

        Args:
            name (str): The name of the child.
            balance (float): The child's balance.
        """
        self._name = str(name)
        new_balance = check_if_valid_balance(balance)
        if new_balance is False:
            return
        self._balance = new_balance
        child_list.append(self)
        self._list_index = (len(child_list) - 1)

        self._name_variable = StringVar()
        self._name_variable.set(self._name)

        self._balance_variable = StringVar()
        self._balance_variable.set(str(self._balance))

        self._bonus_variable = StringVar()
        self._bonus_variable.set(self.bonus())

        self._frame = ttk.Frame(info_frame)
        self._frame.grid(row=0, column=self._list_index)

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
        self._child_selection_radio_button.grid(row=(6 + self._list_index),
                                                column=0)

        for widget in self._frame.winfo_children():
            widget.grid(pady=5, padx=5)

        set_size()

    def __getstate__(self) -> dict[str, str | float]:
        """Get the state of the instance for saving with pickle.

        Returns:
            The name and balance attributes of Child.
        """
        return {'_name': self._name, '_balance': self._balance}

    def bonus(self) -> str:
        """Return the bonus state as an emoji so it can be used in the UI.

        Returns:
            A check-mark emoji if the balance is 50 or greater,
            a cross emoji otherwise.
        """
        if self._balance >= 50.00:
            return "✅"
        return "❌"

    def deduct_balance(self, deduction_amount: float | str) -> None:
        """Deduct balance for object.

        Args:
            deduction_amount (float): The amount to deduct from the instance.
        """
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
                "Please enter a smaller amount", True)
            return
        self.set_balance(new_balance)

        show_user_message(
            f"Success, removed ${deduction_amount} from {self.get_name()}'s " +
            f"balance, {self.get_name()}'s balance is now " +
            f"${self.get_balance()}.",
            error=False)

        set_size()

    def set_balance(self, new_balance: float | str) -> None:
        """Set _balance for the instance.

        Args:
            new_balance (float): The value to set self._balance to.
        """
        balance = check_if_valid_balance(new_balance)
        if balance is False:
            return
        self._balance = balance
        self._balance_variable.set(str(self._balance))
        self._bonus_variable.set(self.bonus())

        save_data(GLOBAL_SAVE_FILE)

        show_user_message(f"Success, set {self.get_name()}'s balance to " +
                          f"${self.get_balance()}.",
                          error=False)

        set_size()

    def get_balance(self) -> float:
        """Get the balance of the object.

        Returns:
            The instance's balance.
        """
        return self._balance

    def set_name(self, name: str) -> None:
        """Set _name for the instance.

        Args:
            name (str): The string to set self._name to.
        """
        if name.strip() != "":
            self._name = name
            self._name_variable.set(self._name)

            save_data(GLOBAL_SAVE_FILE)

            show_user_message(f"Success, set {self._name}'s name.",
                              error=False)
        else:
            show_user_message("Name entered must contain some characters",
                              True)

    def get_name(self) -> str:
        """Get instance attribute _name.

        Returns:
            Name as a string.
        """
        return self._name

    def delete_child(self) -> None:
        """Delete instance.

        Since this is a irreversible operation, it asks the user whether they
        really want to delete the child. If the user cancels the operation, it
        gives the user reassuring feedback that the child has not been deleted.
        If the user affirms that they want to delete the child, these actions
        are carried out:
        - The child deletes itself from the child_list
        - The child deletes it's GUI widgets
        - The child saves the program data, now without itself as it is no
            longer in the child_list
        - Now that the program has saved, a soft reload is initiated, in this
            soft reload the following happens:
            - all Child class generated elements are destroyed
            - child_list is cleared
            - child_list and the GUI are repopulated by get_saved_data()
        After the soft reload, the user is shown a success message, and the
        child_select radio buttons is set back to the default value. This is
        because the value is no longer valid, as that value has been deleted.
        """
        response = messagebox.askyesno(
            "Are You Sure?",
            f"Are you sure you want to delete {self.get_name()} PERMANENTLY?")
        if response is True:
            child_list.pop(self._list_index)
            self._frame.destroy()
            self._child_selection_radio_button.destroy()
            save_data(GLOBAL_SAVE_FILE)
            for child in child_list:
                child._frame.destroy()
                child._child_selection_radio_button.destroy()
            child_list.clear()
            get_saved_data(GLOBAL_SAVE_FILE)
            show_user_message(f"Success, deleted child {self._name}",
                              error=False)
            child_select_radio_button_result.set(0)
        else:
            show_user_message(f"Canceled {self._name}'s deletion", error=False)


child_list: list[Child] = []

if __name__ == '__main__':
    main()
