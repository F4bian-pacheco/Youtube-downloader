from audioop import mul
import eel
import sys
from tkinter import filedialog, Tk
import os
# from source import Downloader
import pafy
import json


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

@eel.expose
def get_info():
    data = get_data_from_js()
    url = data["url"]
    ext = data["ext"]

    multimedia = pafy.new(url)
    streams = multimedia.allstreams
    info = {"titulo": multimedia.title,"img": multimedia.thumb,"stream_list":str(streams)}
    print(type(info))
    info = json.dumps(info)
    return info


def get_path_from_js():
    return eel.get_path()()


def get_data_from_js():
    return eel.get_data()()


def track(*data):
    total = data[0]
    actual = data[1]
    porcentaje = int((actual/total)*100)
    print(f"progreso {porcentaje}% :{data[1]}")

@eel.expose
def download():
    ...



eel.start("index.html", size=(900, 600))

# TODO
# * Agregar check lists para opciones de mp4 u mp3
# *  Cambiar a boton buscar en lugar de descargar y agregar otro boton para descargar
# - obtener datos del recurso y mostrarlos antes de descargar
# * agregar barra de descarga (posible uso de hilos)
# * mejorar diseño ui (agregar menu)
# * refactorizar

#? Enlace de prueba: https://www.youtube.com/watch?v=woWR2HV-elU
