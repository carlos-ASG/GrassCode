
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AND_LOGICO ANY ASIGNAR BOOL BRING CADENA CATCH CLASS COMA COMILLAS_DOBLES COMILLAS_SIMPLES CONST CORCHETE_APERTURA CORCHETE_CIERRE DECREMENTO DEGREE DIFERENTE DISTANCE DIVISION DOSPUNTOS ELSE FOR FUN GRADOS ID IF IGUAL INCREMENTO INIT LLAVE_APERTURA LLAVE_CIERRE MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MODULO MULTIPLICACION NOT NUMERO OR OR_LOGICO PARENTESIS_APERTURA PARENTESIS_CIERRE POTENCIA PUNTO PUNTOCOMA REAL RESTA RETURN SIMGRADOS STATE SUMA SWITCH TEMP TIME TRY VAR VOID WHILEimportacion : BRING ID PUNTOCOMAprograma : importacion programa\n                | funcion programa\n                | importacion\n                | funcionfunciones : funcion funciones\n                 | funcionfuncion : FUN ID PARENTESIS_APERTURA parametros_declaracion PARENTESIS_CIERRE cuerpoargumentos : expresion\n                  | expresion COMA argumentos\n                  | emptyparametros_declaracion : tipo_dato ID\n                              | tipo_dato ID COMA parametros_declaracion\n                              | emptysentencia_if : IF PARENTESIS_APERTURA expresion PARENTESIS_CIERRE cuerpo\n                    | IF PARENTESIS_APERTURA expresion PARENTESIS_CIERRE cuerpo ELSE cuerposentencia_while : WHILE PARENTESIS_APERTURA expresion PARENTESIS_CIERRE cuerposentencia_for : FOR PARENTESIS_APERTURA declaracion_variable PUNTOCOMA expresion PUNTOCOMA expresion PARENTESIS_CIERRE cuerpo\n    condicion : condicion AND condicion\n              | condicion OR condicion\n              | NOT condicion\n              | PARENTESIS_APERTURA condicion PARENTESIS_CIERRE\n              | exp op_relacional exp\n    \n    op_relacional : MENORQUE\n                  | MAYORQUE\n                  | IGUAL\n                  | MENORIGUAL\n                  | MAYORIGUAL\n                  | DIFERENTE\n    \n    exp : exp op_aritmetico exp\n        | PARENTESIS_APERTURA exp PARENTESIS_CIERRE\n        | ID\n        | dato\n    \n    op_aritmetico : SUMA\n                  | RESTA\n                  | MULTIPLICACION\n                  | DIVISION\n    \n    dato : NUMERO\n         | CADENA\n         | DEGREE\n         | TIME\n         | DISTANCE\n         | TEMP\n         | STATE\n         | ANY\n    cuerpo : LLAVE_APERTURA sentencias LLAVE_CIERREsentencias : sentencia sentencias\n                  | sentenciasentencia : declaracion_variable\n                 | asignacion\n                 | estructura_control\n                 | llamada_funcion\n                 | retorno\n                 | expresion PUNTOCOMAdeclaracion_variable : tipo_dato ID ASIGNAR expresion PUNTOCOMA\n                            | tipo_dato ID PUNTOCOMAasignacion : ID ASIGNAR expresion PUNTOCOMA\n    tipo_dato : DEGREE\n              | TIME\n              | DISTANCE\n              | TEMP\n              | BOOL\n              | STATE\n              | ANY\n    llamada_funcion : ID PARENTESIS_APERTURA argumentos PARENTESIS_CIERRE PUNTOCOMAestructura_control : sentencia_if\n                          | sentencia_for\n                          | sentencia_whileretorno : RETURN expresion PUNTOCOMAexpresion : expresion_logica\n                 | expresion_logica operador_logico expresionexpresion_logica : expresion_relacional\n                        | expresion_relacional operador_relacional expresion_logicaexpresion_relacional : expresion_aritmetica\n                            | expresion_aritmetica operador_relacional expresion_relacionalexpresion_aritmetica : termino\n                            | termino operador_aritmetico expresion_aritmeticatermino : factor\n               | factor operador_termino terminofactor : ID\n              | llamada_funcion\n              | NUMERO\n              | CADENA\n              | PARENTESIS_APERTURA expresion PARENTESIS_CIERREoperador_logico : AND\n                       | ORoperador_relacional : MENORQUE\n                           | MAYORQUE\n                          | IGUAL\n                          | MENORIGUAL\n                          | MAYORIGUAL\n                          | DIFERENTEoperador_aritmetico : SUMA\n                           | RESTA\n                           | MULTIPLICACION\n                           | DIVISIONoperador_termino : MULTIPLICACION\n                        | DIVISION\n                        | MODULOempty :'
    
