from Especificas import *
# Generales.py
# Funciones generales: ingreso de datos, reglas, score, recomendaciones,
# resultado, oferta, estadísticas y presentación de información.



# ---------------- INGRESO DE DATOS ----------------

def pedir_nombre() -> str:
    """
    Descripción: pide el nombre del producto hasta que no esté vacío.
    Parámetros: no recibe.
    Retorno: str -> nombre válido.
    """
    nombre = input("Ingrese el nombre del producto: ")
    while validar_nombre(nombre) == False:
        nombre = input("Error: el nombre no puede estar vacio. Reingrese: ")
    return nombre


def pedir_stock() -> int:
    """
    Descripción: pide el stock actual hasta que no sea negativo.
    Parámetros: no recibe.
    Retorno: int -> stock válido.
    """
    stock = int(input("Ingrese el stock actual: "))
    while validar_stock(stock) == False:
        stock = int(input("Error: el stock no puede ser negativo. Reingrese: "))
    return stock


def pedir_stock_minimo() -> int:
    """
    Descripción: pide el stock mínimo hasta que sea mayor a 0.
    Parámetros: no recibe.
    Retorno: int -> stock mínimo válido.
    """
    stock_minimo = int(input("Ingrese el stock minimo: "))
    while validar_stock_minimo(stock_minimo) == False:
        stock_minimo = int(input("Error: el stock minimo debe ser mayor a 0. Reingrese: "))
    return stock_minimo


def pedir_demanda() -> str:
    """
    Descripción: pide la demanda hasta que sea Baja, Media o Alta.
    Parámetros: no recibe.
    Retorno: str -> demanda válida.
    """
    demanda = input("Ingrese la demanda (Baja, Media, Alta): ")
    while validar_demanda(demanda) == False:
        demanda = input("Error: ingrese exactamente Baja, Media o Alta: ")
    return demanda


def pedir_vencimiento() -> str:
    """
    Descripción: pide el vencimiento hasta que sea Proximo o No_proximo.
    Parámetros: no recibe.
    Retorno: str -> vencimiento válido.
    """
    vencimiento = input("Ingrese el vencimiento (Proximo, No_proximo): ")
    while validar_vencimiento(vencimiento) == False:
        vencimiento = input("Error: ingrese exactamente Proximo o No_proximo: ")
    return vencimiento


def preguntar_continuar() -> bool:
    """
    Descripción: pregunta si se desea evaluar otro producto (S/N).
    Parámetros: no recibe.
    Retorno: bool -> True si responde S, False si responde N.
    """
    respuesta = input("\n¿Desea evaluar otro producto? (S/N): ")
    while validar_respuesta(respuesta) == False:
        respuesta = input("Error: ingrese S o N: ")
    continuar = False
    if respuesta == "S":
        continuar = True
    return continuar


# ---------------- REGLAS, SCORE Y RECOMENDACIONES ----------------

def aplicar_reglas(stock:int, stock_minimo:int, demanda:str, vencimiento:str,
                   cobertura:float, recomendaciones:list) -> int:
    """
    Descripción: aplica las reglas del sistema. Cada regla que se cumple suma (o resta)
                 su puntaje al score y agrega su recomendación a la lista recibida.
                 La lista se modifica directamente porque se pasa por referencia.
    Parámetros: stock (int), stock_minimo (int), demanda (str),
                vencimiento (str), cobertura (float) -> datos del producto.
                recomendaciones (list) -> lista vacía donde se agregan las recomendaciones.
    Retorno: int -> score acumulado.
    """
    score = 0
    if stock == 0 and demanda == "Alta":
        score += 50
        recomendaciones.append("Reposicion de emergencia inmediata.")
    if stock < stock_minimo and demanda == "Alta" and vencimiento == "No_proximo":
        score += 40
        recomendaciones.append("Generar orden de compra prioritaria con proveedor.")
    if stock < stock_minimo and demanda == "Alta":
        score += 20
        recomendaciones.append("Priorizar reposicion en gondola.")
    if stock < stock_minimo and demanda == "Media":
        score += 15
        recomendaciones.append("Programar pedido en el lote de la semana.")
    if stock < stock_minimo and demanda == "Baja":
        score += 10
        recomendaciones.append("Evaluar si es necesario reponer a corto plazo.")
    if stock == stock_minimo and demanda == "Alta":
        score += 10
        recomendaciones.append("Monitorear stock frecuentemente por alta rotacion.")
    if vencimiento == "Proximo" and stock >= stock_minimo and demanda != "Alta":
        score += 15
        recomendaciones.append("Aplicar descuento o promocion por vencimiento cercano.")
    if cobertura > 2 and demanda == "Baja" and vencimiento == "No_proximo":
        score -= 10
        recomendaciones.append("Pausar compras y reevaluar espacio en deposito.")
    if stock >= stock_minimo and demanda == "Baja" and vencimiento == "No_proximo":
        recomendaciones.append("Estado estable. No requiere intervencion inmediata.")
    return score


