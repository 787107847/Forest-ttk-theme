import tkinter as tk
from tkinter import ttk, messagebox
import uuid
from conexion import Registro_datos
from PIL import Image, ImageTk


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

# Load the image using PIL
button_image_2 = Image.open("forest-light/cerrar.png")  # Replace with the path to your image
# Resize the image using LANCZOS filter (previously known as ANTIALIAS)
button_image_2 = button_image_2.resize((12, 12), Image.LANCZOS)
# Convert the PIL image to a PhotoImage
button_image2 = ImageTk.PhotoImage(button_image_2)

# Load the image using PIL
button_image_3 = Image.open("forest-light/comprobar.png")  # Replace with the path to your image
# Resize the mage using LANCZOS filter (previously known as ANTIALIAS)
button_image_3 = button_image_3.resize((12, 12), Image.LANCZOS)
# Convert the PIL image to a PhotoImage
button_image3= ImageTk.PhotoImage(button_image_3)


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
treeview = ttk.Treeview(canvas, selectmode="extended", columns=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"), height=26)
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

# Insertar treeview data
parent_items = {}  # Diccionario para guardar temporalmente los ítems padres

vacio = False

for item in treeview_data:
    parent = item[1][0]  # Acceder al primer elemento de la segunda tupla
    if parent is None:
        parent = ""
    iid = str(uuid.uuid4())  # Generar un iid único para cada ítem

    
    cell_data = list(item[1][3])  # Convertir los datos de la celda en una lista modificable
    """
    for i in range(len(cell_data)):
        if cell_data[i] is None:
            cell_data[i] = button_image2
    """


    if parent:
        if parent in parent_items:
            parent_iid = parent_items[parent]
            treeview.insert(parent=parent_iid, index="end", iid=iid, text=item[1][2], values=cell_data)
        else:
            parent_iid = treeview.insert(parent="", index="end", iid=parent, text=parent)
            parent_items[parent] = parent_iid
            treeview.insert(parent=parent_iid, index="end", iid=iid, text=item[1][2], values=cell_data)
    else:
        treeview.insert(parent="", index="end", iid=iid, text=item[1][2], values=cell_data)
        parent_items[parent] = iid

    # Configurar el icono para los valores None
    for i, cell_value in enumerate(item[1][3]):
        if cell_value is None:
            vacio = True
        
    if(vacio):
        treeview.item(iid, image=button_image2, values=cell_data)  # Asignar el icono solo para el ítem específico
    else:
        treeview.item(iid, image=button_image3, values=cell_data)  # Asignar el icono solo para el ítem específico



# Abrir todos los ítems padres
for parent_iid in parent_items.values():
    treeview.item(parent_iid, open=True)












# Crear un diccionario para almacenar los filtros seleccionados para cada columna
column_filters = {}

# Variable para almacenar las variables de selección de cada columna
selected_vars = {}

selected_values = {}

selected_items = []

# Variable para indicar si es la primera vez que se llama a la función de filtrado
is_first_call = True

# Función para obtener los valores únicos de una columna
def get_unique_values(col):
    global is_first_call
    global vacio

    if is_first_call:
        if col == 0:
            unique_values = set(item[1][0] for item in treeview_data)
        elif 0 < col <= len(treeview_data[0][1][3]):
            unique_values = set(item[1][3][col - 1] for item in treeview_data)
        else:
            return set()
    else:
        if col == 0:
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
        selected_values = [value for value, var in check_vars.items() if str(value) in str(selected_items)]
        print(selected_values)
        if selected_values:
            filtered_data = []
            if col != 0:
                for item in current_treeview_data:
                    if any(str(val) in str(item[1][3]) for val in selected_values):
                        filtered_data.append(item)
            else:
                for item in current_treeview_data:
                    if any(str(val) in str(item[1][0]) for val in selected_values):
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

        cell_data = list(item[1][3])  # Convertir los datos de la celda en una lista modificable
        vacio = any(cell_value is None for cell_value in cell_data)  # Verificar si hay valores None

        if parent:
            if parent in parent_items:
                parent_iid = parent_items[parent]
                treeview.insert(parent=parent_iid, index="end", iid=iid, text=f"{item[1][2]}", values=cell_data)
            else:
                parent_iid = treeview.insert(parent="", index="end", iid=parent, text=parent)
                parent_items[parent] = parent_iid
                treeview.insert(parent=parent_iid, index="end", iid=iid, text=f"{item[1][2]}", values=cell_data)
        else:
            treeview.insert(parent="", index="end", iid=iid, text=f"{item[1][2]}", values=cell_data)
            parent_items[parent] = iid

        # Configurar el icono para los valores None
        if vacio:
            treeview.item(iid, image=button_image2, values=cell_data)  # Asignar el icono para el ítem específico
        else:
            treeview.item(iid, image=button_image3, values=cell_data)  # Asignar el icono para el ítem específico


    # Abrir todos los ítems padres
    for parent_iid in parent_items.values():
        treeview.item(parent_iid, open=True)




def show_filter_window(col):
    global selected_items
    unique_values = get_unique_values(col)
    if unique_values:
        # Crear la ventana emergente
        filter_window = tk.Toplevel(root)
        filter_window.title("Filtrar opciones")

        # Función para aplicar el filtro y cerrar la ventana
        def apply_filter_and_close():
            global selected_items
            selected_values = [value for value in options_listbox.curselection()]
            selected_items = [options_listbox.get(index) for index in selected_values]
            filter_treeview(col)
            filter_window.destroy()

        # Función para seleccionar todos los valores
        def select_all_options():
            options_listbox.select_set(0, tk.END)

        unique_states = {}  # Diccionario para almacenar el valor único y su estado (marcado o no)
        for value in unique_values:
            unique_states[value] = tk.StringVar(value='0')

        # Cuadro de entrada de texto (Entry Box) para búsqueda
        search_entry = tk.Entry(filter_window)
        search_entry.pack(pady=10)
        search_entry_var = tk.StringVar()
        search_entry.config(textvariable=search_entry_var)

        # Frame para mostrar las opciones filtradas con desplazamiento vertical
        frame = tk.Frame(filter_window, height=200)
        frame.pack(padx=10, pady=5)

        # Configurar el desplazamiento vertical con la rueda del mouse
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
        options_listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, selectmode=tk.MULTIPLE)
        scrollbar.config(command=options_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        options_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for value, var in unique_states.items():
            options_listbox.insert(tk.END, value)

        # Función para filtrar opciones a medida que se escribe en el cuadro de búsqueda
        def filter_options(*args):
            search_text = search_entry_var.get()
            options_listbox.delete(0, tk.END)
            for value in unique_states:
                if search_text.lower() in str(value).lower():
                    options_listbox.insert(tk.END, value)

        search_entry_var.trace_add("write", filter_options)

        # Botón "Seleccionar Todo"
        select_all_button = tk.Button(filter_window, text="Seleccionar Todo", command=select_all_options)
        select_all_button.pack(pady=5)

        # Botón para aplicar el filtro
        apply_button = tk.Button(filter_window, text="Aplicar", command=apply_filter_and_close)
        apply_button.pack(pady=10)

        filter_window.geometry(f"+{root.winfo_rootx() + root.winfo_width() // 2 - 150}+{root.winfo_rooty() + root.winfo_height() // 2 - 150}")

        selected_vars[col] = unique_states

    else:
        # No mostrar la ventana si no hay valores únicos en la columna
        pass




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


placeholder_list = [
    'N° Item', 'Fecha de fabricación', 'Stock', 'Costo', 'Proveedor', 'N° de serie',
    'Capacidad', 'Tipo', 'Frecuencia', 'Posición (M)', 'Maximo de ram', 'Marca',
    'Linea', 'Modelo', 'N° producto', 'Tipo Almacenamiento', 'Capacidad',
    'Factor de forma', 'Especificación', 'Horas de uso', 'Nombre Procesador',
    'Núcleos', 'Generación', 'Velocidad CPU', 'Marca',
    'Linea', 'Modelo', 'Capacidad', 'Tipo batería', 'Extendida', 'Capacidad Batería',
    '% Uso', 'Táctil', 'Tamaño de Pantalla', 'Resolución Pantalla', 'Panel',
    'Hercios Pantalla', 'Inclinación de pantalla', 'Antirreflejo', 'Idioma Teclado',
    'Retroiluminado', 'Numérico', 'TouchPad', 'Lector de Huella', 'Cantidad puertos USB',
    'Cantidad puertos Tipo C', 'Unidad Óptica', 'Ranura SD', 'Puerto Dock', 'Puerto Ethernet',
    'Puerto HDMI', 'Puerto H-Jack', 'Puerto VGA', 'Puerto Display', 'Webcam',
    'Posición Webcam', 'Descripción Webcam', 'Cargador Original', 'Alimentación de Cargador',
    'Accesorios', 'Material de Construcción', 'Cumple norma STD',
    'Peso', 'Wifi', 'BlueTooth', '4G', 'Ancho', 'Largo', 'Alto', 'Peso de la caja',
    'Apto para envío', 'Oferente Garantía', 'Tiempo de garantía', 'Tipo Garantía',
    'Comprobante de compra', 'Comentario Garantía', 'Condición', 'Condición Touch',
    'Condición Teclado', 'Condición Reposamuñecas', 'Condición Tapa', 'Condición Pantalla',
    'Otros comentarios'
]

label_frames_values = ['Valores Principales','RAM','Marca y Modelo','Almacenamiento','Procesador',
                       'Grafica','Batería','Pantalla','Teclado y Palmrest','Puertos 1','Puertos 2',
                       'Cargador y accesorios', 'Material y otros componentes','Caja','Garantía',
                       'Condición']

label_frames_names =['c{}'.format(i) for i in range(1, 17)]

lista_letras_c = ['cg{}'.format(i) for i in range(1, 84)]

# Variable para cada Combobox
combo_vars = []

# Crear y configurar los Comboboxes
comboboxes = []

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

automatizador = 0



# Crear y configurar los LabelFrames y Comboboxes
for i in range(len(label_frames_values)):
    # Crear el LabelFrame
    label_frames_names[i] = ttk.LabelFrame(frame_contenedor, text=label_frames_values[i], padding=(20, 10))

    # Agregar el LabelFrame a la lista
    label_frames.append(label_frames_names[i])

    if(automatizador == 0 or automatizador==54 or automatizador == 60):
        for a in range(0,6):
            lista_letras_c[automatizador] = ttk.Combobox(label_frames_names[i],values=combo_list)
            lista_letras_c[automatizador].grid(row=a, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")
            lista_letras_c[automatizador].set(placeholder_list[automatizador])
            lista_letras_c[automatizador].bind("<<ComboboxSelected>>")

            # Agregar el Combobox a la lista correspondiente
            comboboxes.append(lista_letras_c[automatizador])
            automatizador+=1
    elif(automatizador == 6 or automatizador == 15 or automatizador==39 or automatizador==44 or automatizador ==49 or automatizador ==66 or automatizador==71 ):
        for a in range(0,5):
            lista_letras_c[automatizador] = ttk.Combobox(label_frames_names[i], values=combo_list)
            lista_letras_c[automatizador].grid(row=a, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")
            lista_letras_c[automatizador].set(placeholder_list[automatizador])
            lista_letras_c[automatizador].bind("<<ComboboxSelected>>")

            # Agregar el Combobox a la lista correspondiente
            comboboxes.append(lista_letras_c[automatizador])
            automatizador+=1
    elif(automatizador==11 or automatizador == 20 or automatizador==24 or automatizador==28):
        for a in range(0,4):
            lista_letras_c[automatizador] = ttk.Combobox(label_frames_names[i], values=combo_list)
            lista_letras_c[automatizador].grid(row=a, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")
            lista_letras_c[automatizador].set(placeholder_list[automatizador])
            lista_letras_c[automatizador].bind("<<ComboboxSelected>>")

            # Agregar el Combobox a la lista correspondiente
            comboboxes.append(lista_letras_c[automatizador])
            automatizador+=1
    elif(automatizador==32 or automatizador==76):
        for a in range(0,7):
            lista_letras_c[automatizador] = ttk.Combobox(label_frames_names[i], values=combo_list)
            lista_letras_c[automatizador].grid(row=a, column=0, padx=(5, 1), pady=(0, 0), sticky="ew")
            lista_letras_c[automatizador].set(placeholder_list[automatizador])
            lista_letras_c[automatizador].bind("<<ComboboxSelected>>")

            # Agregar el Combobox a la lista correspondiente
            comboboxes.append(lista_letras_c[automatizador])
            automatizador+=1



# Frame para Ingreso de Valores de la máquina
button_1 = ttk.LabelFrame(frame_contenedor, text="Botones", padding=(10, 5))
label_frames.append(button_1)

# Button widget
button1 = ttk.Button(button_1, text="Validar")
button1.grid(row=0, column=0, padx=5, pady=(0, 0), sticky="nse")  # Adjust sticky

button2 = ttk.Button(button_1, text="Guardar")
button2.grid(row=0, column=1, padx=5, pady=(0, 0), sticky="nsw")  # Adjust sticky




root.bind('<Configure>', resize)



root.mainloop()