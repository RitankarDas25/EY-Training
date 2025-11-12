# services/scrape.py
import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}


def _clean_text(txt):
    return re.sub(r'\s+', ' ', txt).strip()


def scrape_amazon_reviews(url: str, max_pages=1):
    reviews = []
    for page in range(1, max_pages + 1):
        page_url = re.sub(r"pageNumber=\d+", f"pageNumber={page}", url)
        page_url = page_url if "pageNumber" in page_url else f"{url}&pageNumber={page}"
        resp = requests.get(page_url, headers=HEADERS)
        if resp.status_code != 200:
            break
        soup = BeautifulSoup(resp.text, "lxml")
        blocks = soup.find_all("span", {"data-hook": "review-body"})
        for b in blocks:
            txt = b.get_text(" ", strip=True)
            if txt:
                reviews.append(_clean_text(txt))
    return reviews


def scrape_flipkart_reviews(url: str, max_pages=1):
    reviews = []
    for page in range(1, max_pages + 1):
        page_url = f"{url}&page={page}" if "?pid=" in url else f"{url}?page={page}"
        resp = requests.get(page_url, headers=HEADERS)
        if resp.status_code != 200:
            break
        soup = BeautifulSoup(resp.text, "lxml")
        blocks = soup.find_all("div", {"class": "t-ZTKy"})
        for b in blocks:
            txt = b.get_text(" ", strip=True)
            if txt:
                reviews.append(_clean_text(txt))
    return reviews


def scrape_generic_reviews(url: str, selector="div.review", limit=50):
    resp = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, "lxml")
    blocks = soup.select(selector)
    reviews = [_clean_text(b.get_text(" ", strip=True)) for b in blocks]
    return reviews[:limit]


def auto_scrape(url: str, max_pages=2):
    """
    Automatically detect and scrape reviews based on domain.
    """
    if "amazon." in url:
        return scrape_amazon_reviews(url, max_pages=max_pages)
    elif "flipkart." in url:
        return scrape_flipkart_reviews(url, max_pages=max_pages)
    else:
        return scrape_generic_reviews(url)
