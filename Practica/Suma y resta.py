import tkinter as tk
from tkinter import ttk

def suma():
    numero_primero = int(suma_dos_numeros_1.get())
    numero_segundo = int(suma_dos_numeros_2.get())
    final_numero = numero_primero + numero_segundo
    etiqueta_final.config(text=f"numero resultante: {final_numero}")
    
def resta():
    numero_primero = int(suma_dos_numeros_1.get())
    numero_segundo = int(suma_dos_numeros_2.get())
    final_numero = numero_primero - numero_segundo
    etiqueta_final.config(text=f"numero resultante: {final_numero}")    
    

ventana = tk.Tk()
ventana.title("Suma de números")
ventana.config(width=500, height=500)

etiqueta_final = ttk.Label(text="primer numero")
etiqueta_final.place(x=20, y=20)

etiqueta_final = ttk.Label(text="segundo numero")
etiqueta_final.place(x=20, y=40)

suma_dos_numeros_1 = ttk.Entry()
suma_dos_numeros_1.place(x=140, y=20, width=60)

suma_dos_numeros_2 = ttk.Entry()
suma_dos_numeros_2.place(x=140, y=40, width=60)

boton_sumar = ttk.Button(text="Sumar", command=suma)
boton_sumar.place(x=20, y=80)

boton_restar = ttk.Button(text="Restar", command=resta)
boton_restar.place(x=150, y=80)


etiqueta_final = ttk.Label(text="numero resultante: ")
etiqueta_final.place(x=20, y=200)

ventana.mainloop()
