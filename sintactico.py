from os import error
import ply.yacc as yacc
from lexer import tokens
import re

tokens = tokens

texto = ""

errores = []
symbol_table = {}
fun_symbol_table = {
    'spin': {'parametros': ({'tipo': 'int', 'nombre': 'grados'}, {'tipo': 'int', 'nombre': 'minutos'}), 'retorno': 'void'},
    'isEmptyWay':{'parametros': None, 'retorno': 'bool'},
    'go':{'parametros': None, 'retorno': 'void'},
    'advanced':{'parametros': ({'tipo': 'float', 'nombre': 'distancia'}), 'retorno': 'void'},
    'reverse':{'parametros': ({'tipo': 'float', 'nombre': 'distancia'}), 'retorno': 'void'},
    'cleanWay':{'parametros': None, 'retorno': 'void'},
    'stop':{'parametros': None, 'retorno': 'void'},
    'tooHot':{'parametros': None, 'retorno': 'bool'}
}
import_table = []

def encontrar_linea(column_token):
    aux_cout = column_token
    codigo = texto.splitlines()
    print(len(codigo))
    for i in range(0, len(codigo)):
        
        if len(codigo[i]) > aux_cout:
            return i + 1
        else:
            aux_cout -= len(codigo[i]) + 1


def evaluate_expression(p):
    global symbol_table
    if isinstance(p,int) or isinstance(p,float):
        return p
    if len(p) == 2:
        # If the expression is a single token (ID, NUMERO, ENTERO, TRUE, FALSE)
        if isinstance(p[1], str):
            # Check if the token is an identifier (ID)
            if p[1] in symbol_table:
                if symbol_table[p[1]]['type'] == 'int' or symbol_table[p[1]]['type'] == 'duble':
                    # If the identifier exists in the symbol table, return its value
                    return symbol_table[p[1]]['value']
                else:
                    linea = encontrar_linea(p.lexpos(1))
                    errores.append('Errore semantico en linea ' + str(linea)+ ': no se puede realizar una operacion matematica con un ' + str(symbol_table[p[1]]['type']))
            else:
                # If the identifier does not exist in the symbol table, raise an error
                linea = encontrar_linea(p.lexpos(1))
                errores.append('Errore semantico en linea ' + str(linea)+ ': Identificador ' +str(p[1])+' no declarado con anterioridad')
        else:
            # If the token is a numeric value (NUMERO, ENTERO), return its value
            return p[1]
    elif len(p) == 4:
        if p[1] != '(':
            left = evaluate_expression(p[1])
            right = evaluate_expression(p[3])
            # If the expression is a combination of two expressions connected by an arithmetic operator
            if p[2] == '+':
                # Perform addition operation
                return left + right
            elif p[2] == '-':
                # Perform subtraction operation
                return left - right
            elif p[2] == '*':
                # Perform multiplication operation
                return left * right
            elif p[2] == '/':
                # Perform division operation
                return left / right
            elif p[2] == '%':
                # Perform modulus operation
                return left % right
        else:
            return evaluate_expression(p[2])
    else:
        linea = encontrar_linea(p.lexpos(1))
        # If the expression is not valid, raise an error
        errores.append(f'error semantico en liena {linea}: expresion invalida')


def evaluar_condicion(condicion,linea):
    print('condicion: ', condicion)
    global symbol_table
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
        errores.append(f'Error semantico en la linea {linea}: expresion boleana no valida')
        return None

def comprobarTipoDato(p):
    if p[1] == 'int' and isinstance(p[4],int):
        return True
    elif p[1] == 'float' and isinstance(p[4],float):
        return True
    elif p[1] == 'bool':
        try:
            p[4] = bool(p[4])
            return isinstance(p[4],bool)
        except:
            return False
    else:
        return False

def comprobarTipoDatoAsignacion(p):
    if symbol_table[p[1]]['type'] == 'int' and isinstance(p[3],int):
        return True
    
    if symbol_table[p[1]]['type'] == 'float' and isinstance(p[3],float):
        return True
    try:
        p[3] = bool(p[3])
        p[3] = eval(p[3])
        return isinstance(p[3],bool)
    except:
        return False

def remove_tuple(tupla):
    tupla_actual = tupla
    if len(tupla_actual) == 1:
        return tupla_actual[0]
    else:
        return [tupla_actual[0], remove_tuple(tupla_actual[1:])]

precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION')
)

