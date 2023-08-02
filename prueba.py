from conexion import Registro_datos

# Crear una instancia de la clase Registro_datos
registro_datos = Registro_datos()

# Llamar al método mostrar_productos usando la instancia creada
datos_productos = registro_datos.mostrar_productos()

# Función para imprimir una línea separadora para mejorar la visualización
def imprimir_linea_separadora():
    print("-" * 80)

# Imprimir los resultados obtenidos
for producto in datos_productos:
    imprimir_linea_separadora()
    print(f"Item: {producto[0]}")
    print(f"Descripción: {producto[1]}")
    print(f"Precio Original: {producto[2]}")
    print(f"Precio Actualizado: {producto[3]}")
    print(f"Tipo de Descuento: {producto[4]}")
    print(f"Valor de Descuento: {producto[5]}")
    print(f"Número de Serie: {producto[6]}")
    print(f"Capacidad de Almacenamiento: {producto[7]} GB")
    print(f"Tipo de RAM: {producto[8]}")
    print(f"Frecuencia de RAM: {producto[9]}")
    print(f"Gráfica: {producto[10]}")
    print(f"Sistema Operativo: {producto[11]}")
    print(f"Marca: {producto[12]}")
    print(f"Modelo: {producto[13]}")
    print(f"Alimentación del Cargador: {producto[14]}")
    print(f"Punta del Cargador: {producto[15]}")
    print(f"Tipo de Otro: {producto[16]}")
    print(f"Tamaño de Pantalla: {producto[17]} pulgadas")
    print(f"Resolución de Pantalla: {producto[18]}")
    print(f"Idioma del Teclado: {producto[19]}")
    print(f"Retroiluminado del Teclado: {producto[20]}")
    print(f"Puerto CD: {producto[21]}")
    print(f"Puerto SD: {producto[22]}")
    print(f"Puerto Dock: {producto[23]}")
    print(f"Puerto Ethernet: {producto[24]}")
    print(f"Puerto HDMI: {producto[25]}")
    print(f"Puerto Hjack: {producto[26]}")
    print(f"Puerto VGA: {producto[27]}")
    print(f"Puerto Display: {producto[28]}")
    print(f"Cantidad de Puertos USB: {producto[29]}")
    print(f"Cantidad de Puertos TypeC: {producto[30]}")

    imprimir_linea_separadora()