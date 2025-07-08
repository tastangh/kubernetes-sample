### **Kurulum ve Çalıştırma: Adım Adım Kılavuz**

Bu bölüm, temiz bir sistemden çalışan bir uygulamaya kadar olan tüm süreci içerir.

#### **Geliştirme Ortamının Kurulması**

Projemiz, yaşanan ağ sorunları nedeniyle en stabil ve sorunsuz çalışan **Docker Desktop** ile kurulmuştur.

**Adım 1: Docker Desktop'ı Kurun**

1.  [Docker'ın resmi web sitesinden](https://www.docker.com/products/docker-desktop/) Linux için olan **.deb** paketini indirin.
2.  Terminal üzerinden `İndirilenler` klasörüne gidin ve paketi `apt` ile kurun:
    ```bash
    cd ~/İndirilenler
    sudo apt-get update
    sudo apt-get install ./docker-desktop-*.deb
    ```

**Adım 2: Docker Desktop İçindeki Kubernetes'i Etkinleştirin**

1.  Uygulamalar menüsünden **Docker Desktop**'ı başlatın.
2.  Uygulama arayüzünde, sağ üstteki **Ayarlar (⚙️) simgesine** tıklayın.
3.  **"Kubernetes"** sekmesine gidin.
4.  **"Enable Kubernetes"** kutucuğunu işaretleyin.
5.  **"Apply & Restart"** butonuna basın. Docker Desktop, gerekli tüm bileşenleri indirip Kubernetes'i sizin için başlatacaktır.

**Adım 3: Ortamı Doğrulayın**
Kurulum tamamlandıktan sonra **yeni bir terminal** açın ve kümenizin durumunu kontrol edin:

```bash
kubectl get nodes
```

Çıktıda `STATUS`'u `Ready` olan bir `docker-desktop` düğümü görmelisiniz. Bu, ortamınızın hazır olduğu anlamına gelir.