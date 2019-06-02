import os, bs4, requests

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
i = 0
while i < 10:  # not url.endswith('#') or:
	i += 1
	print('Dounloding page', url)
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'lxml')
	comic_elem = soup.select('#comic img')

	if comic_elem == []:
		print('No comics')
	else:
		lnk_img = comic_elem[0].get('src')
		print(os.path.basename(lnk_img))
		p = requests.get('https:'+lnk_img)
		out = open(os.path.join('xkcd',os.path.basename(lnk_img)), 'wb')
		out.write(p.content)
		out.close()
	lnk_elem = soup.select('a[rel="prev"]')
	url = 'http://xkcd.com' + str(lnk_elem[0].get('href'))	