def p_statements(p):
    '''
    statements : statement
               | statement statements
               | empty
    '''
    
    if len(p) == 2:
        p[0] = p[1]
        print(f"Valor de p[0] aquí (single statement): {p[0]}")
    elif len(p) == 3:
        p[0] = p[1], p[2]
        print(f"Valor de p[0] aquí (two statements): {p[0]}")
    else:
        p[0] = None
        print(f"Valor de p[0] aquí (empty): {p[0]}")
    print(f"p_statements: {p[:]}")

def p_statement(p):
    '''
    statement : fun_statement
              | variable_declaration
              | assignment
              | if_statement
              | for_statement
              | call_fun
              | import
              | empty
              | leer_arreglo
              | while_statement
    '''
    
    p[0] = p[1]
    print(f"p_statement: {p[:]}")
    #print(f"Valor de p[0] aquí: {p[0]}")

def p_import(p):
    '''
    import : BRING ID PUNTOCOMA
    '''
    global import_table
    p[0] = p[2]
    if p[2] not in import_table:
        import_table.append(p[2])
    else:
        linea = encontrar_linea(p.lexpos(2))
        errores.append(f'error semantico en linea {linea}: paquete anteriormente importado')
    print(f"p_import: {p[:]}")

# FUNCIONES ///////////////////////////////////////////////////////////////////
def p_fun_statement(p):
    '''
    fun_statement : FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    
    p[0] = p[2], p[4], p[7], p[9]
    if p[4] != None:
        tupla_actual = p[4]
        parametros = ()
        print('parametros: ', p[4])
        while True:
            if len(tupla_actual) == 3:
                tipo, nombre, tupla_actual = tupla_actual
                parametros = parametros + ({'tipo': tipo, 'nombre': nombre},)
            else:
                tipo, nombre = tupla_actual
                parametros = parametros + ({'tipo': tipo, 'nombre': nombre},)
                break
        fun_symbol_table[p[2]] = {'parametros': parametros, 'retorno': p[7]}
    else:
        fun_symbol_table[p[2]] = {'parametros': None,'retorno': p[7]}
    print(f"p_fun_statement: {p[:]}")

def p_fun_statement_error1(p):
    '''
    fun_statement : ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(1))
    mensaje = 'error sintactico en linea '+ str(linea) +': falto colocar la palabra "fun" para declarar la funcion'
    errores.append(mensaje)

def p_fun_statement_error2(p):
    '''
    fun_statement : FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(5))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un tipo de dato de retorno para la funcion, por ejemplo ":void"'
    errores.append(mensaje)

def p_fun_statement_error3(p):
    '''
    fun_statement : FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements
    '''
    linea = encontrar_linea(p.lexpos(9))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba una llave de cierre "}"'
    errores.append(mensaje)
    
def p_fun_statement_error4(p):
    '''
    fun_statement : FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(7))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba una llave de apertura "{"'
    errores.append(mensaje)

def p_fun_statement_error5(p):
    '''
    fun_statement : FUN PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    
    linea = encontrar_linea(p.lexpos(1))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un identificador para la funcion'
    errores.append(mensaje)

def p_fun_statement_error6(p):
    '''
    fun_statement : FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(6))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un tipo de dato de retorno para la función, por ejemplo ":void"'
    errores.append(mensaje)

def p_fun_statement_error7(p):
    '''
    fun_statement : FUN ID parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(2))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "("'
    errores.append(mensaje)
    
def p_fun_statement_error8(p):
    '''
    fun_statement : FUN ID PARENTESIS_APERTURA parameters DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(5))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un ")"'
    errores.append(mensaje)

def p_fun_statement_error9(p):
    '''
    fun_statement : FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE datatype LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(5))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaban ":" en la funcion'
    errores.append(mensaje)


# IF //////////////////////////////////////////////////////////////////
def p_if_statement(p):
    '''
    if_statement : IF PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE
                 | IF PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE ELSE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    if len(p) == 8:
        p[0] = p[1],p[3], p[6]
    else:
        p[0] = p[1], p[3], p[6], p[8], p[10]
    print(f"p_if_statement: {p[:]}")

def p_if_statement_error1(p):
    '''
    if_statement : PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE
                 | PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE ELSE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(1))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "if"'
    errores.append(mensaje)

def p_if_statement_error2(p):
    '''
    if_statement : IF condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE
                 | IF condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE ELSE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(1))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "("'
    errores.append(mensaje)

