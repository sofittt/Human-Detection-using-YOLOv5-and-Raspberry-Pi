## pre-setup

Antes de ejecutar los archivos de servicio, debe instalar las dependencias.
Puede instalarlos usando pip.

Para comprobar si pip está instalado o no, puede ejecutar 'python3 -m pip --version'
Debería ver una salida como esta
```bash
pip 22.3.1 from /home/ubuntu/.local/lib/python3.8/site-packages/pip (python 3.8)
```
Si no es así, asegúrese de instalar pip primero [ver](https://pip.pypa.io/en/stable/installation/)

Después de instalar pip. Instale las dependencias de los archivos de servicio ejecutando:
Esto es lo que hacemos siguiendo las intrucciones de los archicos README de backend y camara-module
```bash
cd ruta-a-la-carpeta-backend 
pip install -r requirements.txt
cd ../pi_cctv_camera 
pip install -r requirements.txt
```

## Para correr los servicios ejecutar los siguientes comandos:
IMPORTANTE hay q instalar un plugging para que te reconozca los servicios, en pycharm te lo tira como sugerencia
si ya instalaste el plugging vas a ver los archivos en forma de una tuerca con un simbolo OK 
y no hace falta correr los comando de abajo 
```bash

cd services
systemctl daemon-reload
systemctl enable backend.service
systemctl enable pi_camera.service
systemctl start backend.service
systemctl start pi_camera.service
```
