# Detección de Humanos con YOLO v5

## Getting Started

A continuación se detalla una guia para poder intalar y correr el programa.

## Instalación

- Clonar el repositorio de GITHUB
- Vas a la pestaña de camera_module, abris el archivo README y seguis las intrucciones
- Vas a la pestaña de backend, abris el archivo README y seguis las intrucciones.

## Forma de trabajo del software 

El módulo de cámara toma fotos en un intervalo especificado y envía las imágenes al servidor backend. El servidor backend procesa las imágenes usando YOLOv5 para detectar humanos y envía el resultado al cliente como un archivo HTML codificado en base64 con renderizado del lado del servidor. El archivo HTML incluye la marca de tiempo y la imagen procesada.

## Reconocimientos

- YOLOv5 object detection model by [Ultralytics LLC](https://github.com/ultralytics/yolov5)
