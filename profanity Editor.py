import urllib

def read_text():
	quotes = open (r"C:\movie_quotes.txt")
	contentes_of_file = quotes.read()
	print (contentes_of_file)
	quotes.close()
	check_profanity(contentes_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	print (output)
	connection.close()
	if "true" in output:
		print("profanity Alert !!")
	elif "false" in output :
		print("This document has no curse words !")
	else :
		print("could not scan the document properly.")

read_text()