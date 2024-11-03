# Usar una imagen base de Python
FROM python:3.13-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . /app

# Instalar curl y las dependencias de la aplicación
RUN apt-get update && \
    apt-get install -y curl && \
    pip install --no-cache-dir Flask && \
    apt-get clean

# Exponer el puerto 5001
EXPOSE 5001

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
