# Usar una imagen base de Python
FROM python:3.13-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir Flask

# Exponer el puerto 5001
EXPOSE 5001

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
