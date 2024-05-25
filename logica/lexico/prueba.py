import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from lexer import analisis, errores
from sintactico import prueba_sintactica

class AnalizadorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Analizador Léxico y Sintáctico")
        
        self.label = ttk.Label(master, text="Ingrese el código:")
        self.label.pack()
        
        self.codigo_entry = scrolledtext.ScrolledText(master, width=60, height=10)
        self.codigo_entry.pack()
        
        self.analizar_button = ttk.Button(master, text="Analizar", command=self.analizar)
        self.analizar_button.pack()
        
        self.resultados_label = ttk.Label(master, text="Resultados:")
        self.resultados_label.pack()
        
        self.resultados_text = scrolledtext.ScrolledText(master, width=60, height=10)
        self.resultados_text.pack()
        
        self.errores_label = ttk.Label(master, text="Errores:")
        self.errores_label.pack()
        
        self.errores_text = scrolledtext.ScrolledText(master, width=60, height=5)
        self.errores_text.pack()
        
        self.tokens_label = ttk.Label(master, text="Tabla de Tokens:")
        self.tokens_label.pack()
        
        self.tokens_text = scrolledtext.ScrolledText(master, width=60, height=10)
        self.tokens_text.pack()
    
    def analizar(self):
        codigo = self.codigo_entry.get("1.0", tk.END)
        
        # Limpiar resultados anteriores
        self.resultados_text.delete("1.0", tk.END)
        self.errores_text.delete("1.0", tk.END)
        self.tokens_text.delete("1.0", tk.END)
        
        # Análisis léxico
        resultado_lexico = analisis(codigo)
        self.resultados_text.insert(tk.END, "Análisis Léxico:\n")
        for token in resultado_lexico:
            self.resultados_text.insert(tk.END, f"Token: {token}\n")
        
        # Análisis sintáctico
        resultado_sintactico = prueba_sintactica(codigo)
        self.resultados_text.insert(tk.END, "\nAnálisis Sintáctico:\n")
        for linea in resultado_sintactico:
            self.resultados_text.insert(tk.END, f"{linea}\n")
        
        # Mostrar errores
        if errores:
            self.errores_text.insert(tk.END, "Errores encontrados:\n")
            for error in errores:
                self.errores_text.insert(tk.END, f"{error}\n")
        else:
            self.errores_text.insert(tk.END, "No se encontraron errores.")
        
        # Mostrar tabla de tokens
        self.tokens_text.insert(tk.END, "Tabla de Tokens:\n")
        self.tokens_text.insert(tk.END, "Token\t\tTipo\t\tLínea\t\tColumna\n")
        for token in resultado_lexico:
            self.tokens_text.insert(tk.END, f"{token[0]}\t\t{token[1]}\t\t{token[2]}\t\t{token[3]}\n")

root = tk.Tk()
analizador_gui = AnalizadorGUI(root)
root.mainloop()