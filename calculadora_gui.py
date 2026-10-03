import tkinter as tk
from tkinter import messagebox

def calcular(operacion):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operacion == 'suma':
            resultado = num1 + num2
            simbolo = "+"
        elif operacion == 'resta':
            resultado = num1 - num2
            simbolo = "-"
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
            simbolo = "×"
        elif operacion == 'division':
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir entre cero.")
                return
            resultado = num1 / num2
            simbolo = "÷"
            
        label_resultado.config(text=f"Resultado: {num1} {simbolo} {num2} = {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Mi Calculadora GUI")
ventana.geometry("300x400")

# Etiqueta y campo para el número 1
tk.Label(ventana, text="Primer número:").pack(pady=5)
entry1 = tk.Entry(ventana)
entry1.pack(pady=5)

# Etiqueta y campo para el número 2
tk.Label(ventana, text="Segundo número:").pack(pady=5)
entry2 = tk.Entry(ventana)
entry2.pack(pady=5)

# Botones de operaciones
tk.Button(ventana, text="Sumar (+)", width=15, bg="lightgreen", command=lambda: calcular('suma')).pack(pady=5)
tk.Button(ventana, text="Restar (-)", width=15, bg="lightyellow", command=lambda: calcular('resta')).pack(pady=5)
tk.Button(ventana, text="Multiplicar (×)", width=15, bg="lightblue", command=lambda: calcular('multiplicacion')).pack(pady=5)
tk.Button(ventana, text="Dividir (÷)", width=15, bg="lightpink", command=lambda: calcular('division')).pack(pady=5)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 11, "bold"))
label_resultado.pack(pady=20)

ventana.mainloop()
