import ply.yacc as yacc
from lexer import tokens  # Asegúrate de que 'lexer' esté en el mismo directorio o ajusta el import según sea necesario

# Definición de reglas para construcción de árbol binario
def p_sentencia_if(p):
    '''
    sentencia_if : IF PARENTESIS_APERTURA condicion PARENTESIS_CIERRE cuerpo
                 | IF PARENTESIS_APERTURA condicion PARENTESIS_CIERRE cuerpo ELSE cuerpo
    '''
    if len(p) == 6:
        p[0] = ('sentencia_if', p[3], p[5])
    else:
        p[0] = ('sentencia_if_else', p[3], p[5], p[7])

def p_condicion(p):
    '''
    condicion : condicion AND_LOGICO condicion
              | condicion OR_LOGICO condicion
              | NOT condicion
              | PARENTESIS_APERTURA condicion PARENTESIS_CIERRE
              | exp op_relacional exp
    '''
    if len(p) == 4:
        if p[2] == '&&':
            p[0] = ('and', p[1], p[3])
        elif p[2] == '||':
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
    '''
    p[0] = p[1]

def p_exp(p):
    '''
    exp : NUMERO
        | ID
    '''
    p[0] = p[1]

def p_cuerpo(p):
    '''
    cuerpo : LLAVE_APERTURA declaraciones LLAVE_CIERRE
    '''
    p[0] = p[2]

def p_declaraciones(p):
    '''
    declaraciones : declaraciones declaracion
                  | declaracion
    '''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_declaracion(p):
    '''
    declaracion : declaracion_asignar
                | sentencia_if
    '''
    p[0] = p[1]

def p_declaracion_asignar(p):
    '''
    declaracion_asignar : ID ASIGNAR exp PUNTOCOMA
    '''
    p[0] = (p[1], '=', p[3])

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
    input_data = 'if (x > 5) { y = 10; } else { y = 20; }'

    # Llama a la función de prueba sintáctica y obtiene el resultado
    resultado = prueba_sintactica(input_data)

    # Imprime el resultado del análisis sintáctico
    for linea in resultado:
        print(linea)
