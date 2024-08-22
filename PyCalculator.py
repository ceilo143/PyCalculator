import tkinter as tk

# Create the main application window
app = tk.Tk()
app.title("Calculator")

# Set background color for the app
app.configure(bg='#D3D3D3')  # Light grey background

# Create and configure the display
disp = tk.Entry(app, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
disp.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Define button symbols
btns = [
    '(', ')', 'C', 'Del',
    '7', '8', '9', '÷',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

def clk(b):
    current_text = disp.get()
    if b == "=":
        try:
            # Replace symbols for evaluation
            current_text = current_text.replace('x', '*').replace('÷', '/')
            result = eval(current_text)
            disp.delete(0, tk.END)
            disp.insert(tk.END, result)
        except Exception:
            disp.delete(0, tk.END)
            disp.insert(tk.END, "Error")
    elif b == "C":
        disp.delete(0, tk.END)
    elif b == "Del":
        # Remove the last character from the current input
        current_text = disp.get()
        if current_text:
            disp.delete(len(current_text) - 1, tk.END)
    else:
        # Append button text to the display
        disp.insert(tk.END, b)

def create_rounded_button(parent, text, row, column, command):
    button_width = 80
    button_height = 60
    corner_radius = 30

    # Create a canvas to draw the button
    canvas = tk.Canvas(parent, width=button_width, height=button_height, bg='#D3D3D3', bd=0, highlightthickness=0)
    canvas.grid(row=row, column=column, padx=5, pady=5)

    # Draw rounded rectangle
    canvas.create_oval(0, 0, corner_radius * 2, corner_radius * 2, fill='#FFA500', outline='#FFA500')  # top-left
    canvas.create_oval(button_width - corner_radius * 2, 0, button_width, corner_radius * 2, fill='#FFA500',
                       outline='#FFA500')  # top-right
    canvas.create_oval(0, button_height - corner_radius * 2, corner_radius * 2, button_height, fill='#FFA500',
                       outline='#FFA500')  # bottom-left
    canvas.create_oval(button_width - corner_radius * 2, button_height - corner_radius * 2, button_width, button_height,
                       fill='#FFA500', outline='#FFA500')  # bottom-right

    # Draw center rectangle
    canvas.create_rectangle(corner_radius, 0, button_width - corner_radius, button_height, fill='#FFA500',
                            outline='#FFA500')
    canvas.create_rectangle(0, corner_radius, button_width, button_height - corner_radius, fill='#FFA500',
                            outline='#FFA500')

    # Add text to button with black color
    canvas.create_text(button_width // 2, button_height // 2, text=text, fill='#000000', font=('Arial', 18))

    # Bind click event
    canvas.bind("<Button-1>", lambda event: command())

# Create and place buttons
for i, b in enumerate(btns):
    if i < 4:
        create_rounded_button(app, b, 1, i, lambda x=b: clk(x))
    else:
        create_rounded_button(app, b, (i - 4) // 4 + 2, (i - 4) % 4, lambda x=b: clk(x))

app.mainloop()
