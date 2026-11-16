from Generales import *

def main():

    lista_scores = []
    lista_resultados = []
    lista_demandas = []
    seguir = True

    print("\n------ EVALUACION DE INVENTARIO ------\n")

    while seguir == True:
        print(f"\n--- Consulta N° {len(lista_scores) + 1} ---")
        print("-INGRESO DE DATOS DEL PRODUCTO")

  
        nombre = pedir_nombre()
        stock = pedir_stock()
        stock_minimo = pedir_stock_minimo()
        demanda = pedir_demanda()
        vencimiento = pedir_vencimiento()

  
        cobertura = calcular_cobertura(stock, stock_minimo)
        recomendaciones = []   # lista vacía que aplicar_reglas va a llenar
        score = aplicar_reglas(stock, stock_minimo, demanda, vencimiento, cobertura, recomendaciones)
        resultado = obtener_resultado_general(score)
        oferta = determinar_oferta(stock, stock_minimo, demanda, vencimiento, cobertura)

  
        mostrar_evaluacion(nombre, stock, stock_minimo, demanda, vencimiento, score, resultado, oferta, recomendaciones)
        lista_scores.append(score)
        lista_resultados.append(resultado)
        lista_demandas.append(demanda)
        seguir = preguntar_continuar()

    mostrar_estadisticas(lista_scores, lista_resultados, lista_demandas)
    mostrar_grafico(lista_resultados)


if __name__ == "__main__":
    main()