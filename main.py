import eel,sys
from tkinter import filedialog, Tk
import os
from source import Downloader


sys.path.append("..")
eel.init("web")

@eel.expose
def change_directory():
    root = Tk()
    root.withdraw()
    path = filedialog.askdirectory(initialdir=os.getcwd())
    return path

@eel.expose
def get_path():
    return os.getcwd()

def get_path_from_js():
    return eel.get_path()()

def get_url_from_js():
    return eel.get_url()()

@eel.expose
def download():
    path = get_path_from_js()
    url = get_url_from_js()
    downloader = Downloader(url)
    res = downloader.get_audio(path)
    
    if res:
        return "<p>archivo descargado con exito</p>"
    else:
        return "<p>error al descargar, intente nuevamente</p>"




eel.start("index.html",size=(700,500))

#TODO
#* Agregar check lists para opciones de mp4 u mp3
#* agregar barra de descarga (posible uso de hilos)
#* mejorar diseño ui (agregar menu)
#* refactorizar
