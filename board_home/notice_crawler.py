import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from .models import Notice

def crawl_and_store_notices():
    url = "https://www.cju.ac.kr/www/selectBbsNttList.do?bbsNo=881&key=4577"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.select("table.bbs_default.list tbody tr")

    for row in rows:
        title_tag = row.select_one("td.subject a")
        category_tag = row.select_one("td:nth-of-type(2)")
        date_tag = row.select_one("td.date")

        if not title_tag or not category_tag or not date_tag:
            continue

        title = title_tag.text.strip()
        category = category_tag.text.strip()
        date_str = date_tag.text.strip()
        try:
            date = datetime.strptime(date_str, "%Y.%m.%d").date()
        except ValueError:
            continue

        href = title_tag.get("href", "")
        link = "https://www.cju.ac.kr/www/" + href.lstrip("./")

        # 중복 저장 방지
        if not Notice.objects.filter(title=title, date=date).exists():
            Notice.objects.create(title=title, category=category, date=date, link=link)
