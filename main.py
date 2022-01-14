import eel
import sys
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


def get_data_from_js():
    return eel.get_data()()


@eel.expose
def download():
    path = get_path_from_js()
    data = get_data_from_js()
    url = data["url"]
    ext = data["ext"]
    print(ext)
    downloader = Downloader(url)
    if ext == "mp3":
        res = downloader.get_audio(path)
    elif ext == "mp4":
        res = downloader.get_video(path)
    else:
        res = False

    if res:
        return "<p>archivo descargado con exito</p>"
    else:
        return "<p>error al descargar, intente nuevamente</p>"


eel.start("index.html", size=(700, 500))

# TODO
# * Agregar check lists para opciones de mp4 u mp3
# *  Cambiar a boton buscar en lugar de descargar y agregar otro boton para descargar
# - obtener datos del recurso y mostrarlos antes de descargar
# * agregar barra de descarga (posible uso de hilos)
# * mejorar diseño ui (agregar menu)
# * refactorizar
