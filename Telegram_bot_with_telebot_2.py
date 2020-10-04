import telebot 

#from telebot import apihelper
#apihelper.proxy = {'mtproto':'http://10.10.1.10:3128'}
#apihelper.proxy = {'http', 'socks5://login:pass@12.11.22.33:8000'}
#apihelper.proxy = {'https':'socks5://userproxy:password@proxy_address:port'}
#apihelper.proxy = {'https':'socks5h://userproxy:password@proxy_address:port'}

bot = telebot.TeleBot('...')

@bot.message_handler(content_types=['text'])

def text(message):
	if message.text == "Привет":
		bot.send_message(message.from_user.id, "Привет")
	elif message.text == "Кто ты?":
		bot.send_message(message.from_user.id, "Я тестовый чатбот для учебного примера.")
	elif message.text == "Как тебя зовут?":
		bot.send_message(message.from_user.id, "Меня зовут MyFirstTestBot.")
	elif message.text == "Что ты умеешь?":
		bot.send_message(message.from_user.id, "Я умею отвечать на несколько простых вопросов - кто я, как меня зовут и что я умею делать.")
	else:
		bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши что-то другое.")

bot.polling(none_stop=True, interval=0)
