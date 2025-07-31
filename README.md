#🚀 Prospeku – Lead Scraper Indonetwork
Prospeku adalah alat sederhana namun efektif untuk menghasilkan prospek bisnis dari situs B2B Indonetwork.co.id, dikembangkan dalam waktu kurang dari 5 jam. Proyek ini terinspirasi oleh platform seperti SaasquatchLeads namun berfokus pada pasar Indonesia.
📁 Struktur Repo
Prospeku/
│
├── app/                    # Folder utama aplikasi
│   ├── scraper.py          # Scraper utama menggunakan BeautifulSoup
│   ├── utils.py            # Fungsi tambahan untuk random kontak dan sanitasi data
│
├── static/                 # File statis untuk UI
│   └── style.css
│
├── templates/              # HTML Template (Bootstrap)
│   └── index.html
│
├── results/                # Folder hasil CSV yang diekspor
│   └── lead_results.csv
│
├── demo/                   # 📹 Tempat menyimpan video demo
│   └── demo.mp4            # (Letakkan video demo kamu di sini)
│
├── app.py                  # Main Flask App
├── README.md               # Dokumentasi (file ini)
├── requirements.txt        # Dependensi Python
├── laporan.pdf             # Laporan 1 halaman
└── .gitignore
#1. Clone repo
git clone https://github.com/username/prospeku.git
cd prospeku
#2. Jalankan aplikasi Flask
python app.py

#Buka http://localhost:5000 dan masukkan kata kunci (misal: kapal) dan lokasi (misal: medan), lalu klik "Scrape".
📦 Fitur
🔎 Scraping data dari Indonetwork berdasarkan kata kunci & lokasi
📞 Mengisi kontak secara random jika tidak tersedia
📋 Menyimpan hasil dalam format CSV
💻 UI Bootstrap yang simpel dan cepat
📹 Video demo (lihat folder /demo)
📄 Laporan PDF 1 halaman (lihat laporan.pdf)
