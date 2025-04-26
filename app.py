def hitung_protein(usia, jenis_kelamin, berat_badan, aktivitas_fisik):
    if jenis_kelamin == "laki-laki":
        if usia < 18:
            # Kebutuhan protein untuk anak-anak dan remaja laki-laki
            if usia < 4:
                protein = 13
            elif usia < 9:
                protein = 19
            elif usia < 14:
                protein = 34
            else:
                protein = 52
        elif usia < 65:
            # Kebutuhan protein untuk dewasa laki-laki
            protein = 0.8 * berat_badan
            if aktivitas_fisik == "tinggi":
                protein *= 1.2
            protein = round(protein)
        else:
            # Kebutuhan protein untuk lansia laki-laki
            protein = 1.0 * berat_badan
            protein = round(protein)
    elif jenis_kelamin == "perempuan":
        if usia < 18:
            # Kebutuhan protein untuk anak-anak dan remaja perempuan
            if usia < 4:
                protein = 13
            elif usia < 9:
                protein = 19
            elif usia < 14:
                protein = 34
            else:
                protein = 46
        elif usia < 65:
            # Kebutuhan protein untuk dewasa perempuan
            protein = 0.8 * berat_badan
            if aktivitas_fisik == "tinggi":
                protein *= 1.2
            protein = round(protein)
        else:
            # Kebutuhan protein untuk lansia perempuan
            protein = 1.0 * berat_badan
            protein = round(protein)

    return protein

usia = int(input("Masukkan usia Anda: "))
jenis_kelamin = input("Masukkan jenis kelamin Anda (laki-laki/perempuan): ")
berat_badan = float(input("Masukkan berat badan Anda (kg): "))
aktivitas_fisik = input("Masukkan tingkat aktivitas fisik Anda (rendah/tinggi): ")

protein_dibutuhkan = hitung_protein(usia, jenis_kelamin, berat_badan, aktivitas_fisik)

print(f"Kebutuhan protein harian Anda adalah {protein_dibutuhkan} gram.")