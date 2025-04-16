import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import subprocess
import time

# Modeli yükle
model = load_model("ddos_model.keras")

# Özellik isimleri örnek (senin verine göre değişebilir)
ozellikler = ["duration", "src_bytes", "dst_bytes", "wrong_fragment", "urgent", "hot", "num_failed_logins", "num_compromised"]

# Sahte veri simülasyonu (normalde canlı trafik buraya gelir)
def yeni_gelen_veri():
    return {
        "ip": "192.168.1.100",
        "features": [0.0] * 45
    }


# IP engelleme komutu
def ip_engelle(ip):
    print(f"[!] Saldırı tespit edildi. IP engelleniyor: {ip}")
    subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])

# Ana döngü
while True:
    veri = yeni_gelen_veri()
    features = np.array([veri["features"]]).astype('float32')
    
    tahmin = model.predict(features)
    etiket = np.argmax(tahmin)

    if etiket == 1:  # 1 = saldırı
        ip_engelle(veri["ip"])
    else:
        print(f"{veri['ip']} => Normal trafik.")

    time.sleep(5)  # Her 5 saniyede bir yeni veri kontrol

