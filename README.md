# Sistem Rekomendasi Laptop Berdasarkan Budget & Kebutuhan
### Tugas Kelompok 7 - Proyek Algoritma dan Struktur Data

Aplikasi berbasis komputer ini dibuat untuk membantu Anda mengelola data laptop sekaligus mencari **rekomendasi laptop terbaik** secara otomatis. Aplikasi ini sangat cocok untuk orang yang bingung memilih laptop karena sistem akan mencarikan laptop yang pas sesuai dengan **isi dompet (budget)** dan **tujuan penggunaan** Anda (apakah untuk kerja kantoran, main game, atau desain grafis).

Proyek ini merupakan tugas proyek dari **Algoritma dan Struktur Data** memanfaatkan database lokal berbasis file CSV.

## Fitur Utama

1. **Manajemen Data Laptop (CRUD):**
   * **Create (Tambah):** Memasukkan data laptop baru lengkap dengan Merk, Tipe, RAM, Storage, Harga, dan Kategori.
   * **Read (Tampil):** Menyajikan seluruh data laptop yang terdaftar secara rapi menggunakan tabel berbasis `Treeview`.
   * **Update (Ubah):** Mengedit spesifikasi atau harga laptop yang dipilih dari tabel.
   * **Delete (Hapus):** Menghapus data laptop dari sistem.
2. **Fitur Pembatalan (Undo Delete):** Memulihkan kembali data laptop yang baru saja terhapus dengan memanfaatkan struktur data *Stack*.
3. **Sistem Rekomendasi Pintar:** Menyaring laptop yang sesuai dengan isi dompet pengguna dan melakukan penilaian otomatis (*scoring*) terhadap spesifikasi laptop berdasarkan kategori kebutuhan (Office, Gaming, Desain).
4. **Penyimpanan Permanen (Persistensi Data):** Semua data otomatis tersimpan di dalam file `data_laptop.csv`. Jika file ini belum ada di komputer, aplikasi akan otomatis membuatkannya dengan menyertakan beberapa data bawaan (*default*).

## Algoritma & Struktur Data yang Diterapkan

Di dalam proyek Kelompok 7 ini, kami menerapkan beberapa konsep dasar ilmu komputer:

* **Object-Oriented Programming (OOP):** Penggunaan komponen kelas (`class Laptop`) untuk mengumpulkan seluruh spesifikasi laptop sebagai sebuah objek tunggal yang dinamis.
* **Binary Search:** Digunakan pada proses *Update* dan *Delete* untuk melacak nomor indeks posisi laptop di dalam memori list berdasarkan **ID**-nya secara instan.
* **Linear Search:** Diterapkan pada fitur filter rekomendasi untuk memindai seluruh laptop yang harganya tidak melebihi *budget* pengguna dan menghitung bobot skor kecocokannya.
* **Selection Sort:** Berfungsi mengurutkan hasil rekomendasi laptop dari nilai skor tertinggi ke terendah (*descending*), sehingga laptop yang paling direkomendasikan akan muncul di baris paling atas tabel.
* **Stack (LIFO - Last In, First Out):** Diterapkan pada mekanisme tombol *Undo*. Laptop yang dihapus akan dimasukkan (*push*) ke tumpukan memori sementara, dan dikeluarkan kembali (*pop*) ke tabel utama saat membatalkan penghapusan.

## Teknologi & Prasyarat

* **Bahasa Pemrograman:** Python 3.x
* **Antarmuka (GUI):** Tkinter & TTK (Theme Widget)
* **Penyimpanan Data:** CSV (Comma-Separated Values)

Aplikasi ini **tidak memerlukan instalasi library pihak ketiga (no third-party dependencies)** karena menggunakan modul bawaan Python murni.

## Cara Menginstal dan Menjalankan Proyek

### 1. Clone Repositori
Buka terminal atau Command Prompt (CMD), lalu jalankan perintah berikut:
```bash
git clone [https://github.com/Varrelionnato97/Project_Algoritma_Kelompok_7.git](https://github.com/Varrelionnato97/Project_Algoritma_Kelompok_7.git)
cd Project_Algoritma_Kelompok_7
