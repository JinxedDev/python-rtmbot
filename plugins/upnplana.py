import time
import wikipedia
import re
crontable = []
outputs = []

def process_message(data):
	if 'type' in data:
		if data['type'] == 'message' and 'UPNP' in data['text'].upper():
			outputs.append([data['channel'], 'https://www.youtube.com/watch?v=xn6hhrX34Pw'])
		elif data['type'] == 'message' and re.search(r'lana', data['text'], re.IGNORECASE) is not None:
			outputs.append([data['channel'], 'YUUP!'])