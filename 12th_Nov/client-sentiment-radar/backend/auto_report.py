import requests
import schedule
import time
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch
import matplotlib.pyplot as plt
import io
from datetime import datetime

# Configuration
API_URL = "http://127.0.0.1:8000"
PRODUCT_URL = "https://www.amazon.in/Nothing-Phone-3a-Black-128GB/dp/B0DZTNWWDH"
RECIPIENT_EMAIL = "recipient@example.com"
SENDER_EMAIL = "youremail@gmail.com"
SENDER_PASS = "your_app_password"  # Use Gmail App Password

def fetch_and_analyze():
    print(" Fetching latest reviews...")
    scrape_res = requests.get(f"{API_URL}/scrape/", params={"url": PRODUCT_URL, "pages": 2})
    reviews = scrape_res.json().get("reviews", [])

    if not reviews:
        print(" No reviews found.")
        return None

    print(" Analyzing sentiments...")
    analyze_res = requests.post(f"{API_URL}/analyze/", json={"feedbacks": reviews})
    results = analyze_res.json()

    results["total_reviews"] = len(reviews)
    with open("latest_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    return results


def generate_charts(data):
    print("📊 Generating charts...")

    # Sentiment Pie Chart
    stats = data.get("stats", {})
    labels = list(stats.keys())
    values = list(stats.values())

    plt.figure(figsize=(4, 4))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Sentiment Distribution")
    pie_buf = io.BytesIO()
    plt.savefig(pie_buf, format="png", bbox_inches="tight")
    pie_buf.seek(0)
    plt.close()

    # Bar Chart of Topics (optional)
    topics = data.get("topics", [])
    if topics:
        topic_labels = [t["topic"] for t in topics]
        topic_counts = [t["count"] for t in topics]
        plt.figure(figsize=(5, 3))
        plt.barh(topic_labels, topic_counts)
        plt.title("Top Mentioned Topics")
        plt.xlabel("Frequency")
        plt.tight_layout()
        bar_buf = io.BytesIO()
        plt.savefig(bar_buf, format="png", bbox_inches="tight")
        bar_buf.seek(0)
        plt.close()
    else:
        bar_buf = None

    return pie_buf, bar_buf


def generate_pdf(data, filename="Sentiment_Report.pdf"):
    print("📄 Generating PDF report...")
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(1 * inch, height - 1 * inch, "📊 Client Sentiment Radar Report")
    c.setFont("Helvetica", 11)
    c.drawString(1 * inch, height - 1.3 * inch, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, height - 1.7 * inch, f"Total Reviews: {data.get('total_reviews', len(data.get('feedbacks', [])))}")

    # Add Charts
    pie_buf, bar_buf = generate_charts(data)
    y_pos = height - 3 * inch
    c.drawImage(ImageReader(pie_buf), 1 * inch, y_pos, width=3.2 * inch, height=3.2 * inch)

    if bar_buf:
        c.drawImage(ImageReader(bar_buf), 4.5 * inch, y_pos, width=3 * inch, height=3 * inch)

    # Sentiment Breakdown
    y = y_pos - 0.5 * inch
    stats = data.get("stats", {})
    c.setFont("Helvetica-Bold", 13)
    c.drawString(1 * inch, y, "Sentiment Breakdown:")
    y -= 0.3 * inch
    c.setFont("Helvetica", 11)
    for k, v in stats.items():
        c.drawString(1.2 * inch, y, f"{k.capitalize()}: {v}")
        y -= 0.25 * inch

    # Top topics
    topics = data.get("topics", [])
    if topics:
        y -= 0.3 * inch
        c.setFont("Helvetica-Bold", 13)
        c.drawString(1 * inch, y, "Top Topics:")
        y -= 0.3 * inch
        c.setFont("Helvetica", 11)
        for t in topics:
            c.drawString(1.2 * inch, y, f"- {t['topic']} ({t['count']})")
            y -= 0.25 * inch

    # AI Summary
    y -= 0.4 * inch
    c.setFont("Helvetica-Bold", 13)
    c.drawString(1 * inch, y, "AI Summary:")
    y -= 0.3 * inch
    c.setFont("Helvetica", 10)
    text_obj = c.beginText(1.2 * inch, y)
    text_obj.setLeading(13)
    for line in data.get("summary", "").split("\n"):
        text_obj.textLine(line)
    c.drawText(text_obj)

    c.showPage()
    c.save()
    print(" PDF with charts generated successfully.")


def send_email_with_pdf(pdf_filename):
    print(" Sending email report...")

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = "Weekly Sentiment Dashboard Report"

    body = MIMEText("Attached is your latest sentiment dashboard report ", "plain")
    msg.attach(body)

    with open(pdf_filename, "rb") as f:
        part = MIMEApplication(f.read(), Name=pdf_filename)
        part["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
        msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASS)
        server.send_message(msg)

    print(" Email with charts sent successfully!")


def job():
    data = fetch_and_analyze()
    if data:
        pdf_file = "Sentiment_Report.pdf"
        generate_pdf(data, pdf_file)
        send_email_with_pdf(pdf_file)
    else:
        print(" Skipping email — no data available.")


# Schedule weekly (e.g., every Monday 8 AM)
schedule.every().monday.at("08:00").do(job)
# For testing, you can run it every 1 minute:
# schedule.every(1).minutes.do(job)

print(" Scheduler started — waiting for next run...")
while True:
    schedule.run_pending()
    time.sleep(60)
