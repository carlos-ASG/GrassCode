from os import error
import ply.yacc as yacc
from lexer import tokens
import re
from ASTNode import ASTNode

tokens = tokens

texto = ""

errores = []
symbol_table = {}
fun_symbol_table = {}
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
                    errores.append('Errore semantico en linea ' +linea+ ': no se puede realizar una operacion matematica con un ' + str(symbol_table[p[1]]['type']))
            else:
                # If the identifier does not exist in the symbol table, raise an error
                linea = encontrar_linea(p.lexpos(1))
                errores.append('Errore semantico en linea ' +linea+ ': Identificador ' +p[1]+' no declarado con anterioridad')
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
        # If the expression is not valid, raise an error
        errores.append('expresion invalida')


def evaluar_condicion(condicion,linea):
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
    print(type(p[4]))
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
        p[0] = []
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
    

# FOR ///////////////////////////////////////////////////////////////////////////////////////

def p_for_statement(p):
    '''
    for_statement : FOR PARENTESIS_APERTURA datatype ID ASIGNAR expression PUNTOCOMA condition PUNTOCOMA ID ASIGNAR expression PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE
    '''
    p[0] = p[3], p[4], p[6], p[8], p[10]
    print(f"p_for_statement: {p[:]}")

def p_call_fun(p):
    '''
    call_fun : ID PARENTESIS_APERTURA expression_list PARENTESIS_CIERRE PUNTOCOMA
             | ID PUNTO ID PARENTESIS_APERTURA expression_list PARENTESIS_CIERRE PUNTOCOMA
    '''
    global fun_symbol_table
    global import_table
    if len(p) == 6:
        p[0] = p[1], p[3]
        if p[1] not in fun_symbol_table:
            linea = encontrar_linea(p.lexpos(1))
            errores.append(f"Error semantico en la linea{linea}: Funcion '{p[1]}' no declarada")
    else:
        p[0] = p[1], p[3], p[5]
        if p[1] not in import_table:
            linea = encontrar_linea(p.lexpos(1))
            errores.append(f"Error semantico en la linea{linea}: Paquete '{p[1]}' no encontrado")
            p[0] = p[1], p[3], p[5], p[7]
    print(f"p_call_fun: {p[:]}")

def p_variable_declaration(p):
    '''
    variable_declaration : datatype ID ASIGNAR expression PUNTOCOMA
                         | datatype ID ASIGNAR condition PUNTOCOMA
                         | datatype ID PUNTOCOMA
                         | datatype CORCHETE_APERTURA CORCHETE_CIERRE ID ASIGNAR CORCHETE_APERTURA expression_list CORCHETE_CIERRE PUNTOCOMA
                         | datatype CORCHETE_APERTURA CORCHETE_CIERRE ID ASIGNAR CORCHETE_APERTURA CORCHETE_CIERRE PUNTOCOMA
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
        p[0] = p[1], p[2], None
    elif len(p) == 9: #declaracion con asignacion en arreglo
        variable_type = p[1] + '[]'
        variable_name = p[2]
        value = p[7]
        if variable_name in symbol_table:
            linea = encontrar_linea(p.lexpos(4))
            errores.append(f"Error semantico en la linea {linea}: Variable '{variable_name}' ya declarada")
        else:
            symbol_table[variable_name] = {'type': variable_type, 'value': value}
    print(f"p_variable_declaration: {p[:]}")
    

def p_assignment(p):
    '''
    assignment : ID ASIGNAR expression PUNTOCOMA
    '''
     # Check for self-assignment (identifier = identifier)
    if p[1] == p[3]:
        raise SyntaxError("Error de sintaxis: Asignación recursiva")  # Raise error if self-assignment detected

    p[0] = p[1], p[3]
    print(f"p_assignment: {p[:]}")

def p_expression_list(p):
    '''
    expression_list : expression
                    | expression COMA expression_list
                    | empty
    '''
    
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + p[3]
    print(f"p_expression_list: {p[:]}")

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
    '''
    linea = encontrar_linea(p.lexpos(1))
    if len(p) == 2:
        p[0] = p[1]
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
               | PARENTESIS_APERTURA expression PARENTESIS_CIERRE
    '''
    p[0] = evaluate_expression(p)
    print(f"expression: {p[:]}")
    

def p_parameters(p):
    '''
    parameters : datatype ID
               | datatype ID COMA parameters
               | empty
    '''
    if len(p) == 3:
        p[0] = p[2]
    elif len(p) == 5:
        p[0] = p[2], p[4]
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
    fun_symbol_table = {}
    import_table = []
    ast = parser.parse(codigo)
    print(symbol_table)
    return ast, errores

# Test the parser
def traverse_ast(node):
    if node is not None:
        print(node.type)  # Print the node type

        # Traverse the children of the node
        for child in node.children:
            traverse_ast(child)
