import pandas as pd
import matplotlib.pyplot as plt
dosya_yolu = r"C:\Users\Lenovo\Desktop\nsl_kdd_cleaned..csv"

# Dosyayı tekrar oku
df = pd.read_csv(dosya_yolu, delimiter=";", low_memory=False)

# Sayısal olması gereken sütunları belirle
numeric_columns = [
    "duration", "src_bytes", "dst_bytes", "wrong_fragment", "urgent", "hot",
    "num_failed_logins", "logged_in", "num_compromised", "root_shell", "su_attempted",
    "num_root", "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
    "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate",
    "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate",
    "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
    "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate",
    "difficulty_level"
]

# Hata verenleri görmezden gelerek dönüştür
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Dönüştürülen sütunları kontrol et
print(df.dtypes)

df.fillna(0, inplace=True)

df.fillna(df.mean(numeric_only=True), inplace=True)

print(df.columns)

df.columns = df.columns.str.strip()  # Boşlukları temizle



guvenli_paketler = df[df['class'] == 'normal']
saldiri_paketler = df[df['class'] == '']

print(f"Normal paket sayısı: {len(guvenli_paketler)}")
print(f"Saldırı paket sayısı: {len(saldiri_paketler)}")

print(df['class'].value_counts())  # Her saldırı türünün sayısını göster


df['class'].value_counts().plot(kind='bar', figsize=(10,5), title="Saldırı Türleri Dağılımı")
plt.show()

df.to_excel("temizlenmis_veri.xlsx", index=False)