def p_if_statement_error3(p):
    '''
    if_statement : IF PARENTESIS_APERTURA PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE
                 | IF PARENTESIS_APERTURA PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE ELSE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(2))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba una condicion en el IF'
    errores.append(mensaje)

def p_if_statement_error4(p):
    '''
    if_statement : IF PARENTESIS_APERTURA condition LLAVE_APERTURA statements LLAVE_CIERRE
                 | IF PARENTESIS_APERTURA condition LLAVE_APERTURA statements LLAVE_CIERRE ELSE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(4))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un ")"'
    errores.append(mensaje)

def p_if_statement_error5(p):
    '''
    if_statement : IF PARENTESIS_APERTURA condition PARENTESIS_CIERRE statements LLAVE_CIERRE
                 | IF PARENTESIS_APERTURA condition PARENTESIS_CIERRE statements LLAVE_CIERRE ELSE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(4))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "{"'
    errores.append(mensaje)

def p_if_statement_error6(p):
    '''
    if_statement : IF PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements
                 | IF PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements ELSE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(5))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "}"'
    errores.append(mensaje)

def p_if_statement_error7(p):
    '''
    if_statement : IF PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(7))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "else"'
    errores.append(mensaje)

def p_if_statement_error8(p):
    '''
    if_statement : IF PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE ELSE statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(7))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "{"'
    errores.append(mensaje)

def p_if_statement_error9(p):
    '''
    if_statement : IF PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE ELSE LLAVE_APERTURA statements
    '''
    linea = encontrar_linea(p.lexpos(9))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "}"'
    errores.append(mensaje)

# FOR ///////////////////////////////////////////////////////////////////////////////////////

def p_for_statement(p):
    '''
    for_statement : FOR PARENTESIS_APERTURA variable_declaration condition PUNTOCOMA expression PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    p[0] = p[3], p[4], p[6], p[8], p[10]
    print(f"p_for_statement: {p[:]}")

# call fun ///////////////////////////////////////////////////////////////////////

def p_call_fun(p):
    '''
    call_fun : ID PARENTESIS_APERTURA expression_list PARENTESIS_CIERRE PUNTOCOMA
             | ID PUNTO ID PARENTESIS_APERTURA expression_list PARENTESIS_CIERRE PUNTOCOMA
    '''
    global fun_symbol_table
    global import_table
    if len(p) == 6:
        p[0] = p[1], p[3]
        print('id Funciona:', p[1])
        if p[1] not in fun_symbol_table: # verifica si existe en la table
            linea = encontrar_linea(p.lexpos(1))
            errores.append(f"Error semantico en la linea {linea}: Funcion '{p[1]}' no declarada")
        else: # verifica los parametros
            if fun_symbol_table[p[1]]['parametros'] is not None:
                numero_parametros = len(fun_symbol_table[p[1]]['parametros'])
            else:
                numero_parametros = 0
            #obtiene los parametros registrados en la tabla
            
            if p[3][0] is not None:
                numero_parametros_llamada = len(p[3])
            else:
                numero_parametros_llamada = 0

            print('numero_parametros:', numero_parametros)
            print('numero_parametros_llamda', numero_parametros_llamada)
            if numero_parametros_llamada != numero_parametros: # verifica si la cantidad de parametros dados son los mismos que los de la tabla
                linea = encontrar_linea(p.lexpos(1))
                errores.append(f"Error semantico en la linea {linea}: Numero de parametros incorrecto en la funcion '{p[1]}'")
            else:
                pass  
    else:
        p[0] = p[1], p[3], p[5]
        if p[1] not in import_table:
            linea = encontrar_linea(p.lexpos(1))
            errores.append(f"Error semantico en la linea {linea}: Paquete '{p[1]}' no encontrado")
            p[0] = p[1], p[3], p[5], p[7]
    print(f"p_call_fun: {p[:]}")

def p_call_fun_error1(p):
    '''
    call_fun : PARENTESIS_APERTURA expression_list PARENTESIS_CIERRE PUNTOCOMA
             | PUNTO ID PARENTESIS_APERTURA expression_list PARENTESIS_CIERRE PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(1))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "ID"'
    errores.append(mensaje)

def p_call_fun_error2(p):
    '''
    call_fun : ID expression_list PARENTESIS_CIERRE PUNTOCOMA
             | ID PUNTO ID expression_list PARENTESIS_CIERRE PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(3))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "("'
    errores.append(mensaje)

def p_call_fun_error3(p):
    '''
    call_fun : ID PARENTESIS_APERTURA expression_list PUNTOCOMA
             | ID PUNTO ID PARENTESIS_APERTURA expression_list PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(4))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un ")"'
    errores.append(mensaje)

