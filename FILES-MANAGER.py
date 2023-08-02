import customtkinter 
from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from customtkinter import filedialog
from PIL import ImageTk, Image
import os
from pytube import YouTube 

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("green")

class InterfazComprimirImagenes:
    def __init__(self):
        self.ventana = customtkinter.CTk()
        self.ventana.title("Files Manager")
        self.ventana.geometry("200x360")
        self.ventana.resizable(False,False)
        self.boton_comprimir = None
        self.boton_ordenar = None
        self.boton_descarga = None
        self.crear_interfaz()

    def crear_interfaz(self):
        self.titulo = Label(self.ventana,text="Files Manager", font=["Arial", 20], fg="white",bg='#148554')
        self.titulo.grid(column=1,row=0,padx=10,pady=10,columnspan=2)
        self.boton_comprimir =customtkinter.CTkButton(self.ventana, text="Comprimir Imagenes", command=self.comprimir_imagenes)
        self.boton_comprimir.grid(column=1,row=1,padx=10,pady=10,columnspan=1)
        self.boton_ordenar = customtkinter.CTkButton(self.ventana, text="Ordenar Archivos", command=self.ordenar_archivos)
        self.boton_ordenar.grid(column=1,row=2,padx=10,pady=10,columnspan=1)
        self.boton_descarga = customtkinter.CTkButton(self.ventana, text="Descargar video de YouTube", command=self.downloadVideo)
        self.boton_descarga.grid(column=1,row=3,padx=10,pady=10,columnspan=1)
        self.image = Image.open("logo.png")
        self.image = self.image.resize((80,137), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.label_img = tk.Label(self.ventana, image = self.img)
        self.label_img.grid(column=1,row=4,padx=10,pady=10,columnspan=1)

    def comprimir_imagenes(self):
        carpeta_a_ejecutar = filedialog.askdirectory(title="Seleccionar carpeta") + "\\"
        
        for nombre_de_archivo in os.listdir(carpeta_a_ejecutar):
            nombre, extension = os.path.splitext(carpeta_a_ejecutar + nombre_de_archivo)

            if extension.lower() in [".jpg", ".png", ".jpeg"]:
                imagen = Image.open(carpeta_a_ejecutar  + nombre_de_archivo)
                imagen.save(carpeta_a_ejecutar + "comprimido_" + nombre_de_archivo, optimize=True, quality=60)
                    
    def ordenar_archivos(self):
        carpeta_inicio = filedialog.askdirectory(title="Seleccionar carpeta de inicio")
        carpeta_destino = filedialog.askdirectory(title="Seleccionar carpeta destino")
        ext1 = customtkinter.CTkInputDialog(text="Escriba la extension de los archivos que movera:", title="Extension")
        ext = ext1.get_input()
        
        if carpeta_inicio and carpeta_destino and ext:
            for nombre_archivo in os.listdir(carpeta_inicio):
                nombre, extension = os.path.splitext(carpeta_inicio + "/" + nombre_archivo)
            
                if extension.lower() == ext.lower():
                    os.rename(carpeta_inicio + "/" + nombre_archivo, carpeta_destino + "/" + nombre_archivo) 
    
    def downloadVideo(self):
        url = simpledialog.askstring("URL:","URL")
        exit_dir = filedialog.askdirectory(title="Seleccionar carpeta destino")
        
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path = exit_dir)

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    interfaz = InterfazComprimirImagenes()
    interfaz.iniciar()
