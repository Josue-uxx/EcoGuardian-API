from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import cv2
from ultralytics import YOLO

from datetime import datetime


app = FastAPI(title="EcoScore API - Mapeo de Funciones Directas")

from assistant.actions import *
import json
import random
import subprocess
import sys

# --- IMPORTACIONES DE TUS MÓDULOS INTERNOS REALES ---
from vision.classifier import classify

try:
    from assistant.ecotips import get_tip
except ImportError:
    get_tip = lambda: "¡Reduce, reutiliza y recicla para proteger el planeta!"

try:
    from assistant.recycling_guide import get_recycling_guide
except ImportError:
    get_recycling_guide = lambda: "Separa adecuadamente plásticos, vidrios y cartón limpios."

try:
    from assistant.compost_guide import get_compost_guide
except ImportError:
    get_compost_guide = lambda: "Utiliza restos de frutas, verduras y cáscaras para tu compost."

try:
    from assistant.statistics import get_statistics
except ImportError:
    get_statistics = lambda: {"total": 231, "reciclado": 142, "organico": 89}


# --- CONFIGURACIÓN DE CORS INTEGRADA ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("data/object_map.json", "r", encoding="utf-8") as f:
    object_map = json.load(f)

# ==========================================================
# YOLO + CAMARA
# ==========================================================

model = YOLO("yolov8n.pt")
camera = cv2.VideoCapture(0)

ultima_deteccion = {
    "objeto": "",
    "reciclable": False,
    "compostable": False,
    "recommendation": ""
}

def generate_frames():

    global ultima_deteccion

    while True:

        success, frame = camera.read()

        if not success:
            break

        results = model(frame)

        # Reiniciar estado
        deteccion_encontrada = False

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])
                object_name = model.names[class_id]

            if object_name in object_map:

                    deteccion_encontrada = True

                    material = object_map[object_name]

                    resultado = classify(material)

                    ultima_deteccion = {
                        "detectado": True,
                        "objeto": material,
                        "reciclable": resultado["recyclable"],
                        "compostable": resultado["compostable"],
                        "recommendation": resultado["recommendation"]
                    }

                    break

        # Si no detectó nada
        if not deteccion_encontrada:

            ultima_deteccion = {
                "detectado": False,
                "objeto": None,
                "reciclable": False,
                "compostable": False,
                "recommendation": ""
            }

        annotated_frame = results[0].plot()

        ret, buffer = cv2.imencode(".jpg", annotated_frame)

        frame_bytes = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame_bytes +
            b'\r\n'
        )

  

@app.get("/video_feed")
def video_feed():

    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )

def generar_frames():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()

        if not success:
            break

        _, buffer = cv2.imencode(".jpg", frame)

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            buffer.tobytes() +
            b'\r\n'
        )

@app.get("/api/deteccion")
def obtener_deteccion():

    return ultima_deteccion
# ============================================================================
# --- FUNCIÓN: ABRIR CÁMARA DIRECTA (ABRE EL SCRIPT SIN ENTRAR AL PANEL) ---
# ============================================================================
@app.get("/api/clasificar-camara")
def clasificar_desde_camara_local():

    return {
        "status": "success",
        "mensaje": "Streaming iniciado",
        "video_url": "https://ecoguardian-api-production.up.railway.app/video_feed"
    }


# ============================================================================
# --- FUNCIÓN: CONSEJO ECOLÓGICO DIRECTO ---
# ============================================================================
import random

@app.get("/api/consejo")
def consejo():

    consejos = [

        "Apaga las luces cuando no las uses.",

        "Usa bolsas reutilizables.",

        "Separa los residuos reciclables.",

        "Reduce el consumo de plástico.",

        "Aprovecha el agua de lluvia.",

        "Composta los residuos orgánicos.",

        "Desconecta cargadores que no estés usando."

    ]

    return {
        "status": "success",
        "consejo": random.choice(consejos)
    }


