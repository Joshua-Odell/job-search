import requests
from bs4 import BeautifulSoup
from csv import writer
from datetime import datetime

response = requests.get(
    'https://www.indeed.com/jobs?as_and=Full+Stack+Developer&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=Minneapolis-Saint+Paul%2C+MN&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch')

soup = BeautifulSoup(response.text, 'html.parser')

serpJobCard = soup.find_all(class_ = 'jobsearch-SerpJobCard')


with open('indeedjob-fs.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Company', 'Link', 'Added']
    csv_writer.writerow(headers)

    for card in serpJobCard:
        title = card.find(class_ = 'title').get_text().strip()
        company = card.find(class_ = 'company').get_text().strip()
        link = card.find('a')['href']
        link = 'https://www.indeed.com' + link
        added = datetime.today()
        csv_writer.writerow([title, company, link, added])
        

