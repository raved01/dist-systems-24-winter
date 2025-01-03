FROM python:3.10-slim

WORKDIR /app

# Kopieren Sie den Inhalt des backend-Ordners
COPY backend/ /app/

# Requirements installieren
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]