# ---------------- RESULTADO Y OFERTA ----------------

def obtener_resultado_general(score:int) -> str:
    """
    Descripción: clasifica el producto según su score.
    Parámetros: score (int) -> score acumulado.
    Retorno: str -> Reposicion urgente / Prioridad alta / media / baja.
    """
    if score >= 70:
        resultado = "Reposicion urgente"
    elif score >= 40:
        resultado = "Prioridad alta"
    elif score >= 20:
        resultado = "Prioridad media"
    else:
        resultado = "Prioridad baja"
    return resultado


def determinar_oferta(stock:int, stock_minimo:int, demanda:str, vencimiento:str, cobertura:float) -> str:
    """
    Descripción: decide si corresponde hacer una oferta sobre el producto.
    Parámetros: stock (int), stock_minimo (int), demanda (str),
                vencimiento (str), cobertura (float) -> datos del producto.
    Retorno: str -> aviso de oferta.
    """
    oferta = "No"
    if vencimiento == "Proximo" and stock == 0:
        oferta = "No hay oferta, sin stock"
    elif vencimiento == "Proximo" and demanda == "Alta":
        oferta = "No, la alta demanda deberia agotar el stock antes del vencimiento"
    elif vencimiento == "Proximo" and cobertura > 2:
        oferta = "Si, oferta muy grande por exceso de stock y vencimiento proximo"
    elif vencimiento == "Proximo" and stock >= stock_minimo:
        oferta = "Si, hacer oferta por vencimiento proximo"
    elif vencimiento == "Proximo" and demanda == "Media":
        oferta = "Si, descuento moderado para liquidar antes del vencimiento"
    elif vencimiento == "Proximo" and demanda == "Baja":
        oferta = "Si, descuento grande para liquidar antes del vencimiento"
    elif vencimiento == "No_proximo" and cobertura > 2 and demanda == "Baja":
        oferta = "Si, promocion para liberar espacio en deposito"
    return oferta


# ---------------- ESTADÍSTICAS ----------------

def calcular_promedio(lista:list) -> float:
    """
    Descripción: calcula el promedio de los valores de una lista.
    Parámetros: lista (list) -> lista de números.
    Retorno: float -> promedio (0 si la lista está vacía).
    """
    acumulador = 0
    for i in range(0, len(lista), 1):
        acumulador += lista[i]
    promedio = 0
    if len(lista) > 0:
        promedio = acumulador / len(lista)
    return promedio


def buscar_maximo(lista:list) -> int:
    """
    Descripción: busca el mayor valor de una lista.
    Parámetros: lista (list) -> lista de números (con al menos un elemento).
    Retorno: int -> valor máximo.
    """
    maximo = lista[0]
    for i in range(1, len(lista), 1):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo


def buscar_minimo(lista:list) -> int:
    """
    Descripción: busca el menor valor de una lista.
    Parámetros: lista (list) -> lista de números (con al menos un elemento).
    Retorno: int -> valor mínimo.
    """
    minimo = lista[0]
    for i in range(1, len(lista), 1):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo


