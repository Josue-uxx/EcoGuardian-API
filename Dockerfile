# 1. Usamos una imagen oficial de Python optimizada
FROM python:3.10-slim

# 2. Instalamos dependencias del sistema necesarias para OpenCV y YOLO
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 3. Establecemos la carpeta de trabajo dentro del servidor
WORKDIR /code

# 4. Copiamos el archivo de librerías e instalamos todo
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. Copiamos todo el resto de tus carpetas y archivos al servidor
COPY . .

# 6. Exponemos el puerto 7860 (el puerto estándar que usa Hugging Face)
CMD ["sh", "-c", "uvicorn api:app --host 0.0.0.0 --port $PORT"]
