import ply.lex as lex

# Tabla de hash para palabras reservadas
palabras_reservadas = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'switch': 'SWITCH',
    'fun': 'FUN',
    'for': 'FOR',
    'bring': 'BRING',
    'try': 'TRY',
    'catch': 'CATCH',
    'void': 'VOID',
    'class': 'CLASS',
    'const': 'CONST',
    'return': 'RETURN',
    'init': 'INIT',
    'degree': 'DEGREE',
    'time': 'TIME',
    'distance': 'DISTANCE',
    'temp': 'TEMP',
    'bool': 'BOOL',
    'state': 'STATE',
    'any': 'ANY',
    'or': 'OR',
    'not': 'NOT',
    'and': 'AND',
    'var': 'VAR'
}

# Lista de tokens
tokens = [
    'ID', 'PARENTESIS_APERTURA', 'PARENTESIS_CIERRE', 'LLAVE_APERTURA', 'LLAVE_CIERRE',
    'CORCHETE_APERTURA', 'CORCHETE_CIERRE', 'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION',
    'MODULO', 'POTENCIA', 'MENORQUE', 'MAYORQUE', 'IGUAL', 'MENORIGUAL', 'MAYORIGUAL',
    'ASIGNAR', 'PUNTOCOMA', 'COMA', 'COMILLAS_SIMPLES', 'COMILLAS_DOBLES', 'DOSPUNTOS',
    'PUNTO', 'NUMERO', 'CADENA', 'GRADOS', 'SIMGRADOS', 'REAL', 'AND_LOGICO', 'OR_LOGICO',
    'INCREMENTO', 'DECREMENTO'
] + list(palabras_reservadas.values())

# Expresiones regulares para identificar los caracteres en el código
t_PARENTESIS_APERTURA = r'\('
t_PARENTESIS_CIERRE = r'\)'
t_LLAVE_APERTURA = r'\{'
t_LLAVE_CIERRE = r'\}'
t_CORCHETE_APERTURA = r'\['
t_CORCHETE_CIERRE = r'\]'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'
t_POTENCIA = r'\^'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_IGUAL = r'=='
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_AND_LOGICO = r'&&'
t_OR_LOGICO = r'\|\|'
t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'--'
t_PUNTOCOMA = r';'
t_COMA = r','
t_ASIGNAR = r'='
t_ignore = ' \t'

# Manejo de comentarios
def t_COMENTARIO_LINEA(t):
    r'//.*'
    pass  # Ignorar comentarios de una sola línea

def t_COMENTARIO_BLOQUE(t):
    r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/'
    t.lexer.lineno += t.value.count('\n')
    pass  # Ignorar comentarios de múltiples líneas

# Métodos para iniciar la tokenización
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palabras_reservadas.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_GRADOS(t):
    r'(\d{1,3})°\*(\d{1,2})\'\*(\d{1,2})"'
    return t

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  # Remover las comillas
    return t

errores = []

def t_error(t):
    mensaje_error = f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}, columna {t.lexpos}"
    errores.append(mensaje_error)
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

def find_column(input, token):
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = -1
    return token.lexpos - last_cr

def analisis(cadena):
    lexer.input(cadena)  # Introducir la cadena de entrada al lexer
    tokens = []
    for tok in lexer:
        columna = find_column(cadena, tok)
        tokens.append((tok.value, tok.type, tok.lineno, columna))
    return tokens

if __name__ == '__main__':
    codigo = 'x==5;'
    resultado =analisis(codigo)
    print(resultado)
    if errores:
        print("Errores encontrados:")
        for error in errores:
            print(error)
