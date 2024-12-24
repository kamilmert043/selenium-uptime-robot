# Python tabanlı bir Docker imajı kullan
FROM python:3.9-slim

# Gerekli bağımlılıkları yükle
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini ayarla
WORKDIR /app

# Gereken Python kütüphanelerini yükle
COPY .env .
COPY sendMail.py .
COPY sendRequest.py .
COPY databaseAuth.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Python betiğini kopyala
COPY main.py .

# Uygulamayı çalıştır
CMD ["python", "main.py"]
