"""
Program Tugas 5: Rekap Nilai dari File
Mata Kuliah: Algoritma dan Pemrograman
Pertemuan 12: File Input-Output dan Penanganan Error Dasar
"""

def baca_data(nama_file):
    data = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()
                
                # Test Case: Baris kosong dilewati
                if not baris:
                    continue
                
                try:
                    nim, teks_nilai = baris.split(",")
                    # Test Case: Nilai invalid (misal: "abc") ditangani per baris
                    nilai = float(teks_nilai.strip())
                    data.append((nim.strip(), nilai))
                except ValueError:
                    # Test Case: Baris invalid dilaporkan dan dilewati, record lain diproses
                    print(f"Baris {nomor} tidak valid (dilewati): {baris}")
                    
    except FileNotFoundError:
        # Test Case: File hilang ditangani dengan pesan jelas, program tidak crash
        print(f"File tidak ditemukan: {nama_file}. Pastikan path file dan folder 'data' sudah benar.")
    return data

def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return
    
    nilai = [item[1] for item in data]
    jumlah_data_valid = len(nilai)
    rata_rata = sum(nilai) / jumlah_data_valid
    nilai_min = min(nilai)
    nilai_max = max(nilai)
    
    # Test Case: Batas lulus (Nilai minimal 60 dihitung sebagai lulus)
    jumlah_lulus = sum(1 for x in nilai if x >= 60)
    
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {jumlah_data_valid}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Minimum: {nilai_min:.2f}\n")
        file.write(f"Maksimum: {nilai_max:.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")

if __name__ == "__main__":
    input_file = "data/nilai.txt"
    output_file = "data/hasil_rekap.txt"
    
    print("=== PROGRAM REKAP NILAI MAHASISWA ===")
    print("Membaca dan memvalidasi file input...")
    
    data = baca_data(input_file)
    
    if data:
        tulis_rekap(output_file, data)
        print(f"Sukses! Rekap berhasil ditulis ke {output_file}")
    else:
        print("Proses rekap dihentikan karena tidak ada data valid.")