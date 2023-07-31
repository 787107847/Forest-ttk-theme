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
    

    def rellenar_productos(self):
        # Campos de la lista proporcionada
        campos = [
            # Lista de campos con las tablas correspondientes (tabla, campo)
            ('i', 'item'),
            ('e', 'fechaFabricacion'),
            ('e', 'stock'),
            ('i', 'costo'),
            ('pr', 'nombre'),
            ('ns', 'numeroSerie'),
            ('r', 'capacidadRam'),
            ('r', 'tipoRam'),
            ('r', 'frecuencia'),
            ('r', 'disposicion'),
            ('e', 'capacidadRamTotal'),
            ('m', 'nombreMarca'),
            ('m', 'lineaMarca'),
            ('md', 'nombreModelo'),
            ('np', 'numeroProducto'),
            ('at', 'Tipo'),
            ('a', 'capacidad'),
            ('a', 'factorForma'),
            ('ae', 'Especificacion'),
            ('e','horasEncendido'),
            ('p', 'nombreProcesador'),  # Agregamos el campo "nombreProcesador" de "PROCESADOR"
            ('p', 'nucleosProcesador'),  # Agregamos el campo "nucleosProcesador" de "PROCESADOR"
            ('p', 'generacionProcesador'),  # Agregamos el campo "generacionProcesador" de "PROCESADOR"
            ('p', 'velProcesador'),  # Agregamos el campo "velProcesador" de "PROCESADOR"
            ('pa', 'tamannoPantalla'),
            ('pa', 'resolucionPantalla'),
            ('t', 'idiomaTeclado'),
            ('t', 'retroiluminado'),
            ('pt', 'puertoCD'),
            ('pt', 'puertoSd'),
            ('pt', 'puertoDock'),
            ('pt', 'puertoEthernet'),
            ('pt', 'puertoHDMI'),
            ('pt', 'puertoHjack'),
            ('pt', 'puertoVGA'),
            ('pt', 'puertoDisplay'),
            ('pt', 'cantidadUsb'),
            ('pt', 'cantidadTypeC')
        ]

        # Construir la lista de campos para la consulta SQL
        campos_sql = ', '.join([f'{tabla}.{campo}' for tabla, campo in campos])

        # Subconsulta para obtener los datos únicos de RAM
        subconsulta_ram = """
            SELECT DISTINCT r.tipoRam, r.frecuencia, r.capacidadRam, r.disposicion
            FROM RAM r
        """

        # Consulta SQL
        sql = f"""
        SELECT {campos_sql}, GROUP_CONCAT(DISTINCT pr.nombre) AS proveedores
        FROM ECOMPUTO e
        LEFT JOIN ITEM i ON e.item = i.item
        LEFT JOIN ECOMPUTO_REPOSICION erp ON e.item = erp.item
        LEFT JOIN REPOSICION_STOCK rs ON erp.idReposicion = rs.idReposicion
        LEFT JOIN PROVEEDOR pr ON rs.idProveedor = pr.idProveedor
        LEFT JOIN MARCA m ON e.idMarca = m.idMarca
        LEFT JOIN MODELO md ON e.idModelo = md.idModelo
        LEFT JOIN NUMERO_PRODUCTO np ON e.idNumeroProducto = np.idNumeroProducto
        LEFT JOIN PROCESADOR p ON e.idProcesador = p.idProcesador  -- Agregamos el JOIN con PROCESADOR
        LEFT JOIN NUMERO_SERIE ns ON e.item = ns.item
        LEFT JOIN ECOMPUTO_ALMACENAMIENTO ea ON e.item = ea.item
        LEFT JOIN ALMACENAMIENTO a ON ea.idAlmacenamiento = a.idAlmacenamiento
        LEFT JOIN ECOMPUTO_RAM er ON e.item = er.item
        LEFT JOIN RAM r ON er.idRam = r.idRam
        LEFT JOIN ECOMPUTO_PANTALLA ep ON e.item = ep.item
        LEFT JOIN PANTALLA pa ON ep.idPantalla = pa.idPantalla
        LEFT JOIN TECLADO t ON e.idTeclado = t.idTeclado
        LEFT JOIN PUERTOS pt ON e.idPuerto = pt.idPuerto
        LEFT JOIN ALMACENAMIENTO_TIPO at ON a.idTipo = at.idTipo
        LEFT JOIN ALMACENAMIENTO_ESPECIFICACION ae ON a.idEspecificacion = ae.idEspecificacion
        LEFT JOIN ({subconsulta_ram}) sub_ram ON r.tipoRam = sub_ram.tipoRam
                                                AND r.frecuencia = sub_ram.frecuencia
                                                AND r.capacidadRam = sub_ram.capacidadRam
                                                AND r.disposicion = sub_ram.disposicion
        GROUP BY e.item, {', '.join([f'{tabla}.{campo}' for tabla, campo in campos if tabla == 'i'])}
        """

        cursor = self.conexion.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        return registros









    




    
