🚀 Prospeku – Lead Scraper Indonetwork
Prospeku adalah alat sederhana namun efektif untuk menghasilkan prospek bisnis dari situs B2B Indonetwork.co.id. Aplikasi ini dikembangkan dalam waktu kurang dari 5 jam, terinspirasi dari platform seperti SaasquatchLeads, namun difokuskan pada pasar Indonesia.
📁 Struktur Direktori
Prospeku/
├── app/            # Logika scraping & utilitas
│   ├── scraper.py
│   └── utils.py
├── static/         # CSS untuk tampilan
│   └── style.css
├── templates/      # UI HTML (Bootstrap)
│   └── index.html
├── results/        # Output CSV hasil scraping
│   └── lead_results.csv
├── demo/           # Video demo aplikasi
│   └── demo.mp4
├── app.py          # Entry point Flask
├── README.md       # Dokumentasi
├── requirements.txt# Daftar dependensi
├── laporan.pdf     # Laporan 1 halaman
└── .gitignore
⚙️ Cara Menjalankan
git clone https://github.com/username/prospeku.git
cd prospeku
Jalankan aplikasi:
python app.py
Buka browser ke http://localhost:5000, masukkan kata kunci (misal: kapal) dan lokasi (misal: medan), lalu klik tombol "Scrape".

📦 Fitur Unggulan
🔎 Scraping data bisnis dari Indonetwork berdasarkan kata kunci & lokasi

📞 Kontak otomatis diisi secara acak bila tidak tersedia

📋 Hasil scraping disimpan dalam format CSV

💻 UI simpel berbasis Bootstrap

📹 Tersedia video demo dalam folder /demo

📄 Laporan singkat tersedia dalam bentuk PDF (laporan.pdf)
