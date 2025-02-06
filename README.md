# 🚢 Port Automation

Bu proje bir liman otomasyon sistemini simüle eder. Tırların ve gemilerin yönetimi, yüklerin istiflenmesi ve gemilere yüklenmesi gibi işlemleri gerçekleştirir. Proje, `olaylar.csv` ve `gemiler.csv` dosyalarından veri okuyarak tır ve gemi bilgilerini işler.

## 📋 Proje Açıklaması
- **Yapılış Tarihi:** 7 Aralık 2023  
- **Son Güncelleme:** 6 Şubat 2025
 
Proje bir limanın günlük operasyonlarını otomatikleştirmek için tasarlanmıştır. Tırlar, limana belirli zamanlarda gelir ve yüklerini istif alanına bırakır. Gemiler, bu yükleri alarak hedef ülkelere taşır. Sistem, tır ve gemi bilgilerini CSV dosyalarından okur ve bu bilgileri kullanarak simülasyonu gerçekleştirir.

## 🌟 Ana Özellikler
- **Tır Yönetimi**: Tırların plaka, ülke, yük miktarı ve maliyet bilgilerini yönetir.
- **Gemi Yönetimi**: Gemilerin adı, kapasitesi, gideceği ülke ve geliş zamanı bilgilerini yönetir.
- **İstif Alanı Yönetimi**: Yüklerin istif alanına indirilmesi ve gemilere yüklenmesi işlemlerini simüle eder.
- **Simülasyon**: Tırların ve gemilerin zaman içindeki hareketlerini simüle eder.

## 🚀 Başlarken
Bu projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler
- Python 3.x
- pandas kütüphanesi
- tkinter kütüphanesi

### Kurulum
1. Repoyu klonlayın:
    ```bash
    git clone https://github.com/SenemAdalan/Port_Automation.git
    ```
2. Proje dizinine gidin:
    ```bash
    cd Port_Automation
    ```
3. Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install pandas
    ```
4. Projeyi çalıştırın:
    ```bash
    python main.py
    ```

## 🛠️ Kullanım
Proje, bir GUI (Grafiksel Kullanıcı Arayüzü) üzerinden çalışır. Aşağıdaki seçeneklerle liman operasyonlarını simüle edebilirsiniz:

- **Tırları Göster**: Tırların plaka ve ad bilgilerini listeler.
- **Tır Bilgilerini Göster**: Belirli bir tırın detaylı bilgilerini gösterir.
- **Gemi Bilgilerini Göster**: Gemilerin ad, kapasite, gideceği ülke ve geliş zamanı bilgilerini listeler.
- **Simülasyonu Başlat**: Tırların yüklerini indirme ve gemilere yükleme işlemlerini simüle eder.
- **Çıkış**: Programdan çıkar.

## 🖥️ Proje Arayüzü
![Image](https://github.com/user-attachments/assets/17c5f393-4f3d-4b93-8ebf-bc2596f7dc40)
