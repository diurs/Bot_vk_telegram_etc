from flask import Flask, request, json
from settings import *
import vk
def get_answer(body):
    our_message = "Привет, я новый бот!"
    return our_message
app = Flask(__name__)
@app.route('/', methods=['POST'])
def processing():
    #Распаковываем json из пришедшего POST-запроса
    data = json.loads(request.data)
    #Вконтакте в своих запросах всегда отправляет поле типа
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        session = vk.Session()

        api = vk.API(session, v=5.5)
        user_id = data['object']['user_id']
        our_message = get_answer(data['body'])
        api.messages.send(access_token=token, user_id=str(user_id), message='Привет, я новый бот!')
        # Сообщение о том, что обработка прошла успешно
        return 'ok'