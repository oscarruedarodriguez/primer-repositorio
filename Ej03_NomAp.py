# oscar ivan rueda rodriguez
# 3° programacion T.M:
# cbtis #89
#muestra tu nombre y apellido

import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mostrar Nombre y Apellido")
ventana.geometry("300x200")

# Etiquetas
tk.Label(ventana, text="Nombre:").pack(pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Apellido:").pack(pady=5)
entrada_apellido = tk.Entry(ventana)
entrada_apellido.pack()

# Función para mostrar el nombre completo
def mostrar_nombre():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    etiqueta_resultado.config(text=f"Nombre completo: {nombre} {apellido}")

# Botón
tk.Button(ventana, text="Mostrar el Nombre", command=mostrar_nombre).pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()