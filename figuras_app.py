from tkinter import *
from tkinter import colorchooser # Importar colorchooser para la seleccion de color (opcional, pero mejora la UX)

class Aplicacion:
    def __init__(self, master):
        """
        Constructor de la clase Aplicacion.
        Configura la ventana principal y sus widgets.
        """
        self.master = master
        master.title("Dibujo de Figuras")
        master.geometry("600x400") # Aumentar el tamano para acomodar nuevos elementos

        # Variables de instancia
        self.figura_seleccionada = None
        self.x_click = 0
        self.y_click = 0
        self.color_actual = "blue" # Color inicial por defecto

        # --- Widgets de Interfaz ---

        # Listbox para seleccionar la figura
        self.lista_figuras = Listbox(master, height=5)
        self.lista_figuras.insert(1, "Circulo")
        self.lista_figuras.insert(2, "Rectangulo")
        self.lista_figuras.insert(3, "Elipse") # Nueva figura: Elipse
        self.lista_figuras.pack(side=LEFT, fill=Y, padx=10, pady=10)
        self.lista_figuras.bind("<<ListboxSelect>>", self.seleccionar_figura)

        # Frame para los controles de color y el boton de borrado
        self.control_frame = Frame(master)
        self.control_frame.pack(side=BOTTOM, fill=X, pady=10)

        # Etiqueta y Entry para el color
        self.label_color = Label(self.control_frame, text="Color (ej. red, #RRGGBB):")
        self.label_color.pack(side=LEFT, padx=5)
        self.entry_color = Entry(self.control_frame, width=15)
        self.entry_color.insert(0, self.color_actual) # Establecer color inicial en la caja de texto
        self.entry_color.pack(side=LEFT, padx=5)

        # Boton para abrir el selector de color (opcional, pero util)
        self.btn_elegir_color = Button(self.control_frame, text="Elegir Color", command=self.elegir_color)
        self.btn_elegir_color.pack(side=LEFT, padx=5)


        # Boton para borrar todas las figuras
        self.btn_borrar = Button(self.control_frame, text="Borrar Figuras", command=self.borrar_figuras)
        self.btn_borrar.pack(side=RIGHT, padx=5)


        # Canvas para dibujar
        self.canvas = Canvas(master, bg="white", width=400, height=300, bd=2, relief="groove")
        self.canvas.pack(side=RIGHT, expand=True, fill=BOTH, padx=10, pady=10)
        self.canvas.bind("<Button-1>", self.clic_canvas) # El evento <Button-1> detecta un clic con el boton izquierdo del raton

    def seleccionar_figura(self, event):
        """
        Maneja el evento de seleccion en el Listbox.
        Actualiza la variable de instancia figura_seleccionada.
        """
        seleccion = self.lista_figuras.curselection()
        if seleccion:
            self.figura_seleccionada = self.lista_figuras.get(seleccion[0])
            print(f"Figura seleccionada: {self.figura_seleccionada}")

    def elegir_color(self):
        """
        Abre un dialogo de seleccion de color y actualiza el Entry y el color actual.
        """
        color_code = colorchooser.askcolor(title="Seleccionar Color")[1] # [1] obtiene el codigo hexadecimal
        if color_code: # Si se selecciono un color (no se cancelo)
            self.entry_color.delete(0, END)
            self.entry_color.insert(0, color_code)
            self.color_actual = color_code
            print(f"Color seleccionado: {self.color_actual}")

    def clic_canvas(self, event):
        """
        Maneja el evento de clic en el Canvas.
        Almacena las coordenadas del clic y llama al metodo dibujar.
        """
        self.x_click, self.y_click = event.x, event.y
        self.dibujar()

    def dibujar(self):
        """
        Dibuja la figura seleccionada en las coordenadas del clic,
        utilizando el color especificado en la caja de texto.
        """
        # Obtener el color de la caja de texto, por defecto azul si esta vacio o es invalido
        fill_color = self.entry_color.get()
        if not fill_color:
            fill_color = "blue" # Color por defecto si el Entry esta vacio

        if self.figura_seleccionada == "Circulo":
            # Coordenadas para un circulo de radio 25
            self.canvas.create_oval(self.x_click - 25, self.y_click - 25,
                                    self.x_click + 25, self.y_click + 25,
                                    fill=fill_color, outline=fill_color)
        elif self.figura_seleccionada == "Rectangulo":
            # Coordenadas para un rectangulo de 60x40 (ancho x alto)
            self.canvas.create_rectangle(self.x_click - 30, self.y_click - 20,
                                         self.x_click + 30, self.y_click + 20,
                                         fill=fill_color, outline=fill_color)
        elif self.figura_seleccionada == "Elipse":
            # Coordenadas para una elipse con dimensiones 60x30 (ancho x alto)
            self.canvas.create_oval(self.x_click - 30, self.y_click - 15, # x1, y1 (esquina superior izquierda del bounding box)
                                    self.x_click + 30, self.y_click + 15, # x2, y2 (esquina inferior derecha del bounding box)
                                    fill=fill_color, outline=fill_color)
        else:
            print("Por favor, selecciona una figura para dibujar.")

    def borrar_figuras(self):
        """
        Borra todas las figuras dibujadas en el Canvas.
        """
        self.canvas.delete("all")
        print("Todas las figuras han sido borradas.")

# --- Ejecucion principal del programa ---
if __name__ == "__main__":
    root = Tk()
    app = Aplicacion(root)
    root.mainloop()