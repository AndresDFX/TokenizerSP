#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import emojis
from tkinter import ttk

# Función que obtiene la información dentro de un archivo txt
# @return un String con la información del archivo.
 
def leerArchivo(archivo):
    texto = ""
    with open(archivo, 'rt',encoding='utf8' ) as o:
        texto = o.read()
    return texto
 
# Función que separa la información obtenido del archivo
# @return una lista con la información de los archivos
 
def extraerEmojis(archivo):
    lista = []
    for t in archivo.split('\n'):
        emoji = t.split(';')[2][78:79]
        lista.append(emoji)
    lista.pop()
    return lista


#Obtener la lista de caracteres unicode
def unicodeEmojis(listaEmojis):
    lista = []
    for t in range(len(listaEmojis)):
        lista.append(emojis.decode(listaEmojis[t]))
    return lista

text = leerArchivo("emojis_sequence.txt")
listaEmojis = extraerEmojis(text)
listaUnicode = unicodeEmojis(listaEmojis)

#print(listaEmojis)
print(listaUnicode)

#Pendiente hacer otro listbox y agregar ListaUnicode

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Lista en Tcl/Tk")
        
        self.listbox = tk.Listbox(self)
        self.listbox.insert(0, "😀")
        self.listbox.insert(1,emojis.decode("😀"))
        self.listbox.insert(0, *listaEmojis)
        self.listbox.pack()
        self.pack()
        
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()

