import mysql.connector

class Registro_datos():
    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost', database='ultrapc', user='root', password='95781432365zZ@', port='3306')

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
    
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
        LEFT JOIN PUERTO pt ON i.item = pt.idPuerto
        """
        cursor.execute(sql)
        registros = cursor.fetchall()
        return registros
    
    def obtener_datos_unicos(self):
        # Crear una lista con los nombres de los campos y las tablas a las que pertenecen
        campos = [
            # Tabla ITEM
            ('ITEM', 'item'),
            # Tabla ECOMPUTO-STOCK
            ('ECOMPUTO', 'fechaFabricacion', 'stock'),
            #Tabla ITEM-2
            ('ITEM', 'precio'),
            # Tabla PROVEEDOR
            ('PROVEEDOR', 'nombre'),
            # Tabla NUMERO_SERIE
            ('NUMERO_SERIE', 'numeroSerie'),
            # Tabla RAM
            ('RAM', 'capacidadRam', 'tipoRam', 'frecuencia', 'disposicion'),
            # Tabla ECOMPUTO
            ('ECOMPUTO', 'capacidadRamTotal'),
            # Tabla MARCA
            ('MARCA', 'nombreMarca', 'lineaMarca'),
            # Tabla MODELO
            ('MODELO', 'nombreModelo'),
            # Tabla NUMERO_PRODUCTO
            ('NUMERO_PRODUCTO', 'numeroProducto'),
            # Tabla ALMACENAMIENTO_TIPO
            ('ALMACENAMIENTO_TIPO', 'Tipo'),
            # Tabla ALMACENAMIENTO
            ('ALMACENAMIENTO', 'capacidad', 'factorForma'),
            # Tabla ALMACENAMIENTO_ESPECIFICACION
            ('ALMACENAMIENTO_ESPECIFICACION', 'Especificacion'),
            #Tabla ECOMPUTO-HORAS DE USO
            ('ECOMPUTO', 'horasEncendido'),
            # Tabla PROCESADOR
            ('PROCESADOR', 'nombreProcesador', 'nucleosProcesador', 'generacionProcesador', 'velProcesador'),
            #Tabla GRAFICA
            ('GRAFICA', 'nomGrafica', 'capacidadGrafica', 'tipoVram', 'integrada'),
            #Tabla BATERIA
            ('BATERIA', 'tipoBateria', 'extendida', 'capacidadBateria', 'usoBateria'),
            #Tabla Pantalla
            ('PANTALLA', 'tactil', 'tamannoPantalla', 'resolucionPantalla', 'panel', 'hzPantalla', 'inclinacionPantalla', 'antirreflejo'),
            #Tabla TECLADO
            ('TECLADO', 'idiomaTeclado', 'retroiluminado', 'esNumerico'),
            #Tabla ECOMPUTO-TECLADO
            ('ECOMPUTO', 'touchpad', 'lectorHuellas'),
            #Tabla PUERTO
            ('PUERTO', 'cantidadUsb', 'cantidadTypeC', 'puertoCD', 'puertoSd', 'puertoDock', 'puertoEthernet', 'puertoHDMI', 'puertoHjack', 'puertoVGA', 'puertoDisplay'),
            #Tabla ECOMPUTO-WEBCAM
            ('ECOMPUTO', 'webCam', 'pocicionWebCam', 'descripcionWebCam'),
            #Tabla CARGADOR
            ('CARGADOR', 'original', 'alimentacion', 'accesorios'),
            #Tabla ECOMPUTO-MATERIAL
            ('ECOMPUTO', 'descripcionMaterial', 'milStd', 'peso', 'wifi', 'bt', '4G'),
            #Tabla CAJA
            ('CAJA', 'anchoCaja', 'longitudCaja', 'altoCaja', 'pesoCaja', 'aptoEnvio'),
            #Tabla GARANTÍA
            ('GARANTIA', 'oferenteGarantia', 'tiempoGarantia', 'tipoGarantia', 'comprobantedeCompra', 'comentarioGarantia'),
            #Tabla CONDICIÓN
            ('CONDICION', 'estetica', 'eTouch', 'eTeclado', 'eReposa', 'eTapa', 'ePantalla', 'eOtros')

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
    
    def obtener_valores_item(self, numero_item):
        """
        Obtiene los valores de un ítem específico para su actualización en la base de datos.

        Parameters:
            numero_item (int): El número de ítem que se desea actualizar.

        Returns:
            dict: Un diccionario con las columnas y sus valores correspondientes para el ítem especificado.
        """
        consulta_obtener_item = f"""
            SELECT 
                ITEM.item,
                ECOMPUTO.fechaFabricacion,
                ECOMPUTO.stock,
                ITEM.precio,
                MARCA.nombreMarca,
                MARCA.lineaMarca,
                MODELO.nombreModelo,
                NUMERO_PRODUCTO.numeroProducto,
                ALMACENAMIENTO_TIPO.Tipo,
                ALMACENAMIENTO.capacidad,
                ALMACENAMIENTO.factorForma,
                ALMACENAMIENTO_ESPECIFICACION.Especificacion,
                ECOMPUTO.horasEncendido,
                PROCESADOR.nombreProcesador,
                PROCESADOR.nucleosProcesador,
                PROCESADOR.generacionProcesador,
                PROCESADOR.velProcesador,
                BATERIA.tipoBateria,
                BATERIA.extendida,
                BATERIA.capacidadBateria,
                BATERIA.usoBateria,
                PANTALLA.tactil,
                PANTALLA.tamannoPantalla,
                PANTALLA.resolucionPantalla,
                PANTALLA.panel,
                PANTALLA.hzPantalla,
                PANTALLA.inclinacionPantalla,
                PANTALLA.antirreflejo,
                TECLADO.idiomaTeclado,
                TECLADO.retroiluminado,
                TECLADO.esNumerico,
                ECOMPUTO.touchpad,
                ECOMPUTO.lectorHuellas,
                PUERTO.cantidadUsb,
                PUERTO.cantidadTypeC,
                PUERTO.puertoCD,
                PUERTO.puertoSd,
                PUERTO.puertoDock,
                PUERTO.puertoEthernet,
                PUERTO.puertoHDMI,
                PUERTO.puertoHjack,
                PUERTO.puertoVGA,
                PUERTO.puertoDisplay,
                ECOMPUTO.webCam,
                ECOMPUTO.pocicionWebCam,
                ECOMPUTO.descripcionWebCam,
                CAJA.anchoCaja,
                CAJA.longitudCaja,
                CAJA.altoCaja,
                CAJA.pesoCaja,
                CAJA.aptoEnvio,
                GARANTIA.oferenteGarantia,
                GARANTIA.tiempoGarantia,
                GARANTIA.tipoGarantia,
                GARANTIA.comprobantedeCompra,
                GARANTIA.comentarioGarantia,
                CONDICION.estetica,
                CONDICION.eTouch,
                CONDICION.eTeclado,
                CONDICION.eReposa,
                CONDICION.eTapa,
                CONDICION.ePantalla,
                CONDICION.eOtros,
                ECOMPUTO.wifi,
                ECOMPUTO.bt,
                ECOMPUTO.`4G`,
                GRAFICA.nomGrafica,
                GRAFICA.capacidadGrafica,
                GRAFICA.tipoVram,
                GRAFICA.integrada,
                CARGADOR.original,
                CARGADOR.alimentacion,
                CARGADOR.accesorios,
                ECOMPUTO.descripcionMaterial,
                ECOMPUTO.milStd,
                ECOMPUTO.peso,
                RAM.capacidadRam,
                RAM.tipoRam,
                RAM.frecuencia,
                RAM.disposicion,
                ECOMPUTO.capacidadRamTotal,
                PROVEEDOR.nombre AS nombreProveedor,
                NUMERO_SERIE.numeroSerie
            FROM ITEM
            LEFT JOIN ECOMPUTO ON ITEM.item = ECOMPUTO.item
            LEFT JOIN MARCA ON ECOMPUTO.idMarca = MARCA.idMarca
            LEFT JOIN MODELO ON ECOMPUTO.idModelo = MODELO.idModelo
            LEFT JOIN NUMERO_PRODUCTO ON ECOMPUTO.idNumeroProducto = NUMERO_PRODUCTO.idNumeroProducto
            LEFT JOIN ECOMPUTO_ALMACENAMIENTO ON ECOMPUTO.item = ECOMPUTO_ALMACENAMIENTO.item
            LEFT JOIN ALMACENAMIENTO ON ECOMPUTO_ALMACENAMIENTO.idAlmacenamiento = ALMACENAMIENTO.idAlmacenamiento
            LEFT JOIN ALMACENAMIENTO_TIPO ON ALMACENAMIENTO.idTipo = ALMACENAMIENTO_TIPO.idTipo
            LEFT JOIN ALMACENAMIENTO_ESPECIFICACION ON ALMACENAMIENTO.idEspecificacion = ALMACENAMIENTO_ESPECIFICACION.idEspecificacion
            LEFT JOIN PROCESADOR ON ECOMPUTO.idProcesador = PROCESADOR.idProcesador
            LEFT JOIN BATERIA ON ECOMPUTO.idBateria = BATERIA.idBateria
            LEFT JOIN ECOMPUTO_PANTALLA ON ECOMPUTO.item = ECOMPUTO_PANTALLA.item
            LEFT JOIN PANTALLA ON ECOMPUTO_PANTALLA.idPantalla = PANTALLA.idPantalla
            LEFT JOIN TECLADO ON ECOMPUTO.idTeclado = TECLADO.idTeclado
            LEFT JOIN PUERTO ON ECOMPUTO.idPuerto = PUERTO.idPuerto
            LEFT JOIN CAJA ON ECOMPUTO.idCaja = CAJA.idCaja
            LEFT JOIN ECOMPUTO_GARANTIA ON ECOMPUTO.item = ECOMPUTO_GARANTIA.item
            LEFT JOIN GARANTIA ON ECOMPUTO_GARANTIA.idGarantia = GARANTIA.idGarantia
            LEFT JOIN CONDICION ON ECOMPUTO.item = CONDICION.item
            LEFT JOIN ECOMPUTO_REPOSICION ON ECOMPUTO.item = ECOMPUTO_REPOSICION.item
            LEFT JOIN REPOSICION_STOCK ON ECOMPUTO_REPOSICION.idReposicion = REPOSICION_STOCK.idReposicion
            LEFT JOIN PROVEEDOR ON REPOSICION_STOCK.idProveedor = PROVEEDOR.idProveedor
            LEFT JOIN NUMERO_SERIE ON ITEM.item = NUMERO_SERIE.item
            LEFT JOIN ECOMPUTO_GRAFICA ON ECOMPUTO.item = ECOMPUTO_GRAFICA.item
            LEFT JOIN GRAFICA ON ECOMPUTO_GRAFICA.idGrafica = GRAFICA.idGrafica
            LEFT JOIN CARGADOR ON ECOMPUTO.item = CARGADOR.item
            LEFT JOIN ECOMPUTO_RAM ON ECOMPUTO.item = ECOMPUTO_RAM.item
            LEFT JOIN RAM ON ECOMPUTO_RAM.idRam = RAM.idRam
            WHERE ITEM.item = {numero_item};


        """



        cursor = self.conexion.cursor()
        cursor.execute(consulta_obtener_item)
        resultado_item = cursor.fetchall()
        cursor.close()

        if resultado_item:
            # Obtener solo el primer elemento de la lista (el primer registro)
            resultado_item = resultado_item[0]
            # Mapear las columnas y sus valores en un diccionario
            
            valores_item = {
                'item': resultado_item[0],
                'fechaFabricacion': resultado_item[1],
                'stock': resultado_item[2],
                'precio': resultado_item[3],
                'nombre': resultado_item[81],
                'numeroSerie': resultado_item[82],
                'capacidadRam': resultado_item[76],
                'tipoRam': resultado_item[77],
                'frecuencia': resultado_item[78],
                'disposicion': resultado_item[79],
                'capacidadRamTotal': resultado_item[80],
                'nombreMarca': resultado_item[4],
                'lineaMarca': resultado_item[5],
                'nombreModelo': resultado_item[6],
                'numeroProducto': resultado_item[7],
                'Tipo': resultado_item[8],
                'capacidad': resultado_item[9],
                'factorForma': resultado_item[10],
                'Especificacion': resultado_item[11],
                'horasEncendido': resultado_item[12],
                'nombreProcesador': resultado_item[13],
                'nucleosProcesador': resultado_item[14],
                'generacionProcesador': resultado_item[15],
                'velProcesador': resultado_item[16],
                'nomGrafica': resultado_item[66],
                'capacidadGrafica': resultado_item[67],
                'tipoVram': resultado_item[68],
                'integrada': resultado_item[69],
                'tipoBateria': resultado_item[17],
                'extendida': resultado_item[18],
                'capacidadBateria': resultado_item[19],
                'usoBateria': resultado_item[20],
                'tactil': resultado_item[21],
                'tamannoPantalla': resultado_item[22],
                'resolucionPantalla': resultado_item[23],
                'panel': resultado_item[24],
                'hzPantalla': resultado_item[25],
                'inclinacionPantalla': resultado_item[26],
                'antirreflejo': resultado_item[27],
                'idiomaTeclado': resultado_item[28],
                'retroiluminado': resultado_item[29],
                'esNumerico': resultado_item[30],
                'touchpad': resultado_item[31],
                'lectorHuellas': resultado_item[32],
                'cantidadUsb': resultado_item[33],
                'cantidadTypeC': resultado_item[34],
                'puertoCD': resultado_item[35],
                'puertoSd': resultado_item[36],
                'puertoDock': resultado_item[37],
                'puertoEthernet': resultado_item[38],
                'puertoHDMI': resultado_item[39],
                'puertoHjack': resultado_item[40],
                'puertoVGA': resultado_item[41],
                'puertoDisplay': resultado_item[42],
                'webCam': resultado_item[43],
                'pocicionWebCam': resultado_item[44],
                'descripcionWebCam': resultado_item[45],
                'original': resultado_item[70],
                'alimentacion': resultado_item[71],
                'accesorios': resultado_item[72],
                'descripcionMaterial': resultado_item[73],
                'milStd': resultado_item[74],
                'peso': resultado_item[75],
                'wifi': resultado_item[63],
                'bt': resultado_item[64],
                '4G': resultado_item[65],
                'anchoCaja': resultado_item[46],
                'longitudCaja': resultado_item[47],
                'altoCaja': resultado_item[48],
                'pesoCaja': resultado_item[49],
                'aptoEnvio': resultado_item[50],
                'oferenteGarantia': resultado_item[51],
                'tiempoGarantia': resultado_item[52],
                'tipoGarantia': resultado_item[53],
                'comprobantedeCompra': resultado_item[54],
                'comentarioGarantia': resultado_item[55],
                'estetica': resultado_item[56],
                'eTouch': resultado_item[57],
                'eTeclado': resultado_item[58],
                'eReposa': resultado_item[59],
                'eTapa': resultado_item[60],
                'ePantalla': resultado_item[61],
                'eOtros': resultado_item[62]
            }

            # Reorganizar el diccionario de acuerdo con el orden especificado en valores_bd
            valores_bd = [
                'item',
                'fechaFabricacion', 'stock',
                'precio',
                'nombre',
                'numeroSerie',
                'capacidadRam', 'tipoRam', 'frecuencia', 'disposicion',
                'capacidadRamTotal',
                'nombreMarca', 'lineaMarca',
                'nombreModelo',
                'numeroProducto',
                'Tipo',
                'capacidad', 'factorForma',
                'Especificacion', 'horasEncendido',
                'nombreProcesador', 'nucleosProcesador', 'generacionProcesador', 'velProcesador',
                'nomGrafica', 'capacidadGrafica', 'tipoVram', 'integrada',
                'tipoBateria', 'extendida', 'capacidadBateria', 'usoBateria',
                'tactil', 'tamannoPantalla', 'resolucionPantalla', 'panel', 'hzPantalla', 'inclinacionPantalla', 'antirreflejo',
                'idiomaTeclado', 'retroiluminado', 'esNumerico',
                'touchpad', 'lectorHuellas',
                'cantidadUsb', 'cantidadTypeC', 'puertoCD', 'puertoSd', 'puertoDock', 'puertoEthernet', 'puertoHDMI', 'puertoHjack', 'puertoVGA', 'puertoDisplay',
                'webCam', 'pocicionWebCam', 'descripcionWebCam',
                'original', 'alimentacion', 'accesorios',
                'descripcionMaterial', 'milStd', 'peso', 'wifi', 'bt', '4G',
                'anchoCaja', 'longitudCaja', 'altoCaja', 'pesoCaja', 'aptoEnvio',
                'oferenteGarantia', 'tiempoGarantia', 'tipoGarantia', 'comprobantedeCompra', 'comentarioGarantia',
                'estetica', 'eTouch', 'eTeclado', 'eReposa', 'eTapa', 'ePantalla', 'eOtros'
            ]

            # Crear un OrderedDict con las claves en el orden deseado
            valores_item_ordenados = {key: valores_item[key] for key in valores_bd}
            return valores_item_ordenados
        else:
            return None
        
    def obtener_valores_producto(self, numero_producto):
        """
        Obtiene los valores de un ítem específico para su actualización en la base de datos.

        Parameters:
            numero_item (int): El número de ítem que se desea actualizar.

        Returns:
            dict: Un diccionario con las columnas y sus valores correspondientes para el ítem especificado.
        """
        consulta_obtener_item = f"""
                            SELECT 
                    ITEM.item,
                    ECOMPUTO.fechaFabricacion,
                    ECOMPUTO.stock,
                    ITEM.precio,
                    MARCA.nombreMarca,
                    MARCA.lineaMarca,
                    MODELO.nombreModelo,
                    NUMERO_PRODUCTO.numeroProducto,
                    ALMACENAMIENTO_TIPO.Tipo,
                    ALMACENAMIENTO.capacidad,
                    ALMACENAMIENTO.factorForma,
                    ALMACENAMIENTO_ESPECIFICACION.Especificacion,
                    ECOMPUTO.horasEncendido,
                    PROCESADOR.nombreProcesador,
                    PROCESADOR.nucleosProcesador,
                    PROCESADOR.generacionProcesador,
                    PROCESADOR.velProcesador,
                    BATERIA.tipoBateria,
                    BATERIA.extendida,
                    BATERIA.capacidadBateria,
                    BATERIA.usoBateria,
                    PANTALLA.tactil,
                    PANTALLA.tamannoPantalla,
                    PANTALLA.resolucionPantalla,
                    PANTALLA.panel,
                    PANTALLA.hzPantalla,
                    PANTALLA.inclinacionPantalla,
                    PANTALLA.antirreflejo,
                    TECLADO.idiomaTeclado,
                    TECLADO.retroiluminado,
                    TECLADO.esNumerico,
                    ECOMPUTO.touchpad,
                    ECOMPUTO.lectorHuellas,
                    PUERTO.cantidadUsb,
                    PUERTO.cantidadTypeC,
                    PUERTO.puertoCD,
                    PUERTO.puertoSd,
                    PUERTO.puertoDock,
                    PUERTO.puertoEthernet,
                    PUERTO.puertoHDMI,
                    PUERTO.puertoHjack,
                    PUERTO.puertoVGA,
                    PUERTO.puertoDisplay,
                    ECOMPUTO.webCam,
                    ECOMPUTO.pocicionWebCam,
                    ECOMPUTO.descripcionWebCam,
                    CAJA.anchoCaja,
                    CAJA.longitudCaja,
                    CAJA.altoCaja,
                    CAJA.pesoCaja,
                    CAJA.aptoEnvio,
                    GARANTIA.oferenteGarantia,
                    GARANTIA.tiempoGarantia,
                    GARANTIA.tipoGarantia,
                    GARANTIA.comprobantedeCompra,
                    GARANTIA.comentarioGarantia,
                    CONDICION.estetica,
                    CONDICION.eTouch,
                    CONDICION.eTeclado,
                    CONDICION.eReposa,
                    CONDICION.eTapa,
                    CONDICION.ePantalla,
                    CONDICION.eOtros,
                    ECOMPUTO.wifi,
                    ECOMPUTO.bt,
                    ECOMPUTO.`4G`,
                    GRAFICA.nomGrafica,
                    GRAFICA.capacidadGrafica,
                    GRAFICA.tipoVram,
                    GRAFICA.integrada,
                    CARGADOR.original,
                    CARGADOR.alimentacion,
                    CARGADOR.accesorios,
                    ECOMPUTO.descripcionMaterial,
                    ECOMPUTO.milStd,
                    ECOMPUTO.peso,
                    RAM.capacidadRam,
                    RAM.tipoRam,
                    RAM.frecuencia,
                    RAM.disposicion,
                    ECOMPUTO.capacidadRamTotal,
                    PROVEEDOR.nombre AS nombreProveedor,
                    NUMERO_SERIE.numeroSerie
                FROM ITEM
                LEFT JOIN ECOMPUTO ON ITEM.item = ECOMPUTO.item
                LEFT JOIN MARCA ON ECOMPUTO.idMarca = MARCA.idMarca
                LEFT JOIN MODELO ON ECOMPUTO.idModelo = MODELO.idModelo
                LEFT JOIN NUMERO_PRODUCTO ON ECOMPUTO.idNumeroProducto = NUMERO_PRODUCTO.idNumeroProducto
                LEFT JOIN ECOMPUTO_ALMACENAMIENTO ON ECOMPUTO.item = ECOMPUTO_ALMACENAMIENTO.item
                LEFT JOIN ALMACENAMIENTO ON ECOMPUTO_ALMACENAMIENTO.idAlmacenamiento = ALMACENAMIENTO.idAlmacenamiento
                LEFT JOIN ALMACENAMIENTO_TIPO ON ALMACENAMIENTO.idTipo = ALMACENAMIENTO_TIPO.idTipo
                LEFT JOIN ALMACENAMIENTO_ESPECIFICACION ON ALMACENAMIENTO.idEspecificacion = ALMACENAMIENTO_ESPECIFICACION.idEspecificacion
                LEFT JOIN PROCESADOR ON ECOMPUTO.idProcesador = PROCESADOR.idProcesador
                LEFT JOIN BATERIA ON ECOMPUTO.idBateria = BATERIA.idBateria
                LEFT JOIN ECOMPUTO_PANTALLA ON ECOMPUTO.item = ECOMPUTO_PANTALLA.item
                LEFT JOIN PANTALLA ON ECOMPUTO_PANTALLA.idPantalla = PANTALLA.idPantalla
                LEFT JOIN TECLADO ON ECOMPUTO.idTeclado = TECLADO.idTeclado
                LEFT JOIN PUERTO ON ECOMPUTO.idPuerto = PUERTO.idPuerto
                LEFT JOIN CAJA ON ECOMPUTO.idCaja = CAJA.idCaja
                LEFT JOIN ECOMPUTO_GARANTIA ON ECOMPUTO.item = ECOMPUTO_GARANTIA.item
                LEFT JOIN GARANTIA ON ECOMPUTO_GARANTIA.idGarantia = GARANTIA.idGarantia
                LEFT JOIN CONDICION ON ECOMPUTO.item = CONDICION.item
                LEFT JOIN ECOMPUTO_REPOSICION ON ECOMPUTO.item = ECOMPUTO_REPOSICION.item
                LEFT JOIN REPOSICION_STOCK ON ECOMPUTO_REPOSICION.idReposicion = REPOSICION_STOCK.idReposicion
                LEFT JOIN PROVEEDOR ON REPOSICION_STOCK.idProveedor = PROVEEDOR.idProveedor
                LEFT JOIN NUMERO_SERIE ON ITEM.item = NUMERO_SERIE.item
                LEFT JOIN ECOMPUTO_GRAFICA ON ECOMPUTO.item = ECOMPUTO_GRAFICA.item
                LEFT JOIN GRAFICA ON ECOMPUTO_GRAFICA.idGrafica = GRAFICA.idGrafica
                LEFT JOIN CARGADOR ON ECOMPUTO.item = CARGADOR.item
                LEFT JOIN ECOMPUTO_RAM ON ECOMPUTO.item = ECOMPUTO_RAM.item
                LEFT JOIN RAM ON ECOMPUTO_RAM.idRam = RAM.idRam
                WHERE NUMERO_PRODUCTO.numeroProducto = {numero_producto};



        """



        cursor = self.conexion.cursor()
        cursor.execute(consulta_obtener_item)
        resultado_item = cursor.fetchall()
        cursor.close()

        if resultado_item:
            # Obtener solo el primer elemento de la lista (el primer registro)
            resultado_item = resultado_item[0]
            # Mapear las columnas y sus valores en un diccionario
            
            valores_item = {
                'item': resultado_item[0],
                'fechaFabricacion': resultado_item[1],
                'stock': resultado_item[2],
                'precio': resultado_item[3],
                'nombre': resultado_item[81],
                'numeroSerie': resultado_item[82],
                'capacidadRam': resultado_item[76],
                'tipoRam': resultado_item[77],
                'frecuencia': resultado_item[78],
                'disposicion': resultado_item[79],
                'capacidadRamTotal': resultado_item[80],
                'nombreMarca': resultado_item[4],
                'lineaMarca': resultado_item[5],
                'nombreModelo': resultado_item[6],
                'numeroProducto': resultado_item[7],
                'Tipo': resultado_item[8],
                'capacidad': resultado_item[9],
                'factorForma': resultado_item[10],
                'Especificacion': resultado_item[11],
                'horasEncendido': resultado_item[12],
                'nombreProcesador': resultado_item[13],
                'nucleosProcesador': resultado_item[14],
                'generacionProcesador': resultado_item[15],
                'velProcesador': resultado_item[16],
                'nomGrafica': resultado_item[66],
                'capacidadGrafica': resultado_item[67],
                'tipoVram': resultado_item[68],
                'integrada': resultado_item[69],
                'tipoBateria': resultado_item[17],
                'extendida': resultado_item[18],
                'capacidadBateria': resultado_item[19],
                'usoBateria': resultado_item[20],
                'tactil': resultado_item[21],
                'tamannoPantalla': resultado_item[22],
                'resolucionPantalla': resultado_item[23],
                'panel': resultado_item[24],
                'hzPantalla': resultado_item[25],
                'inclinacionPantalla': resultado_item[26],
                'antirreflejo': resultado_item[27],
                'idiomaTeclado': resultado_item[28],
                'retroiluminado': resultado_item[29],
                'esNumerico': resultado_item[30],
                'touchpad': resultado_item[31],
                'lectorHuellas': resultado_item[32],
                'cantidadUsb': resultado_item[33],
                'cantidadTypeC': resultado_item[34],
                'puertoCD': resultado_item[35],
                'puertoSd': resultado_item[36],
                'puertoDock': resultado_item[37],
                'puertoEthernet': resultado_item[38],
                'puertoHDMI': resultado_item[39],
                'puertoHjack': resultado_item[40],
                'puertoVGA': resultado_item[41],
                'puertoDisplay': resultado_item[42],
                'webCam': resultado_item[43],
                'pocicionWebCam': resultado_item[44],
                'descripcionWebCam': resultado_item[45],
                'original': resultado_item[70],
                'alimentacion': resultado_item[71],
                'accesorios': resultado_item[72],
                'descripcionMaterial': resultado_item[73],
                'milStd': resultado_item[74],
                'peso': resultado_item[75],
                'wifi': resultado_item[63],
                'bt': resultado_item[64],
                '4G': resultado_item[65],
                'anchoCaja': resultado_item[46],
                'longitudCaja': resultado_item[47],
                'altoCaja': resultado_item[48],
                'pesoCaja': resultado_item[49],
                'aptoEnvio': resultado_item[50],
                'oferenteGarantia': resultado_item[51],
                'tiempoGarantia': resultado_item[52],
                'tipoGarantia': resultado_item[53],
                'comprobantedeCompra': resultado_item[54],
                'comentarioGarantia': resultado_item[55],
                'estetica': resultado_item[56],
                'eTouch': resultado_item[57],
                'eTeclado': resultado_item[58],
                'eReposa': resultado_item[59],
                'eTapa': resultado_item[60],
                'ePantalla': resultado_item[61],
                'eOtros': resultado_item[62]
            }

            # Reorganizar el diccionario de acuerdo con el orden especificado en valores_bd
            valores_bd = [
                'item',
                'fechaFabricacion', 'stock',
                'precio',
                'nombre',
                'numeroSerie',
                'capacidadRam', 'tipoRam', 'frecuencia', 'disposicion',
                'capacidadRamTotal',
                'nombreMarca', 'lineaMarca',
                'nombreModelo',
                'numeroProducto',
                'Tipo',
                'capacidad', 'factorForma',
                'Especificacion', 'horasEncendido',
                'nombreProcesador', 'nucleosProcesador', 'generacionProcesador', 'velProcesador',
                'nomGrafica', 'capacidadGrafica', 'tipoVram', 'integrada',
                'tipoBateria', 'extendida', 'capacidadBateria', 'usoBateria',
                'tactil', 'tamannoPantalla', 'resolucionPantalla', 'panel', 'hzPantalla', 'inclinacionPantalla', 'antirreflejo',
                'idiomaTeclado', 'retroiluminado', 'esNumerico',
                'touchpad', 'lectorHuellas',
                'cantidadUsb', 'cantidadTypeC', 'puertoCD', 'puertoSd', 'puertoDock', 'puertoEthernet', 'puertoHDMI', 'puertoHjack', 'puertoVGA', 'puertoDisplay',
                'webCam', 'pocicionWebCam', 'descripcionWebCam',
                'original', 'alimentacion', 'accesorios',
                'descripcionMaterial', 'milStd', 'peso', 'wifi', 'bt', '4G',
                'anchoCaja', 'longitudCaja', 'altoCaja', 'pesoCaja', 'aptoEnvio',
                'oferenteGarantia', 'tiempoGarantia', 'tipoGarantia', 'comprobantedeCompra', 'comentarioGarantia',
                'estetica', 'eTouch', 'eTeclado', 'eReposa', 'eTapa', 'ePantalla', 'eOtros'
            ]

            # Crear un OrderedDict con las claves en el orden deseado
            valores_item_ordenados = {key: valores_item[key] for key in valores_bd}
            return valores_item_ordenados
        else:
            return None

    def insertar_datos(self, datos):
        
            
        

            try:
                columnas = ', '.join(datos.keys())
                valores = ', '.join(['%s'] * len(datos))
                sql = f'INSERT INTO {tabla} ({columnas}) VALUES ({valores})'
                self.cursor.execute(sql, tuple(datos.values()))
                self.conexion.commit()
                return True
            except Exception as e:
                print(f"Error al insertar en la tabla {tabla}: {e}")
                self.conexion.rollback()
                return False




















    




    
