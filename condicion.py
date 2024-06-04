def evaluar_condicion(condicion, symbol_table):
    """
    Evalúa una expresión booleana y devuelve True o False.

    Args:
        condicion (str): La expresión booleana a evaluar.
        symbol_table (dict): Tabla de símbolos con identificadores y sus valores.

    Returns:
        bool: True si la condición es verdadera, False si es falsa.
    """
    try:
        # Reemplaza los identificadores con sus valores en la expresión
        for identificador, info in symbol_table.items():
            condicion = condicion.replace(identificador, str(info['value']))

        # Utiliza eval() para evaluar la expresión booleana
        resultado = eval(condicion)
        return bool(resultado)
    except Exception as e:
        print(f"Error al evaluar la condición: {e}")
        return False

# Ejemplo de uso con una tabla de símbolos
symbol_table = {
    'x': {'type': 'int', 'value': 5},
    'y': {'type': 'float', 'value': 3.14},
    'f': {'type': 'bool', 'value': 'True'}
}

expresion1 = "3.14 > f"
expresion2 = "x == 5 or y != 2.71"

print(f"Resultado 1: {evaluar_condicion(expresion1, symbol_table)}")  # Debería ser True
print(f"Resultado 2: {evaluar_condicion(expresion2, symbol_table)}")  # Debería ser True