# ============================================================================
# --- FUNCIÓN: GUÍA DE RECICLAJE DIRECTA ---
# ============================================================================
@app.get("/api/guia-reciclaje")
def obtener_guia_reciclaje():
    return {
        "status": "success",
        "objeto": "GUÍA DE RECICLAJE",
        "reciclable": True,
        "compostable": False,
        "recomendacion": get_recycling_guide(),
        "esp32_status": "Ok"
    }


# ============================================================================
# --- FUNCIÓN: GUÍA DE COMPOSTAJE DIRECTA ---
# ============================================================================
@app.get("/api/guia-compostaje")
def obtener_guia_compostaje():
    return {
        "status": "success",
        "objeto": "GUÍA DE COMPOSTAJE",
        "reciclable": False,
        "compostable": True,
        "recomendacion": get_compost_guide(),
        "esp32_status": "Ok"
    }


# ============================================================================
# --- FUNCIÓN: MÉTRICAS Y GRÁFICOS DIRECTOS ---
# ============================================================================
@app.get("/api/historial")
def obtener_historial():

    return {
    "total": 442,
    "reciclables": 440,
    "compostables": 97,
    "score": 977,
    "level": "🏆 EcoHéroe"
}

# ==========================================================
# CHAT ECOLOGICO
# ==========================================================


@app.get("/api/chat")
def abrir_chat():

    return {
        "status": "success",
        "mensaje": "Chat ecológico conectado"
    }

# ==========================================================
# ECOSCORE
# ==========================================================

@app.get("/api/ecoscore")
def abrir_ecoscore():

    return {
        "status": "success",
        "score": 977,
        "level": "🏆 EcoHéroe"
    }

# ==========================================================
# REPORTE
# ==========================================================

@app.get("/api/reporte")
def generar_reporte():

    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    contenido = f"""
========== REPORTE ECOGUARDIAN AI ==========

Fecha: {fecha}

Objetos detectados: 293
Reciclables: 292
Compostables: 77
EcoScore: 661
Nivel: 🏆 EcoHéroe

===========================================
"""

    nombre_archivo = f"reporte_{fecha}.txt"

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

    return {
        "status": "success",
        "mensaje": "Reporte generado exitosamente",
        "reporte": contenido
    }
# ==========================================================
# GRAFICOS
# ==========================================================

@app.get("/api/graficos")
def ver_graficos():

    try:

        get_chart()

        return {
            "status": "success",
            "mensaje": "Grafico abierto"
        }

    except Exception as e:

        return {
            "status": "error",
            "error": str(e)
        }


# ==========================================================
# LOGROS
# ==========================================================

@app.get("/api/logros")
def obtener_logros():

    return {
        "logros": [
            "🥉 Primer reciclaje",
            "🥈 100 objetos clasificados",
            "🥇 EcoMaster",
            "🏆 EcoHéroe"
        ]
    }


# ==========================================================
# HOGAR
# ==========================================================

@app.get("/api/hogar")
def abrir_hogar():

    try:

        open_home()

        return {
            "status": "success",
            "mensaje": "Asistente del hogar abierto"
        }

    except Exception as e:

        return {
            "status": "error",
            "error": str(e)
        }


# ==========================================================
# METAS
# ==========================================================

@app.get("/api/metas")
def obtener_metas():

    return {
        "metas": [
            "♻️ Reciclar 500 objetos",
            "🌱 Compostar 100 residuos",
            "🏆 Alcanzar EcoScore 1000"
        ],
        "progreso": "100%"
    }
    
@app.get("/api/estadisticas")
def estadisticas():

    return {
        "total": 442,
        "reciclables": 440,
        "compostables": 97,
        "no_reciclables": 2,
        "score": 977,
        "level": "🏆 EcoHéroe"
    }
@app.get("/")
def home():
    return {
        "status": "online",
        "api": "EcoGuardian",
        "message": "API funcionando correctamente"
    }
