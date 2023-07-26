import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import uuid
from conexion import Registro_datos
from PIL import Image, ImageTk
import decimal

# Create the main application window
root = tk.Tk()
root.title("UltraPC")
root.option_add("*tearOff", False)  # This is always a good idea

# Load the image using PIL
button_image_pil = Image.open("forest-light/filtro-de-barras.png")  # Replace with the path to your image
# Resize the image using LANCZOS filter (previously known as ANTIALIAS)
button_image_pil = button_image_pil.resize((12, 12), Image.LANCZOS)
# Convert the PIL image to a PhotoImage
button_image = ImageTk.PhotoImage(button_image_pil)


def on_canvas_configure2(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas_tab_2.configure(scrollregion=canvas_tab_2.bbox("all"))  # Add this line for tab_2

def on_mousewheel2(event):
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
        if entry.get() == "" or entry.get() == " ":
            entry.state(["invalid"])
        else:
            entry.state(["!invalid"])


def check_fields():
    # Lista de Combobox que se deben verificar
    combo_list = [readonly_combo, readonly_combo3, readonly_combo4, readonly_combo5, readonly_combo6,
                  readonly_combo7, readonly_combo8, readonly_combo9, readonly_combo10, readonly_combo11,
                  readonly_combo12, readonly_combo13, readonly_combo14, readonly_combo15, readonly_combo16,
                  readonly_combo17, readonly_combo18, readonly_combo19, readonly_combo20]

    for combo in combo_list:
        while True:
            if combo.get() == "" or combo.current() == 0:
                result = messagebox.askyesnocancel("Modificación de campo",
                                                   f"El combobox {combo.get()} está vacío o en posición [0]. ¿Desea modificar el campo?\n\nResponda con:\n\n[Sí] para modificar el campo.\n[No] para dejar el campo sin modificar.\n[Cancelar] para no modificar ninguno de los campos.",
                                                   icon='warning', default=messagebox.YES)
                if result is None:
                    # Si elige "Cancelar", guardar el cambio al instante y salir del bucle while
                    messagebox.showinfo("Todo listo", "Configuración aceptada")
                    return
                elif result:
                    # Si elige "Sí", permitir modificar el campo
                    break
                else:
                    # Si elige "No", pasar al siguiente combo en la lista
                    index = combo_list.index(combo)
                    if index + 1 < len(combo_list):
                        combo = combo_list[index + 1]
                    else:
                        # Si ya no hay más combos para verificar, guardar el cambio al instante y salir del bucle while
                        messagebox.showinfo("Todo listo", "Configuración aceptada")
                        return
            else:
                # Si el combo no está vacío y no es la posición [0], pasar al siguiente combo en la lista
                index = combo_list.index(combo)
                if index + 1 < len(combo_list):
                    combo = combo_list[index + 1]
                else:
                    # Si ya no hay más combos para verificar, guardar el cambio al instante y salir del bucle while
                    messagebox.showinfo("Todo listo", "Configuración aceptada")
                    return


# Make the app responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create a style
# Apply the theme
style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
style.theme_use("forest-light")
style.map("TCombobox", selectbackground=[("readonly", "#005b9d")], selectforeground=[("readonly", "#ffffff")],
          fieldbackground=[("readonly", "#ffffff")], foreground=[("readonly", "#ffffff")])
style.map("TButton", background=[("!active", "#313131"), ("active", "#005b9d")], foreground=[("!active", "#ffffff"), ("active", "#ffffff")])

# Create lists for the Comboboxes
option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
combo_list = ["Capacidad", "4 GB", "8 GB", "12 GB", "etc"]
combo_list1 = ["Marca", "Lenovo", "HP", "DELL", "ACER", "etc"]
combo_list2 = ["Linea", "ThinkPad", "Latitude", "IdeaPad Gaming", "Aspire", "etc"]
combo_list3 = ["Tipo Almacenamiento", "SSD", "HDD", ""]
combo_list4 = ["Factor de forma", "SATA", "M.2", "PCIe", "etc"]
combo_list5 = ["Tipo batería", "Interna", "Externa"]
combo_list6 = ["H", "SI", "NO", ""]
combo_list7 = ["Panel", "LED IPS", "Retina", "LED TN", "etc"]
combo_list8 = ["Condición", "Nuevo", "OpenBox", "Usado - Nuevo", "Usado - Bueno", "Usado", "Dañado", ""]

# Crear notebook
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

titulos_prints_list = [
    "Descripción",
    "Precio Original",
    "Precio Actualizado",
    "Tipo de Descuento",
    "Valor de Descuento",
    "Número de Serie",
    "Capacidad de Almacenamiento",
    "Tipo de RAM",
    "Frecuencia de RAM",
    "Gráfica",
    "Sistema Operativo",
    "Marca",
    "Modelo",
    "Alimentación del Cargador",
    "Punta del Cargador",
    "Tipo de Otro",
    "Tamaño de Pantalla",
    "Resolución de Pantalla",
    "Idioma del Teclado",
    "Retroiluminado del Teclado",
    "Puerto CD",
    "Puerto SD",
    "Puerto Dock",
    "Puerto Ethernet",
    "Puerto HDMI",
    "Puerto Hjack",
    "Puerto VGA",
    "Puerto Display",
    "Cantidad de Puertos USB",
    "Cantidad de Puertos TypeC"
]

# Contenido de la pestaña 1
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text="Tab 1")
# Crear el Frame para el botón de resetear
resetear = tk.Frame(tab_1)
resetear.pack(side=tk.TOP, fill="x") 


