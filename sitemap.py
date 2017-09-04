import urllib2
import re 
from download import download

def crawl_sitemap(url):
	#download sitemap
	sitemap = download(url)
	#extract the sitemap links
	links = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,sitemap)
	#downlaod each link
	for link in links:
		html = download(link)
	
crawl_sitemap('http://www.dyned.com.cn/sitemap')