import streamlit as st

# Input User
berat = st.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0, step=1.0)
tinggi = st.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=220.0, step=1.0)
umur = st.number_input("Umur", min_value=1, max_value=100, step=1)
jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
aktivitas = st.selectbox("Tingkat Aktivitas", [
    "Sedentari (minim aktivitas)",
    "Aktif ringan (olahraga ringan 1-3x/minggu)",
    "Aktif sedang (olahraga sedang 3-5x/minggu)",
    "Sangat aktif (olahraga berat tiap hari)"
])

# Fungsi menghitung protein berdasarkan aktivitas
def hitung_protein_aktivitas(berat, aktivitas):
    faktor = {
        "Sedentari (minim aktivitas)": 0.8,
        "Aktif ringan (olahraga ringan 1-3x/minggu)": 1.2,
        "Aktif sedang (olahraga sedang 3-5x/minggu)": 1.5,
        "Sangat aktif (olahraga berat tiap hari)": 2.0
    }
    return round(berat * faktor[aktivitas], 1)

# Fungsi menghitung protein berdasarkan umur & jenis kelamin
def hitung_kebutuhan_protein(umur, berat, jenis_kelamin):
    if umur <= 3:
        kebutuhan_protein = berat * 1.05
    elif umur <= 8:
        kebutuhan_protein = berat * 0.95
    elif umur <= 18:
        kebutuhan_protein = berat * 0.85
    else:
        if jenis_kelamin == "Laki-laki":
            kebutuhan_protein = berat * 0.9
        else:
            kebutuhan_protein = berat * 0.8
    return round(kebutuhan_protein, 2)

# Tombol submit
if st.button("Hitung Kebutuhan Protein"):
    kebutuhan1 = hitung_protein_aktivitas(berat, aktivitas)
    kebutuhan2 = hitung_kebutuhan_protein(umur, berat, jenis_kelamin)

    st.success(f"Kebutuhan protein berdasarkan aktivitas: {kebutuhan1} gram")
    st.success(f"Kebutuhan protein berdasarkan usia & jenis kelamin: {kebutuhan2} gram")
    # Rekomendasi makanan
    kebutuhan_rata2 = (kebutuhan_aktivitas + kebutuhan_umur_gender) / 2

    st.markdown("### Rekomendasi Makanan Tinggi Protein:")
    if kebutuhan_rata2 < 50:
        st.write("- Telur rebus")
        st.write("- Tahu dan tempe")
        st.write("- Yogurt")
        st.write("- Susu kedelai")
    elif kebutuhan_rata2 <= 100:
        st.write("- Dada ayam")
        st.write("- Ikan tuna / salmon")
        st.write("- Telur")
        st.write("- Susu tinggi protein")
        st.write("- Edamame")
    else:
        st.write("- Steak daging sapi")
        st.write("- Dada ayam + telur")
        st.write("- Whey protein shake")
        st.write("- Ikan laut (tuna, salmon)")
        st.write("- Kacang-kacangan (almond, kacang hitam)")

    st.info("Tips: Sebaiknya konsumsi protein tersebar sepanjang hari untuk penyerapan optimal.")
