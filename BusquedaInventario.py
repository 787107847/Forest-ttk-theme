import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Forest")
root.option_add("*tearOff", False)  # This is always a good idea

# Make the app responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "forest-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("forest-dark")

# Create lists for the Comboboxes
option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
combo_list = ["Capacidad", "4"+" GB", "8"+" GB","12"+" GB","ETC"]
readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

# Create control variables
a = tk.BooleanVar()
b = tk.BooleanVar(value=True)
c = tk.BooleanVar()
d = tk.IntVar(value=2)
e = tk.StringVar(value=option_menu_list[1])
f = tk.BooleanVar()
g = tk.DoubleVar(value=75.0)
h = tk.BooleanVar()

# Panedwindow
paned = ttk.PanedWindow(root)
paned.grid(row=0, column=0, sticky="nsew")

# Configure expansion for the PanedWindow
paned.columnconfigure(0, weight=1)
paned.rowconfigure(0, weight=1)

# Notebook
notebook = ttk.Notebook(paned)
paned.add(notebook)

# Tab #1
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text="Buscar Item")

# Configure expansion for tab_1
tab_1.columnconfigure(0, weight=1)
tab_1.rowconfigure(1, weight=1)

# Create a Frame for the input_busqueda_frame
input_busqueda_frame = ttk.LabelFrame(tab_1, text="Búsqueda de productos", padding=(20, 10))
input_busqueda_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ns")


# Configure expansion for input_busqueda_frame
input_busqueda_frame.columnconfigure(0, weight=1)
input_busqueda_frame.rowconfigure(0, weight=0)  # Set weight to 0 to prevent vertical expansion

# Entry widget
entry = ttk.Entry(input_busqueda_frame)
entry.insert(0, "N° Item")
entry.grid(row=0, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")  # Adjust sticky to expand horizontally only

# Button widget
button = ttk.Button(input_busqueda_frame, text="Buscar")
button.grid(row=0, column=1, padx=5, pady=(0, 0), sticky="nse")  # Adjust sticky

# Create a Frame for the Treeview
treeFrame = ttk.Frame(tab_1)
treeFrame.grid(row=1, column=0, sticky="nsew")

# Configure expansion for treeFrame
treeFrame.columnconfigure(0, weight=1)
treeFrame.rowconfigure(0, weight=1)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

# Treeview
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=12)
treeview.pack(expand=True, fill="both", padx=5, pady=5)
treeScroll.config(command=treeview.yview)

# Treeview headings
treeview.heading("#0", text="Column 1", anchor="center")
treeview.heading(1, text="Column 2", anchor="center")
treeview.heading(2, text="Column 3", anchor="center")

# Define treeview data
treeview_data = [
    ("", "end", 1, "Parent", ("Item 1", "Value 1")),
    (1, "end", 2, "Child", ("Subitem 1.1", "Value 1.1")),
    (1, "end", 3, "Child", ("Subitem 1.2", "Value 1.2")),
    (1, "end", 4, "Child", ("Subitem 1.3", "Value 1.3")),
    (1, "end", 5, "Child", ("Subitem 1.4", "Value 1.4")),
    ("", "end", 6, "Parent", ("Item 2", "Value 2")),
    (6, "end", 7, "Child", ("Subitem 2.1", "Value 2.1")),
    (6, "end", 8, "Sub-parent", ("Subitem 2.2", "Value 2.2")),
    (8, "end", 9, "Child", ("Subitem 2.2.1", "Value 2.2.1")),
    (8, "end", 10, "Child", ("Subitem 2.2.2", "Value 2.2.2")),
    (8, "end", 11, "Child", ("Subitem 2.2.3", "Value 2.2.3")),
    (6, "end", 12, "Child", ("Subitem 2.3", "Value 2.3")),
    (6, "end", 13, "Child", ("Subitem 2.4", "Value 2.4")),
    ("", "end", 14, "Parent", ("Item 3", "Value 3")),
    (14, "end", 15, "Child", ("Subitem 3.1", "Value 3.1")),
    (14, "end", 16, "Child", ("Subitem 3.2", "Value 3.2")),
    (14, "end", 17, "Child", ("Subitem 3.3", "Value 3.3")),
    (14, "end", 18, "Child", ("Subitem 3.4", "Value 3.4")),
    ("", "end", 19, "Parent", ("Item 4", "Value 4")),
    (19, "end", 20, "Child", ("Subitem 4.1", "Value 4.1")),
    (19, "end", 21, "Sub-parent", ("Subitem 4.2", "Value 4.2")),
    (21, "end", 22, "Child", ("Subitem 4.2.1", "Value 4.2.1")),
    (21, "end", 23, "Child", ("Subitem 4.2.2", "Value 4.2.2")),
    (21, "end", 24, "Child", ("Subitem 4.2.3", "Value 4.2.3")),
    (19, "end", 25, "Child", ("Subitem 4.3", "Value 4.3"))
    ]


