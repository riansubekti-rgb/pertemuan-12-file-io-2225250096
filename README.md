# Pertemuan 12 - File I/O dan Error Handling

Nama: Rian Subekti  
NIM: 2225250096  
Kelas: 3F  

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input
NIM, nilai

## Cara Menjalankan
python3 tugas/rekap_nilai_file.py

## Error yang Ditangani
- FileNotFoundError
- ValueError

## Test Case
| Kasus | Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Normal** | Semua baris valid | Semua record diproses dan rekap benar. | Semua record terproses dan file rekap berhasil dibuat. | Berhasil |
| **File hilang** | `nilai.txt` tidak tersedia | Pesan file tidak ditemukan; program tidak *crash*. | Menampilkan pesan error file tidak ditemukan dan berhenti aman. | Berhasil |
| **Nilai invalid** | `A004,abc` | Baris invalid dilewati/dilaporkan; record lain tetap diproses. | Baris invalid dilaporkan via terminal, baris lain tetap diproses. | Berhasil |
| **Baris kosong** | Ada baris kosong | Baris kosong dilewati. | Baris kosong diabaikan tanpa error. | Berhasil |
| **Batas lulus** | Nilai 60 | Dihitung sebagai lulus. | Nilai 60 masuk ke dalam hitungan jumlah lulus (`>= 60`). | Berhasil |

## Refleksi
Selama pengerjaan tugas ini, salah satu error yang sering ditemui adalah `ValueError` ketika program mencoba mengonversi data teks atau string non-angka pada kolom nilai (seperti pada kasus `A004,abc`) menjadi tipe data pecahan (`float`). Program mengatasinya dengan menerapkan blok `try-except` di dalam perulangan baris (`for loop`), sehingga ketika konversi gagal, program tidak berhenti secara mendadak (*crash*), melainkan mencetak pesan peringatan baris tidak valid di terminal dan tetap melanjutkan proses untuk data record mahasiswa lainnya.

## Sumber
Bahan_Ajar_Pertemuan_12_File_IO_Error_Handling_VSCode_GitHub