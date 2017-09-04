import re
from download import download
def link_crawler(seed_url, link_regex):
	"""Crawl from the given seed URL following inks matched by link_regex
	"""
	crawl_queue = [seed_url]
	while crawl_queue:
		url = crawl_queue.pop()
		html = download(url)
		for link in get_links(html):
			crawl_queue.append(link)
	
def get_links(html):
	"""Return a list of links from html
	"""
	webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
	# list of all links from the webpage
	return webpage_regex.findall(html)
		
		
		
link_crawler('http://example.webscraping.com','/(index|view)')
	
	