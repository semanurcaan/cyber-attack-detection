import pandas as pd
import requests
import random
import time

# Trafik dosyaları
NORMAL_DOSYA = "normal_trafik_numeric.xlsx"
SALDIRI_DOSYA = "dos_saldiri_numeric.xlsx"

# Sunucu adresi
SUNUCU_URL = "http://192.168.154.128:5000/gelen_paket"

# Dosyaları oku
df_normal = pd.read_excel(NORMAL_DOSYA)
df_saldiri = pd.read_excel(SALDIRI_DOSYA)

def excelden_karisik_paket_gonder():
    while True:
        # %50 ihtimalle saldırı ya da normal trafik seç
        if random.random() < 0.5:
            secilen_df = df_normal
        else:
            secilen_df = df_saldiri

        satir = secilen_df.sample(n=1).iloc[0].to_dict()

        try:
            response = requests.post(SUNUCU_URL, json=satir)
            print(f"Gönderilen etiket: {satir.get('label')} → Cevap: {response.status_code}")
        except Exception as e:
            print(f"Hata: {e}")

        time.sleep(random.uniform(0.5, 2))

if __name__ == "__main__":
    excelden_karisik_paket_gonder()

