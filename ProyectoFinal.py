import customtkinter 
from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from customtkinter import filedialog
from PIL import ImageTk, Image
import os
from pytube import YouTube 

#seleccionamos el modo oscuro para nuestra interfaz
customtkinter.set_appearance_mode("dark")

#seleccionamos el color por default de nuestra interfaz, en este caso verde
customtkinter.set_default_color_theme("green")

#Creamos una clase que tendra dentro todos los parametros de nuestra interfaz
class APP:
    #Por facilidad decidimos utilizar programacion orientada a objetos para manipular la interfaz
    def __init__(self):
        #Declaramos nuestro frame de la ventana
        self.ventana = customtkinter.CTk()
        
        #Colocamos un nombre a la ventana
        self.ventana.title("Files Manager")
        
        #Ajustamos las medidas de la ventana
        self.ventana.geometry("200x360")
        
        #Declaramos que la ventana tenga un tamano fijo y no sea ajustable
        self.ventana.resizable(False,False)
        
        #Declaramos el valor de los botones que se integraran a la interfaz
        self.boton_comprimir = None
        self.boton_ordenar = None
        self.boton_descarga = None
        
        #Usamos la funcion crar interfaz
        self.crear_interfaz()

#Dentro de esta funcion "imprimiremos" los elementos de nuestra interfaz
    def crear_interfaz(self):
        #Declaramos un encabezado dentro de la ventana
        self.titulo = Label(self.ventana,text="Files Manager", font=["Arial", 20], fg="white",bg='#148554')
        
        #Lo posicionamos
        self.titulo.grid(column=1,row=0,padx=10,pady=10,columnspan=2)

        #Modifiamos el boton pasandole los parametros de donde aparecera, el texto que llevara y el comando que realizara al accionarse
        self.boton_comprimir =customtkinter.CTkButton(self.ventana, text="Comprimir Imagenes", command=self.comprimir_imagenes)
        
        #Ubicamos el boton dentro del espacio de nuestra ventana
        self.boton_comprimir.grid(column=1,row=1,padx=10,pady=10,columnspan=1)
        
        #Modifiamos el boton pasandole los parametros de donde aparecera, el texto que llevara y el comando que realizara al accionarse
        self.boton_ordenar = customtkinter.CTkButton(self.ventana, text="Ordenar Archivos", command=self.ordenar_archivos)
        
         #Ubicamos el boton dentro del espacio de nuestra ventana
        
        self.boton_ordenar.grid(column=1,row=2,padx=10,pady=10,columnspan=1)
        
        #Modifiamos el boton pasandole los parametros de donde aparecera, el texto que llevara y el comando que realizara al accionarse
        self.boton_descarga = customtkinter.CTkButton(self.ventana, text="Descargar video de YouTube", command=self.downloadVideo)
        
        #Ubicamos el boton dentro del espacio de nuestra ventana
        self.boton_descarga.grid(column=1,row=3,padx=10,pady=10,columnspan=1)
        
        #Declaramos una imagen que colocaremos en nuestro frame, esta declaracion es especial para imagenes las cuales queremos modificar su tamno
        self.image = Image.open("logo.png")
        
        #Modificamos sus medidas
        self.image = self.image.resize((80,137), Image.ANTIALIAS)
        
        #Le pasamos el valor de image a una nueva variable para asi poder imprimirla
        self.img = ImageTk.PhotoImage(self.image)
        
        #Pasamos los parametros del frame y la imagen que contendra
        self.label_img = tk.Label(self.ventana, image = self.img)
        
        #la ubicamos dentro de la ventana
        self.label_img.grid(column=1,row=4,padx=10,pady=10,columnspan=1)

#Funcion para comprimir las imagenes de una carpeta que proporcionara el usuario
    def comprimir_imagenes(self):
        #Con el siguiente codigo abrimos los documentos del dispositivo para que el usuario nos
        #indique una carpeta la cual leeremos
        carpeta_a_ejecutar = filedialog.askdirectory(title="Seleccionar carpeta") 
        
        #con la funcion os.listdir creamos una lista con los nombres de los archivos de una ruta
        #iteramos sobre esta misma para analizar cada archivo por separado
        for nombre_de_archivo in os.listdir(carpeta_a_ejecutar):
            
            #El nombre y extension seran iguales a la funcion splittext que separa los
            #parametros de un archivo que sera sobre la carpeta y el nombre del archivo
            nombre, extension = os.path.splitext(carpeta_a_ejecutar + nombre_de_archivo)

            #si la extension del archivo es igual a la siguientes podemos concluir que es una imagen 
            #por lo que pasara el condicionamiento
            if extension.lower() in [".jpg", ".png", ".jpeg"]:
                #abrimos la imagen para poder manipularla
                imagen = Image.open(carpeta_a_ejecutar  + nombre_de_archivo)
                
                #guardamos la misma imagen con el nombre de comprimdo que sera la misma imagen pero con
                #peor calidad, por lo que ocupara menos espacio en la memoria
                imagen.save(carpeta_a_ejecutar + "comprimido_" + nombre_de_archivo, optimize=True, quality=60)
    
    #funcion para ordenar archivos              
    def ordenar_archivos(self):
        #pedimos que nos proporicone una carpeta que leeremos
        carpeta_inicio = filedialog.askdirectory(title="Seleccionar carpeta de inicio")
        
        #pedimos otra carpeta sobre la cual enviaremos los archivos
        carpeta_destino = filedialog.askdirectory(title="Seleccionar carpeta destino")
        
        #pedimos quese nos proporcione la extension de los tipos de archivo que moveremos
        ext1 = customtkinter.CTkInputDialog(text="Escriba la extension de los archivos que movera:", title="Extension")
        ext = ext1.get_input()
        
        #si se nos proporcionaron todos los datos pasaremos el condicional
        if carpeta_inicio and carpeta_destino and ext:
            #iteramos sobre la lsiuta de los archivos de la primer carpeta
            for nombre_archivo in os.listdir(carpeta_inicio):
                #separamos el nombre y la extension del archivo
                nombre, extension = os.path.splitext(carpeta_inicio + "/" + nombre_archivo)

                #si la extension del archivo es igual a la que el usario nos indico mover el archivo
                #se renombrara cambiando la carpeta de ubicacion por lo que pasara de una a la otra
                if extension.lower() == ext.lower():
                    os.rename(carpeta_inicio + "/" + nombre_archivo, carpeta_destino + "/" + nombre_archivo) 
    #funcion apra descargar videos
    def downloadVideo(self):
        #pedimos que se nos proporcuine la url del video a descargar
        url_ = customtkinter.CTkInputDialog(text="URL:", title="URL")
        url = url_.get_input()
       #pedimos que s enos indique en cual direccion descargaremos el video 
        exit_dir = filedialog.askdirectory(title="Seleccionar carpeta destino")
        
        #declaramos el vidoe como perteneciente a youtube
        video = YouTube(url)
        #modificamos la esolucion al mazimo posible
        stream = video.streams.get_highest_resolution()
        #ordenamos a descargar sobre la carpeta indicada
        stream.download(output_path = exit_dir)
#esta funcion iniciara con la interfaz
    def iniciar(self):
        self.ventana.mainloop()

#si ejecutamos el archivo se pasara el condicional
if __name__ == "__main__":
    #declaramos nuestra interfas como clase app
    interfaz = APP()
    
    #iniciamos nuestra interfaz
    interfaz.iniciar()
