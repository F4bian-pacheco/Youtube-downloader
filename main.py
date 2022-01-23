import eel
import sys
from tkinter import filedialog, Tk
import os
# from source import Downloader
import pafy
import json

#Se inicializa el proyecto eel en una ruta
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

    multimedia = pafy.new(url)
    streams = multimedia.allstreams
    sizes = [bytes_mb(i.get_filesize()) for i in streams]
    info = {"titulo": multimedia.title,"img": multimedia.thumb,"stream_list":str(streams),"stream_size":str(sizes)}
    info = json.dumps(info)
    return info

def get_path_from_js():
    return eel.get_path()()


def get_data_from_js():
    return eel.get_data()()

# def get_stream_from_js():
#     return eel.send_data()()

def bytes_mb(input):
    a = input / 1048576
    return round(a,2)


def track(*data):
    total = data[0]
    actual = data[1]
    porcentaje = int((actual/total)*100)
    print(f"progreso {porcentaje}% :{data[1]}")

@eel.expose
def download(data,url,path):
    data_cl = list(map(lambda x: x.lstrip(), data))
    try:
        video = pafy.new(url)
        streams = video.allstreams
        all_streams = list(map(str,streams))
        print(data_cl)
        print(all_streams[:5])
        for i,j in enumerate(data_cl):
            if j in all_streams:
                print("entro", j,"-",type(streams[i]), streams[all_streams.index(j)])
                elemento = streams[all_streams.index(j)]
                elemento.download(path,meta=True)
    except Exception:
        raise ValueError("Ha ocurrido un error")


eel.start("index.html", size=(900, 600))

# TODO
# * Agregar check lists para opciones de mp4 u mp3
# *  Cambiar a boton buscar en lugar de descargar y agregar otro boton para descargar
# - obtener datos del recurso y mostrarlos antes de descargar
# * agregar barra de descarga (posible uso de hilos)
# * mejorar diseño ui (agregar menu)
# * refactorizar
# * cuando busco, resetear la lista de resultados

#? Enlace de prueba: https://www.youtube.com/watch?v=woWR2HV-elU
