# Imagine de bază
FROM python:3.10-slim

# Setare director de lucru
WORKDIR /app

# Copierea fișierelor necesare
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Expunere portului pentru Flask
EXPOSE 5001

# Comanda de rulare a aplicației
CMD ["python", "main.py"]
