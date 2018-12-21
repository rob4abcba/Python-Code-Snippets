from bs4 import BeautifulSoup
import requests
import csv

#RL Start1
print("Beginning of RL1")

with open('simpleRL.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

title = soup.title
print('title: ', title)

titleText = soup.title.text
print('titleText: ', titleText)

div = soup.find('div')
print('\ndiv(unpretty):\n', div)
footer = soup.find('div', class_='footer'
)
print('\ndiv class footer:\n', footer)

article = soup.find('div', class_='article')
print('\ndiv class article:\n', article)

headline = article.h2.a.text
print('\nheadline:\n', headline)

summary = article.p.text
print('\nsummary:\n', summary)

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print('\nheadline:\n', headline)

    summary = article.p.text
    print('\nsummary:\n', summary)

    print()

print("End of RL1")
#RL End1

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

#RL Start2
print("Beginning of RL2")
print('\rsoup.prettify:\r',soup.prettify())

article = soup.find('article')
print('\narticle.prettify:\n', article.prettify())

headline = article.h2.a.text
print('\nheadline:\n', headline)

summary = article.find('div', class_='entry-content').p.text
print('\nsummary = article.find div class_ entry-content .p.text:\n', summary)

vid_src1 = article.find('iframe', class_='youtube-player')
print('\nvid_src1 = article.find iframe class_ youtube-player:\n', vid_src1)

vid_src2 = article.find('iframe', class_='youtube-player')['src']
print('\nvid_src2 = article.find iframe class_ youtube-player src\n', vid_src2)

print("End of RL2\r")
#RL End2



csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print('\nheadline = article.h2.a.text:\n',headline)


    summary = article.find('div', class_='entry-content').p.text
    print('\nsummary = :\n', summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