def p_call_fun_error4(p):
    '''
    call_fun : ID PUNTO PARENTESIS_APERTURA expression_list PARENTESIS_CIERRE PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(2))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "ID"'
    errores.append(mensaje)

def p_call_fun_error5(p):
    '''
    call_fun : ID PARENTESIS_APERTURA expression_list PARENTESIS_CIERRE
             | ID PUNTO ID PARENTESIS_APERTURA expression_list PARENTESIS_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(4))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un ";"'
    errores.append(mensaje)



# declatopm de variable /////////////////////////////////////////////////
def p_variable_declaration(p):
    '''
    variable_declaration : datatype ID ASIGNAR expression PUNTOCOMA
                         | datatype ID ASIGNAR condition PUNTOCOMA
                         | datatype ID PUNTOCOMA
                         | datatype CORCHETE_APERTURA CORCHETE_CIERRE ID ASIGNAR expression_list PUNTOCOMA
    '''
    if len(p) == 6: #declaracion con asignacion
        p[0] = p[1], p[2], p[4]
        variable_type = p[1]
        variable_name = p[2]
        value = p[4]
        if variable_name in symbol_table: # variable en tabla de simbolos
            linea = encontrar_linea(p.lexpos(2))
            errores.append(f"Error semantico en la linea{linea}: Variable '{variable_name}' ya declarada")
        elif comprobarTipoDato(p): # verificar si se asigna el tipo de dato correcto
            symbol_table[variable_name] = {'type': variable_type, 'value': value}
        else:
            linea = encontrar_linea(p.lexpos(4))
            errores.append(f"Error semantico en la linea {linea}: Tipo de dato '{value}' no valido para la variable '{variable_name}'")
    elif len(p) == 4: #declaracion sin asignacion
        variable_type = p[1]
        variable_name = p[2]
        if variable_name in symbol_table:
            linea = encontrar_linea(p.lexpos(2))
            errores.append(f"Error semantico en la linea {linea}: Variable '{variable_name}' ya declarada")
        else:
            symbol_table[variable_name] = {'type': variable_type, 'value': None}
        p[0] = p[1], p[2]
    elif len(p) == 8: #declaracion con asignacion en arreglo
        variable_type = p[1] + '[]'
        variable_name = p[4]
        value = p[6]
        print('valor:', value)
        p[0] = variable_type, variable_name, value
        if variable_name in symbol_table:
            linea = encontrar_linea(p.lexpos(4))
            errores.append(f"Error semantico en la linea {linea}: Variable '{variable_name}' ya declarada")
        else:
            symbol_table[variable_name] = {'type': variable_type, 'value': value}
    print(f"p_variable_declaration: {p[:]}")
    

def p_variable_declaration_eror1(p):
    '''
    variable_declaration : ID PUNTOCOMA
                         | CORCHETE_APERTURA CORCHETE_CIERRE ID ASIGNAR expression_list PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(1))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "TIPO DE DATO"'
    errores.append(mensaje)

def p_variable_declarationeror2(p):
    '''
    variable_declaration : datatype ASIGNAR expression PUNTOCOMA
                         | datatype ASIGNAR condition PUNTOCOMA
                         | datatype PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(1))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "ID"'
    errores.append(mensaje)
    
def p_variable_declarationeror3(p):
    '''
    variable_declaration : datatype ID expression PUNTOCOMA
                         | datatype ID condition PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(2))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "="'
    errores.append(mensaje)
    
def p_variable_declarationeror4(p):
    '''
    variable_declaration : datatype ID ASIGNAR expression
                         | datatype ID ASIGNAR condition
                         | datatype ID
                         | datatype CORCHETE_APERTURA CORCHETE_CIERRE ID ASIGNAR expression_list
    '''
    linea = encontrar_linea(p.lexpos(2))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un ";"'
    errores.append(mensaje)

def p_variable_declarationeror5(p):
    '''
    variable_declaration : datatype CORCHETE_CIERRE ID ASIGNAR expression_list PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(1))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "[]"'
    errores.append(mensaje)

