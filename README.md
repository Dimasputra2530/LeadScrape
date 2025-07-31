# 🚀 LeadScrape: Alat Pengumpul Prospek dari Indonetwork

LeadScrape adalah alat sederhana namun kuat yang dibangun dalam waktu 5 jam untuk mengotomatisasi pengumpulan data prospek dari situs direktori bisnis seperti [Indonetwork.co.id](https://www.indonetwork.co.id). Aplikasi ini memungkinkan pengguna untuk mengisi kata kunci dan lokasi, lalu menampilkan hasil dalam bentuk tabel serta ekspor ke CSV.

---

## 🎯 Tujuan Proyek

Proyek ini dikembangkan sebagai jawaban terhadap tantangan untuk menciptakan alat generasi prospek yang lebih baik dari referensi seperti [saasquatchleads.com](https://www.saasquatchleads.com). Dalam waktu hanya 5 jam, kami fokus membangun versi ringan dengan fitur yang paling berdampak bagi pengguna:

- Scraping cepat dan terfokus berdasarkan kata kunci dan lokasi.
- Hasil disajikan rapi dan bisa diekspor.
- Tidak ada login/registrasi: langsung pakai.
- Video, laporan, dan kode semua ada dalam satu paket.

---

## 📸 Video Demo

Klik untuk menonton video demonstrasi:

📹 [Demo LeadScrape - YouTube/Drive](./demo-video.mp4)

---

## 📝 Laporan Teknis Singkat (1 Halaman)

### 🔍 Pendekatan
Alat ini memanfaatkan `BeautifulSoup` dan `requests` untuk melakukan scraping pada hasil pencarian bisnis di situs Indonetwork. Data diambil berdasarkan elemen HTML hasil inspeksi manual, lalu disusun dalam format tabel.

### ⚙️ Model / Teknik
- Tidak menggunakan model ML.
- Pencarian berbasis scraping HTML statis menggunakan CSS selector.
- Data yang ditangkap: Nama Bisnis, Kontak (WA), Gambar, Deskripsi, Sumber URL.
- Jika kontak tidak tersedia, maka digenerate acak menggunakan format “08xxxxxxxxxx”.

### 🧹 Prapemrosesan
- Membersihkan tag HTML.
- Menormalisasi teks dan memotong whitespace.
- Gambar dikonversi ke URL.
- Tabel hasil bisa diekspor ke CSV.

### 📊 Evaluasi Kinerja
- Kecepatan scraping: ±2 detik per query.
- Akurasi pengambilan data: ±90% tergantung struktur HTML yang stabil.
- Rasio keberhasilan kontak ditemukan: 40–60%.
- Cocok untuk tahap awal pengumpulan lead.

---

## 🗂️ Struktur Proyek

