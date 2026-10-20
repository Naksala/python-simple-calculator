import tkinter as tk


# Create application window
window = tk.Tk()
window.title("Python Simple Calculator")
window.geometry("350x470")
window.resizable(False, False)
window.configure(bg="#202124")


# Store calculator input
expression = ""


# Display variable
display_var = tk.StringVar()


# Update calculator display
def press(value):
    global expression

    expression += str(value)
    display_var.set(expression)


# Clear calculator
def clear():
    global expression

    expression = ""
    display_var.set("")


# Calculate result
def calculate():
    global expression

    try:
        # Only allow calculator characters
        allowed = "0123456789+-*/.%() "

        if not expression or any(
            char not in allowed for char in expression
        ):
            raise ValueError("Invalid expression")

        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        if isinstance(result, complex):
            raise ValueError("Complex result")

        expression = str(result)
        display_var.set(expression)

    except Exception:
        expression = ""
        display_var.set("Error")


# Calculator display
display = tk.Entry(
    window,
    textvariable=display_var,
    font=("Arial", 26),
    bg="#303134",
    fg="white",
    justify="right",
    bd=0,
    state="readonly",
    readonlybackground="#303134"
)

display.pack(
    fill="x",
    padx=15,
    pady=20,
    ipady=15
)


# Button container
button_frame = tk.Frame(
    window,
    bg="#202124"
)

button_frame.pack(
    expand=True,
    fill="both",
    padx=10,
    pady=10
)


# Calculator buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", ".", "+"],
    ["%", "(", ")", "="]
]


# Create buttons
for row_index, row in enumerate(buttons):
    for col_index, text in enumerate(row):

        if text == "C":
            command = clear
            color = "#EA4335"

        elif text == "=":
            command = calculate
            color = "#34A853"

        else:
            command = lambda value=text: press(value)
            color = (
                "#4285F4"
                if text in "+-*/%"
                else "#3C4043"
            )

        button = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 18),
            bg=color,
            fg="white",
            activebackground="#5F6368",
            activeforeground="white",
            bd=0,
            command=command
        )

        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=4,
            pady=4
        )


# Make buttons fill the available space
for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)


# Start the GUI application
window.mainloop()