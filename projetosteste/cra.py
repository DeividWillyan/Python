import Queue, threading, urllib, urllib2

threads = 50
target_url  = "http://www.pudim.com.br"
wordlist_file = "/pentest/wordlist/diretorios/all.txt"
resume = None
user_agent = "googlebot"

def build_wordlist(wordlist_file):

	fd = open(wordlist_file, "rb")
	raw_words = fd.readlines()
	fd.close()

	found_resume = False
	words = Queue.Queue()

	for word in raw_words:

		word = word.rstrip()

		if resume is not None:
			if found_resume:
				words.put(word)
			else:
				if word == resume:
					found_resume = True
					print "Resuming wordlist from: %s" % resume
		else:
			words.put(word)

	return words

def dir_brute(word_queue, extensions=None):

	while not word_queue.empty():
		attempt = word_queue.get()
		attempt_list = []

		if "." not in attempt:
			attempt_list.append("/%s/" % attempt)
		else:
			attempt_list.append("/%s" % attempt)

		if extensions:
			for extensions in extensions:
				attempt_list.append("/%s%s" % (attempt, extensions))

		for brute in attempt_list:

			url = "%s%s" % (target_url, urllib.quote(brute))
			try:
				headers = {}
				headers["User-Agent"] = user_agent
				r = urllib2.Request(url, headers=headers)

				response = urllib2.urlopen(r)

				if len(response.read()):
					print "[%d] => %s" % (response.code, url)

			except urllib2.URLError,e:
				if hasattr(e, 'code') and e.code != 404:
					print "!!! %d = %s" % (e.code, url)

				pass

word_queue = build_wordlist(wordlist_file)
extensions = [".php", ".bak", ".orig", ".inc"]
for i in range(threads):
	t = threading.Thread(target=dir_brute, args=(word_queue,extensions))
	t.start()