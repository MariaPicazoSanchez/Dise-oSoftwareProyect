

import tkinter as tk

# Crear la ventana
ventana = tk.Tk()

# Configurar el tamaño de la ventana
ventana.geometry("300x200")

# Crear un lienzo (canvas) con un recuadro blanco
lienzo = tk.Canvas(ventana, bg="white", width=200, height=100)

# Ubicar el lienzo en la ventana
lienzo.pack()

# Mostrar la ventana
ventana.mainloop()