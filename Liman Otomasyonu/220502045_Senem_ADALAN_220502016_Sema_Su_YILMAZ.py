import pandas as pd
import tkinter as tk
from tkinter import PhotoImage

# Olaylar.csv ve Gemiler.csv dosyalarını oku
olaylar_df = pd.read_csv("olaylar.csv", encoding='ISO-8859-9')
gemiler_df = pd.read_csv("gemiler.csv", encoding='ISO-8859-9')

# Tır ve Gemi bilgilerini içeren sınıfları oluştur
class Tir:
    def __init__(self, plaka, ulke, ton20, ton30, yuk_miktari, maliyet, gelis_zamani):
        self.ad = "1000" if plaka == "41_kostu_1000" else plaka[-3:]
        self.plaka = plaka
        self.ulke = ulke
        self.ton20 = ton20
        self.ton30 = ton30
        self.yuk_miktari = yuk_miktari
        self.maliyet = maliyet
        self.gelis_zamani = gelis_zamani
        self.bilgi_sozlugu = {
            'ulke': ulke,
            'ton20_adet': ton20,
            'ton30_adet': ton30,
            'yuk_miktari': yuk_miktari,
            'maliyet': maliyet,
            'yuk': []
        }

class Gemi:
    def __init__(self, adi, kapasite, gidecek_ulke, gelis_zamani):
        self.adi = adi
        self.kapasite = kapasite
        self.gidecek_ulke = gidecek_ulke
        self.gelis_zamani = gelis_zamani
        self.yuk = Stack()
        self.bilgi_sozlugu = {
            'adi': adi,
            'kapasite': kapasite,
            'gidecek_ulke': gidecek_ulke,
            'yuk': self.yuk.items,
            'yük_miktarı': 0
        }

#Liman bilgilerini içeren sınıfı oluştur
class Liman:
    def __init__(self):
        self.istif_alani1 = Stack()
        self.istif_alani2 = Stack()
        self.max_kapasite = 750

    def yuk_indir(self, yuk):
        indirilen_tonaj = sum([y['yuk_miktari'] for y in yuk])
        if indirilen_tonaj > self.max_kapasite:
            print(f"İstif alanı kapasitesi aşıldı. İkinci istif alanına geçiliyor.")
            self.istif_alani2.push(yuk)
            print(f"{indirilen_tonaj} ton yük ikinci istif alanına önceki yüklerin üzerine yerleştirildi.","\n")
        else:
            print(f"{indirilen_tonaj} ton yük istif alanına indiriliyor.")
            for y in yuk:
                self.istif_alani1.push([y])  # Her yükü ayrı bir listeye koy
            print(f"{indirilen_tonaj} ton yük birinci istif alanına önceki yüklerin üzerine yerleştirildi.", "\n")

    def bosalt(self):
        if not self.istif_alani1.is_empty():
            print("İstif alanı boşaltılıyor.")
            kenara_alinan_yukler = self.istif_alani1.peek()[-1 * t.yuk_miktari:]   # İlgili yükün üstündeki yükleri kenara al
            self.istif_alani1.pop()  # İlk istif alanındaki yükü çıkar
            self.istif_alani1.items += kenara_alinan_yukler  # Kenara alınan yükleri üste yerleştir

            total_load = sum([y['yuk_miktari'] for y in self.istif_alani1.peek()[0]])   # İstif alanındaki toplam yükü hesapla
            print(f"İstif alanındaki toplam yük: {total_load} ton")
        else:
            print("İstif alanı boş.")

    def gemileri_beklet(self, t_grubu, gemiler):
        loading_message_printed = False
        for t in t_grubu:
            uygun_gemi_bulundu = False
            for gemi in gemiler:
                if gemi.gidecek_ulke == t.ulke and gemi.gelis_zamani <= t.gelis_zamani:
                    uygun_gemi_bulundu = True
                    gemi.yuk.push(t.bilgi_sozlugu['yuk'])
                    if not loading_message_printed:
                        print(f"Gemi Yükleniyor:")
                        loading_message_printed = True
                    print(f"   - Gemi: {gemi.adi}, Ülke: {gemi.gidecek_ulke}, "
                          f"Kapasite: {gemi.kapasite} ton, {t.plaka} plakalı Tır yüklendi.")
                    break
            else:
                if not uygun_gemi_bulundu:
                    print(f"{t.plaka}'nın uygun olduğu gemi bulunamadı. Yük istif alanında bekletiliyor.")
                    self.istif_alani1.push([t])

class Stack:    #Yüklerin üst üste istiflenebilmesi için stack sınıfı oluştur
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items

    def size(self):
        return len(self.items)

#Liman nesnesi ve Tır/Gemi listeleri oluştur
tirlar = []
gemiler = []
liman = Liman()

# Olaylar.csv'den tırların listesini oluştur
for index, row in olaylar_df.iterrows():
    plaka = row['tır_plakası']
    ulke = row['ülke']
    ton20 = row['20_ton_adet']
    ton30 = row['30_ton_adet']
    yuk_miktari = row['yük_miktarı']
    maliyet = row['maliyet']
    gelis_zamani = row['geliş_zamanı']
    t = Tir(plaka, ulke, ton20, ton30, yuk_miktari, maliyet, gelis_zamani)
    tirlar.append(t)
    t.bilgi_sozlugu['gemi'] = None

