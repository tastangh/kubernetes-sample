## 1\. Proje Hakkında

Bu proje, Docker ve Kubernetes'in temel kavramlarını anlamak için oluşturulmuş basit bir web uygulamasıdır. Uygulama, bir backend API servisinden ve bu servisten veri çeken bir frontend arayüzünden oluşur.

**Kullanılan Teknolojiler ve Öğrenilen Kavramlar:**

  * **Backend:** Python (Flask)
  * **Frontend:** HTML, CSS, JavaScript (Nginx ile sunuluyor)
  * **Konteynerleştirme:** Docker, Dockerfile
  * **Orkestrasyon:** Kubernetes (Minikube ile yerel kurulum)
  * **Kubernetes Nesneleri:** `Deployment`, `Service` (`NodePort` ve `ClusterIP`)
  * **Uygulama Güncelleme:** `Rolling Update` (Kademeli Güncelleme) stratejisi

## 2\. Proje Mimarisi

  * **Frontend Servisi:** Kullanıcının tarayıcıda gördüğü arayüzü sunan bir Nginx konteyneridir. Dış dünyaya `NodePort` (30001) ile açılır.
  * **Backend Servisi:** Frontend'e JSON formatında bir mesaj dönen bir Flask API sunucusudur. Dış dünyaya `NodePort` (30002) ile açılır ve frontend tarafından bu port üzerinden çağrılır.

## 3\. Gereksinimler

Bu projeyi kendi bilgisayarınızda kurmak için gereken araçlar:

  * **Docker:** Konteynerleri oluşturmak ve yönetmek için.
  * **Minikube:** Yerel bir Kubernetes kümesi oluşturmak için.
  * **kubectl:** Kubernetes kümesiyle iletişim kurmak için komut satırı aracı.

## 4\. Kurulum ve Çalıştırma Adımları

**Adım 1: Proje Dosyalarını Oluşturun**
Projenin tüm dosyalarını içeren klasör yapısını oluşturun. (Dosyaların tam içerikleri aşağıda "Dosya İçerikleri" bölümünde verilmiştir.)

**Adım 2: Docker İmajlarını Oluşturun**
Projenin ana dizinindeyken, her servis için Docker imajlarını oluşturun.

```bash
# Backend imajını oluştur (v1.0)
docker build -t kubernetes-sample-backend:1.0 ./backend

# Frontend imajını oluştur (v1.0)
docker build -t kubernetes-sample-frontend:1.0 ./frontend
```

**Adım 3: Minikube Kubernetes Cluster'ını Başlatın**
Bilgisayarınızda yerel bir Kubernetes kümesi başlatın.

```bash
minikube start --driver=docker
```

*(Eğer network sorunları yaşarsanız `--kubernetes-version=v1.28.3` gibi belirli bir versiyonla başlatmayı deneyebilirsiniz.)*

**Adım 4: Lokal İmajları Minikube'e Yükleyin**
Oluşturduğunuz Docker imajlarını Minikube'ün kendi ortamına yükleyerek Kubernetes'in bu imajları bulmasını sağlayın.

```bash
minikube image load kubernetes-sample-backend:1.0
minikube image load kubernetes-sample-frontend:1.0
```

**Adım 5: Kubernetes'e Uygulamayı Dağıtın**
`kubernetes/` klasöründeki tüm YAML yapılandırma dosyalarını kümenize uygulayın.

```bash
kubectl apply -f kubernetes/
```

**Adım 6: Doğrulama**
Pod'ların ve servislerin doğru bir şekilde çalıştığını kontrol edin.

```bash
# Pod'ların "Running" durumuna gelmesini bekleyin
kubectl get pods

# Servislerin oluştuğunu ve portların doğru olduğunu kontrol edin
kubectl get services
```

**Adım 7: Uygulamaya Erişin**
Tarayıcınızı açın ve frontend servisi için atanan port olan **30001**'e gidin:
[http://localhost:30001](https://www.google.com/search?q=http://localhost:30001)

-----

## 5\. Geliştirme Döngüsü: Bir Güncelleme Nasıl Yapılır?

`backend` servisinde bir değişiklik yaptığınızda izlemeniz gereken adımlar:

1.  **Kodu Değiştirin:** `backend/app.py` dosyasında istediğiniz değişikliği yapın.
2.  **Yeni İmaj Oluşturun:** Değişikliği yansıtmak için **yeni bir versiyon etiketi** ile imajınızı tekrar oluşturun.
    ```bash
    docker build -t kubernetes-sample-backend:1.1 ./backend
    ```
3.  **Yeni İmajı Minikube'e Yükleyin:**
    ```bash
    minikube image load kubernetes-sample-backend:1.1
    ```
4.  **Deployment YAML'ını Güncelleyin:** `kubernetes/backend-deployment.yaml` dosyasını açın ve `image` alanını yeni etiketle (`:1.1`) değiştirin.
5.  **Güncellemeyi Uygulayın:** Değişikliği Kubernetes'e bildirin. Kubernetes, kesinti olmadan kademeli bir güncelleme (`Rolling Update`) yapacaktır.
    ```bash
    kubectl apply -f kubernetes/backend-deployment.yaml
    ```
6.  **Doğrulayın:** `kubectl get pods -w` komutuyla yeni pod'ların oluşmasını izleyin ve tarayıcıda değişikliği kontrol edin.

-----

## 6\. Proje Dosya Yapısı

```
kubernetes-sample/
├── backend/
│   ├── app.py
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── Dockerfile
└── kubernetes/
    ├── backend-deployment.yaml
    ├── backend-service.yaml
    ├── frontend-deployment.yaml
    └── frontend-service.yaml
```

-----