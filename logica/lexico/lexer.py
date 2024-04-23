from typing import List
import ply.lex as lex

tokens = [
    'ID',
    'PARENTESIS_A',
    'PARENTESIS_C',
    'LLAVE_A',
    'LLAVE_C',
    'IF_token',
    'ELSE_token',
    'WHILE_token',
    'SWITCH_token',
    'FUN_token',
    'FOR_token',
    'BRING_token',
    'TRY_token',
    'CATCH_token',
    'VOID_token',
    'CLASS_token',
    'CONST_token',
    'RETURN_token',
    'INIT_token',
    'DEGREE_token',
    'TIME_token',
    'DISTANCE_token',
    'TEMP_token',
    'BOOL_token',
    'STATE_TOKEN',
    'ANY_token',
    'OR_token',
    'NOT_token',
    'AND_token',
    'RETURN_token',
    'POTENCIA',
    'CORIZQ',
    'CORDER',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'MODULO',
    'ASIGNAR',
    'MENORQUE',
    'MAYORQUE',
    'PUNTOCOMA',
    'COMA'
],


reservadas = [
    'if',
    'else', 
    'while',
    'switch',
    'fun',
    'for',
    'bring',
    'try',
    'catch',
    'void',
    'class',
    'const',
    'return',
    'init',
    'degree',
    'time',
    'distance',
    'temp',
    'bool',
    'state',
    'any',
    'or',
    'not',
    'and',
    'return'
]

t_PARENTESIS_A = r"\("
t_PARENTESIS_C = r"\)"
t_LLAVE_A = r"\{"
t_LLAVE_C = r"\}"
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_SUMA = r"\+"
t_RESTA = r"\-"
t_MULT = r'\*'
t_DIV = r'\/'
t_MODULO = r'\%'
t_POTENCIA = r'\^'
t_ASIGNAR = r'='
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = ';'
t_COMA = r','


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reservadas:
        t.type = t.value.upper() + '_token'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CADENA(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t


def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

t_ignore = ' \t'

lexer = lex.lex()

def analisis(cadena):
    lexer.input(cadena)
    tokens = []

    for tok in lexer:
        columna =  tok.lexpos - cadena.rfind('\n',0,tok.lexpos)
        tokens.append((tok.value, tok.type, tok.lineno, columna))
    return tokens

if __name__ == '__main__':
    codigo = '() carlos if switch'
    print(analisis(codigo))
