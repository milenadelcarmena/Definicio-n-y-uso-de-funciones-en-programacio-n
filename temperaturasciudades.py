def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de múltiples ciudades durante un período de tiempo.

    Parámetros:
    temperaturas (dict): Un diccionario donde las llaves son nombres de ciudades y los valores
                         son listas de temperaturas durante diferentes semanas.

    Retorna:
    dict: Un diccionario con la temperatura promedio de cada ciudad.
    """
    promedios = {}

    for ciudad, temps in temperaturas.items():
        if temps:  # aseguramos que la lista no esté vacía
            promedio = sum(temps) / len(temps)
            promedios[ciudad] = promedio
        else:
            promedios[ciudad] = None  # o se puede manejar como se desee

    return promedios


# Ejemplo
temperaturas_ciudades = {
    "Ciudad A": [22, 24, 23, 21],
    "Ciudad B": [30, 32, 31, 29],
    "Ciudad C": [15, 16, 14, 15]
}

promedios = calcular_temperatura_promedio(temperaturas_ciudades)

for ciudad, promedio in promedios.items():
    print(f"La temperatura promedio en {ciudad} es: {promedio:.2f}°C")