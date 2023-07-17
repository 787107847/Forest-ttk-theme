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
combo_list = ["Capacidad", "4"+" GB", "8"+" GB","12"+" GB","etc"]
combo_list1 = ["Marca", "Lenovo", "HP","DELL","ACER","etc"]
combo_list2 = ["Modelo","ThinkPad","Latitude","IdeaPad Gaming","Aspire","etc"]
combo_list3 = ["TIPO","SSD","HDD",""]
combo_list4 = ["Factor de forma","SATA","M.2","PCIe","etc"]
combo_list5 = []
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
    (1, "end", 5, "Child", ("Subitem 1.4", "Value 1.4"))
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

spinbox = ttk.Spinbox(input_valor_1, from_=0, to=100)
spinbox.insert(0, "Stock")
spinbox.grid(row=1, column=0, padx=(5,1), pady=(0,0), sticky="ew")

entry3 = ttk.Entry(input_valor_1)
entry3.insert(0, "Costo")
entry3.grid(row=2, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry4 = ttk.Entry(input_valor_1)
entry4.insert(0, "Proveedor")
entry4.grid(row=3, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry5 = ttk.Entry(input_valor_1)
entry5.insert(0, "N° de serie")
entry5.grid(row=4, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_2 = ttk.LabelFrame(tab_2, text="RAM", padding=(20, 10))
input_valor_2.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="ns")

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
input_valor_3 = ttk.LabelFrame(tab_2, text="Marca y Modelo", padding=(20, 10))
input_valor_3.grid(row=0, column=3, padx=(20, 10), pady=(20, 10), sticky="ns")

# Entry widgets
combobox = ttk.Combobox(input_valor_3, values=combo_list1)
combobox.current(0)
combobox.grid(row=1, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

combobox = ttk.Combobox(input_valor_3, values=combo_list2)
combobox.current(0)
combobox.grid(row=2, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

entry13 = ttk.Entry(input_valor_3)
entry13.insert(0, "Linea")
entry13.grid(row=3, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry14 = ttk.Entry(input_valor_3)
entry14.insert(0, "N° producto")
entry14.grid(row=4, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_4 = ttk.LabelFrame(tab_2, text="Almacenamiento", padding=(20, 10))
input_valor_4.grid(row=0, column=4, padx=(20, 10), pady=(20, 10), sticky="ns")

# Entry widgets
combobox = ttk.Combobox(input_valor_4, values=combo_list3)
combobox.current(0)
combobox.grid(row=0, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

entry17 = ttk.Entry(input_valor_4)
entry17.insert(0, "Capacidad")
entry17.grid(row=1, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

combobox = ttk.Combobox(input_valor_4, values=combo_list4)
combobox.current(0)
combobox.grid(row=0, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

entry19 = ttk.Entry(input_valor_4)
entry19.insert(0, "Especificación")
entry19.grid(row=3, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_5 = ttk.LabelFrame(tab_2, text="Procesador", padding=(20, 10))
input_valor_5.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="ns")

entry20 = ttk.Entry(input_valor_5)
entry20.insert(0, "Nombre Procesador")
entry20.grid(row=0, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry21 = ttk.Entry(input_valor_5)
entry21.insert(0, "Núcleos")
entry21.grid(row=1, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry21 = ttk.Entry(input_valor_5)
entry21.insert(0, "Generación")
entry21.grid(row=2, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry21 = ttk.Entry(input_valor_5)
entry21.insert(0, "Velocidad CPU")
entry21.grid(row=3, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")


# Tab #3
tab_3 = ttk.Frame(notebook)
notebook.add(tab_3, text="Tab 3")

# Start the main loop
root.mainloop()
