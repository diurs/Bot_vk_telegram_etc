import requests
import json
import datetime
from time import sleep

# удалить токен для github
a = "https://api.telegram.org/bot1029594886:AAGZYqngglwyzxvmIEm8rCNjk5Qffghk5HE/"

def get_url_dec_json(request):
	global response
	global username
	global name
	global slovo
	#mark viewed updates - "offset"
	# timeout - работает только при отсутствии последних обновлений
	url = requests.get(a + "getUpdates" , params = {'timeout': 50 , 'mark_viewed_updates': None} )
	#print(url.status_code)
	response = url.json()
	username = response['result'][0]['message']['chat']['username']
	name = response['result'][0]['message']['chat']['first_name']
	slovo = response['result'][0]['message']['text']
	return response

def word(request):
	global slovo
	slovo = response['result'][0]['message']['text']
	slovo = prin
	#print("")


def get_id(update):
	idd = response['result'][0]['message']['chat']['id']
	return idd

def last_update(data):
	result = response['result']
	last_updates = len(result) - 1
	return result[last_updates]

def send_message(chat , text):
	#params = {'id' : chat , 'text' : text }
	message = requests.post(a + 'SendMessage' , params = {'chat_id' : chat , 'text' : text })
	print(message.status_code , "good") 
	return message

def main():
	#get_url_dec_json()
	#get_id(response)
	
	last_update_id = last_update(get_url_dec_json(a))['update_id']

	idd = get_id(last_update(get_url_dec_json(a)))

	#idd2 = get_id(last_update(get_url_dec_json(slovo(a))))
	send_message(idd, 'Добрый день, ' + str(name))
	send_message(idd, 'Ваш ник для входа: ' + username)
	send_message(idd, 'Выберите интересующую Вас тематику: ')
	#send_message(idd, 'вы выбрали ' + slovo)
	while True:
		if last_update_id == last_update(get_url_dec_json(a))['update_id']:
		#idd = get_id(last_update(get_url_dec_json(a)))
		#send_message(idd , 'мяк')
			send_message(get_id(last_update(get_url_dec_json(a))), 'пасинг из словаря : ' + slovo)
			#send_message(get_id(last_update(get_url_dec_json(a))), 'ddd')
			#who()
			last_update_id +=1
			send_message(idd, 'ответная реакция на смс пользователя ')
	sleep(1)


if __name__ == "__main__":
	main()
