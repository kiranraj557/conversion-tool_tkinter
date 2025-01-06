import tkinter as tk
import ttkbootstrap as ttk

# Initialize the history list
conversion_history = []

# Function to load history from a file
def load_history():
    try:
        with open('history.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                conversion_history.append(line.strip())
    except FileNotFoundError:
        pass  # If file doesn't exist, do nothing

# Function to save history to a file
def save_history():
    with open('history.txt', 'w') as file:
        for entry in conversion_history:
            file.write(entry + '\n')

def convert_temperature():
    temp_input = entry_temp.get()
    unit = temp_unit_var.get()

    if unit == 'Celsius':
        fahrenheit = (temp_input * 9/5) + 32
        kelvin = temp_input + 273.15
        temp_output_string.set(f"Fahrenheit: {fahrenheit:.2f}\nKelvin: {kelvin:.2f}")
        history_entry = f"Temperature: {temp_input} {unit} -> Fahrenheit: {fahrenheit:.2f}, Kelvin: {kelvin:.2f}"
    elif unit == 'Fahrenheit':
        celsius = (temp_input - 32) * 5/9
        kelvin = celsius + 273.15
        temp_output_string.set(f"Celsius: {celsius:.2f}\nKelvin: {kelvin:.2f}")
        history_entry = f"Temperature: {temp_input} {unit} -> Celsius: {celsius:.2f}, Kelvin: {kelvin:.2f}"
    elif unit == 'Kelvin':
        celsius = temp_input - 273.15
        fahrenheit = (celsius * 9/5) + 32
        temp_output_string.set(f"Celsius: {celsius:.2f}\nFahrenheit: {fahrenheit:.2f}")
        history_entry = f"Temperature: {temp_input} {unit} -> Celsius: {celsius:.2f}, Fahrenheit: {fahrenheit:.2f}"
    
    # Add the conversion to history and save to file
    conversion_history.append(history_entry)
    save_history()

def convert_length():
    length_input = entry_length.get()
    unit = length_unit_var.get()

    if unit == 'Meter':
        kilometer = length_input / 1000
        centimeter = length_input * 100
        millimeter = length_input * 1000
        length_output_string.set(f"Kilometer: {kilometer:.2f}\nCentimeter: {centimeter:.2f}\nMillimeter: {millimeter:.2f}")
        history_entry = f"Length: {length_input} {unit} -> Kilometer: {kilometer:.2f}, Centimeter: {centimeter:.2f}, Millimeter: {millimeter:.2f}"
    elif unit == 'Kilometer':
        meter = length_input * 1000
        centimeter = length_input * 100000
        millimeter = length_input * 1000000
        length_output_string.set(f"Meter: {meter:.2f}\nCentimeter: {centimeter:.2f}\nMillimeter: {millimeter:.2f}")
        history_entry = f"Length: {length_input} {unit} -> Meter: {meter:.2f}, Centimeter: {centimeter:.2f}, Millimeter: {millimeter:.2f}"
    elif unit == 'Centimeter':
        meter = length_input / 100
        kilometer = length_input / 100000
        millimeter = length_input * 10
        length_output_string.set(f"Meter: {meter:.2f}\nKilometer: {kilometer:.2f}\nMillimeter: {millimeter:.2f}")
        history_entry = f"Length: {length_input} {unit} -> Meter: {meter:.2f}, Kilometer: {kilometer:.2f}, Millimeter: {millimeter:.2f}"
    elif unit == 'Millimeter':
        meter = length_input / 1000
        kilometer = length_input / 1000000
        centimeter = length_input / 10
        length_output_string.set(f"Meter: {meter:.2f}\nKilometer: {kilometer:.2f}\nCentimeter: {centimeter:.2f}")
        history_entry = f"Length: {length_input} {unit} -> Meter: {meter:.2f}, Kilometer: {kilometer:.2f}, Centimeter: {centimeter:.2f}"
    
    # Add the conversion to history and save to file
    conversion_history.append(history_entry)
    save_history()

def show_history():
    # Create a new window to display the history
    history_window = ttk.Toplevel(window)
    history_window.title("Conversion History")
    history_window.geometry('400x400')

    history_label = ttk.Label(history_window, text="Conversion History", font='caliber 14 bold')
    history_label.pack(pady=10)

    # Create a listbox to display history
    history_listbox = tk.Listbox(history_window, width=100, height=100)
    history_listbox.pack(pady=10)

    # Add history items to the listbox
    for entry in conversion_history:
        history_listbox.insert(tk.END, entry)

# window
window = ttk.Window(themename='journal')
window.title('Conversions')
window.geometry('700x400')
window.resizable(False,False)

# Load history from file at the start
load_history()

# title
title_label = ttk.Label(master=window, text='Conversion', font='caliber 18 bold')
title_label.pack(pady=10)

# Menu Bar
menu_bar = ttk.Menu(window)
window.config(menu=menu_bar)

# History Menu
history_menu = ttk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="History", menu=history_menu)
history_menu.add_command(label="Show History", command=show_history)

