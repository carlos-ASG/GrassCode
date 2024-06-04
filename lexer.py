from re import T
import ply.lex as lex

# Tabla de hash para palabras reservadas
palabras_reservadas = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'fun': 'FUN',
    'for': 'FOR',
    'bring': 'BRING',
    'try': 'TRY',
    'catch': 'CATCH',
    'void': 'VOID',
    'const': 'CONST',
    'return': 'RETURN',
    'init': 'INIT',
    'or': 'OR',
    'not': 'NOT',
    'True': 'TRUE',
    'False': 'FALSE',
    'and': 'AND',
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOL',
}

# Lista de tokens
tokens = [
    'ID', 'PARENTESIS_APERTURA', 'PARENTESIS_CIERRE', 'LLAVE_APERTURA', 'LLAVE_CIERRE',
    'CORCHETE_APERTURA', 'CORCHETE_CIERRE', 'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION',
    'MODULO', 'MENORQUE', 'MAYORQUE', 'IGUAL','DIFERENTE', 'MENORIGUAL', 'MAYORIGUAL',
    'ASIGNAR', 'PUNTOCOMA', 'COMA', 'DOSPUNTOS','MASIGUAL','MENOSIGUAL','DIVIGUAL','MULTIGUAL',
    'PUNTO', 'NUMERO','MODULO'
    'INCREMENTO','ENTERO'
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
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_PUNTOCOMA = r';'
t_COMA = r','
t_ASIGNAR = r'='
t_MASIGUAL = r'\+='
t_MENOSIGUAL = r'-='
t_MULTIGUAL = r'\*='
t_DIVIGUAL = r'\\='
t_DOSPUNTOS = r':'
t_PUNTO = r'\.'
t_ignore = ' \t'

# Expresiones regulares para tipos de datos personalizados

# Expresiones regulares para operadores lógicos
t_AND = r'\band\b'
t_OR = r'\bor\b'
t_NOT = r'\bnot\b'

# Manejo de comentarios
def t_COMENTARIO_LINEA(t):
    r'//.*'
    t.lexer.lineno += t.value.count('\n')
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
    
def t_NUMERO(t):
    r'[-]?\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'[-]?\d+'
    t.value = int(t.value)
    return t

errores = []

def t_error(t):
    mensaje_error = f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}, columna {find_column(t.lexer.lexdata, t)}"
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
        tokens.append({'value':tok.value, 'type':tok.type, 'line':tok.lineno, 'column':columna})
    return tokens, errores

if __name__ == '__main__':
    codigo = 'x==5;'
    resultado = analisis(codigo)
    print(resultado)
    if errores:
        print("Errores encontrados:")
        for error in errores:
            print(error)
