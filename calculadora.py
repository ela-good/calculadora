#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import tkinter as tk
from math import sqrt, factorial, pi

cuenta = "" # similar a calculo = tk.StringVar() del lado gráfico

####### funciones  #######################
def clic(tecla):
    """
    Funciòn que captura la pulsión de cada tecla y la concatena con la
    expresión existente en la variable cuenta mostrando por pantalla
    """
    global cuenta
    cuenta = cuenta + tecla
    calculo.set(cuenta)
    
def borrar_caracter():
    """
    Función que borra el último caracter añadido en la pantalla de la calculadora
    """
    global cuenta
    cuenta = cuenta[:-1]
    if cuenta:
        calculo.set(cuenta)
    else:
        calculo.set("0")
        
def limpieza():
    global cuenta
    cuenta = ""
    calculo.set("0")

    
def hacer_cuenta():
    global cuenta
    try:
        total = str(eval(cuenta))
    except Exception:
        limpieza()
        total = "ERROR"
    calculo.set(total)
    


# Ventana para contener la calculadora
ventana = tk.Tk()
ventana.title("Calculadora ACME")
ventana.config(width=390, height=600, bg="Light Steel Blue")
ventana.resizable(0,0)

# Creo una variable para almacenar el cálculo a mostrar en la pantalla
calculo = tk.StringVar() # similar a cuenta = "" del lado consola

limpieza()

# creamos la pantalla
pantalla = tk.Entry(
                font=["arial",20,"bold"],
                width=21,         # ancho
                bd=20,            # grosor del borde
                bg="powder blue",  # color de fondo
                justify="right",      # alineación del texto
                state=tk.DISABLED,    # la hago solo lectura
                textvariable=calculo  # variable a mostrar
            )
pantalla.place(x=16, y=50)

# defino las dimensiones de las teclas
ancho = 9
alto = 2

#################   TECLAS  ################################
# tecla para borrar
boton = tk.Button(text="\u2190", width=ancho, height=alto, bg="SkyBlue", command=borrar_caracter)
boton.place(x=288, y=140)


## Primera fila 1 2 3 +
boton = tk.Button(text="\uFF11", width=ancho, height=alto, command=lambda:clic("1"))
boton.place(x=18, y=200)
boton = tk.Button(text="2", width=ancho, height=alto, command=lambda:clic("2"))
boton.place(x=108, y=200)
boton = tk.Button(text="3", width=ancho, height=alto, command=lambda:clic("3"))
boton.place(x=198, y=200)
boton = tk.Button(text="+", width=ancho, height=alto, bg="SteelBlue", command=lambda:clic("+"))
boton.place(x=288, y=200)

## Segunda fila 4 5 6 -
boton = tk.Button(text="4", width=ancho, height=alto, command=lambda:clic("4"))
boton.place(x=18, y=260)
boton = tk.Button(text="5", width=ancho, height=alto, command=lambda:clic("5"))
boton.place(x=108, y=260)
boton = tk.Button(text="6", width=ancho, height=alto, command=lambda:clic("6"))
boton.place(x=198, y=260)
boton = tk.Button(text="-", width=ancho, height=alto, bg="SteelBlue", command=lambda:clic("-"))
boton.place(x=288, y=260)

## Tercera fila 7 8 9 x
boton = tk.Button(text="7", width=ancho, height=alto, command=lambda:clic("7"))
boton.place(x=18, y=320)
boton = tk.Button(text="8", width=ancho, height=alto, command=lambda:clic("8"))
boton.place(x=108, y=320)
boton = tk.Button(text="9", width=ancho, height=alto, command=lambda:clic("9"))
boton.place(x=198, y=320)
boton = tk.Button(text="x", width=ancho, height=alto, bg="SteelBlue", command=lambda:clic("*"))
boton.place(x=288, y=320)

## Cuarta fila ( 0 ) /
boton = tk.Button(text="(", width=ancho, height=alto, bg="SkyBlue", command=lambda:clic("("))
boton.place(x=18, y=380)
boton = tk.Button(text="0", width=ancho, height=alto, command=lambda:clic("0"))
boton.place(x=108, y=380)
boton = tk.Button(text=")", width=ancho, height=alto, bg="SkyBlue", command=lambda:clic(")"))
boton.place(x=198, y=380)
boton = tk.Button(text="/", width=ancho, height=alto, bg="SteelBlue", command=lambda:clic("/"))
boton.place(x=288, y=380)

## Quinta fila Raiz Coma Potencia Modulo  ##TODO: buscar caracter unicode para  POW
boton = tk.Button(text="\u221A", width=ancho, height=alto, bg="SkyBlue", command=lambda:clic("sqrt("))
boton.place(x=18, y=440)
boton = tk.Button(text=".", width=ancho, height=alto, bg="SkyBlue", command=lambda:clic("."))
boton.place(x=108, y=440)
boton = tk.Button(text="POW", width=ancho, height=alto, bg="SkyBlue", command=lambda:clic("**"))
boton.place(x=198, y=440)
boton = tk.Button(text="%", width=ancho, height=alto, bg="SkyBlue", command=lambda:clic("%"))
boton.place(x=288, y=440)

## Sexta fila Clear factorial pi =
boton = tk.Button(text="CL", width=ancho, height=alto, bg="SkyBlue", command=limpieza)
boton.place(x=18, y=500)
boton = tk.Button(text="!", width=ancho, height=alto, bg="SkyBlue", command=lambda:clic("factorial("))
boton.place(x=108, y=500)
boton = tk.Button(text="\u03c0", width=ancho, height=alto, bg="SkyBlue", command=lambda:clic(str(pi)))
boton.place(x=198, y=500)
boton = tk.Button(text="=", width=ancho, height=alto, bg="medium aquamarine", command=hacer_cuenta)
boton.place(x=288, y=500)

ventana.mainloop()

"""
BONUS TRACK
Para hacer una carpeta dist con un ejecutable adentro (.exe)
1) Descargar pyinstaller
python -m pip install pyinstaller

2) Crear el ejecutable sin consola y en un solo archivo
pyinstaller --noconsole --onefile calc.py

"""