# Temperature Conversion Section
temp_section = ttk.LabelFrame(master=window, text="Temperature Conversion", padding=10)
temp_section.pack(padx=20, pady=10, fill='x')

# Temperature Input 
temp_input_label = ttk.Label(master=temp_section, text="Enter Value :")
temp_input_label.grid(row=0, column=0, padx=10, pady=5)
entry_temp = tk.DoubleVar()
entry_temp_field = ttk.Entry(master=temp_section, textvariable=entry_temp)
entry_temp_field.grid(row=0, column=1, padx=10, pady=5)

# Temperature Unit Dropdown 
temp_unit_label = ttk.Label(master=temp_section, text="Select Input Format :")
temp_unit_label.grid(row=0, column=2, padx=10, pady=5)
temp_unit_var = tk.StringVar()
temp_unit_var.set('Celsius')
temp_unit_menu = ttk.Combobox(master=temp_section, textvariable=temp_unit_var, values=['Celsius', 'Fahrenheit', 'Kelvin'], state='readonly')
temp_unit_menu.grid(row=0, column=3, padx=10, pady=5)

# Temperature Convert Button
temp_button = ttk.Button(master=temp_section, text="Convert", command=convert_temperature)
temp_button.grid(row=0, column=4, pady=5)

# Temperature Output
temp_output_string = tk.StringVar()
temp_output_label = ttk.Label(master=temp_section, textvariable=temp_output_string, font='calibri 12')
temp_output_label.grid(row=2, columnspan=2, pady=10)

# Length Conversion Section
length_section = ttk.LabelFrame(master=window, text="Length Conversion", padding=10)
length_section.pack(padx=20, pady=10, fill='x')

# Length Input
length_input_label = ttk.Label(master=length_section, text="Enter Value :")
length_input_label.grid(row=0, column=0, padx=10, pady=5)
entry_length = tk.DoubleVar()
entry_length_field = ttk.Entry(master=length_section, textvariable=entry_length)
entry_length_field.grid(row=0, column=1, padx=10, pady=5)

# Length Unit Dropdown 
length_unit_label = ttk.Label(master=length_section, text="Select Input Format :")
length_unit_label.grid(row=0, column=2, padx=10, pady=5)
length_unit_var = tk.StringVar()
length_unit_var.set('Meter')
length_unit_menu = ttk.Combobox(master=length_section, textvariable=length_unit_var, values=['Meter', 'Kilometer', 'Centimeter', 'Millimeter'], state='readonly')
length_unit_menu.grid(row=0, column=3, padx=10, pady=5)

# Length Convert Button
length_button = ttk.Button(master=length_section, text="Convert", command=convert_length)
length_button.grid(row=0, column=4, pady=5)

# Length Output
length_output_string = tk.StringVar()
length_output_label = ttk.Label(master=length_section, textvariable=length_output_string, font='calibri 12')
length_output_label.grid(row=2, columnspan=2, pady=10)

# run the application
window.mainloop()
