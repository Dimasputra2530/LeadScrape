import requests
from bs4 import BeautifulSoup
import random

def generate_fake_phone():
    prefix = "08" + str(random.randint(11, 99))
    number = "".join([str(random.randint(0, 9)) for _ in range(8)])
    return prefix + number

def scrape_indonetwork(keyword, location=None):
    base_url = "https://www.indonetwork.co.id/search"
    params = {
        "q": keyword
    }

    if location:
        params["loc"] = location

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(base_url, params=params, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    items = soup.select(".row.box-shadow.box-ruby")

    for item in items:
        # Nama Bisnis
        nama_tag = item.select_one(".col-12.title.mb-2 a")
        nama_bisnis = nama_tag.text.strip() if nama_tag else "Tidak Diketahui"
        sumber = f"https://www.indonetwork.co.id{nama_tag['href']}" if nama_tag and nama_tag.has_attr("href") else "-"

        # Kontak (WhatsApp atau telp) — mengunakan nomor acak jika tidak ada
        kontak_tag = item.select_one("a[href^='https://wa.me']")
        kontak = kontak_tag.text.strip() if kontak_tag else generate_fake_phone()

        results.append({
            "Nama Bisnis": nama_bisnis,
            "Kontak": kontak,
            "Sumber": sumber
        })

    return results