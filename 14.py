from download import download
import itertools

# maximum error times
max_errors = 5
# current error times
num_errors = 0



for page in itertools.count(1):
	url = 'http://example.webscraping.com/view/-%d' % page
	html = download(url)
	if html is None:
	#receive an error
		num_errors += 1
		if num_errors == max_errors:
			# reachd the cap
			# exit			
		    break
	else :
		#success
		# ...
		num_errors = 0
	

