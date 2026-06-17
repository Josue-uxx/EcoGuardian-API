from ultralytics import YOLO
from vision.classifier import classify
from assistant.history import save_detection

import cv2
import json
import time  # <--- IMPORTANTE: Para controlar el tiempo del historial

# Cargar mapa de objetos
with open("data/object_map.json", "r", encoding="utf-8") as f:
    object_map = json.load(f)

# Modelo YOLO
model = YOLO("yolov8n.pt")

# Cámara
camera = cv2.VideoCapture(0)

ultimo_objeto = ""
ultimo_tiempo_guardado = 0  # <--- Guarda el timestamp de la última detección registrada
COOLDOWN_HISTORIAL = 3  # <--- Segundos mínimos para volver a registrar el mismo objeto

while True:
    ret, frame = camera.read()
    if not ret:
        break

    results = model(frame)
    
    # Inicializar banderas para saber si se detectó algo válido en ESTE fotograma
    objeto_detectado_en_frame = False

    # Revisar detecciones
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            object_name = model.names[class_id]

            if object_name in object_map:
                material = object_map[object_name]
                resultado = classify(material)
                objeto_detectado_en_frame = True

                # Tiempo actual
                tiempo_actual = time.time()

                # Solo guarda si es un objeto diferente O si ya pasaron 3 segundos
                if material != ultimo_objeto or (tiempo_actual - ultimo_tiempo_guardado > COOLDOWN_HISTORIAL):
                    ultimo_objeto = material
                    ultimo_tiempo_guardado = tiempo_actual

                    save_detection(
                        material,
                        resultado["recyclable"],
                        resultado["compostable"]
                    )

                    print("\n===== EcoGuardian AI =====")
                    print(f"Objeto: {material}")
                    print(f"Reciclable: {'Si' if resultado['recyclable'] else 'No'}")
                    print(f"Compostable: {'Si' if resultado['compostable'] else 'No'}")
                    print(f"Recomendacion: {resultado['recommendation']}")

                # Actualizar los textos con lo que se está viendo actualmente
                texto_reciclable = f"Reciclable: {'Si' if resultado['recyclable'] else 'No'}"
                texto_compostable = f"Compostable: {'Si' if resultado['compostable'] else 'No'}"
                
                # Rompemos el bucle interno para procesar solo el objeto principal del frame
                break 
        if objeto_detectado_en_frame:
            break

    # Si en este fotograma no se detectó nada del mapa, limpiamos los textos de la pantalla
    if not objeto_detectado_en_frame:
        texto_reciclable = ""
        texto_compostable = ""

    # Dibujar detecciones YOLO
    annotated_frame = results[0].plot()

    # Mostrar clasificación en pantalla (solo si hay un objeto válido visible)
    if texto_reciclable:
        cv2.putText(
            annotated_frame,
            texto_reciclable,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    if texto_compostable:
        cv2.putText(
            annotated_frame,
            texto_compostable,
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2
        )

    cv2.imshow("EcoGuardian AI", annotated_frame)

    # ESC para salir
    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()