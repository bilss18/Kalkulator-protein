import streamlit as st

# Input User
berat_badan = st.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0, step=1.0)
usia = st.number_input("Usia", min_value=10, max_value=100, step=1)
jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
aktivitas = st.selectbox("Tingkat Aktivitas", ["Sedentari (minim aktivitas)","Aktif ringan (olahraga ringan 1-3x/minggu)", "Aktif sedang (olahraga sedang 3-5x/minggu)","Sangat aktif (olahraga berat tiap hari)"])

# Hitung kebutuhan protein
def hitung_protein(berat, aktivitas):
    faktor = {"Sedentari (minim aktivitas)": 0.8,"Aktif ringan (olahraga ringan 1-3x/minggu)": 1.2,"Aktif sedang (olahraga sedang 3-5x/minggu)": 1.5,"Sangat aktif (olahraga berat tiap hari)": 2.0}
    return round(berat * faktor[aktivitas], 1)

if berat_badan:
    kebutuhan = hitung_protein(berat_badan, aktivitas)
    st.subheader("Kebutuhan protein harianmu: *{kebutuhan} gram*")
    
def hitung_kebutuhan_protein(umur, tinggi_cm, berat_kg, jenis_kelamin):
    """
    Menghitung kebutuhan protein harian (gram per hari) berdasarkan:
    - Umur (tahun)
    - Tinggi (cm)
    - Berat badan (kg)
    - Jenis kelamin ("L" atau "P")

    Rumus umum (perkiraan berdasarkan berat badan dan jenis kelamin):
    - Laki-laki: 0.9 gram protein per kg berat badan
    - Perempuan: 0.8 gram protein per kg berat badan
    - Anak-anak: > 1 gram/kg tergantung usia

    Return: kebutuhan protein per hari dalam gram
    """

    if umur <= 3:
        kebutuhan_protein = berat_kg * 1.05
    elif umur <= 8:
        kebutuhan_protein = berat_kg * 0.95
    elif umur <= 18:
        kebutuhan_protein = berat_kg * 0.85
    else:
        if jenis_kelamin.upper() == "L":
            kebutuhan_protein = berat_kg * 0.9
        elif jenis_kelamin.upper() == "P":
            kebutuhan_protein = berat_kg * 0.8
        else:
            return "Jenis kelamin tidak valid. Gunakan 'L' atau 'P'."

    return round(kebutuhan_protein, 2)


# Contoh penggunaan program
umur = int(input("Masukkan umur (tahun): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))
berat = float(input("Masukkan berat badan (kg): "))
jenis_kelamin = input("Masukkan jenis kelamin (L/P): ")

hasil = hitung_kebutuhan_protein(umur, tinggi, berat, jenis_kelamin)

print(f"Kebutuhan protein harian Anda diperkirakan: {hasil} gram")