def p_variable_declarationeror6(p):
    '''
    variable_declaration : datatype CORCHETE_APERTURA ID ASIGNAR expression_list PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(2))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "]"'
    errores.append(mensaje)

def p_variable_declarationeror7(p):
    '''
    variable_declaration : datatype CORCHETE_APERTURA CORCHETE_CIERRE ASIGNAR expression_list PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(3))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "ID"'
    errores.append(mensaje)

def p_variable_declarationeror8(p):
    '''
    variable_declaration : datatype CORCHETE_APERTURA CORCHETE_CIERRE ID expression_list PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(4))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "="'
    errores.append(mensaje)
def p_variable_declarationeror9(p):
    '''
    variable_declaration : datatype ID ASIGNAR PUNTOCOMA
                         | datatype CORCHETE_APERTURA CORCHETE_CIERRE ID ASIGNAR PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(4))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un valor a asignar'
    errores.append(mensaje)
# ASIGNACION ////////////////////////////////////////////////////////////////////////

def p_assignment(p):
    '''
    assignment : ID ASIGNAR expression PUNTOCOMA
               | ID ASIGNAR condition PUNTOCOMA
    '''
     # Check for self-assignment (identifier = identifier)
    if p[1] == p[3]:
        linea = encontrar_linea(p.lexpos(1))
        errores.append(f'"Error de sintaxis en la linea {linea}: Asignación recursiva"')  # Raise error if self-assignment detected
    else:
        p[0] = p[1], p[3]
        variable_name = p[1]
        value = p[3]
        if variable_name not in symbol_table:
            linea = encontrar_linea(p.lexpos(1))
            errores.append(f"Error semantico en la linea {linea}: Variable '{variable_name}' no declarada")
        elif comprobarTipoDatoAsignacion(p):
            symbol_table[variable_name]['value'] = value
        else:
            linea = encontrar_linea(p.lexpos(3))
            errores.append(f"Error semantico en la linea {linea}: Tipo de dato '{value}' no valido para la variable '{variable_name}'")

def p_assignment_error1(p):
    '''
    assignment : ASIGNAR expression PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(1))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "ID"'
    errores.append(mensaje)

def p_assignment_error2(p):
    '''
    assignment : ID expression PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(1))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "="'
    errores.append(mensaje)

def p_assignment_error3(p):
    '''
    assignment : ID ASIGNAR PUNTOCOMA
    '''
    linea = encontrar_linea(p.lexpos(2))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un valor a asignar'
    errores.append(mensaje)

def p_assignment_error4(p):
    '''
    assignment : ID ASIGNAR expression
    '''
    linea = encontrar_linea(p.lexpos(2))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un ";"'
    errores.append(mensaje)

# lista de expresiones ////////////////////////////////////////////////////
def p_expression_list(p):
    '''
    expression_list : expression
                    | expression COMA expression_list
                    | empty
    '''
    
    if len(p) == 2:
        p[0] = p[1],
    else:
        p[0] = p[1], p[3]
    
        
    print(f"p_expression_list: {p[:]}")

def p_leer_arreglo(p):
    '''
    leer_arreglo : ID CORCHETE_APERTURA expression CORCHETE_CIERRE PUNTOCOMA
    '''
    p[0] = p[1], p[3]
    if p[1] not in symbol_table:
        linea = encontrar_linea(p.lexpos(1))
        errores.append(f"Error semantico en la linea {linea}: arreglo {p[1]} no declarado")

def p_while(p):
    '''
    while_statement : WHILE PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    p[0] = p[1], p[3], p[5]

def p_while_error1(p):
    '''
    while_statement : WHILE condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(1))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "("'
    errores.append(mensaje)

def p_while_error2(p):
    '''
    while_statement : WHILE PARENTESIS_APERTURA  PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(2))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba una condicon en while'
    errores.append(mensaje)

def p_while_error3(p):
    '''
    while_statement : WHILE PARENTESIS_APERTURA condition LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(4))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un ")"'
    errores.append(mensaje)

def p_while_error2(p):
    '''
    while_statement : WHILE PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements
    '''
    linea = encontrar_linea(p.lexpos(1))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "}"'
    errores.append(mensaje)


