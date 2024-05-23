import ply.yacc as yacc
from lexer import tokens

# Definición de reglas para construcción de árbol binario
def p_importacion(p):
    '''importacion : BRING ID PUNTOCOMA'''
    p[0] = ('importacion', p[2])

def p_programa(p):
    '''programa : importacion programa
                | funcion programa
                | importacion
                | funcion'''
    if len(p) == 3:
        p[0] = ('programa', p[1], p[2])
    else:
        p[0] = ('programa', p[1])

def p_funciones(p):
    '''funciones : funcion funciones
                 | funcion'''
    if len(p) == 3:
        p[0] = ('funciones', p[1], p[2])
    else:
        p[0] = ('funciones', p[1])

def p_funcion(p):
    '''funcion : FUN ID PARENTESIS_APERTURA parametros_declaracion PARENTESIS_CIERRE cuerpo'''
    p[0] = ('funcion', p[2], p[4], p[6])

def p_argumentos(p):
    '''argumentos : expresion
                  | expresion COMA argumentos
                  | empty'''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = []

def p_parametros_declaracion(p):
    '''parametros_declaracion : tipo_dato ID
                              | tipo_dato ID COMA parametros_declaracion
                              | empty'''
    if len(p) == 3:
        p[0] = [(p[1], p[2])]
    elif len(p) == 5:
        p[0] = [(p[1], p[2])] + p[4]
    else:
        p[0] = []

def p_sentencia_if(p):
    '''sentencia_if : IF PARENTESIS_APERTURA expresion PARENTESIS_CIERRE cuerpo
                    | IF PARENTESIS_APERTURA expresion PARENTESIS_CIERRE cuerpo ELSE cuerpo'''
    if len(p) == 6:
        p[0] = ('if', p[3], p[5], None)
    else:
        p[0] = ('if', p[3], p[5], p[7])

def p_sentencia_while(p):
    '''sentencia_while : WHILE PARENTESIS_APERTURA expresion PARENTESIS_CIERRE cuerpo'''
    p[0] = ('while', p[3], p[5])

def p_sentencia_for(p):
    '''sentencia_for : FOR PARENTESIS_APERTURA declaracion_variable PUNTOCOMA expresion PUNTOCOMA expresion PARENTESIS_CIERRE cuerpo'''
    p[0] = ('for', p[3], p[5], p[7], p[9])

def p_condicion(p):
    '''
    condicion : condicion AND condicion
              | condicion OR condicion
              | NOT condicion
              | PARENTESIS_APERTURA condicion PARENTESIS_CIERRE
              | exp op_relacional exp
    '''
    if len(p) == 4:
        if p[2] == 'and':
            p[0] = ('and', p[1], p[3])
        elif p[2] == 'or':
            p[0] = ('or', p[1], p[3])
        else:
            p[0] = (p[2], p[1], p[3])
    elif len(p) == 3:
        p[0] = ('not', p[2])
    else:
        p[0] = ('parentesis', p[2])

def p_op_relacional(p):
    '''
    op_relacional : MENORQUE
                  | MAYORQUE
                  | IGUAL
                  | MENORIGUAL
                  | MAYORIGUAL
                  | DIFERENTE
    '''
    p[0] = p[1]

def p_exp(p):
    '''
    exp : exp op_aritmetico exp
        | PARENTESIS_APERTURA exp PARENTESIS_CIERRE
        | ID
        | dato
    '''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    elif len(p) == 3:
        p[0] = ('parentesis', p[2])
    else:
        p[0] = p[1]

def p_op_aritmetico(p):
    '''
    op_aritmetico : SUMA
                  | RESTA
                  | MULTIPLICACION
                  | DIVISION
    '''
    p[0] = p[1]

def p_dato(p):
    '''
    dato : NUMERO
         | CADENA
         | DEGREE
         | TIME
         | DISTANCE
         | TEMP
         | STATE
         | ANY
    '''
    p[0] = p[1]

