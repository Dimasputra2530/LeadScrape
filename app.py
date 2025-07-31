from flask import Flask, render_template, request, send_file
from scraper import scrape_indonetwork
import csv
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    keyword = location = ""
    if request.method == "POST":
        keyword = request.form.get("keyword")
        location = request.form.get("location")
        results = scrape_indonetwork(keyword, location)
    return render_template("index.html", results=results, keyword=keyword, location=location)

@app.route("/download", methods=["GET"])
def download():
    keyword = request.args.get("keyword")
    location = request.args.get("location")

    if not keyword:
        return "❌ Kata kunci harus diisi terlebih dahulu.", 400

    results = scrape_indonetwork(keyword, location)

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["Nama Bisnis", "Kontak", "Sumber"])
    writer.writeheader()
    writer.writerows(results)

    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode("utf-8")),
        mimetype="text/csv",
        as_attachment=True,
        download_name="lead_indonetwork.csv"
    )

if __name__ == "__main__":
    app.run(debug=True)
