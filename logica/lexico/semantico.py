class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, ast):
        for node in ast:
            self.visit(node)

    def visit(self, node):
        if isinstance(node, tuple):
            node_type = node[0]
            if node_type == 'declaracion_variable':
                self.visit_declaration(node)
            elif node_type == 'asignacion':
                self.visit_assignment(node)
            elif node_type == 'llamada_funcion':
                self.visit_function_call(node)
            elif node_type == 'if':
                self.visit_if_statement(node)
            elif node_type == 'while':
                self.visit_while_loop(node)
            # Agrega más visitas para otros tipos de nodos si es necesario

    def visit_declaration(self, node):
        _, var_name, value = node
        if var_name in self.symbol_table:
            print(f"Error semántico: La variable '{var_name}' ya ha sido declarada.")
        else:
            self.symbol_table[var_name] = value

    def visit_assignment(self, node):
        _, var_name, expr = node
        if var_name not in self.symbol_table:
            print(f"Error semántico: La variable '{var_name}' no ha sido declarada.")
        else:
            # Aquí podrías realizar más verificaciones, como verificar la compatibilidad de tipos
            self.symbol_table[var_name] = expr

    def visit_function_call(self, node):
        _, func_name, args = node
        # Aquí podrías realizar verificaciones adicionales, como verificar si la función existe y los tipos de argumentos

    def visit_if_statement(self, node):
        _, condition, body, else_body = node
        # Aquí podrías realizar verificaciones adicionales, como verificar la validez de la condición

    def visit_while_loop(self, node):
        _, condition, body = node
        # Aquí podrías realizar verificaciones adicionales, como verificar la validez de la condición

# Ejemplo de uso:
semantic_analyzer = SemanticAnalyzer()
ast = [('declaracion_variable', 'x', 5), ('asignacion', 'y', 'x')]
semantic_analyzer.analyze(ast)
