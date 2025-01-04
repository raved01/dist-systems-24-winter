FROM python:3.10-slim

WORKDIR /app

# Kopieren Sie den Inhalt des backend-Ordners
COPY backend/ /app/

# Requirements installieren
RUN pip install --no-cache-dir -r requirements.txt

# Migrations beim Start ausführen
RUN chmod +x /app/entrypoint.sh

EXPOSE 80

# Ändern des Befehls, um auf 0.0.0.0:80 zu hören
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]