# Crear el canvas
canvas = tk.Canvas(tab_1)
canvas.pack(fill="both", expand=True)

# Crear el árbol (Treeview)
treeview = ttk.Treeview(canvas, selectmode="extended", columns=("#0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"), height=26)
treeview.pack(side=tk.BOTTOM)

# Treeview headings
treeview.heading("#0", text="Item", anchor="center")
for i in range(1, 31):
    if i <= len(titulos_prints_list):
        column_title = titulos_prints_list[i - 1]
    else:
        column_title = " "  # Espacio en blanco si no hay más elementos en la lista
    treeview.heading(str(i), text=column_title, anchor="center")

# Crear una instancia de la clase Registro_datos
registro_datos = Registro_datos()

# Llamar al método mostrar_productos usando la instancia creada
datos_productos = registro_datos.mostrar_productos()

# Define una función para transformar los datos del producto en el formato adecuado
def transformar_producto(producto):
    item = producto[0]
    subitem = producto[1]
    data_values = tuple(producto[2:])  # Convertir data_values en una tupla
    result = (None, "", "Item", ()), (item, "", "", (subitem,) + data_values)
    yield result

# Crear una lista para almacenar los datos en el formato del treeview
treeview_data = []
for producto in datos_productos:
    treeview_data.extend(transformar_producto(producto))

# Insert treeview data 
parent_items = {}  # Diccionario para guardar temporalmente los ítems padres

for item in treeview_data:
    parent = item[1][0]  # Acceder al primer elemento de la segunda tupla
    if parent is None:
        parent = ""
    iid = str(uuid.uuid4())  # Generar un iid único para cada ítem

    if parent:
        if parent in parent_items:
            parent_iid = parent_items[parent]
            treeview.insert(parent=parent_iid, index="end", iid=iid, text=item[1][2], values=item[1][3])
        else:
            parent_iid = treeview.insert(parent="", index="end", iid=parent, text=parent)
            parent_items[parent] = parent_iid
            treeview.insert(parent=parent_iid, index="end", iid=iid, text=item[1][2], values=item[1][3])
    else:
        treeview.insert(parent="", index="end", iid=iid, text=item[1][2], values=item[1][3])
        parent_items[parent] = iid

# Abrir todos los ítems padres
for parent_iid in parent_items.values():
    treeview.item(parent_iid, open=True)








# Crear un diccionario para almacenar los filtros seleccionados para cada columna
column_filters = {}

# Variable para almacenar las variables de selección de cada columna
selected_vars = {}

selected_values = {}

current_treeview_data = []
# Variable para indicar si es la primera vez que se llama a la función
is_first_call = True

# Función para obtener los valores únicos de una columna
def get_unique_values(col):
    global is_first_call

    if is_first_call:
        if col == 0:
            print("SÍ")
            unique_values = set(item[1][0] for item in treeview_data)
        elif 0 < col <= len(treeview_data[0][1][3]):
            unique_values = set(item[1][3][col - 1] for item in treeview_data)
        else:
            return set()
    else:
        if col == 0:
            print("SÍ")
            unique_values = set(item[1][0] for item in current_treeview_data)
        elif 0 < col <= len(treeview_data[0][1][3]):
            unique_values = set(item[1][3][col - 1] for item in current_treeview_data)
        else:
            return set()

    # Descartar valores vacíos si existen
    unique_values.discard(None)

    # Actualizar la bandera para indicar que ya se ha llamado a la función al menos una vez
    is_first_call = False

    return unique_values