def p_cuerpo(p):
    '''cuerpo : LLAVE_APERTURA sentencias LLAVE_CIERRE'''
    p[0] = p[2]

def p_sentencias(p):
    '''sentencias : sentencia sentencias
                  | sentencia'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_sentencia(p):
    '''sentencia : declaracion_variable
                 | asignacion
                 | estructura_control
                 | llamada_funcion
                 | retorno
                 | expresion PUNTOCOMA'''
    p[0] = p[1]

def p_declaracion_variable(p):
    '''declaracion_variable : VAR ID ASIGNAR expresion PUNTOCOMA
                            | VAR ID PUNTOCOMA'''
    if len(p) == 6:
        p[0] = ('declaracion_variable', p[2], p[4])
    elif len(p) == 4:
        p[0] = ('declaracion_variable', p[2], None)
    else:
        raise ValueError(f"Sintaxis inválida en la declaración de variable: {p}")

def p_asignacion(p):
    '''asignacion : ID ASIGNAR expresion PUNTOCOMA'''
    p[0] = ('asignacion', p[1], p[3])

def p_tipo_dato(p):
    '''
    tipo_dato : DEGREE
              | TIME
              | DISTANCE
              | TEMP
              | BOOL
              | STATE
              | ANY
    '''
    p[0] = p[1]

def p_llamada_funcion(p):
    '''llamada_funcion : ID PARENTESIS_APERTURA argumentos PARENTESIS_CIERRE PUNTOCOMA'''
    p[0] = ('llamada_funcion', p[1], p[3])

def p_estructura_control(p):
    '''estructura_control : sentencia_if
                          | sentencia_for
                          | sentencia_while'''
    p[0] = p[1]

def p_retorno(p):
    '''retorno : RETURN expresion PUNTOCOMA'''
    p[0] = ('retorno', p[2])

def p_expresion(p):
    '''expresion : expresion_logica
                 | expresion_logica operador_logico expresion'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_expresion_logica(p):
    '''expresion_logica : expresion_relacional
                        | expresion_relacional operador_relacional expresion_logica'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_expresion_relacional(p):
    '''expresion_relacional : expresion_aritmetica
                            | expresion_aritmetica operador_relacional expresion_relacional'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_expresion_aritmetica(p):
    '''expresion_aritmetica : termino
                            | termino operador_aritmetico expresion_aritmetica'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_termino(p):
    '''termino : factor
               | factor operador_termino termino'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_factor(p):
    '''factor : ID
              | llamada_funcion
              | NUMERO
              | CADENA
              | PARENTESIS_APERTURA expresion PARENTESIS_CIERRE'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_operador_logico(p):
    '''operador_logico : AND
                       | OR'''
    p[0] = p[1]

def p_operador_relacional(p):
    '''operador_relacional : MENORQUE
                           | MAYORQUE
                          | IGUAL
                          | MENORIGUAL
                          | MAYORIGUAL
                          | DIFERENTE'''
    p[0] = p[1]

def p_operador_aritmetico(p):
    '''operador_aritmetico : SUMA
                           | RESTA
                           | MULTIPLICACION
                           | DIVISION'''
    p[0] = p[1]

def p_operador_termino(p):
    '''operador_termino : MULTIPLICACION
                        | DIVISION
                        | MODULO'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en la entrada: {p.value} en la línea {p.lineno}")
    else:
        print("Error de sintaxis en la entrada")

# Resultado del análisis
resultado_gramatica = []

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()  # Limpiar los resultados anteriores

    gram = parser.parse(data)
    if gram is not None:
        resultado_gramatica.append(str(gram))

    return resultado_gramatica

# Instanciamos el analizador sintáctico
parser = yacc.yacc()

if __name__ == "__main__":
    input_data = '''
var x = 5;
'''

    # Llama a la función de prueba sintáctica y obtiene el resultado
    resultado = prueba_sintactica(input_data)

    # Imprime el resultado del análisis sintáctico
    for linea in resultado:
        print(linea)                          

