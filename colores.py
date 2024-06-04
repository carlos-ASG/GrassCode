import tkinter as tk
import tkinter.scrolledtext as tkst

class MiVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("ScrolledText con Colores")

        # Crear un frame para el ScrolledText
        self.frame1 = tk.Frame(master=self.root, bg="#808000")
        self.frame1.pack(fill="both", expand="yes")

        # Crear el widget ScrolledText
        self.editArea = tkst.ScrolledText(master=self.frame1, wrap=tk.WORD, width=20, height=10)
        self.editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Insertar texto de ejemplo
        self.editArea.insert(tk.INSERT, """
        Integer posuere erat a ante venenatis dapibus. Posuere velit aliquet.
        Aenean eu leo quam. Pellentesque ornare sem. Lacinia quam venenatis vestibulum.
        Nulla vitae elit libero, a pharetra augue. Cum sociis natoque penatibus et magnis dis.
        Parturient montes, nascetur ridiculus mus.
        """)

        # Función para colorear palabras específicas
        self.colorear_palabras()

        # Vincular evento de teclado
        self.editArea.bind("<KeyRelease>", self.actualizar_colores)

    def colorear_palabras(self):
        palabras_a_colorear = ["leo", "ornare", "pharetra"]
        for palabra in palabras_a_colorear:
            inicio = "1.0"
            while True:
                inicio = self.editArea.search(palabra, inicio, stopindex=tk.END)
                if not inicio:
                    break
                fin = f"{inicio}+{len(palabra)}c"
                self.editArea.tag_add(palabra, inicio, fin)
                self.editArea.tag_config(palabra, foreground="red")
                inicio = fin

    def actualizar_colores(self, event):
        # Obtener el texto actual
        texto_actual = self.editArea.get("1.0", "end-1c")

        # Actualizar colores
        self.editArea.tag_remove("leo", "1.0", "end")
        self.editArea.tag_remove("ornare", "1.0", "end")
        self.editArea.tag_remove("pharetra", "1.0", "end")
        self.colorear_palabras()

if __name__ == "__main__":
    root = tk.Tk()
    app = MiVentana(root)
    root.mainloop()
