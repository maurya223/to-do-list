import requests
from bs4 import BeautifulSoup

url = "https://www.abplive.com/"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text, 'html.parser')

# Try this: headlines in .featured_cont .header or .newsHdng
headlines = soup.find_all('div', class_='featured_cont')

print(" Top News Headlines from abplive:\n")

count = 0
for item in headlines:
    title_tag = item.find('a')
    if title_tag:
        title = title_tag.text.strip()
        link = title_tag['href']
        count += 1
        print(f"{count}. {title}\n   ➤ {link}\n")
    if count >= 10:
        break

if count == 0:
    print(" Could not find any headlines. Website structure may have changed.")
