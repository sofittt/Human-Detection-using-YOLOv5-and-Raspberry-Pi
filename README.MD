# Detección de Humanos con YOLO v5

## Getting Started

A continuación se detalla una guia para poder intalar y correr el programa.

## Instalación

- Clonar el repositorio de GITHUB
- Vas a la pestaña de camera_module, abris el archivo README y seguis las intrucciones
- Vas a la pestaña de backend, abris el archivo README y seguis las intrucciones.
- Una vez que tenes todas las dependencias instaladas te vas a los archivos, app.py e camera_module.py y los corres en el de app.py te tira unos warning pero no hay problema y despues al final te tira la direccion del sitio web que es http://0.0.0.0:8000 en esta direccion cambia el 0.0.0.0 por la ip de tu computadora.


## Forma de trabajo del software 

El módulo de cámara toma fotos en un intervalo especificado y envía las imágenes al servidor backend. El servidor backend procesa las imágenes usando YOLOv5 para detectar humanos y envía el resultado al cliente como un archivo HTML codificado en base64 con renderizado del lado del servidor. El archivo HTML incluye la marca de tiempo y la imagen procesada.

## Reconocimientos

- YOLOv5 object detection model by [Ultralytics LLC](https://github.com/ultralytics/yolov5)
