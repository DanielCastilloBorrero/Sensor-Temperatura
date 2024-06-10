import tkinter as tk

class Root(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry(self.window_size())
        self.title("Monitor de Recursos")
        self.resizable(False, False)
        self.wm_iconphoto(True, tk.PhotoImage(file='./View/src/Icon.png'))

    def window_size(self):
        # Obtener las dimensiones de la pantalla
        width_display = self.winfo_screenwidth()
        height_display = self.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        width_window = 850
        height_window = 250
        pos_x = (width_display - width_window) // 2
        pos_y = (height_display - height_window) // 2

        # Retornar el tamaño y la posicion de la ventana
        return f"{width_window}x{height_window}+{pos_x}+{pos_y}"
    
    def start_mainloop(self):
        self.mainloop()