def contar_ocurrencias(lista:list, valor:str) -> int:
    """
    Descripción: cuenta cuántas veces aparece un valor en una lista.
    Parámetros: lista (list) -> lista donde buscar.
                valor (str) -> valor a contar.
    Retorno: int -> cantidad de apariciones.
    """
    contador = 0
    for i in range(0, len(lista), 1):
        if lista[i] == valor:
            contador += 1
    return contador


# ---------------- PRESENTACIÓN ----------------

def mostrar_recomendaciones(recomendaciones:list):
    """
    Descripción: muestra las recomendaciones una por línea.
                 Si la lista está vacía, avisa que no hay recomendaciones.
    Parámetros: recomendaciones (list) -> lista de recomendaciones (str).
    Retorno: no retorna, solo muestra.
    """
    print("Recomendaciones generadas:")
    if len(recomendaciones) > 0:
        for i in range(0, len(recomendaciones), 1):
            print(f"- {recomendaciones[i]}")
    else:
        print("- Sin recomendaciones.")


def mostrar_evaluacion(nombre:str, stock:int, stock_minimo:int, demanda:str, vencimiento:str,
                       score:int, resultado:str, oferta:str, recomendaciones:list):
    """
    Descripción: muestra la evaluación completa de un producto.
    Parámetros: datos del producto, resultados calculados y
                recomendaciones (list) -> lista de recomendaciones.
    Retorno: no retorna, solo muestra.
    """
    print(f"\n-EVALUACION DE INVENTARIO\n"
          f"Producto: {nombre}\n"
          f"Stock: ({stock}/{stock_minimo})\n"
          f"Demanda: {demanda}\n"
          f"Vencimiento: {vencimiento}\n"
          f"Score acumulado: {score}\n"
          f"Resultado General: {resultado}\n"
          f"Aviso de Oferta: {oferta}")
    mostrar_recomendaciones(recomendaciones)


def mostrar_estadisticas(lista_scores:list, lista_resultados:list, lista_demandas:list):
    """
    Descripción: muestra las estadísticas finales de todas las consultas.
    Parámetros: lista_scores (list) -> scores de cada consulta.
                lista_resultados (list) -> resultado general de cada consulta.
                lista_demandas (list) -> demanda de cada consulta.
    Retorno: no retorna, solo muestra.
    """
    cantidad = len(lista_scores)
    urgentes = contar_ocurrencias(lista_resultados, "Reposicion urgente")
    demanda_alta = contar_ocurrencias(lista_demandas, "Alta")

    print("\n------ ESTADISTICAS FINALES ------")
    print(f"Cantidad de consultas realizadas: {cantidad}")
    print(f"Score promedio: {calcular_promedio(lista_scores)}")
    print(f"Score maximo: {buscar_maximo(lista_scores)}")
    print(f"Score minimo: {buscar_minimo(lista_scores)}")
    print(f"Porcentaje con Reposicion urgente: {calcular_porcentaje(urgentes, cantidad)}%")
    print(f"Porcentaje con demanda Alta: {calcular_porcentaje(demanda_alta, cantidad)}%")


def mostrar_grafico(lista_resultados:list):
    """
    Descripción: muestra un gráfico de barras por consola con la cantidad
                 de consultas de cada resultado (usa la función recursiva generar_barra).
    Parámetros: lista_resultados (list) -> resultado general de cada consulta.
    Retorno: no retorna, solo muestra.
    """
    print("\n--- Grafico: Resultados por consulta ---")
    print(f"Reposicion urgente  | {generar_barra(contar_ocurrencias(lista_resultados, 'Reposicion urgente'))}")
    print(f"Prioridad alta      | {generar_barra(contar_ocurrencias(lista_resultados, 'Prioridad alta'))}")
    print(f"Prioridad media     | {generar_barra(contar_ocurrencias(lista_resultados, 'Prioridad media'))}")
    print(f"Prioridad baja      | {generar_barra(contar_ocurrencias(lista_resultados, 'Prioridad baja'))}")