import requests
import psycopg2
from bs4 import BeautifulSoup
from csv import writer
from datetime import datetime
     
def addToDb(title, company, link, added):   
    con = psycopg2.connect(
                host="localhost",
                database="job",
                user="job",
                password="job")

    cur = con.cursor()

    cur.execute("insert into indeed (title, company, link, added) values (%s, %s, %s, %s)", (title, company, link, added))

    con.commit()

    cur.close()

    con.close()

        
def scrape(URL, fileName):
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')

    serpJobCard = soup.find_all(class_ = 'jobsearch-SerpJobCard')


    for card in serpJobCard:
            title = card.find(class_ = 'title').get_text().strip()
            company = card.find(class_ = 'company').get_text().strip()
            valid = "Senior" not in title
            if "Sr." in title or "Sr" in title or title == '' or "intern" in title or "internship" in title:
                valid = False
            link = card.find('a')['href']
            link = 'https://www.indeed.com' + link
            added = datetime.today()
            if valid:
                try:
                    addToDb(title, company, link, added)
                except Exception:
                    pass
        

scrape('https://www.indeed.com/jobs?as_and=Full+Stack+Developer&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=Minneapolis-Saint+Paul%2C+MN&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch', 'indeedjob.csv')
scrape('https://www.indeed.com/jobs?as_and=Junior+Developer&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=Minneapolis-Saint+Paul%2C+MN&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch', 'indeedjob.csv')