def p_while_error2(p):
    '''
    while_statement : WHILE PARENTESIS_APERTURA condition PARENTESIS_CIERRE statements LLAVE_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(1))
    mensaje = 'error sintactico en linea '+ str(linea) +': Se esperaba un "{"'
    errores.append(mensaje)


def p_condition(p):
    '''
    condition : condition AND condition
              | condition OR condition
              | NOT condition
              | condition MENORQUE condition
              | condition MAYORQUE condition
              | condition IGUAL condition
              | condition DIFERENTE condition
              | condition MENORIGUAL condition
              | condition MAYORIGUAL condition
              | PARENTESIS_APERTURA condition PARENTESIS_CIERRE
              | boleano
              | ID
              | NUMERO
              | ENTERO
              | call_fun
    '''
    linea = encontrar_linea(p.lexpos(1))
    if len(p) == 2:
        if isinstance(p[1], int):
            p[0] = p[1]
        elif isinstance(p[1], float):
            p[0] = p[1]
        elif isinstance(p[1],bool):
            p[0] = p[1]
        elif isinstance(p[1],str):
            p[0] = p[1]
        else:
            try:
                if fun_symbol_table[p[1][0]]['retorno'] != 'bool':
                    linea = encontrar_linea(p.lexpos(1))
                    errores.append(f"Error semantico en la linea {linea}: La funcion {p[1][0]} no retorna un 'bool'")
            except:
                pass
            p[0] = False
            
    elif len(p) == 3:
        condicion = f'{p[1]} {p[2]}'
        p[0] = evaluar_condicion(condicion, linea)
    else:
        condicion = f'{p[1]} {p[2]} {p[3]}'
        p[0] = evaluar_condicion(condicion, linea)
    print(f"condition: {p[:]}")


def p_expression(p):
    '''
    expression : ID
               | NUMERO
               | ENTERO
               | expression SUMA expression
               | expression RESTA expression
               | expression MULTIPLICACION expression
               | expression DIVISION expression
               | expression MODULO expression
               | expression MASIGUAL expression
               | expression MENOSIGUAL expression
               | expression DIVIGUAL expression
               | expression MULTIGUAL condition
               | PARENTESIS_APERTURA expression PARENTESIS_CIERRE
    '''
    linea = encontrar_linea(p.lexpos(1))
    p[0] = evaluate_expression(p)
    print(f"expression: {p[:]}")
    

def p_parameters(p):
    '''
    parameters : datatype ID
               | datatype ID COMA parameters
               | empty
    '''
    if len(p) == 3:
        p[0] = p[1],p[2]
    elif len(p) == 5:
        p[0] = p[1],p[2], p[4]
    print(f"p_parameters: {p[:]}")
    
def p_datatype(p):
    '''
    datatype : VOID
             | FLOAT
             | INT
             | BOOL
    '''
    p[0] = p[1]
    print(f"p_datatype: {p[:]}")

def p_boleano(p):
    '''
    boleano : TRUE
            | FALSE
    '''
    p[0] = p[1]
    print(f"p_boleano: {p[:]}")

def p_empty(p):
    '''
    empty :
    '''
    print(f"p_empty: {p[:]}")

def p_error(p):
    if p:
        linea = encontrar_linea(p.lexpos)
        mensaje = 'Error de sintaxis en la línea ' + str(linea) + ': ' + str(p.value)
        errores.append(mensaje)
    else:
        pass

# Build the parser
parser = yacc.yacc()

def sintactico(codigo):
    global texto 
    global errores
    global symbol_table
    global fun_symbol_table
    global import_table
    texto = codigo
    errores = []
    symbol_table = {}
    fun_symbol_table = {
    'spin': {'parametros': ({'tipo': 'int', 'nombre': 'grados'}, {'tipo': 'int', 'nombre': 'minutos'}), 'retorno': 'void'},
    'isEmptyWay':{'parametros': None, 'retorno': 'bool'},
    'go':{'parametros': None, 'retorno': 'void'},
    'advanced':{'parametros': ({'tipo': 'int', 'nombre': 'metros'},{'tipo': 'int', 'nombre': 'centimetros'}), 'retorno': 'void'},
    'reverse':{'parametros': ({'tipo': 'int', 'nombre': 'metros'},{'tipo': 'int', 'nombre': 'centimetros'}), 'retorno': 'void'},
    'cleanWay':{'parametros': None, 'retorno': 'bool'},
    'stop':{'parametros': None, 'retorno': 'void'},
    'tooHot':{'parametros': None, 'retorno': 'bool'}
}
    import_table = []
    ast = parser.parse(codigo)
    print(symbol_table)
    return ast, errores, symbol_table

# Test the parser
def traverse_ast(node):
    if node is not None:
        print(node.type)  # Print the node type

        # Traverse the children of the node
        for child in node.children:
            traverse_ast(child)
