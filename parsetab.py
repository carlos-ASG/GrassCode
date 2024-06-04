
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSUMARESTAleftMULTIPLICACIONDIVISIONAND ASIGNAR BOOL BRING CATCH COMA CONST CORCHETE_APERTURA CORCHETE_CIERRE DIFERENTE DIVISION DOSPUNTOS ELSE ENTERO FALSE FLOAT FOR FUN ID IF IGUAL INIT INT LLAVE_APERTURA LLAVE_CIERRE MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MODULO MODULOINCREMENTO MULTIPLICACION NOT NUMERO OR PARENTESIS_APERTURA PARENTESIS_CIERRE PUNTO PUNTOCOMA RESTA RETURN SUMA TRUE TRY VOID WHILE\n    statements : statement\n               | statement statements\n               | empty\n    \n    statement : fun_statement\n              | variable_declaration\n              | assignment\n              | if_statement\n              | for_statement\n              | call_fun\n              | import\n              | empty\n    \n    import : BRING ID PUNTOCOMA\n    \n    fun_statement : FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE\n    \n    fun_statement : ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE\n    \n    fun_statement : FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE\n    \n    fun_statement : FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements\n    \n    fun_statement : FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype statements LLAVE_CIERRE\n    \n    fun_statement : FUN PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE\n    \n    fun_statement : FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS LLAVE_APERTURA statements LLAVE_CIERRE\n    \n    fun_statement : FUN ID parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE\n    \n    fun_statement : FUN ID PARENTESIS_APERTURA parameters DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE\n    \n    fun_statement : FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE datatype LLAVE_APERTURA statements LLAVE_CIERRE\n    \n    if_statement : IF PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE\n                 | IF PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE ELSE LLAVE_APERTURA statements LLAVE_CIERRE\n    \n    for_statement : FOR PARENTESIS_APERTURA datatype ID ASIGNAR expression PUNTOCOMA condition PUNTOCOMA ID ASIGNAR expression PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE\n    \n    call_fun : ID PARENTESIS_APERTURA expression_list PARENTESIS_CIERRE PUNTOCOMA\n             | ID PUNTO ID PARENTESIS_APERTURA expression_list PARENTESIS_CIERRE PUNTOCOMA\n    \n    variable_declaration : datatype ID ASIGNAR expression PUNTOCOMA\n                         | datatype ID ASIGNAR condition PUNTOCOMA\n                         | datatype ID PUNTOCOMA\n                         | datatype CORCHETE_APERTURA CORCHETE_CIERRE ID ASIGNAR CORCHETE_APERTURA expression_list CORCHETE_CIERRE PUNTOCOMA\n                         | datatype CORCHETE_APERTURA CORCHETE_CIERRE ID ASIGNAR CORCHETE_APERTURA CORCHETE_CIERRE PUNTOCOMA\n    \n    assignment : ID ASIGNAR expression PUNTOCOMA\n    \n    expression_list : expression\n                    | expression COMA expression_list\n                    | empty\n    \n    condition : condition AND condition\n              | condition OR condition\n              | NOT condition\n              | condition MENORQUE condition\n              | condition MAYORQUE condition\n              | condition IGUAL condition\n              | condition DIFERENTE condition\n              | condition MENORIGUAL condition\n              | condition MAYORIGUAL condition\n              | PARENTESIS_APERTURA condition PARENTESIS_CIERRE\n              | boleano\n              | ID\n              | NUMERO\n              | ENTERO\n    \n    expression : ID\n               | NUMERO\n               | ENTERO\n               | expression SUMA expression\n               | expression RESTA expression\n               | expression MULTIPLICACION expression\n               | expression DIVISION expression\n               | expression MODULO expression\n               | PARENTESIS_APERTURA expression PARENTESIS_CIERRE\n    \n    parameters : datatype ID\n               | datatype ID COMA parameters\n               | empty\n    \n    datatype : VOID\n             | FLOAT\n             | INT\n             | BOOL\n    \n    boleano : TRUE\n            | FALSE\n    \n    empty :\n    '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,21,48,60,74,102,111,112,145,148,150,154,159,163,164,165,166,167,168,169,170,171,174,177,183,],[-69,0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-30,-12,-33,-26,-28,-29,-27,-23,-69,-15,-32,-16,-17,-19,-22,-21,-20,-18,-14,-31,-13,-24,-25,]),'FUN':([0,2,3,4,5,6,7,8,9,10,17,18,19,20,21,48,60,74,102,111,112,115,127,137,138,139,141,142,143,144,145,148,150,154,159,163,164,165,166,167,168,169,170,171,172,174,177,181,183,],[11,11,-3,-4,-5,-6,-7,-8,-9,-10,-63,-64,-65,-66,-2,-30,-12,-33,-26,-28,-29,11,11,11,11,11,11,11,11,11,-27,-23,11,-15,-32,-16,-17,-19,-22,-21,-20,-18,-14,-31,11,-13,-24,11,-25,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,21,24,25,26,29,34,38,47,48,49,50,52,59,60,68,69,70,71,72,73,74,75,81,85,86,87,88,89,90,91,92,102,111,112,115,124,127,134,137,138,139,141,142,143,144,145,148,149,150,154,159,163,164,165,166,167,168,169,170,171,172,173,174,177,178,181,183,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,22,27,31,-63,-64,-65,-66,-2,37,37,46,54,63,37,76,-30,82,54,54,94,-12,37,37,37,37,37,37,-33,37,76,54,54,54,54,54,54,54,54,-26,-28,-29,12,37,12,37,12,12,12,12,12,12,12,-27,-23,54,12,-15,-32,-16,-17,-19,-22,-21,-20,-18,-14,-31,12,176,-13,-24,37,12,-25,]),'IF':([0,2,3,4,5,6,7,8,9,10,17,18,19,20,21,48,60,74,102,111,112,115,127,137,138,139,141,142,143,144,145,148,150,154,159,163,164,165,166,167,168,169,170,171,172,174,177,181,183,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-63,-64,-65,-66,-2,-30,-12,-33,-26,-28,-29,14,14,14,14,14,14,14,14,14,-27,-23,14,-15,-32,-16,-17,-19,-22,-21,-20,-18,-14,-31,14,-13,-24,14,-25,]),'FOR':([0,2,3,4,5,6,7,8,9,10,17,18,19,20,21,48,60,74,102,111,112,115,127,137,138,139,141,142,143,144,145,148,150,154,159,163,164,165,166,167,168,169,170,171,172,174,177,181,183,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-63,-64,-65,-66,-2,-30,-12,-33,-26,-28,-29,15,15,15,15,15,15,15,15,15,-27,-23,15,-15,-32,-16,-17,-19,-22,-21,-20,-18,-14,-31,15,-13,-24,15,-25,]),'BRING':([0,2,3,4,5,6,7,8,9,10,17,18,19,20,21,48,60,74,102,111,112,115,127,137,138,139,141,142,143,144,145,148,150,154,159,163,164,165,166,167,168,169,170,171,172,174,177,181,183,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-63,-64,-65,-66,-2,-30,-12,-33,-26,-28,-29,16,16,16,16,16,16,16,16,16,-27,-23,16,-15,-32,-16,-17,-19,-22,-21,-20,-18,-14,-31,16,-13,-24,16,-25,]),'VOID':([0,2,3,4,5,6,7,8,9,10,17,18,19,20,21,22,23,24,30,32,48,60,74,95,96,97,98,99,101,102,111,112,115,125,127,137,138,139,141,142,143,144,145,148,150,154,159,163,164,165,166,167,168,169,170,171,172,174,177,181,183,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-63,-64,-65,-66,-2,17,17,17,17,17,-30,-12,-33,17,17,17,17,17,17,-26,-28,-29,17,17,17,17,17,17,17,17,17,17,-27,-23,17,-15,-32,-16,-17,-19,-22,-21,-20,-18,-14,-31,17,-13,-24,17,-25,]),'FLOAT':([0,2,3,4,5,6,7,8,9,10,17,18,19,20,21,22,23,24,30,32,48,60,74,95,96,97,98,99,101,102,111,112,115,125,127,137,138,139,141,142,143,144,145,148,150,154,159,163,164,165,166,167,168,169,170,171,172,174,177,181,183,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-63,-64,-65,-66,-2,18,18,18,18,18,-30,-12,-33,18,18,18,18,18,18,-26,-28,-29,18,18,18,18,18,18,18,18,18,18,-27,-23,18,-15,-32,-16,-17,-19,-22,-21,-20,-18,-14,-31,18,-13,-24,18,-25,]),'INT':([0,2,3,4,5,6,7,8,9,10,17,18,19,20,21,22,23,24,30,32,48,60,74,95,96,97,98,99,101,102,111,112,115,125,127,137,138,139,141,142,143,144,145,148,150,154,159,163,164,165,166,167,168,169,170,171,172,174,177,181,183,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-63,-64,-65,-66,-2,19,19,19,19,19,-30,-12,-33,19,19,19,19,19,19,-26,-28,-29,19,19,19,19,19,19,19,19,19,19,-27,-23,19,-15,-32,-16,-17,-19,-22,-21,-20,-18,-14,-31,19,-13,-24,19,-25,]),'BOOL':([0,2,3,4,5,6,7,8,9,10,17,18,19,20,21,22,23,24,30,32,48,60,74,95,96,97,98,99,101,102,111,112,115,125,127,137,138,139,141,142,143,144,145,148,150,154,159,163,164,165,166,167,168,169,170,171,172,174,177,181,183,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-63,-64,-65,-66,-2,20,20,20,20,20,-30,-12,-33,20,20,20,20,20,20,-26,-28,-29,20,20,20,20,20,20,20,20,20,20,-27,-23,20,-15,-32,-16,-17,-19,-22,-21,-20,-18,-14,-31,20,-13,-24,20,-25,]),'LLAVE_CIERRE':([2,3,4,5,6,7,8,9,10,17,18,19,20,21,48,60,74,102,111,112,115,127,135,137,138,139,140,141,142,143,144,145,148,150,151,152,153,154,155,156,157,158,159,163,164,165,166,167,168,169,170,171,172,174,175,177,181,182,183,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-63,-64,-65,-66,-2,-30,-12,-33,-26,-28,-29,-69,-69,148,-69,-69,-69,154,-69,-69,-69,-69,-27,-23,-69,164,165,166,-15,167,168,169,170,-32,174,-17,-19,-22,-21,-20,-18,-14,-31,-69,-13,177,-24,-69,183,-25,]),'PARENTESIS_APERTURA':([11,12,14,15,22,24,25,29,38,46,47,50,52,68,69,70,71,72,73,75,81,85,86,87,88,89,90,91,92,124,134,149,178,],[23,24,29,30,32,38,38,50,38,75,81,50,50,38,38,38,38,38,38,38,81,50,50,50,50,50,50,50,50,38,38,50,38,]),'ASIGNAR':([12,27,82,94,176,],[25,47,113,124,178,]),'PUNTO':([12,],[26,]),'CORCHETE_APERTURA':([13,17,18,19,20,113,],[28,-63,-64,-65,-66,134,]),'LLAVE_APERTURA':([17,18,19,20,84,95,125,126,128,129,131,132,137,161,180,],[-63,-64,-65,-66,115,127,138,139,141,142,143,144,150,172,181,]),'PARENTESIS_CIERRE':([22,23,24,32,33,35,36,37,39,40,41,42,43,44,51,53,54,55,56,57,58,61,63,65,68,75,76,79,80,83,93,98,100,103,104,105,106,107,108,109,110,114,116,117,118,119,120,121,122,123,130,179,],[-69,-69,-69,-69,62,-62,64,-51,66,67,-36,-34,-52,-53,84,-47,-48,-49,-50,-67,-68,95,-60,100,-69,-69,-48,-49,-50,114,-39,-69,-59,-35,-36,-54,-55,-56,-57,-58,133,-46,-37,-38,-40,-41,-42,-43,-44,-45,-61,180,]),'NUMERO':([24,25,29,38,47,50,52,68,69,70,71,72,73,75,81,85,86,87,88,89,90,91,92,124,134,149,178,],[43,43,55,43,79,55,55,43,43,43,43,43,43,43,79,55,55,55,55,55,55,55,55,43,43,55,43,]),'ENTERO':([24,25,29,38,47,50,52,68,69,70,71,72,73,75,81,85,86,87,88,89,90,91,92,124,134,149,178,],[44,44,56,44,80,56,56,44,44,44,44,44,44,44,80,56,56,56,56,56,56,56,56,44,44,56,44,]),'PUNTOCOMA':([27,31,37,43,44,45,53,54,55,56,57,58,67,76,77,78,79,80,93,100,105,106,107,108,109,114,116,117,118,119,120,121,122,123,133,136,146,160,162,],[48,60,-51,-52,-53,74,-47,-48,-49,-50,-67,-68,102,-48,111,112,-49,-50,-39,-59,-54,-55,-56,-57,-58,-46,-37,-38,-40,-41,-42,-43,-44,-45,145,149,159,171,173,]),'CORCHETE_CIERRE':([28,37,42,43,44,68,100,103,104,105,106,107,108,109,134,147,],[49,-51,-34,-52,-53,-69,-59,-35,-36,-54,-55,-56,-57,-58,146,160,]),'NOT':([29,47,50,52,81,85,86,87,88,89,90,91,92,149,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'TRUE':([29,47,50,52,81,85,86,87,88,89,90,91,92,149,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'FALSE':([29,47,50,52,81,85,86,87,88,89,90,91,92,149,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'DOSPUNTOS':([32,35,61,62,63,64,66,95,98,130,],[-69,-62,96,97,-60,99,101,125,-69,-61,]),'COMA':([37,42,43,44,63,100,105,106,107,108,109,],[-51,68,-52,-53,98,-59,-54,-55,-56,-57,-58,]),'SUMA':([37,42,43,44,45,65,76,77,79,80,100,105,106,107,108,109,136,179,],[-51,69,-52,-53,69,69,-51,69,-52,-53,-59,-54,-55,-56,-57,69,69,69,]),'RESTA':([37,42,43,44,45,65,76,77,79,80,100,105,106,107,108,109,136,179,],[-51,70,-52,-53,70,70,-51,70,-52,-53,-59,-54,-55,-56,-57,70,70,70,]),'MULTIPLICACION':([37,42,43,44,45,65,76,77,79,80,100,105,106,107,108,109,136,179,],[-51,71,-52,-53,71,71,-51,71,-52,-53,-59,71,71,-56,-57,71,71,71,]),'DIVISION':([37,42,43,44,45,65,76,77,79,80,100,105,106,107,108,109,136,179,],[-51,72,-52,-53,72,72,-51,72,-52,-53,-59,72,72,-56,-57,72,72,72,]),'MODULO':([37,42,43,44,45,65,76,77,79,80,100,105,106,107,108,109,136,179,],[-51,73,-52,-53,73,73,-51,73,-52,-53,-59,-54,-55,-56,-57,73,73,73,]),'AND':([51,53,54,55,56,57,58,76,78,79,80,83,93,114,116,117,118,119,120,121,122,123,162,],[85,-47,-48,-49,-50,-67,-68,-48,85,-49,-50,85,85,-46,85,85,85,85,85,85,85,85,85,]),'OR':([51,53,54,55,56,57,58,76,78,79,80,83,93,114,116,117,118,119,120,121,122,123,162,],[86,-47,-48,-49,-50,-67,-68,-48,86,-49,-50,86,86,-46,86,86,86,86,86,86,86,86,86,]),'MENORQUE':([51,53,54,55,56,57,58,76,78,79,80,83,93,114,116,117,118,119,120,121,122,123,162,],[87,-47,-48,-49,-50,-67,-68,-48,87,-49,-50,87,87,-46,87,87,87,87,87,87,87,87,87,]),'MAYORQUE':([51,53,54,55,56,57,58,76,78,79,80,83,93,114,116,117,118,119,120,121,122,123,162,],[88,-47,-48,-49,-50,-67,-68,-48,88,-49,-50,88,88,-46,88,88,88,88,88,88,88,88,88,]),'IGUAL':([51,53,54,55,56,57,58,76,78,79,80,83,93,114,116,117,118,119,120,121,122,123,162,],[89,-47,-48,-49,-50,-67,-68,-48,89,-49,-50,89,89,-46,89,89,89,89,89,89,89,89,89,]),'DIFERENTE':([51,53,54,55,56,57,58,76,78,79,80,83,93,114,116,117,118,119,120,121,122,123,162,],[90,-47,-48,-49,-50,-67,-68,-48,90,-49,-50,90,90,-46,90,90,90,90,90,90,90,90,90,]),'MENORIGUAL':([51,53,54,55,56,57,58,76,78,79,80,83,93,114,116,117,118,119,120,121,122,123,162,],[91,-47,-48,-49,-50,-67,-68,-48,91,-49,-50,91,91,-46,91,91,91,91,91,91,91,91,91,]),'MAYORIGUAL':([51,53,54,55,56,57,58,76,78,79,80,83,93,114,116,117,118,119,120,121,122,123,162,],[92,-47,-48,-49,-50,-67,-68,-48,92,-49,-50,92,92,-46,92,92,92,92,92,92,92,92,92,]),'ELSE':([148,],[161,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,2,115,127,137,138,139,141,142,143,144,150,172,181,],[1,21,135,140,151,152,153,155,156,157,158,163,175,182,]),'statement':([0,2,115,127,137,138,139,141,142,143,144,150,172,181,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'empty':([0,2,22,23,24,32,68,75,98,115,127,134,137,138,139,141,142,143,144,150,172,181,],[3,3,35,35,41,35,104,104,35,3,3,104,3,3,3,3,3,3,3,3,3,3,]),'fun_statement':([0,2,115,127,137,138,139,141,142,143,144,150,172,181,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'variable_declaration':([0,2,115,127,137,138,139,141,142,143,144,150,172,181,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'assignment':([0,2,115,127,137,138,139,141,142,143,144,150,172,181,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'if_statement':([0,2,115,127,137,138,139,141,142,143,144,150,172,181,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'for_statement':([0,2,115,127,137,138,139,141,142,143,144,150,172,181,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'call_fun':([0,2,115,127,137,138,139,141,142,143,144,150,172,181,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'import':([0,2,115,127,137,138,139,141,142,143,144,150,172,181,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'datatype':([0,2,22,23,24,30,32,95,96,97,98,99,101,115,125,127,137,138,139,141,142,143,144,150,172,181,],[13,13,34,34,34,59,34,126,128,129,34,131,132,13,137,13,13,13,13,13,13,13,13,13,13,13,]),'parameters':([22,23,24,32,98,],[33,36,39,61,130,]),'expression_list':([24,68,75,134,],[40,103,110,147,]),'expression':([24,25,38,47,68,69,70,71,72,73,75,81,124,134,178,],[42,45,65,77,42,105,106,107,108,109,42,65,136,42,179,]),'condition':([29,47,50,52,81,85,86,87,88,89,90,91,92,149,],[51,78,83,93,83,116,117,118,119,120,121,122,123,162,]),'boleano':([29,47,50,52,81,85,86,87,88,89,90,91,92,149,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statement','statements',1,'p_statements','sintactico.py',90),
  ('statements -> statement statements','statements',2,'p_statements','sintactico.py',91),
  ('statements -> empty','statements',1,'p_statements','sintactico.py',92),
  ('statement -> fun_statement','statement',1,'p_statement','sintactico.py',108),
  ('statement -> variable_declaration','statement',1,'p_statement','sintactico.py',109),
  ('statement -> assignment','statement',1,'p_statement','sintactico.py',110),
  ('statement -> if_statement','statement',1,'p_statement','sintactico.py',111),
  ('statement -> for_statement','statement',1,'p_statement','sintactico.py',112),
  ('statement -> call_fun','statement',1,'p_statement','sintactico.py',113),
  ('statement -> import','statement',1,'p_statement','sintactico.py',114),
  ('statement -> empty','statement',1,'p_statement','sintactico.py',115),
  ('import -> BRING ID PUNTOCOMA','import',3,'p_import','sintactico.py',124),
  ('fun_statement -> FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE','fun_statement',10,'p_fun_statement','sintactico.py',138),
  ('fun_statement -> ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE','fun_statement',9,'p_fun_statement_error1','sintactico.py',147),
  ('fun_statement -> FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE','fun_statement',8,'p_fun_statement_error2','sintactico.py',155),
  ('fun_statement -> FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements','fun_statement',9,'p_fun_statement_error3','sintactico.py',163),
  ('fun_statement -> FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype statements LLAVE_CIERRE','fun_statement',9,'p_fun_statement_error4','sintactico.py',171),
  ('fun_statement -> FUN PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE','fun_statement',9,'p_fun_statement_error5','sintactico.py',179),
  ('fun_statement -> FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE DOSPUNTOS LLAVE_APERTURA statements LLAVE_CIERRE','fun_statement',9,'p_fun_statement_error6','sintactico.py',188),
  ('fun_statement -> FUN ID parameters PARENTESIS_CIERRE DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE','fun_statement',9,'p_fun_statement_error7','sintactico.py',196),
  ('fun_statement -> FUN ID PARENTESIS_APERTURA parameters DOSPUNTOS datatype LLAVE_APERTURA statements LLAVE_CIERRE','fun_statement',9,'p_fun_statement_error8','sintactico.py',204),
  ('fun_statement -> FUN ID PARENTESIS_APERTURA parameters PARENTESIS_CIERRE datatype LLAVE_APERTURA statements LLAVE_CIERRE','fun_statement',9,'p_fun_statement_error9','sintactico.py',212),
  ('if_statement -> IF PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE','if_statement',7,'p_if_statement','sintactico.py',222),
  ('if_statement -> IF PARENTESIS_APERTURA condition PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE ELSE LLAVE_APERTURA statements LLAVE_CIERRE','if_statement',11,'p_if_statement','sintactico.py',223),
  ('for_statement -> FOR PARENTESIS_APERTURA datatype ID ASIGNAR expression PUNTOCOMA condition PUNTOCOMA ID ASIGNAR expression PARENTESIS_CIERRE LLAVE_APERTURA statements LLAVE_CIERRE','for_statement',16,'p_for_statement','sintactico.py',236),
  ('call_fun -> ID PARENTESIS_APERTURA expression_list PARENTESIS_CIERRE PUNTOCOMA','call_fun',5,'p_call_fun','sintactico.py',243),
  ('call_fun -> ID PUNTO ID PARENTESIS_APERTURA expression_list PARENTESIS_CIERRE PUNTOCOMA','call_fun',7,'p_call_fun','sintactico.py',244),
  ('variable_declaration -> datatype ID ASIGNAR expression PUNTOCOMA','variable_declaration',5,'p_variable_declaration','sintactico.py',263),
  ('variable_declaration -> datatype ID ASIGNAR condition PUNTOCOMA','variable_declaration',5,'p_variable_declaration','sintactico.py',264),
  ('variable_declaration -> datatype ID PUNTOCOMA','variable_declaration',3,'p_variable_declaration','sintactico.py',265),
  ('variable_declaration -> datatype CORCHETE_APERTURA CORCHETE_CIERRE ID ASIGNAR CORCHETE_APERTURA expression_list CORCHETE_CIERRE PUNTOCOMA','variable_declaration',9,'p_variable_declaration','sintactico.py',266),
  ('variable_declaration -> datatype CORCHETE_APERTURA CORCHETE_CIERRE ID ASIGNAR CORCHETE_APERTURA CORCHETE_CIERRE PUNTOCOMA','variable_declaration',8,'p_variable_declaration','sintactico.py',267),
  ('assignment -> ID ASIGNAR expression PUNTOCOMA','assignment',4,'p_assignment','sintactico.py',305),
  ('expression_list -> expression','expression_list',1,'p_expression_list','sintactico.py',316),
  ('expression_list -> expression COMA expression_list','expression_list',3,'p_expression_list','sintactico.py',317),
  ('expression_list -> empty','expression_list',1,'p_expression_list','sintactico.py',318),
  ('condition -> condition AND condition','condition',3,'p_condition','sintactico.py',329),
  ('condition -> condition OR condition','condition',3,'p_condition','sintactico.py',330),
  ('condition -> NOT condition','condition',2,'p_condition','sintactico.py',331),
  ('condition -> condition MENORQUE condition','condition',3,'p_condition','sintactico.py',332),
  ('condition -> condition MAYORQUE condition','condition',3,'p_condition','sintactico.py',333),
  ('condition -> condition IGUAL condition','condition',3,'p_condition','sintactico.py',334),
  ('condition -> condition DIFERENTE condition','condition',3,'p_condition','sintactico.py',335),
  ('condition -> condition MENORIGUAL condition','condition',3,'p_condition','sintactico.py',336),
  ('condition -> condition MAYORIGUAL condition','condition',3,'p_condition','sintactico.py',337),
  ('condition -> PARENTESIS_APERTURA condition PARENTESIS_CIERRE','condition',3,'p_condition','sintactico.py',338),
  ('condition -> boleano','condition',1,'p_condition','sintactico.py',339),
  ('condition -> ID','condition',1,'p_condition','sintactico.py',340),
  ('condition -> NUMERO','condition',1,'p_condition','sintactico.py',341),
  ('condition -> ENTERO','condition',1,'p_condition','sintactico.py',342),
  ('expression -> ID','expression',1,'p_expression','sintactico.py',349),
  ('expression -> NUMERO','expression',1,'p_expression','sintactico.py',350),
  ('expression -> ENTERO','expression',1,'p_expression','sintactico.py',351),
  ('expression -> expression SUMA expression','expression',3,'p_expression','sintactico.py',352),
  ('expression -> expression RESTA expression','expression',3,'p_expression','sintactico.py',353),
  ('expression -> expression MULTIPLICACION expression','expression',3,'p_expression','sintactico.py',354),
  ('expression -> expression DIVISION expression','expression',3,'p_expression','sintactico.py',355),
  ('expression -> expression MODULO expression','expression',3,'p_expression','sintactico.py',356),
  ('expression -> PARENTESIS_APERTURA expression PARENTESIS_CIERRE','expression',3,'p_expression','sintactico.py',357),
  ('parameters -> datatype ID','parameters',2,'p_parameters','sintactico.py',365),
  ('parameters -> datatype ID COMA parameters','parameters',4,'p_parameters','sintactico.py',366),
  ('parameters -> empty','parameters',1,'p_parameters','sintactico.py',367),
  ('datatype -> VOID','datatype',1,'p_datatype','sintactico.py',377),
  ('datatype -> FLOAT','datatype',1,'p_datatype','sintactico.py',378),
  ('datatype -> INT','datatype',1,'p_datatype','sintactico.py',379),
  ('datatype -> BOOL','datatype',1,'p_datatype','sintactico.py',380),
  ('boleano -> TRUE','boleano',1,'p_boleano','sintactico.py',387),
  ('boleano -> FALSE','boleano',1,'p_boleano','sintactico.py',388),
  ('empty -> <empty>','empty',0,'p_empty','sintactico.py',395),
]