# Crear una copia de los datos originales del treeview
original_treeview_data = treeview_data.copy()

# Crear una variable para almacenar los datos filtrados actualizados
current_treeview_data = original_treeview_data.copy()

# Filtrado
def filter_treeview(col):
    global selected_vars
    global current_treeview_data

    # Reiniciar los datos filtrados cada vez que se ejecute desde cero
    if not any(selected_vars.values()):
        current_treeview_data = original_treeview_data.copy()

    # Aplicar los filtros sucesivamente
    for check_vars in selected_vars.values():
        selected_values = [value for value, var in check_vars.items() if var.get() == '1']
        if selected_values:
            filtered_data = []
            for item in current_treeview_data:
                if(col == 0):
                   if item[1][0] in selected_values:
                        filtered_data.append(item)
                else:
                    if (any(val in item[1][3] for val in selected_values)):
                        filtered_data.append(item)
            current_treeview_data = filtered_data

    # Limpiar el treeview actual
    treeview.delete(*treeview.get_children())

    # Restablecer la estructura parent_items
    parent_items.clear()

    # Re-insertar los elementos filtrados en el treeview
    for index, item in enumerate(current_treeview_data, start=1):
        parent = item[1][0]  # Acceder al primer elemento de la segunda tupla
        if parent is None:
            parent = ""
        iid = str(uuid.uuid4())  # Generar un iid único para cada ítem

        if parent:
            if parent in parent_items:
                parent_iid = parent_items[parent]
                treeview.insert(parent=parent_iid, index="end", iid=iid, text=f"{index}. {item[1][2]}", values=item[1][3])
            else:
                parent_iid = treeview.insert(parent="", index="end", iid=parent, text=parent)
                parent_items[parent] = parent_iid
                treeview.insert(parent=parent_iid, index="end", iid=iid, text=f"{index}. {item[1][2]}", values=item[1][3])
        else:
            treeview.insert(parent="", index="end", iid=iid, text=f"{index}. {item[1][2]}", values=item[1][3])
            parent_items[parent] = iid

    # Abrir todos los ítems padres
    for parent_iid in parent_items.values():
        treeview.item(parent_iid, open=True)

    # Actualizar valores únicos y estados de checkbuttons
    for col in selected_vars:
        unique_values = get_unique_values(col)
        if unique_values:
            selected_var = selected_vars[col]
            for value in selected_var:
                if value not in unique_values:
                    selected_var[value].set('0')
            update_filter_window_values(col, unique_values)

def update_filter_window_values(col, unique_values):
    if col in selected_vars:
        selected_var = selected_vars[col]
        for value in unique_values:
            if value not in selected_var:
                selected_var[value] = tk.StringVar(value='0')



def show_filter_window(col):
    unique_values = get_unique_values(col)
    if unique_values:
        # Crear la ventana emergente
        filter_window = tk.Toplevel(root)
        filter_window.title("Filtrar opciones")

        # Función para aplicar el filtro y cerrar la ventana
        def apply_filter_and_close():
            selected_values = [value for value, checked in unique_states.items() if checked.get() == '1']
            filter_treeview(col)
            filter_window.destroy()

        unique_states = {}  # Diccionario para almacenar el valor único y su estado (marcado o no)
        for value in unique_values:
            unique_states[value] = tk.StringVar(value='0')

        checkbuttons = []  # Lista para almacenar los botones de verificación
        for value, var in unique_states.items():
            checkbutton = tk.Checkbutton(filter_window, text=value, variable=var)
            checkbutton.pack(anchor="w", padx=10)
            checkbuttons.append(checkbutton)

        apply_button = tk.Button(filter_window, text="Aplicar", command=apply_filter_and_close)
        apply_button.pack(pady=10)

        filter_window.geometry(f"+{root.winfo_pointerx()}+{root.winfo_pointery()}")

        selected_vars[col] = unique_states

    else:
        # No mostrar la ventana si no hay valores únicos en la columna
        pass


def update_checkbuttons_state():
    for col, selected_states in selected_vars.items():
        unique_values = get_unique_values(col)
        for value, var in selected_states.items():
            if value not in unique_values:
                var.set('0')

def reset_treeview():
    global selected_vars

    selected_vars.clear()
    filter_treeview(1)

# Agregar el botón al Frame
reset_button = tk.Button(resetear, text="Resetear", command=reset_treeview)
reset_button.pack(side=tk.LEFT, padx=10)