_lr_action_items = {'BRING':([0,],[2,]),'$end':([1,4,],[0,-1,]),'ID':([2,],[3,]),'PUNTOCOMA':([3,],[4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'importacion':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> importacion","S'",1,None,None,None),
  ('importacion -> BRING ID PUNTOCOMA','importacion',3,'p_importacion','sintactico.py',6),
  ('programa -> importacion programa','programa',2,'p_programa','sintactico.py',10),
  ('programa -> funcion programa','programa',2,'p_programa','sintactico.py',11),
  ('programa -> importacion','programa',1,'p_programa','sintactico.py',12),
  ('programa -> funcion','programa',1,'p_programa','sintactico.py',13),
  ('funciones -> funcion funciones','funciones',2,'p_funciones','sintactico.py',20),
  ('funciones -> funcion','funciones',1,'p_funciones','sintactico.py',21),
  ('funcion -> FUN ID PARENTESIS_APERTURA parametros_declaracion PARENTESIS_CIERRE cuerpo','funcion',6,'p_funcion','sintactico.py',28),
  ('argumentos -> expresion','argumentos',1,'p_argumentos','sintactico.py',32),
  ('argumentos -> expresion COMA argumentos','argumentos',3,'p_argumentos','sintactico.py',33),
  ('argumentos -> empty','argumentos',1,'p_argumentos','sintactico.py',34),
  ('parametros_declaracion -> tipo_dato ID','parametros_declaracion',2,'p_parametros_declaracion','sintactico.py',43),
  ('parametros_declaracion -> tipo_dato ID COMA parametros_declaracion','parametros_declaracion',4,'p_parametros_declaracion','sintactico.py',44),
  ('parametros_declaracion -> empty','parametros_declaracion',1,'p_parametros_declaracion','sintactico.py',45),
  ('sentencia_if -> IF PARENTESIS_APERTURA expresion PARENTESIS_CIERRE cuerpo','sentencia_if',5,'p_sentencia_if','sintactico.py',54),
  ('sentencia_if -> IF PARENTESIS_APERTURA expresion PARENTESIS_CIERRE cuerpo ELSE cuerpo','sentencia_if',7,'p_sentencia_if','sintactico.py',55),
  ('sentencia_while -> WHILE PARENTESIS_APERTURA expresion PARENTESIS_CIERRE cuerpo','sentencia_while',5,'p_sentencia_while','sintactico.py',62),
  ('sentencia_for -> FOR PARENTESIS_APERTURA declaracion_variable PUNTOCOMA expresion PUNTOCOMA expresion PARENTESIS_CIERRE cuerpo','sentencia_for',9,'p_sentencia_for','sintactico.py',66),
  ('condicion -> condicion AND condicion','condicion',3,'p_condicion','sintactico.py',71),
  ('condicion -> condicion OR condicion','condicion',3,'p_condicion','sintactico.py',72),
  ('condicion -> NOT condicion','condicion',2,'p_condicion','sintactico.py',73),
  ('condicion -> PARENTESIS_APERTURA condicion PARENTESIS_CIERRE','condicion',3,'p_condicion','sintactico.py',74),
  ('condicion -> exp op_relacional exp','condicion',3,'p_condicion','sintactico.py',75),
  ('op_relacional -> MENORQUE','op_relacional',1,'p_op_relacional','sintactico.py',91),
  ('op_relacional -> MAYORQUE','op_relacional',1,'p_op_relacional','sintactico.py',92),
  ('op_relacional -> IGUAL','op_relacional',1,'p_op_relacional','sintactico.py',93),
  ('op_relacional -> MENORIGUAL','op_relacional',1,'p_op_relacional','sintactico.py',94),
  ('op_relacional -> MAYORIGUAL','op_relacional',1,'p_op_relacional','sintactico.py',95),
  ('op_relacional -> DIFERENTE','op_relacional',1,'p_op_relacional','sintactico.py',96),
  ('exp -> exp op_aritmetico exp','exp',3,'p_exp','sintactico.py',102),
  ('exp -> PARENTESIS_APERTURA exp PARENTESIS_CIERRE','exp',3,'p_exp','sintactico.py',103),
  ('exp -> ID','exp',1,'p_exp','sintactico.py',104),
  ('exp -> dato','exp',1,'p_exp','sintactico.py',105),
  ('op_aritmetico -> SUMA','op_aritmetico',1,'p_op_aritmetico','sintactico.py',116),
  ('op_aritmetico -> RESTA','op_aritmetico',1,'p_op_aritmetico','sintactico.py',117),
  ('op_aritmetico -> MULTIPLICACION','op_aritmetico',1,'p_op_aritmetico','sintactico.py',118),
  ('op_aritmetico -> DIVISION','op_aritmetico',1,'p_op_aritmetico','sintactico.py',119),
  ('dato -> NUMERO','dato',1,'p_dato','sintactico.py',125),
  ('dato -> CADENA','dato',1,'p_dato','sintactico.py',126),
  ('dato -> DEGREE','dato',1,'p_dato','sintactico.py',127),
  ('dato -> TIME','dato',1,'p_dato','sintactico.py',128),
  ('dato -> DISTANCE','dato',1,'p_dato','sintactico.py',129),
  ('dato -> TEMP','dato',1,'p_dato','sintactico.py',130),
  ('dato -> STATE','dato',1,'p_dato','sintactico.py',131),
  ('dato -> ANY','dato',1,'p_dato','sintactico.py',132),
  ('cuerpo -> LLAVE_APERTURA sentencias LLAVE_CIERRE','cuerpo',3,'p_cuerpo','sintactico.py',137),
  ('sentencias -> sentencia sentencias','sentencias',2,'p_sentencias','sintactico.py',141),
  ('sentencias -> sentencia','sentencias',1,'p_sentencias','sintactico.py',142),
  ('sentencia -> declaracion_variable','sentencia',1,'p_sentencia','sintactico.py',149),
  ('sentencia -> asignacion','sentencia',1,'p_sentencia','sintactico.py',150),
  ('sentencia -> estructura_control','sentencia',1,'p_sentencia','sintactico.py',151),
  ('sentencia -> llamada_funcion','sentencia',1,'p_sentencia','sintactico.py',152),
  ('sentencia -> retorno','sentencia',1,'p_sentencia','sintactico.py',153),
  ('sentencia -> expresion PUNTOCOMA','sentencia',2,'p_sentencia','sintactico.py',154),
  ('declaracion_variable -> tipo_dato ID ASIGNAR expresion PUNTOCOMA','declaracion_variable',5,'p_declaracion_variable','sintactico.py',158),
  ('declaracion_variable -> tipo_dato ID PUNTOCOMA','declaracion_variable',3,'p_declaracion_variable','sintactico.py',159),
  ('asignacion -> ID ASIGNAR expresion PUNTOCOMA','asignacion',4,'p_asignacion','sintactico.py',168),
  ('tipo_dato -> DEGREE','tipo_dato',1,'p_tipo_dato','sintactico.py',173),
  ('tipo_dato -> TIME','tipo_dato',1,'p_tipo_dato','sintactico.py',174),
  ('tipo_dato -> DISTANCE','tipo_dato',1,'p_tipo_dato','sintactico.py',175),
  ('tipo_dato -> TEMP','tipo_dato',1,'p_tipo_dato','sintactico.py',176),
  ('tipo_dato -> BOOL','tipo_dato',1,'p_tipo_dato','sintactico.py',177),
  ('tipo_dato -> STATE','tipo_dato',1,'p_tipo_dato','sintactico.py',178),
  ('tipo_dato -> ANY','tipo_dato',1,'p_tipo_dato','sintactico.py',179),
  ('llamada_funcion -> ID PARENTESIS_APERTURA argumentos PARENTESIS_CIERRE PUNTOCOMA','llamada_funcion',5,'p_llamada_funcion','sintactico.py',184),
  ('estructura_control -> sentencia_if','estructura_control',1,'p_estructura_control','sintactico.py',188),
  ('estructura_control -> sentencia_for','estructura_control',1,'p_estructura_control','sintactico.py',189),
  ('estructura_control -> sentencia_while','estructura_control',1,'p_estructura_control','sintactico.py',190),
  ('retorno -> RETURN expresion PUNTOCOMA','retorno',3,'p_retorno','sintactico.py',194),
  ('expresion -> expresion_logica','expresion',1,'p_expresion','sintactico.py',198),
  ('expresion -> expresion_logica operador_logico expresion','expresion',3,'p_expresion','sintactico.py',199),
  ('expresion_logica -> expresion_relacional','expresion_logica',1,'p_expresion_logica','sintactico.py',206),
  ('expresion_logica -> expresion_relacional operador_relacional expresion_logica','expresion_logica',3,'p_expresion_logica','sintactico.py',207),
  ('expresion_relacional -> expresion_aritmetica','expresion_relacional',1,'p_expresion_relacional','sintactico.py',214),
  ('expresion_relacional -> expresion_aritmetica operador_relacional expresion_relacional','expresion_relacional',3,'p_expresion_relacional','sintactico.py',215),
  ('expresion_aritmetica -> termino','expresion_aritmetica',1,'p_expresion_aritmetica','sintactico.py',222),
  ('expresion_aritmetica -> termino operador_aritmetico expresion_aritmetica','expresion_aritmetica',3,'p_expresion_aritmetica','sintactico.py',223),
  ('termino -> factor','termino',1,'p_termino','sintactico.py',230),
  ('termino -> factor operador_termino termino','termino',3,'p_termino','sintactico.py',231),
  ('factor -> ID','factor',1,'p_factor','sintactico.py',238),
  ('factor -> llamada_funcion','factor',1,'p_factor','sintactico.py',239),
  ('factor -> NUMERO','factor',1,'p_factor','sintactico.py',240),
  ('factor -> CADENA','factor',1,'p_factor','sintactico.py',241),
  ('factor -> PARENTESIS_APERTURA expresion PARENTESIS_CIERRE','factor',3,'p_factor','sintactico.py',242),
  ('operador_logico -> AND','operador_logico',1,'p_operador_logico','sintactico.py',249),
  ('operador_logico -> OR','operador_logico',1,'p_operador_logico','sintactico.py',250),
  ('operador_relacional -> MENORQUE','operador_relacional',1,'p_operador_relacional','sintactico.py',254),
  ('operador_relacional -> MAYORQUE','operador_relacional',1,'p_operador_relacional','sintactico.py',255),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','sintactico.py',256),
  ('operador_relacional -> MENORIGUAL','operador_relacional',1,'p_operador_relacional','sintactico.py',257),
  ('operador_relacional -> MAYORIGUAL','operador_relacional',1,'p_operador_relacional','sintactico.py',258),
  ('operador_relacional -> DIFERENTE','operador_relacional',1,'p_operador_relacional','sintactico.py',259),
  ('operador_aritmetico -> SUMA','operador_aritmetico',1,'p_operador_aritmetico','sintactico.py',263),
  ('operador_aritmetico -> RESTA','operador_aritmetico',1,'p_operador_aritmetico','sintactico.py',264),
  ('operador_aritmetico -> MULTIPLICACION','operador_aritmetico',1,'p_operador_aritmetico','sintactico.py',265),
  ('operador_aritmetico -> DIVISION','operador_aritmetico',1,'p_operador_aritmetico','sintactico.py',266),
  ('operador_termino -> MULTIPLICACION','operador_termino',1,'p_operador_termino','sintactico.py',270),
  ('operador_termino -> DIVISION','operador_termino',1,'p_operador_termino','sintactico.py',271),
  ('operador_termino -> MODULO','operador_termino',1,'p_operador_termino','sintactico.py',272),
  ('empty -> <empty>','empty',0,'p_empty','sintactico.py',276),
]
