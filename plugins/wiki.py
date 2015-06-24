import time
import wikipedia
crontable = []
outputs = []

def process_message(data):
	if 'type' in data:
		if data['type'] == 'message' and len(data['text']) > 5 and '!wiki' == data['text'][0:5]:
			lookup_str = data['text'][5:]
			lookup_str = lookup_str.strip()

			results = wikipedia.search(lookup_str)
			if len(results) == 0:
				outputs.append([data['channel'], 'I did not find anything :\'(. No knowledge for you.'])
				return
			try:
				wiki = wikipedia.page(title=results[0])
				outputs.append([data['channel'], wiki.url])
			except wikipedia.exceptions.DisambiguationError as e:
				try:
					wiki = wikipedia.page(title=e.options[0])
					outputs.append([data['channel'], wiki.url])
				except:
					outputs.append([data['channel'], 'something went wrong'])
			except:
				outputs.append([data['channel'], 'something went wrong'])

			

