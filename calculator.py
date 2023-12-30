import tkinter as tk

# Function to update the display
def update_display(value):
    current_text = display.get()
    if current_text == "0" and value != ".":
        display.set(value)
    else:
        display.set(current_text + value)

# Function to clear the display
def clear_display():
    display.set("0")

# Function to evaluate the expression and display the result
def calculate():
    try:
        result = eval(display.get())
        display.set(str(result))
    except Exception as e:
        display.set("Error")

# Initialize tkinter
root = tk.Tk()
root.title("Calculator")
root.configure(background='#FFF2D8')

# Create a StringVar to hold the display value
display = tk.StringVar()
display.set("0")

# Create GUI elements
entry_display = tk.Entry(root, textvariable=display, font=('Arial', 20), bd=5, justify="right")
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0 ', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, column) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=('Arial', 16,"bold"), padx=20, pady=10, command=calculate, bg="#BCA37F")
    elif text == '0':
        button = tk.Button(root, text=text, font=('Arial', 16,"bold"), padx=20, pady=10, bg="#BCA37F", command=lambda t=text: update_display(t))
        button.grid(row=row, column=column, columnspan=2, padx=5, pady=5)
        continue
    else:
        button = tk.Button(root, text=text, font=('Arial', 16,"bold"), padx=20, pady=10, bg="#BCA37F", command=lambda t=text: update_display(t))

    button.grid(row=row, column=column, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text='C', font=('Arial', 16,"bold"), padx=20, pady=10,bg="#113946",fg="white", command=clear_display)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
