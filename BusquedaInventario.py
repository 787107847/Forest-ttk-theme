import tkinter as tk
from tkinter import ttk

def on_canvas_configure(event):
    canvas_tab_2.configure(scrollregion=canvas_tab_2.bbox("all"))

def on_mousewheel(event):
    if canvas_tab_2.winfo_height() < content_frame_tab_2.winfo_height():
        canvas_tab_2.yview_scroll(int(-1 * (event.delta / 120)), "units")

def resize(event):
    window_width = root.winfo_width()
    num_columns = max(window_width // 250, 1)  # Calcula el número de columnas basado en el ancho de la ventana
    for i, label_frame in enumerate(label_frames):
        row = i // num_columns
        column = i % num_columns
        label_frame.grid_forget()
        label_frame.grid(row=row, column=column, padx=(20, 10), pady=(20, 10), sticky="ns")


def validate_entry():
    for entry in entry_list:
        print(entry)
        if entry.get() == "":
            entry.state(["invalid"])
        else:
            entry.state(["!invalid"])

root = tk.Tk()
root.title("UltraPC")
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
combo_list2 = ["Linea","ThinkPad","Latitude","IdeaPad Gaming","Aspire","etc"]
combo_list3 = ["TIPO","SSD","HDD",""]
combo_list4 = ["Factor de forma","SATA","M.2","PCIe","etc"]
combo_list5 = ["Tipo","Interna","Externa"]
combo_list6= ["","SI","NO",""]
combo_list7 = ["Panel","LED IPS","Retina","LED TN","etc"]

# Crear notebook
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)


# Contenido de la pestaña 1
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text="Tab 1")

# Create a Frame for the input_busqueda_frame
input_busqueda_frame = ttk.LabelFrame(tab_1, text="Búsqueda de productos", padding=(20, 10))
input_busqueda_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ns")


# Configure expansion for input_busqueda_frame
input_busqueda_frame.columnconfigure(0, weight=1)
input_busqueda_frame.rowconfigure(0, weight=0)  # Set weight to 0 to prevent vertical expansion

