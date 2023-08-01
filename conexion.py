import mysql.connector

class Registro_datos():
    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost', database='ultrapc', user='root', password='95781432365zZ@', port='3306')

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = """
        SELECT i.item, i.descripcion, ph.precioOriginal, ph.precioActualizado,
            de.tipoDescuento, de.valorDescuento, ns.numeroSerie,
            a.capacidad, r.tipoRam, r.frecuencia, g.nomGrafica,
            s.sistemaOperativo, m.nombreMarca, n.nombreModelo,
            c.alimentacion, c.puntaCargador, o.tipoOtro,
            pa.tamannoPantalla, pa.resolucionPantalla,
            t.idiomaTeclado, t.retroiluminado,
            pt.puertoCD, pt.puertoSd, pt.puertoDock,
            pt.puertoEthernet, pt.puertoHDMI, pt.puertoHjack,
            pt.puertoVGA, pt.puertoDisplay, pt.cantidadUsb, pt.cantidadTypeC
        FROM ITEM i
        LEFT JOIN PRECIO_HISTORICO ph ON i.item = ph.item
        LEFT JOIN DESCUENTO_ESPECIAL de ON i.item = de.item
        LEFT JOIN NUMERO_SERIE ns ON i.item = ns.item
        LEFT JOIN ALMACENAMIENTO a ON i.item = a.idAlmacenamiento
        LEFT JOIN RAM r ON i.item = r.idRam
        LEFT JOIN GRAFICA g ON i.item = g.idGrafica
        LEFT JOIN SOFTWARE s ON i.item = s.idSoftware
        LEFT JOIN MARCA m ON i.item = m.idMarca
        LEFT JOIN MODELO n ON i.item = n.idModelo
        LEFT JOIN CARGADOR c ON i.item = c.item
        LEFT JOIN OTRO o ON i.item = o.item
        LEFT JOIN PANTALLA pa ON i.item = pa.idPantalla
        LEFT JOIN TECLADO t ON i.item = t.idTeclado
        LEFT JOIN PUERTOS pt ON i.item = pt.idPuerto
        """
        cursor.execute(sql)
        registros = cursor.fetchall()
        return registros
    
import mysql.connector

class Registro_datos():
    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost', database='ultrapc', user='root', password='95781432365zZ@', port='3306')

    def obtener_datos_unicos(self):
        # Crear una lista con los nombres de los campos y las tablas a las que pertenecen
        campos = [
            # Tabla ITEM
            ('ITEM', 'item', 'descripcion'),
            ('ITEM', 'costo',),
            # Tabla ECOMPUTO
            ('ECOMPUTO', 'stock',),
            # Tabla PROVEEDOR
            ('PROVEEDOR', 'nombre',),
            # Tabla NUMERO_SERIE
            ('NUMERO_SERIE', 'numeroSerie',),
            # Tabla RAM
            ('RAM', 'capacidadRam', 'tipoRam', 'frecuencia', 'disposicion'),
            # Tabla ECOMPUTO
            ('ECOMPUTO', 'capacidadRamTotal',),
            # Tabla MARCA
            ('MARCA', 'nombreMarca', 'lineaMarca'),
            # Tabla MODELO
            ('MODELO', 'nombreModelo',),
            # Tabla NUMERO_PRODUCTO
            ('NUMERO_PRODUCTO', 'numeroProducto',),
            # Tabla ALMACENAMIENTO_TIPO
            ('ALMACENAMIENTO_TIPO', 'Tipo',),
            # Tabla ALMACENAMIENTO
            ('ALMACENAMIENTO', 'capacidad', 'factorForma'),
            # Tabla ALMACENAMIENTO_ESPECIFICACION
            ('ALMACENAMIENTO_ESPECIFICACION', 'Especificacion',),
            # Tabla PROCESADOR
            ('PROCESADOR', 'nombreProcesador', 'nucleosProcesador', 'generacionProcesador', 'velProcesador')
        ]

        # Inicializar un diccionario para almacenar los resultados
        datos_unicos = {}

        # Realizar consultas para obtener datos únicos de cada campo
        cursor = self.conexion.cursor()
        for tabla, *campos_tabla in campos:
            for campo in campos_tabla:
                # Construir la consulta SQL para obtener los valores únicos
                consulta_sql = f"SELECT DISTINCT {campo} FROM {tabla};"
                cursor.execute(consulta_sql)
                resultados = cursor.fetchall()

                # Agregar los resultados al diccionario
                if campo not in datos_unicos:
                    datos_unicos[campo] = []
                for resultado in resultados:
                    datos_unicos[campo].append(resultado[0])

        # Cerrar el cursor y retornar los datos únicos
        cursor.close()
        return datos_unicos





















    




    
