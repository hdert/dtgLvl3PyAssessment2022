"""Define the GUI, GUI elements, and GUI related variables."""
from tkinter import Tk, ttk, StringVar, IntVar
# from tkinter import Tk, ttk, Label, StringVar, Frame, Entry, Button,
# LabelFrame, PhotoImage, ComboBox, DoubleVar

# Initialize Tk window, widgets, and Tk Variables

root = Tk()
root.title("Placeholder Text")
root.minsize(350, 400)

root.geometry("350x400")

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
input_frame.grid(row=2, column=0, padx=0, pady=20)

# Information Frame Variables

child_1_name_variable = StringVar()
child_1_name_variable.set("child_1.name")

child_1_balance_variable = StringVar()
child_1_balance_variable.set("child_1.balance")

child_1_bonus_variable = StringVar()
child_1_bonus_variable.set("child_1.bonus()")

# Information Frame Contents

child_1_frame = ttk.Frame(info_frame)
child_1_frame.grid(row=0, column=0, padx=0, pady=0)

child_1_name = ttk.Label(child_1_frame,
                         textvariable=child_1_name_variable,
                         font="bold")
child_1_name.grid(row=0, column=0, padx=0, pady=0)

child_1_account_balance_label = ttk.Label(child_1_frame,
                                          text="Account Balance:")
child_1_account_balance_label.grid(row=1, column=0, padx=0, pady=0)

child_1_account_balance = ttk.Label(child_1_frame,
                                    textvariable=child_1_balance_variable)
child_1_account_balance.grid(row=2, column=0, padx=0, pady=0)

child_1_bonus_label = ttk.Label(child_1_frame, text="Bonus:")
child_1_bonus_label.grid(row=3, column=0, padx=0, pady=0)

child_1_bonus = ttk.Label(child_1_frame, textvariable=child_1_bonus_variable)
child_1_bonus.grid(row=4, column=0, padx=0, pady=0)

for widget in child_1_frame.winfo_children():
    widget.grid(pady=5)

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

child_1_radio_button = ttk.Radiobutton(
    selection_frame,
    text="child_1.name",
    variable=child_select_radio_button_result,
    value=0)
child_1_radio_button.grid(row=4, column=0, padx=0, pady=0)

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


def configure_global(frame):
    """Configure global options for all widgets.

    Args:
        frame: The Frame to do operations on.

    """
    for widget in frame.winfo_children():
        if widget.winfo_class() == "TFrame":
            configure_global(widget)
        else:
            widget.grid_rowconfigure(0, weight=1)
            widget.grid_columnconfigure(0, weight=1)
            # widget.grid(padx=0, pady=0)
            widget.grid(sticky="N")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)


configure_global(root)

# Start the Tk window

root.mainloop()
