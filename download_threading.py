import requests
import os
import bs4
import threading


def download_file(link, name_dir):
    res_obj = requests.get(link)
    res_obj.raise_for_status()  # if ok then None else exception
    name_file = os.path.basename(link)
    save_f = open(os.path.join(name_dir, name_file), 'wb')
    print('download image: ', name_file)
    for chunk in res_obj.iter_content(100_000):
        save_f.write(chunk)
    save_f.close()

DIR = 'xkcd_T'
url = 'http://xkcd.com'
os.makedirs(DIR, exist_ok=True)
# download_file('https://imgs.xkcd.com/comics/plutonium.png', DIR)

i = 0
download_threads = []
while i < 50:
    i += 1
    try:
        res = requests.get(url)
    except Exception as ex:
        print(ex)
        continue
    res.raise_for_status()
    soup_obj = bs4.BeautifulSoup(res.text, features='lxml')
    comic_elem = soup_obj.select('#comic img')
    link_img = 'https:' + comic_elem[0].get('src')
    # download_file(link_img, DIR)
    thObj = threading.Thread(target=download_file, args=[link_img, DIR])
    download_threads.append(thObj)
    # download_threads[-1].start()
    lnk_elem = soup_obj.select('a[rel="prev"]')
    url = 'http://xkcd.com' + str(lnk_elem[0].get('href'))

for th in download_threads:
	th.start()
for th in download_threads:
	th.join() #wait all threads


print('FINISH')