# Configurar el ancho de las columnas y centrar el contenido
treeview.column("#0", width=50, stretch=True, anchor="center")
treeview.heading("#0", image=button_image, command=lambda col=0: show_filter_window(col))  # Primera columna
for i in range(1, 31):
    treeview.column("#" + str(i), width=200, stretch=True, anchor="center")  # Ancho y centrado de la columna

# Añadir un botón en cada columna del Treeview
for i in range(1, 31):
    treeview.column(f"#{i}", stretch=False)  # Ajustar esta opción para cambiar el ancho de las columnas
    treeview.heading(f"#{i}", image=button_image, command=lambda col=i: show_filter_window(col))  # Mostrar la ventana emergente en la cabecera de la columna

# Ajustar el canvas al tamaño del treeview
canvas.create_window((0, 0), window=treeview, anchor="nw")

# Función para manejar el evento MouseWheel en el treeview (para desplazamiento vertical en tab_1)
def on_treeview_mousewheel(event):
    canvas.yview_scroll(-1 * (event.delta), "units")

# Función para manejar el evento Shift-MouseWheel en el treeview (para desplazamiento horizontal en tab_1)
def on_treeview_shift_mousewheel(event):
    # Adjust this factor to control the horizontal scrolling speed
    horizontal_scroll_speed = 0.1
    canvas.xview_scroll(-1 * int(horizontal_scroll_speed * event.delta), "units")

# Enlazar el evento MouseWheel en el treeview de tab_1 para desplazamiento vertical
treeview.bind("<MouseWheel>", on_treeview_mousewheel)

# Enlazar el evento Shift-MouseWheel en el treeview de tab_1 para desplazamiento horizontal
treeview.bind("<Shift-MouseWheel>", on_treeview_shift_mousewheel)

# Función para ajustar el tamaño del canvas al tamaño del treeview en tab_1
def on_canvas_configure(event):
    canvas_width = event.width
    treeview_width = treeview.winfo_reqwidth()
    if treeview_width != canvas_width:
        canvas.itemconfigure(treeview, width=canvas_width)
        canvas.configure(scrollregion=canvas.bbox("all"))

# Ajustar el canvas al tamaño del treeview en tab_1
canvas.create_window((0, 0), window=treeview, anchor="nw")

# Configurar el canvas para que se desplace con el treeview en tab_1
treeview.bind("<Configure>", on_canvas_configure)

# Barras de desplazamiento
treeScrollY = ttk.Scrollbar(tab_1, orient="vertical", command=treeview.yview)
treeScrollX = ttk.Scrollbar(tab_1, orient="horizontal", command=treeview.xview)

treeview.configure(yscrollcommand=treeScrollY.set, xscrollcommand=treeScrollX.set)

# Ajustar la posición de las barras de desplazamiento
treeScrollY.pack(side="right", fill="y")
treeScrollX.pack(side="bottom", fill="x")

# Configurar el canvas para que se desplace con las barras de desplazamiento
canvas.configure(yscrollcommand=treeScrollY.set, xscrollcommand=treeScrollX.set)






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
content_frame_tab_2.bind("<Configure>", on_canvas_configure2)

# Asociar evento de scroll del mouse
canvas_tab_2.bind_all("<MouseWheel>", on_mousewheel2)

# Contenedor principal
frame_contenedor = ttk.Frame(content_frame_tab_2)
frame_contenedor.pack()

# Lista de LabelFrame
label_frames = []

# Frame para Ingreso de Valores Principales
input_valor_1 = ttk.LabelFrame(frame_contenedor, text="Valores principales", padding=(20, 10))
label_frames.append(input_valor_1)

# Lista de Entry
entry_list = []

