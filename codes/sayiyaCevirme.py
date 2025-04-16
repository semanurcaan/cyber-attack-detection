import pandas as pd

# 📌 Dosya Yolu
file_path = r"C:\sınıf3\excel_ayırma\dos_saldiri_numericcccc.xlsx"

# 📌 Excel Dosyasını Oku
df = pd.read_excel(file_path)

# 📌 Manuel Kodlama Kuralları
protocol_mapping = {"tcp": 1, "udp": 0, "icmp":2}
service_mapping = {"nnsp":51, "pop_2": 52, "printer": 53, "other": 54, "ssh": 42, "smtp": 43, "daytime":44, "shell":45, "netstat":46, "tim_i":47, "pop_3":48, "rje":49, "netbios_ssn":50}
flag_mapping = {"S0": 0, "REJ":1, "SF":2, "S2":5}
class_mapping = {"neptune": 0, "teardrop":1, "smurf":2, "pod":3, "back":4, "land":5}

# 📌 Belirtilen sütunları güncelle
df["protocol_type"] = df["protocol_type"].map(protocol_mapping).fillna(df["protocol_type"])
df["service"] = df["service"].map(service_mapping).fillna(df["service"])
df["flag"] = df["flag"].map(flag_mapping).fillna(df["flag"])
df["class"] = df["class"].map(class_mapping).fillna(df["class"])
# 📌 Yeni Dosya Yolu
output_file = r"dos_saldiri_numericccccc.xlsx"

# 📌 Güncellenmiş Veriyi Kaydet
df.to_excel(output_file, index=False)

print("Dönüştürülmüş dosya kaydedildi:", output_file)
