# backend/Dockerfile

# Python 3.9'u temel al
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinimleri kopyala ve kur
# Bu örnekte basitlik için doğrudan app.py'yi kopyalıyoruz
# Gerçek projede bir requirements.txt dosyası kullanmak daha iyidir
COPY app.py .
RUN pip install Flask Flask-Cors

# Uygulamanın çalışacağı port
EXPOSE 5000

# Uygulamayı başlat
CMD ["python", "app.py"]