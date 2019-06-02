#! python3
import webbrowser, sys, pyperclip, requests, bs4, pprint

# site = 'https://weather.gov/94105' # 'https://weather.gov/94105'
# res = requests.get(site)  # https://lifehacker.ru/zaporot-pomolvku/')#http://tululu.org/txt.php?id=21041')
# res.raise_for_status()
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('There was a problem:', exc)
# print(res.status_code, requests.codes.ok)


# print(res.text[700:1000])
# with open('myFile.txt', 'wb') as f:  # don't forget wb
#     for line in res.iter_content(100_000):  # 100_000 Bt нормально
#         f.write(line)


# exfile = open(example.html)
# exSoup = bs4.BeautifulSoup(exfile.read(), "lxml")
# print(exSoup)
# el=exSoup.select('span')[0]
# print(el.get('id'))
# print('-'*80)
# print(el.get('fghdfg'))


query = 'python3'
res = requests.get('http://google.com/search?q=' + query)
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem:', exc)
soup = bs4.BeautifulSoup(res.text, "lxml")
linkElems = soup.select('.r a')
# pprint.pprint(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    print(linkElems[i].get(''))