
def validar_nombre(nombre:str) -> bool:
    """
    Descripción: verifica que el nombre del producto no esté vacío.
    Parámetros: nombre (str) -> nombre ingresado por el usuario.
    Retorno: bool -> True si el nombre tiene al menos un caracter, False si no.
    """
    valido = False
    if len(nombre) > 0:
        valido = True
    return valido


def validar_stock(stock:int) -> bool:
    """
    Descripción: verifica que el stock actual no sea negativo.
    Parámetros: stock (int) -> stock actual del producto.
    Retorno: bool -> True si el stock es mayor o igual a 0, False si no.
    """
    valido = False
    if stock >= 0:
        valido = True
    return valido


def validar_stock_minimo(stock_minimo:int) -> bool:
    """
    Descripción: verifica que el stock mínimo sea mayor a 0.
    Parámetros: stock_minimo (int) -> stock mínimo del producto.
    Retorno: bool -> True si es mayor a 0, False si no.
    """
    valido = False
    if stock_minimo > 0:
        valido = True
    return valido


def validar_demanda(demanda:str) -> bool:
    """
    Descripción: verifica que la demanda sea Baja, Media o Alta.
    Parámetros: demanda (str) -> demanda ingresada por el usuario.
    Retorno: bool -> True si es una de las tres opciones, False si no.
    """
    valido = False
    if demanda == "Baja" or demanda == "Media" or demanda == "Alta":
        valido = True
    return valido


def validar_vencimiento(vencimiento:str) -> bool:
    """
    Descripción: verifica que el vencimiento sea Proximo o No_proximo.
    Parámetros: vencimiento (str) -> vencimiento ingresado por el usuario.
    Retorno: bool -> True si es una de las dos opciones, False si no.
    """
    valido = False
    if vencimiento == "Proximo" or vencimiento == "No_proximo":
        valido = True
    return valido


def validar_respuesta(respuesta:str) -> bool:
    """
    Descripción: verifica que la respuesta para continuar sea S o N.
    Parámetros: respuesta (str) -> respuesta ingresada por el usuario.
    Retorno: bool -> True si es S o N, False si no.
    """
    valido = False
    if respuesta == "S" or respuesta == "N":
        valido = True
    return valido


def calcular_cobertura(stock:int, stock_minimo:int) -> float:
    """
    Descripción: calcula cuántas veces el stock actual cubre al stock mínimo.
    Parámetros: stock (int) -> stock actual.
                stock_minimo (int) -> stock mínimo (siempre mayor a 0 por validación).
    Retorno: float -> resultado de stock / stock_minimo.
    """
    cobertura = stock / stock_minimo
    return cobertura


def calcular_porcentaje(parte:int, total:int) -> float: 
    """
    Descripción: calcula qué porcentaje representa una parte sobre un total.
    Parámetros: parte (int) -> cantidad a evaluar.
                total (int) -> cantidad total.
    Retorno: float -> porcentaje calculado (0 si el total es 0).
    """
    porcentaje = 0
    if total > 0:
        porcentaje = (parte / total) * 100
    return porcentaje


def generar_barra(cantidad:int) -> str:
    """
    Descripción: función RECURSIVA que arma una barra de asteriscos para el gráfico.
                 Caso base: si la cantidad es 0, devuelve un texto vacío.
                 Caso recursivo: devuelve un "*" más la barra de (cantidad - 1).
    Parámetros: cantidad (int) -> cantidad de asteriscos a generar.
    Retorno: str -> texto con tantos "*" como indique cantidad.
    """
    barra = ""
    if cantidad > 0:
        barra = "*" + generar_barra(cantidad - 1)
    return barra
