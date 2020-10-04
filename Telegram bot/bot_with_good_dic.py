import requests
import json
import datetime
from time import sleep

# удалить токен для github
a = "https://api.telegram.org/..../"

def get_url_dec_json(request):
	global response
	global username
	global name
	global slovo
	offset = None
	#mark viewed updates - "offset"
	# timeout - работает только при отсутствии последних обновлений
	
	#params = {'timeout': 50 , 'mark_viewed_updates': None} 
	url = requests.get(a + "getUpdates")
	if offset:
		url += "?offset={}".format(offset)

	response = url.json()
	username = response['result'][0]['message']['chat']['username']
	name = response['result'][0]['message']['chat']['first_name']
	return response

def last_update(data):
	global last_updates
	result = response['result']
	last_updates = len(result) - 1
	return result[last_updates]

def word(request):
	global slovo
	slovo = response['result'][last_updates]['message']['text']


def get_id(update):
	idd = response['result'][last_updates]['message']['chat']['id']
	return idd

# УПРОСТИТЬ 
def send_message(chat , text):
	message = requests.post(a + 'SendMessage' , params = {'chat_id' : chat , 'text' : text })
	print(message.status_code , "good") 
	return message

def last_update_id(update):
	update_ids = []
	for update in updates['result']:
		update_ids.append(int(update['update_id']))
		return max(update_ids)


def main():
	last_update_id = last_update(get_url_dec_json(a))['update_id']
	idd = get_id(last_update(get_url_dec_json(a)))

	#send_message(idd, 'Добрый день, ' + str(name))
	#send_message(idd, 'Ваш ник для входа: ' + username)
	#send_message(idd, 'Выберите интересующую Вас тематику: ')

	while True:
		if last_update_id == last_update(get_url_dec_json(a))['update_id']:
			send_message(get_id(last_update(word(a))), 'Вы ввели : ' + slovo)
			last_update_id +=1
	sleep(1)


if __name__ == "__main__":
	main()
