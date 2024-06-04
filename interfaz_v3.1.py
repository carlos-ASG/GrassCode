from math import sin
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import Menu, filedialog, messagebox
from lexer import analisis, palabras_reservadas
from  sintactico import sintactico

class GrassCodeEditor:
    def __init__(self, interfaz):
        self.file_path = ""
        self.interfaz = interfaz
        self.interfaz.title("GrassCode - Compiler")   
        self.interfaz.geometry("800x600")
        
        self.create_menu()  
        self.font_size = 12  # Tamaño de fuente inicial
        self.txt_font = ('Roboto', self.font_size)

        # Dimensiones de la ventana
        window_width = 1000
        window_height = 600
        
        #palabras reservadas
        self.palabras_a_colorear = palabras_reservadas.keys()

        # Obtener el tamaño de la pantalla
        screen_width = self.interfaz.winfo_screenwidth()
        screen_height = self.interfaz.winfo_screenheight()

        # Calcular la posición x, y para centrar la ventana
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Establecer la geometría de la ventana para que esté centrada
        self.interfaz.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        # Configurar las filas y columnas para que se expandan
        for i in range(10):
            self.interfaz.columnconfigure(i, weight=1)

        # Ajustar los pesos de las filas para que txtTerminal no se expanda demasiado
        self.interfaz.rowconfigure(0, weight=0)
        self.interfaz.rowconfigure(1, weight=0)
        self.interfaz.rowconfigure(2, weight=3)  # Más espacio para el área de texto principal
        self.interfaz.rowconfigure(3, weight=0)
        self.interfaz.rowconfigure(4, weight=0)
        self.interfaz.rowconfigure(5, weight=1)  # Menos espacio para el terminal
        self.interfaz.rowconfigure(6, weight=0)

        # Componentes
        self.lblTablaTokens = ttk.Label(self.interfaz, text="Tabla de tokens")
        self.lblTerminalErrores = ttk.Label(self.interfaz, text="Terminal de salida para errores")
        self.text_frame = tk.Frame(self.interfaz)
        self.txtNumber = tk.Text(self.text_frame, width=4, padx=4, takefocus=0, border=0,
                                 background='lightgrey', state='disabled', font=self.txt_font)  # Modificación
        self.txtArea = scrolledtext.ScrolledText(self.text_frame, wrap="none", undo=True, font=self.txt_font, width=80, height=20)
        #self.highlighter = RealtimeHighlighter(self.txtArea)
        self.txtNumber.pack(side=tk.LEFT, fill=tk.Y)
        self.txtArea.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.text_frame.grid(row=2, column=0, padx=10, pady=2, sticky="nw")
        
        # Vincular el evento de teclado para actualizar los números de línea
        self.txtArea.bind('<KeyRelease>', self.update_line_numbers)
        self.update_line_numbers()
        self.txtTerminal = tk.Text(self.interfaz, wrap="word", highlightthickness=0.5, highlightbackground="grey", highlightcolor="grey")  
        self.tablaTokens = ttk.Treeview(self.interfaz, columns=("Token", "Tipo de Token"), show="headings")
        self.tablaTokens.column("Token", width=200)
        self.tablaTokens.column("Tipo de Token", width=150)
        self.btnCompilar = ttk.Button(self.interfaz, text = "Compilar", style = 'Custom.TButton', command=self.compilar)

        # Configuración del TreeView (Tabla)
        self.tablaTokens.heading("Token", text="Token")
        self.tablaTokens.heading("Tipo de Token", text="Tipo de Token")

        # Posicionamiento de los componentes en la cuadrícula
        self.lblTablaTokens.grid(row=1, column=3, padx=5, pady=2, sticky='w')
        self.tablaTokens.grid(row=2, column=3, columnspan=7, padx=10, pady=2, sticky='nsew')
        self.btnCompilar.grid(row=3, column=0, padx=10, pady=0, sticky='w')

        self.lblTerminalErrores.grid(row=4, column=0, padx=10, pady=(10, 2), sticky='w')

        self.txtTerminal.grid(row=5, column=0, columnspan=10, padx=10, pady=0, sticky='ew')
        self.txtTerminal.update_idletasks()
        self.txtTerminal.config(height=int(self.interfaz.winfo_height() / 60))
        
        self.colorear_palabras()
        
        # Sincronización del scroll
        self.txtArea.bind('<Control-MouseWheel>', self.zoom)
        self.txtArea.bind('<MouseWheel>', self.sync_scroll)
        self.txtNumber.bind('<MouseWheel>', self.sync_scroll)
        self.txtArea.bind("<KeyRelease>", self.actualizar_colores)
    

    def colorear_palabras(self):
        for palabra in self.palabras_a_colorear:
            inicio = "1.0"
            while True:
                inicio = self.txtArea.search(palabra, inicio, stopindex=tk.END)
                if not inicio:
                    break
                fin = f"{inicio}+{len(palabra)}c"
                self.txtArea.tag_add(palabra, inicio, fin)
                self.txtArea.tag_config(palabra, foreground="blue")
                inicio = fin
    
    def actualizar_colores(self, event):
        # Obtener el texto actual
        texto_actual = self.txtArea.get("1.0", "end-1c")

        # Actualizar colores
        for palabra in self.palabras_a_colorear:
            self.txtArea.tag_remove(palabra, "1.0", "end")
        self.colorear_palabras()
    
    def update_line_numbers(self, event=None):
        self.txtNumber.config(state=tk.NORMAL)
        self.txtNumber.delete(1.0, tk.END)
        current_lines = self.txtArea.get(1.0, tk.END).split('\n')
        for i in range(1, len(current_lines)):
            self.txtNumber.insert(tk.END, f'{i}\n')
        self.txtNumber.config(state=tk.DISABLED)
        self.sync_scroll()
        self.update_line_numbers_width()

    def update_line_numbers_width(self):
        digits = len(str(self.txtArea.index('end-1c').split('.')[0]))
        self.txtNumber.config(width=digits)

    def sync_scroll(self, event=None):
        self.txtNumber.yview_moveto(self.txtArea.yview()[0])

    def create_menu(self):
        menubar = Menu(self.interfaz)
        self.interfaz.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nuevo", command=self.new_file)
        filemenu.add_command(label="Abrir", command=self.open_file)
        filemenu.add_command(label="Guardar", command=self.guardar_archivo)
        filemenu.add_command(label="Cerrar")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.interfaz.quit)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cortar")
        editmenu.add_command(label="Copiar")
        editmenu.add_command(label="Pegar")

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Ayuda")
        helpmenu.add_command(label="Acerca de")

        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Editar", menu=editmenu)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)
        
    def new_file(self):
        self.file_path = ""
        self.txtArea.delete(1.0, tk.END)

    def open_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if not self.file_path:
            return
        self.txtArea.delete(1.0, tk.END)
        with open(self.file_path, "r") as file:
            self.txtArea.insert(tk.END, file.read())

    def guardar_archivo(self):
        if not self.file_path:
            self.file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
            )
            if not self.file_path:
                return
        with open(self.file_path, "w") as file:
            file.write(self.txtArea.get(1.0, tk.END))

    def guardar_como_nuevo(self):
        file_path = filedialog.asksaveasfilename(
            title="Guardar archivo",
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt")])

        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.txtArea.get(1.0, tk.END))
                self.file_path = file_path  #Da a conocer a la interfaz la ruta del archivo abierto
            except Exception as e:
                print(f"Error al guardar el archivo: {e}")
    
    def llenar_tabla(self, tokens = []):
        for item in self.tablaTokens.get_children():
            self.tablaTokens.delete(item)
            
        for token in tokens:
            self.tablaTokens.insert("", tk.END, values=(token["value"], token["type"]))
    
    def zoom(self, event):
        current_font = self.txtArea['font']
        font_name, font_size = current_font.split()
        font_size = int(font_size)

        if event.delta > 0:
            font_size += 1
        else:
            font_size -= 1

        font_size = max(8, min(font_size, 24))  # Limitar el tamaño de la fuente entre 8 y 24

        new_font = (font_name, font_size)
        self.txtArea['font'] = new_font
        self.txtNumber['font'] = new_font
        self.update_line_numbers()

    def compilar(self):
        text = self.txtArea.get(1.0, tk.END)
        tokens_encontrados, errores_lexicos = analisis(text)
        result, errores_sintacticos, symbol_table = sintactico(text)
            
        self.txtTerminal.delete(1.0, tk.END)
        
        if errores_lexicos:
            for error in errores_lexicos:
                self.txtTerminal.insert(tk.END, error + "\n")
        else:
            self.llenar_tabla(tokens=tokens_encontrados)
            #self.txtTerminal.insert(tk.END, result)
        if errores_sintacticos:
            for error in errores_sintacticos:
                self.txtTerminal.insert(tk.END, error + "\n")
        else:
            for variable in symbol_table.keys():
                nombre = symbol_table[variable]['value']
                tipo = symbol_table[variable]['type']
                mensaje = f'variable {variable} - tipo {tipo} - valor {nombre}'
                self.txtTerminal.insert(tk.END, mensaje + "\n")
    
    
if __name__ == "__main__":
    interfaz = tk.Tk()
    editor = GrassCodeEditor(interfaz)
    interfaz.mainloop()
