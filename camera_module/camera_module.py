import argparse
import base64
import time
from argparse import ArgumentParser
from datetime import datetime
from cv2 import VideoCapture, imencode
from requests import post


def capture_timelapsed_images(url: str, delay: int = 10, port: int = 0) -> None:
    cam_port: int = port
    delay_between_captures: int = delay
    cam = VideoCapture(cam_port)

    if not cam.isOpened():
        print(f"No se pudo abrir la cámara en el puerto {cam_port}")
        return

    try:
        while True:
            result, image = cam.read()
            if result:
                _, im_arr = imencode('.jpg', image)
                im_bytes = im_arr.tobytes()
                im_b64: bytes = base64.b64encode(im_bytes)
                decoded_base64_str: str = im_b64.decode("utf-8")
                json_to_send = {
                    "data": decoded_base64_str,
                    "timestamp": str(datetime.now())
                }
                try:
                    post(url, json=json_to_send)
                except Exception as e:
                    print(f"Error al enviar la imagen: {e}")
            time.sleep(delay_between_captures)
    except KeyboardInterrupt:
        print("Interrupción detectada, liberando recursos.")
    finally:
        cam.release()


def arg_parser() -> argparse.Namespace:
    parser: ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, nargs="?",
                        help="URL para enviar las imágenes capturadas",
                        default="http://localhost:8000")
    parser.add_argument("delay", type=int, nargs="?",
                        help="Tiempo en segundos entre capturas de imágenes.",
                        default=10)
    parser.add_argument("port", type=int, nargs="?",
                        help="Puerto de la cámara a ser utilizado (0, 1, 2, etc.).",
                        default=1)  # Cambia este valor al índice de la cámara USB
    opt: argparse.Namespace = parser.parse_args()
    return opt


def main() -> None:
    args: argparse.Namespace = arg_parser()
    delay: int = args.delay
    port: int = args.port
    url: str = args.url
    capture_timelapsed_images(delay=delay, port=port, url=url)


if __name__ == "__main__":
    main()