# Entry widget
entryi = ttk.Entry(input_busqueda_frame)
entryi.insert(0, "N° Item")
entryi.grid(row=0, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")  # Adjust sticky to expand horizontally only

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


# Contenido de la pestaña 2
tab_2 = ttk.Frame(notebook)
notebook.add(tab_2, text="Tab 2")

# Crear canvas para la pestaña 2
canvas_tab_2 = tk.Canvas(tab_2)
canvas_tab_2.pack(side="left", fill="both", expand=True)

# Frame dentro del canvas para la pestaña 2
content_frame_tab_2 = ttk.Frame(canvas_tab_2)
canvas_tab_2.create_window((0, 0), window=content_frame_tab_2, anchor="nw")

# Ajustar el tamaño del canvas al contenido
content_frame_tab_2.bind("<Configure>", on_canvas_configure)

# Asociar evento de scroll del mouse
canvas_tab_2.bind_all("<MouseWheel>", on_mousewheel)

# Contenedor principal
frame_contenedor = ttk.Frame(content_frame_tab_2)
frame_contenedor.pack()

# Lista de LabelFrame
label_frames = []

# Frame para Ingreso de Valores Principales
input_valor_1 = ttk.LabelFrame(frame_contenedor, text="Valores principales", padding=(20, 10))
label_frames.append(input_valor_1)

entry_list = []

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
input_valor_2 = ttk.LabelFrame(frame_contenedor, text="RAM", padding=(20, 10))
label_frames.append(input_valor_2)

# Combobox"
combobox = ttk.Combobox(input_valor_2, values=combo_list)
combobox.current(0)
combobox.grid(row=0, column=0,padx=(5,1), pady=(0, 0), sticky="ew")

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
input_valor_3 = ttk.LabelFrame(frame_contenedor, text="Marca y Modelo", padding=(20, 10))
label_frames.append(input_valor_3)

# Entry widgets
combobox = ttk.Combobox(input_valor_3, values=combo_list1)
combobox.current(0)
combobox.grid(row=1, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

combobox = ttk.Combobox(input_valor_3, values=combo_list2)
combobox.current(0)
combobox.grid(row=2, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

entry13 = ttk.Entry(input_valor_3)
entry13.insert(0, "Modelo")
entry13.grid(row=3, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry14 = ttk.Entry(input_valor_3)
entry14.insert(0, "N° producto")
entry14.grid(row=4, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_4 = ttk.LabelFrame(frame_contenedor, text="Almacenamiento", padding=(20, 10))
label_frames.append(input_valor_4)

# Entry widgets
combobox = ttk.Combobox(input_valor_4, values=combo_list3)
combobox.current(0)
combobox.grid(row=0, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

entry17 = ttk.Entry(input_valor_4)
entry17.insert(0, "Capacidad")
entry17.grid(row=1, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

combobox = ttk.Combobox(input_valor_4, values=combo_list4)
combobox.current(0)
combobox.grid(row=2, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

entry19 = ttk.Entry(input_valor_4)
entry19.insert(0, "Especificación")
entry19.grid(row=3, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry20 = ttk.Entry(input_valor_4)
entry20.insert(0, "Horas de uso")
entry20.grid(row=4, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

#Procesador
input_valor_5 = ttk.LabelFrame(frame_contenedor, text="Procesador", padding=(20, 10))
label_frames.append(input_valor_5)

entry21 = ttk.Entry(input_valor_5)
entry21.insert(0, "Nombre Procesador")
entry21.grid(row=0, column=0, padx=5, pady=(5, 0), sticky="ew")

entry22 = ttk.Entry(input_valor_5)
entry22.insert(0, "Núcleos")
entry22.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

entry23 = ttk.Entry(input_valor_5)
entry23.insert(0, "Generación")
entry23.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

entry24 = ttk.Entry(input_valor_5)
entry24.insert(0, "Velocidad CPU")
entry24.grid(row=3, column=0, padx=5, pady=(0, 5), sticky="ew")


# Frame para Ingreso de Valores de la máquina
input_valor_6 = ttk.LabelFrame(frame_contenedor, text="Grafica", padding=(20, 10))
label_frames.append(input_valor_6)

entry25 = ttk.Entry(input_valor_6)
entry25.insert(0, "Marca")
entry25.grid(row=0, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry26 = ttk.Entry(input_valor_6)
entry26.insert(0, "Linea")
entry26.grid(row=1, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

entry27 = ttk.Entry(input_valor_6)
entry27.insert(0, "Modelo")
entry27.grid(row=2, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry28 = ttk.Entry(input_valor_6)
entry28.insert(0, "Capacidad")
entry28.grid(row=3, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_7 = ttk.LabelFrame(frame_contenedor, text="Batería", padding=(20, 10))
label_frames.append(input_valor_7)

# Read-only combobox
readonly_combo = ttk.Combobox(input_valor_7, state="readonly", values=combo_list5)
readonly_combo.current(0)
readonly_combo.grid(row=0, column=0, padx=5, pady=10,  sticky="ew")

entry30 = ttk.Entry(input_valor_7, width=0)
entry30.insert(0, "Extendida")
entry30.grid(row=1, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

entry31 = ttk.Entry(input_valor_7, width=0)
entry31.insert(0, "Capacidad Batería")
entry31.grid(row=2, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

spinbox = ttk.Spinbox(input_valor_7, from_=0, to=100, width=10)
spinbox.insert(0, "% Uso")
spinbox.grid(row=3, column=0, padx=(5,1), pady=(0,0), sticky="ew")

combo_list6[0] = "Webcam"
readonly_combo2 = ttk.Combobox(input_valor_7, state="readonly", values=combo_list6)
readonly_combo2.current(0)
readonly_combo2.grid(row=5, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

entry32 = ttk.Entry(input_valor_7, width=15)
entry32.insert(0, "Posición Webcam")
entry32.grid(row=6, column=0,padx=(5, 0), pady=(5, 0), sticky="ew")


# Frame para Ingreso de Valores de la máquina
input_valor_8 = ttk.LabelFrame(frame_contenedor, text="Pantalla", padding=(20, 10))
label_frames.append(input_valor_8)

# Read-only combobox
combo_list6[0] = "Táctil"
readonly_combo3 = ttk.Combobox(input_valor_8,  state="readonly", values=combo_list6)
readonly_combo3.current(0)
readonly_combo3.grid(row=0, column=0, padx=(5,0), pady=(0,0),  sticky="ew")

entry33 = ttk.Entry(input_valor_8, width=0)
entry33.insert(0, "Tamaño de Pantalla")
entry33.grid(row=1, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

entry34 = ttk.Entry(input_valor_8, width=18)
entry34.insert(0, "Resolución Pantalla")
entry34.grid(row=2, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

# Entry widgets
combobox = ttk.Combobox(input_valor_8, values=combo_list7)
combobox.current(0)
combobox.grid(row=3, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

entry35 = ttk.Entry(input_valor_8, width=0)
entry35.insert(0, "Hercios Pantalla")
entry35.grid(row=4, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

spinbox = ttk.Spinbox(input_valor_8, from_=0, to=100, width=18)
spinbox.insert(0, "Inclinación de pantalla")
spinbox.grid(row=5, column=0, padx=(5,1), pady=(0,0), sticky="ew")

combo_list6[0] = "Antirreflejo"
readonly_combo4 = ttk.Combobox(input_valor_8,  state="readonly", values=combo_list6)
readonly_combo4.current(0)
readonly_combo4.grid(row=6, column=0, padx=(5,0), pady=(0,0),  sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_9 = ttk.LabelFrame(frame_contenedor, text="Teclado y Palmrest", padding=(20, 10))
label_frames.append(input_valor_9)

entry36 = ttk.Entry(input_valor_9, width=15)
entry36.insert(0, "Idioma Teclado")
entry36.grid(row=0, column=0,padx=(5, 0), pady=(5, 0), sticky="ew")

combo_list6[0] = "Retroiluminado"
readonly_combo5 = ttk.Combobox(input_valor_9, state="readonly", values=combo_list6)
readonly_combo5.current(0)
readonly_combo5.grid(row=1, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

combo_list6[0] = "Numérico"
readonly_combo6 = ttk.Combobox(input_valor_9, state="readonly", values=combo_list6)
readonly_combo6.current(0)
readonly_combo6.grid(row=2, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

entry37 = ttk.Entry(input_valor_9, width=15)
entry37.insert(0, "TouchPad")
entry37.grid(row=3, column=0,padx=(5, 0), pady=(5, 0), sticky="ew")

combo_list6[0] = "Lector de Huella"
readonly_combo7 = ttk.Combobox(input_valor_9, state="readonly", values=combo_list6)
readonly_combo7.current(0)
readonly_combo7.grid(row=4, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_10 = ttk.LabelFrame(frame_contenedor, text="Puertos - 1", padding=(20, 10))
label_frames.append(input_valor_10)

spinbox2 = ttk.Spinbox(input_valor_10, from_=0, to=100, width=20)
spinbox2.insert(0, "Cantidad puertos USB")
spinbox2.grid(row=0, column=0, padx=(5,0), pady=(5,0), sticky="ew")

spinbox3 = ttk.Spinbox(input_valor_10, from_=0, to=100, width=18)
spinbox3.insert(0, "Cantidad puertos Tipo C")
spinbox3.grid(row=1, column=0, padx=(5,0), pady=(5,0), sticky="ew")

combo_list6[0] = "Unidad Óptica"
readonly_combo8 = ttk.Combobox(input_valor_10, state="readonly", values=combo_list6)
readonly_combo8.current(0)
readonly_combo8.grid(row=2, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

combo_list6[0] = "Ranura SD"
readonly_combo9 = ttk.Combobox(input_valor_10, state="readonly", values=combo_list6)
readonly_combo9.current(0)
readonly_combo9.grid(row=3, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

combo_list6[0] = "Puerto Dock"
readonly_combo10 = ttk.Combobox(input_valor_10, state="readonly", values=combo_list6)
readonly_combo10.current(0)
readonly_combo10.grid(row=4, column=0, padx=(5,0), pady=(5,0),  sticky="ew")


# Frame para Ingreso de Valores de la máquina
input_valor_11 = ttk.LabelFrame(frame_contenedor, text="Puertos-2", padding=(20, 10))
label_frames.append(input_valor_11)

combo_list6[0] = "Puerto Ethernet"
readonly_combo11 = ttk.Combobox(input_valor_11, state="readonly", values=combo_list6)
readonly_combo11.current(0)
readonly_combo11.grid(row=0, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

combo_list6[0] = "Puerto HDMI"
readonly_combo12 = ttk.Combobox(input_valor_11, state="readonly", values=combo_list6)
readonly_combo12.current(0)
readonly_combo12.grid(row=1, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

combo_list6[0] = "Puerto H-Jack"
readonly_combo13 = ttk.Combobox(input_valor_11, state="readonly", values=combo_list6)
readonly_combo13.current(0)
readonly_combo13.grid(row=2, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

combo_list6[0] = "Puerto VGA"
readonly_combo14 = ttk.Combobox(input_valor_11, state="readonly", values=combo_list6)
readonly_combo14.current(0)
readonly_combo14.grid(row=3, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

combo_list6[0] = "Puerto Display"
readonly_combo15 = ttk.Combobox(input_valor_11, state="readonly", values=combo_list6)
readonly_combo15.current(0)
readonly_combo15.grid(row=4, column=0, padx=(5,0), pady=(5,0),  sticky="ew")


# Frame para Ingreso de Valores de la máquina
input_valor_12 = ttk.LabelFrame(frame_contenedor, text="Caja", padding=(20, 10))
label_frames.append(input_valor_12)

entry38 = ttk.Entry(input_valor_12, width=15)
entry38.insert(0, "-")
entry38.grid(row=4, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_13 = ttk.LabelFrame(frame_contenedor, text="Material", padding=(20, 10))
label_frames.append(input_valor_13)

entry39 = ttk.Entry(input_valor_13, width=15)
entry39.insert(0, "-")
entry39.grid(row=4, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_14 = ttk.LabelFrame(frame_contenedor, text="Cargador y accesorios", padding=(20, 10))
label_frames.append(input_valor_14)

entry40 = ttk.Entry(input_valor_14, width=15)
entry40.insert(0, "-")
entry40.grid(row=2, column=3,padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_14 = ttk.LabelFrame(frame_contenedor, text="Garantía", padding=(20, 10))
label_frames.append(input_valor_14)

entry40 = ttk.Entry(input_valor_14, width=15)
entry40.insert(0, "-")
entry40.grid(row=2, column=3,padx=(5, 1), pady=(0, 0), sticky="ew")

# Configurar el sistema de gestión de geometría 'grid' para el tab_2
tab_2.grid_rowconfigure(0, weight=1)
tab_2.grid_columnconfigure(0, weight=1)

# Agregar los LabelFrame al contenedor principal
for i, label_frame in enumerate(label_frames):
    row = i // 4
    column = i % 4
    label_frame.grid(row=row, column=column, padx=(20, 10), pady=(20, 10), sticky="ns")

# Asociar el evento de cambio de tamaño de la ventana a la función resize
root.bind('<Configure>', resize)
entry_list = [globals().get(f"entry{i}") for i in range(1, 41) if isinstance(globals().get(f"entry{i}"), ttk.Entry)]

root.mainloop()
