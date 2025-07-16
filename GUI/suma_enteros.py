from tkinter import *
from tkinter import messagebox
def sumar(): # Definir la función que se ejecuta al pulsar el botón
    try:
        num1 = float(entNum1.get()) # Obtener el primer número del campo de entrada
        num2 = float(entNum2.get()) # Obtener el segundo número del campo de entrada
        resultado = num1 + num2 # Calcular la suma
        entResultado.delete(0, END) # Limpiar el campo de resultado
        entResultado.config(state="normal") # Habilitar el campo de resultado para mostrar el resultado
        entResultado.insert(0, str(resultado)) # Mostrar el resultado en el campo de entrada
    except ValueError: # Manejar errores si la entrada no es un número válido
        entResultado.delete(0, END) # Limpiar el campo de resultado
        entResultado.insert(0, "Error") # Mostrar un mensaje de error
        messagebox.showerror("Error", "Por favor, introduce números válidos.") # Mostrar un mensaje de error

ventana = Tk() # Crear la ventana principal

ventana.title("Sumador de Enteros") # Título de la ventana

ventana.geometry("300x200") # Tamaño de la ventana



# Crear etiquetas para solicitar números al usuario
lblNum1 = Label(ventana, text="Introduce el primer número") # Crear una etiqueta con un mensaje

lblNum2 = Label(ventana, text="Introduce el segundo número:") # Etiqueta para instrucciones

#definir los entradas de texto
entNum1 = Entry(ventana) # Campo de entrada para el primer número
entNum2 = Entry(ventana) # Campo de entrada para el segundo número
entResultado = Entry(ventana ) # Campo de entrada para mostrar el resultado
entResultado.config(state="disabled") 
#Botón para realizar la suma
btnSumar = Button(ventana, text="Sumar", command = sumar) # Botón que suma los números


#añadir los componentes a la ventana
lblNum1.pack() # Añadir la etiqueta a la ventana con un margen vertical
entNum1.pack() # Añadir el campo de entrada del primer número a la ventana
lblNum2.pack() # Añadir la etiqueta del segundo número a la ventana
entNum2.pack() # Añadir el campo de entrada del segundo número a la ventana
btnSumar.pack() # Añadir el botón de suma a la ventana
entResultado.pack() # Añadir el campo de entrada del resultado a la ventana



ventana.mainloop() # Iniciar el bucle principal de la ventana
# Esto mantiene la ventana abierta hasta que el usuario la cierre