# Insert treeview data
for item in treeview_data:
    treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])
    if item[0] == "" or item[2] in (8, 12):
        treeview.item(item[2], open=True)  # Open parents

# Tab #2
tab_2 = ttk.Frame(notebook)
notebook.add(tab_2, text="Ingresar Item")

# Frame para Ingreso de Valores Principales
input_valor_1 = ttk.LabelFrame(tab_2, text="Valores principales", padding=(20, 10))
input_valor_1.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="ns")

# Entry widgets
entry1 = ttk.Entry(input_valor_1)
entry1.insert(0, "N° Item")
entry1.grid(row=0, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry2 = ttk.Entry(input_valor_1)
entry2.insert(0, "Stock Auto")
entry2.grid(row=1, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry3 = ttk.Entry(input_valor_1)
entry3.insert(0, "Costo")
entry3.grid(row=2, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry4 = ttk.Entry(input_valor_1)
entry4.insert(0, "Proveedor")
entry4.grid(row=3, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry5 = ttk.Entry(input_valor_1)
entry5.insert(0, "Fecha de Recibido")
entry5.grid(row=4, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_2 = ttk.LabelFrame(tab_2, text="RAM", padding=(20, 10))
input_valor_2.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="ns")

# Entry widgets
# Combobox"
combobox = ttk.Combobox(input_valor_2, values=combo_list)
combobox.current(0)
combobox.grid(row=0, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

entry7 = ttk.Entry(input_valor_2)
entry7.insert(0, "Tipo")
entry7.grid(row=1, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry8 = ttk.Entry(input_valor_2)
entry8.insert(0, "Frecuencia")
entry8.grid(row=2, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry9 = ttk.Entry(input_valor_2)
entry9.insert(0, "Posición (M)")
entry9.grid(row=3, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry10 = ttk.Entry(input_valor_2)
entry10.insert(0, "Maximo de ram")
entry10.grid(row=4, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_3 = ttk.LabelFrame(tab_2, text="Componentes", padding=(20, 10))
input_valor_3.grid(row=0, column=3, padx=(20, 10), pady=(20, 10), sticky="ns")

# Entry widgets
entry11 = ttk.Entry(input_valor_3)
entry11.insert(0, "N° Item")
entry11.grid(row=0, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry12 = ttk.Entry(input_valor_3)
entry12.insert(0, "N° Item")
entry12.grid(row=1, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry13 = ttk.Entry(input_valor_3)
entry13.insert(0, "N° Item")
entry13.grid(row=2, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry14 = ttk.Entry(input_valor_3)
entry14.insert(0, "N° Item")
entry14.grid(row=3, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry15 = ttk.Entry(input_valor_3)
entry15.insert(0, "N° Item")
entry15.grid(row=4, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_4 = ttk.LabelFrame(tab_2, text="Componentes", padding=(20, 10))
input_valor_4.grid(row=0, column=4, padx=(20, 10), pady=(20, 10), sticky="ns")

# Entry widgets
entry16 = ttk.Entry(input_valor_4)
entry16.insert(0, "N° Item")
entry16.grid(row=0, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry17 = ttk.Entry(input_valor_4)
entry17.insert(0, "N° Item")
entry17.grid(row=1, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry18 = ttk.Entry(input_valor_4)
entry18.insert(0, "N° Item")
entry18.grid(row=2, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry19 = ttk.Entry(input_valor_4)
entry19.insert(0, "N° Item")
entry19.grid(row=3, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry14 = ttk.Entry(input_valor_4)
entry14.insert(0, "N° Item")
entry14.grid(row=4, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")


# Tab #3
tab_3 = ttk.Frame(notebook)
notebook.add(tab_3, text="Tab 3")

# Start the main loop
root.mainloop()
