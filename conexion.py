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





    