# Gemiler.csv'den gemilerin listesini oluştur
for index, row in gemiler_df.iterrows():
    adi = row['gemi_adı']
    kapasite = row['kapasite']
    gidecek_ulke = row['gidecek_ülke']
    gelis_zamani = row['geliş_zamanı']
    g = Gemi(adi, kapasite, gidecek_ulke, gelis_zamani)
    gemiler.append(g)

gemiler.sort(key=lambda x: x.kapasite, reverse=True)   #Gemileri kapasitelerine göre sırala
tirlar.sort(key=lambda x: (x.gelis_zamani, x.plaka))   #Tırları geliş zamanına ve plaka numarasına göre sırala

gruplar = {}
for t in tirlar:
    if t.gelis_zamani in gruplar:
        gruplar[t.gelis_zamani].append(t)
    else:
        gruplar[t.gelis_zamani] = [t]


def sirali_tirlar():
    tirlar_sirali = sorted(tirlar, key=lambda x: (x.ad == "1000", x.ad))
    print("\nSıralı Tırlar:")
    plakalar = set()
    for tir in tirlar_sirali:
        if tir.plaka not in plakalar:
            print(f"Tır Plakası: {tir.plaka}, Tır Adı: {tir.ad}")
            plakalar.add(tir.plaka)

def tir_bilgileri():
    plaka = input("Hangi Tır'ın bilgilerini görmek istiyorsunuz? (Örneğin: 41_kostu_001): ")
    secili_tir = next((tir for tir in tirlar if tir.plaka == plaka), None)
    if secili_tir:
        print(f"\nTır Plakası: {secili_tir.plaka}, Tır Adı: {secili_tir.ad}")
        girisler = sorted(zip(olaylar_df[(olaylar_df['tır_plakası'] == plaka)]['geliş_zamanı'],
                              olaylar_df[(olaylar_df['tır_plakası'] == plaka)]['ülke'],
                              olaylar_df[(olaylar_df['tır_plakası'] == plaka)]['20_ton_adet'],
                              olaylar_df[(olaylar_df['tır_plakası'] == plaka)]['30_ton_adet'],
                              olaylar_df[(olaylar_df['tır_plakası'] == plaka)]['yük_miktarı'],
                              olaylar_df[(olaylar_df['tır_plakası'] == plaka)]['maliyet']
                              ))

        # Her bir giriş için ayrı satırlar oluştur
        for guncel_gelis_zamani, ulke, ton20_adet, ton30_adet, yuk_miktari, maliyet in girisler:
            print(f"Geliş Zamanı: {guncel_gelis_zamani}")
            print(f"Ülkeler: {ulke}")
            print(f"20_ton_konteyner_adedi: {ton20_adet}")
            print(f"30_ton_konteyner_adedi: {ton30_adet}")
            print(f"Yük_miktarı: {yuk_miktari}")
            print(f"Maliyet: {maliyet}", "\n")
    else:
        print("Belirtilen Tır bulunamadı.")

def gemi_bilgileri():
    print("\nGemi Bilgileri:")
    for index, row in gemiler_df.iterrows():
        adi = row['gemi_adı']
        kapasite = row['kapasite']
        gidecek_ulke = row['gidecek_ülke']
        gelis_zamani = row['geliş_zamanı']

        print(f"Gemi Adı: {adi}, Kapasite: {kapasite} ton, Gidecek Ülke: {gidecek_ulke}, Geliş Zamanı: {gelis_zamani}")

def tirlari_indir():
    for gelis_zamani, t_grubu in gruplar.items():
        print("----------------------------------------------")
        print(f"Zaman: {gelis_zamani}")

        for gemi in gemiler:
            if gemi.gidecek_ulke == t_grubu[0].ulke and gemi.gelis_zamani == gelis_zamani:
                print(f"Gemi Geliyor: Gemi: {gemi.adi} (Ülke: {gemi.gidecek_ulke}) - Kapasite: {gemi.kapasite} ton")
                break

        print("Tırlar İndiriliyor:")
        for t in t_grubu:
            print(f"   - Tır: {t.plaka}, Ülke: {t.ulke}, 20 ton konteyner: {t.ton20} adet, 30 ton konteyner: {t.ton30} adet")
            total_ton20 = t.ton20 * 20
            total_ton30 = t.ton30 * 30
            total_ton = total_ton20 + total_ton30
            print(f"   - İstif Alanına {total_ton} ton konteyner indiriliyor. (Üst üste, Plaka: {t.plaka})")

        liman.gemileri_beklet(t_grubu, gemiler)

def cikis():
    root.destroy()


root = tk.Tk()
root.title("Liman Otomasyon Sistemi")

# Arka plan resmini yükle
resim_image = PhotoImage(file="liman.png")
resim_label = tk.Label(root, image=resim_image)
resim_label.place(relwidth=1, relheight=1)

menu_label = tk.Label(root, text="Menü:")
menu_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Butonları ekle
sirali_tirlar = tk.Button(root, text="1. Tırları Göster", command=sirali_tirlar)
sirali_tirlar.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

tir_bilgileri = tk.Button(root, text="2. Tır Bilgilerini Göster", command=tir_bilgileri)
tir_bilgileri.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

gemi_bilgileri = tk.Button(root, text="3. Gemi Bilgilerini Göster", command=gemi_bilgileri)
gemi_bilgileri.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

tirlari_indir = tk.Button(root, text="4. Simülasyonu Başlat", command=tirlari_indir)
tirlari_indir.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

cikis = tk.Button(root, text="5. Çıkış", command=cikis)
cikis.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

root.mainloop()