# Entry widgets
entry0 = ttk.Entry(input_valor_1,width=0)
entry0.insert(0, "N° Item")
entry0.grid(row=0, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

entry1 = ttk.Entry(input_valor_1,width=18)
entry1.insert(0, "Fecha de fabricación")
entry1.grid(row=1, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")


spinbox = ttk.Spinbox(input_valor_1, from_=0, to=100,width=0)
spinbox.insert(0, "Stock")
spinbox.grid(row=2, column=0, padx=(5,1), pady=(0,0), sticky="ew")

entry3 = ttk.Entry(input_valor_1,width=0)
entry3.insert(0, "Costo")
entry3.grid(row=3, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")


entry4 = ttk.Entry(input_valor_1,width=0)
entry4.insert(0, "Proveedor")
entry4.grid(row=4, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")


entry5 = ttk.Entry(input_valor_1,width=0)
entry5.insert(0, "N° de serie")
entry5.grid(row=5, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_2 = ttk.LabelFrame(frame_contenedor, text="RAM", padding=(20, 10))
label_frames.append(input_valor_2)

# Combobox"
combobox0 = ttk.Combobox(input_valor_2, values=combo_list)
combobox0.current(0)
combobox0.grid(row=0, column=0,padx=(5,1), pady=(0, 0), sticky="ew")

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
combobox1 = ttk.Combobox(input_valor_3, values=combo_list1)
combobox1.current(0)
combobox1.grid(row=1, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

combobox2 = ttk.Combobox(input_valor_3, values=combo_list2)
combobox2.current(0)
combobox2.grid(row=2, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

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
combobox3 = ttk.Combobox(input_valor_4, values=combo_list3)
combobox3.current(0)
combobox3.grid(row=0, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

entry17 = ttk.Entry(input_valor_4)
entry17.insert(0, "Capacidad")
entry17.grid(row=1, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")

combobox4 = ttk.Combobox(input_valor_4, values=combo_list4)
combobox4.current(0)
combobox4.grid(row=2, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

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
combobox5 = ttk.Combobox(input_valor_8, values=combo_list7)
combobox5.current(0)
combobox5.grid(row=3, column=0,padx=(5, 1), pady=(0, 0),  sticky="ew")

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
input_valor_10 = ttk.LabelFrame(frame_contenedor, text="Puertos-1", padding=(20, 10))
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
input_valor_12 = ttk.LabelFrame(frame_contenedor, text="Cargador y accesorios", padding=(20, 10))
label_frames.append(input_valor_12)

combo_list6[0] = "Webcam"
readonly_combo15 = ttk.Combobox(input_valor_12, state="readonly", values=combo_list6)
readonly_combo15.current(0)
readonly_combo15.grid(row=0, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

entry39 = ttk.Entry(input_valor_12, width=15)
entry39.insert(0, "Posición Webcam")
entry39.grid(row=1, column=0,padx=(5, 0), pady=(5, 0), sticky="ew")

entry40 = ttk.Entry(input_valor_12, width=15)
entry40.insert(0, "Descripción Webcam")
entry40.grid(row=2, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

combo_list6[0] = "Cargador Original"
readonly_combo16 = ttk.Combobox(input_valor_12, state="readonly", values=combo_list6)
readonly_combo16.current(0)
readonly_combo16.grid(row=3, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

entry41 = ttk.Entry(input_valor_12, width=15)
entry41.insert(0, "Alimentación de Cargador")
entry41.grid(row=4, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

entry41 = ttk.Entry(input_valor_12, width=15)
entry41.insert(0, "Alimentación de Cargador")
entry41.grid(row=4, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

entry42 = ttk.Entry(input_valor_12, width=15)
entry42.insert(0, "Accesorios")
entry42.grid(row=5, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")


# Frame para Ingreso de Valores de la máquina
input_valor_13 = ttk.LabelFrame(frame_contenedor, text="Material y otros componentes", padding=(20, 10))
label_frames.append(input_valor_13)

entry43 = ttk.Entry(input_valor_13, width=15)
entry43.insert(0, "Material de Construcción")
entry43.grid(row=0, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

combo_list6[0] = "Cumple norma STD"
readonly_combo17 = ttk.Combobox(input_valor_13, state="readonly", values=combo_list6)
readonly_combo17.current(0)
readonly_combo17.grid(row=1, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

spinbox4 = ttk.Spinbox(input_valor_13, from_=0, to=100, width=18)
spinbox4.insert(0, "Peso")
spinbox4.grid(row=2, column=0, padx=(5,0), pady=(5,0), sticky="ew")

combo_list6[0] = "Wifi"
readonly_combo18 = ttk.Combobox(input_valor_13, state="readonly", values=combo_list6)
readonly_combo18.current(0)
readonly_combo18.grid(row=3, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

combo_list6[0] = "BlueTooth"
readonly_combo19 = ttk.Combobox(input_valor_13, state="readonly", values=combo_list6)
readonly_combo19.current(0)
readonly_combo19.grid(row=4, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

combo_list6[0] = "4G"
readonly_combo20 = ttk.Combobox(input_valor_13, state="readonly", values=combo_list6)
readonly_combo20.current(0)
readonly_combo20.grid(row=5, column=0, padx=(5,0), pady=(5,0),  sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_14 = ttk.LabelFrame(frame_contenedor, text="Caja", padding=(20, 10))
label_frames.append(input_valor_14)

spinbox5 = ttk.Spinbox(input_valor_14, from_=0, to=100, width=18)
spinbox5.insert(0, "Ancho")
spinbox5.grid(row=0, column=0, padx=(5,0), pady=(5,0), sticky="ew")

spinbox6 = ttk.Spinbox(input_valor_14, from_=0, to=100, width=18)
spinbox6.insert(0, "Largo")
spinbox6.grid(row=1, column=0, padx=(5,0), pady=(5,0), sticky="ew")

spinbox7 = ttk.Spinbox(input_valor_14, from_=0, to=100, width=18)
spinbox7.insert(0, "Alto")
spinbox7.grid(row=2, column=0, padx=(5,0), pady=(5,0), sticky="ew")

spinbox8 = ttk.Spinbox(input_valor_14, from_=0, to=100, width=18)
spinbox8.insert(0, "Peso de la caja")
spinbox8.grid(row=3, column=0, padx=(5,0), pady=(5,0), sticky="ew")

entry40 = ttk.Entry(input_valor_14, width=15)
entry40.insert(0, "Apto para envío")
entry40.grid(row=4, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_15 = ttk.LabelFrame(frame_contenedor, text="Garantía", padding=(20, 10))
label_frames.append(input_valor_15)

entry41 = ttk.Entry(input_valor_15, width=15)
entry41.insert(0, "Oferente Garantía")
entry41.grid(row=0, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

spinbox9 = ttk.Spinbox(input_valor_15, from_=0, to=100, width=18)
spinbox9.insert(0, "Tiempo de garantía")
spinbox9.grid(row=1, column=0, padx=(5,0), pady=(5,0), sticky="ew")

entry42 = ttk.Entry(input_valor_15, width=15)
entry42.insert(0, "Tipo Garantía")
entry42.grid(row=2, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

entry43 = ttk.Entry(input_valor_15, width=15)
entry43.insert(0, "Comprobante de compra")
entry43.grid(row=3, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

entry44 = ttk.Entry(input_valor_15, width=15)
entry44.insert(0, "Comentario Garantía")
entry44.grid(row=4, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
input_valor_16 = ttk.LabelFrame(frame_contenedor, text="Condición", padding=(20, 10))
label_frames.append(input_valor_16)

combobox6 = ttk.Combobox(input_valor_16, values=combo_list8)
combobox6.current(0)
combobox6.grid(row=0, column=0,padx=(5,1), pady=(0, 0), sticky="ew")

entry46 = ttk.Entry(input_valor_16, width=15)
entry46.insert(0, "Condición Touch")
entry46.grid(row=1, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

entry47 = ttk.Entry(input_valor_16, width=15)
entry47.insert(0, "Condición Teclado")
entry47.grid(row=2, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

entry48 = ttk.Entry(input_valor_16, width=15)
entry48.insert(0, "Condición Reposamuñecas")
entry48.grid(row=3, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

entry49 = ttk.Entry(input_valor_16, width=15)
entry49.insert(0, "Condición Tapa")
entry49.grid(row=4, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

entry50 = ttk.Entry(input_valor_16, width=15)
entry50.insert(0, "Condición Pantalla")
entry50.grid(row=5, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

entry51 = ttk.Entry(input_valor_16, width=20)
entry51.insert(0, "Otros comentarios")
entry51.grid(row=6, column=0,padx=(5, 1), pady=(0, 0), sticky="ew")

# Frame para Ingreso de Valores de la máquina
button_1 = ttk.LabelFrame(frame_contenedor, text="Botones", padding=(10, 5))
label_frames.append(button_1)

# Button widget
button1 = ttk.Button(button_1, text="Validar",command=validate_entry)
button1.grid(row=0, column=0, padx=5, pady=(0, 0), sticky="nse")  # Adjust sticky

button2 = ttk.Button(button_1, text="Guardar",command=check_fields)
button2.grid(row=0, column=1, padx=5, pady=(0, 0), sticky="nsw")  # Adjust sticky


# Asociar el evento de cambio de tamaño de la ventana a la función resize
root.bind('<Configure>', resize)
entry_list = [globals().get(f"entry{i}") for i in range(0, 51) if isinstance(globals().get(f"entry{i}"), ttk.Entry)]

# Make the app responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()