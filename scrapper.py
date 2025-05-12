import asyncio
import aiohttp
import feedparser

with open("mots_cles.txt", "r", encoding="utf-8") as f:
    keywords = [line.strip().lower() for line in f if line.strip()]

with open("rss_list.txt", "r", encoding="utf-8") as f:
    rss_urls = [line.strip() for line in f if line.strip() and not line.startswith("RSS_URL")]

async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            return await response.text()
    except:
        return None

async def parse_and_filter(session, url):
    html = await fetch(session, url)
    if not html:
        return []
    feed = feedparser.parse(html)
    matches = []
    for entry in feed.entries:
        title = entry.get("title", "")
        summary = entry.get("summary", "")
        published = entry.get("published", "N/A")
        link = entry.get("link", "N/A")
        for keyword in keywords:
            if keyword in title.lower() or keyword in summary.lower():
                matches.append((title, published, link, keyword))
                break
    return matches

async def main():
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = [parse_and_filter(session, url) for url in rss_urls]
        all_results = await asyncio.gather(*tasks)
        for match_list in all_results:
            results.extend(match_list)

    with open("resultat.txt", "w", encoding="utf-8") as f:
        for title, published, link, keyword in results:
            print(f"{title} ({published})\n{link}\n")
            f.write(f"{title}\n{published}\n{link}\nMot-clé : {keyword}\n\n")

if __name__ == "__main__":
    asyncio.run(main())
