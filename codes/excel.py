import pandas as pd

# Dosya yolunu belirt
dosya_yolu = r"C:\Users\Lenovo\Desktop\nsl_kdd_cleaned..csv"

# Veriyi oku
df = pd.read_csv(dosya_yolu, delimiter=";", header=0)  # İlk satır başlık olarak alınıyor

# Tüm string değerleri küçük harfe çevir ve boşlukları temizle
df['class'] = df['class'].str.lower().str.strip()

# Normal paketleri filtrele
normal_paketler = df[df['class'] == 'normal']

# DoS saldırılarını filtrele
dos_saldirilar = df[df['class'].isin(['neptune', 'smurf', 'back', 'teardrop', 'pod', 'land'])]

# Excel dosyalarına kaydet
normal_paketler.to_excel("normal_trafik.xlsx", index=False)
dos_saldirilar.to_excel("dos_saldiri.xlsx", index=False)

print("Normal ve DoS saldırıları ayrı Excel dosyalarına kaydedildi!")
