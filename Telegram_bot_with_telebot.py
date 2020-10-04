import telebot 
name = '';
surname = '';
age = '';

bot = telebot.TeleBot('...')
@bot.message_handler(content_types=['text' , 'document' , 'audio' , 'video'])

def registration(message):
	if message.text == "/registration":
		bot.send_message(message.from_user.id, "Регистрация пользователя для создания индивидуальной подборки")
		bot.register_next_step_handler(message , start)
	else:
		bot.send_message(message, ' для регистрации напиши : /registration ')

def start(message):
	bot.send_message(message.from_user.id , 'введи чето')
	bot.register_next_step_handler(message , name)

def name(message):
	global name
	name = message.text
	bot.send_message(message.from_user.id, 'Твое имя: ')
	bot.register_next_step_handler(message, surname)

def surname(message):
	global surname
	surname = message.text
	bot.send_message(message.from_user.id, 'Твоя фамилия: ')
	bot.register_next_step_handler(message , age)

def age(message):
	global age
	age = message.text
	bot.send_message(message.from_user.id, 'Твой возраст. Введи цифрами: ')
	bot.register_next_step_handler(message , nic)
	try:
		age = int(message.text)
	except Exception:
		bot.send_message(message.from_user.id, 'Цифрами вводи: ')

def nic(message):
	global nic
	nic = message.text
	bot.send_message(message.from_user.id, 'твой ник для входа: ')
	bot.register_next_step_handler(message , check)

def check(message):
	answer = message.text
	return_inf = 'Добро пожаловать, ' + nic + ' . твое имя: ' + name + ' и фамилия: ' + surname + ', а возраст: ' + age + ' лет. Все правильно? '
	bot.send_message(message.from_user.id, return_inf)

	if answer == 'Да':
		bot.register_next_step_handler(message.user.id, text = return_inf)
	else :
		bot.send_message(message.from_user.id, 'Введем данные заново')
		bot.register_next_step_handler(message, name)
	


bot.polling(none_stop=True, interval=0)






