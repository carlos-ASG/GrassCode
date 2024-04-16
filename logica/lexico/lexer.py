from typing import List
import ply.lex as lex

tokens = [
    'ID',
    'PARENTESIS_A',
    'PARENTESIS_C',
    'LLAVE_A',
    'LLAVE_C',
    'IF_token',
    'WHILE_token',
]

t_PARENTESIS_A = r"\("
t_PARENTESIS_C = r"\)"
t_LLAVE_A = r"\{"
t_LLAVE_C = r"\}"

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in ['if', 'while']:
        t.type = t.value.upper() + '_token'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

# Move this line to here
lexer = lex.lex()

def analisis(cadena):
    lexer.input(cadena)
    tokens = []

    for tok in lexer:
        columna =  tok.lexpos - cadena.rfind('\n',0,tok.lexpos)
        tokens.append((tok.value, tok.type, tok.lineno, columna))
    return tokens

if __name__ == '__main__':
    codigo = r'(){} carlos'
    print(analisis(codigo))
