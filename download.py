import urllib2 

def download(url,user_agent='wswp',num_retries=2):
	print 'Downloading',url
	headers = {'User-agent':user_agent}
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print 'Download error:',e.reason
		html = None
		if hasattr(e,'code') and 500 <= e.code < 600:
			#retry
			return download(url, num_retries-1)
	return html
	