import requests
import bs4
import os


def main():
	html = get_urls()
	get_data_from_cr(html)


def get_urls():
	print("getting urls")
	urls = {
		'east_bay': {'name': 'eby', 'url': 'https://sfbay.craigslist.org/search/eby/roo'},
		'north_bay': {'name': 'nby', 'url': 'https://sfbay.craigslist.org/search/nby/roo'},
		'peninsula': {'name': 'pen', 'url': 'https://sfbay.craigslist.org/search/pen/roo'},
		'san_francisco': {'name': 'sfc', 'url': 'https://sfbay.craigslist.org/search/sfc/roo'},
		'santa_cruz': {'name': 'scz', 'url': 'https://sfbay.craigslist.org/search/scz/roo'},
		'south_bay': {'name': 'sby', 'url': 'https://sfbay.craigslist.org/search/sby/roo'}
	}

	for value in urls:
		response = requests.get(urls[value]['url'])
		print("get urls complete")
		print(response.status_code)
		print('getting first text characters')
		print(response.text[0:250])
		print('finished getting text')
		return response.text


def get_data_from_cr(html):
	# priceCss =

	soup = bs4.BeautifulSoup(html, 'html.parser')
	print(soup)

def parse_data():
	pass


def create_temporary_document():
	pass


def append_to_permanent_document():
	pass


def erase_duplicates():
	pass


if __name__ == '__main__':
	main()
