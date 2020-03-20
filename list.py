#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import emojis
import unicodedata2 as ud
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
    lista2 =[]
    for t in archivo.split('\n'):
        emoji = t.split(';')[2][78:79]
        lista.append(emoji)  
    lista.pop()
    char_list = [lista[j] for j in range(len(lista)) if ord(lista[j]) in range(65536)]
    return char_list


#Obtener la lista de caracteres unicode
def unicodeEmojis(listaEmojis):
    lista = []
    for t in range(len(listaEmojis)):       
        lista.append(emojis.encode(listaEmojis[t]))
    return lista



text = leerArchivo("emojis_sequence.txt")
listaEmojis = extraerEmojis(text)
listaUnicode = unicodeEmojis(listaEmojis)

#print(listaEmojis)
#print(listaUnicode)

#Pendiente hacer otro listbox y agregar ListaUnicode

class Application(ttk.Frame):
    
    def __init__(self, main_window):

        super().__init__(main_window)
        main_window.title("Lista en Tcl/Tk")
        self.listbox = tk.Listbox(self)
        self.listbox.insert(0, *listaUnicode)
        self.listbox.pack()
        self.pack()
        
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()

