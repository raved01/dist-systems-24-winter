FROM python:3.10-slim

WORKDIR /app

# Kopieren Sie den Inhalt des backend-Ordners
COPY backend/ /app/

# Kopiere wait-for-it.sh und mache es ausführbar
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Requirements installieren
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["wait-for-it.sh", "db:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]