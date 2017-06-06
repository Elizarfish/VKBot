#-*- coding utf8 -*-
# Author: https://vk.com/id181265169
import vk
import urllib2
import json
import random
import time

config = {}# Создаём массив с конфигурацией
execfile("config.py", config)# Загружаем туда конфигурацию из файла

url = "https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username=%s&password=%s" % (config['username'], config['password'])
r = urllib2.urlopen(url)# Переходим по ссылке(логинимся)
r = r.read()# Читаем, что нам вернул сайт
token = json.loads(r)["access_token"]# Декодируем через JSON и читаем access_token(то, зачем мы вообще логинились)

session = vk.Session(access_token = token)# Создаём сессию ВК
api = vk.API(session)

foo = [u"Я ебал твою мать арматурой, уёбище!", u"Хуй моей собаки тебя любит))",u"Твоя мать так охуенно сосёт:P", 
u"Завали ебло, шавка подзаборная!", u"Я думал я тебя в гандоне забыл, но видимо какая-то шлюха  подобрала  его  и  родила  тебя, говноеда!!", u"Заткни ебло, кусок говна!", 
u"У меня залупа больше, чем твой мозг.", u"Пошёл в пизду, сын собаки ебаный", u"Хуйло ссаное", 
u"Рот открывать будешь перед хуём", u"Вьеби говна, уебан", u"Прямо сейчас я верчу твою мать на хуе, как на качелях, ты понимаешь?", 
u"Я тебе ебало разобью",  u"Ебись конём, уёбок!"]

while(1):# Повторять, пока не выключим
        time.sleep(1)# Ждём 1 секунду
        r = api.messages.get(count = 1, time_offset = 1)# Получаем 1 сообщение не старше 1 секунды
        if len(r) > 1:# Если сообщения есть
			r = r[1]
			if('chat_id' in r):# Если сообщение получено из беседы
				print u"Отвечаем беседе id: %s" % (r['chat_id'])# Пишем id беседы
				r = api.messages.send(peer_id = 2000000000 + r['chat_id'], 
				message=random.choice(foo),  v=5.38)# Отправляем рандомное сообщение из списка(насчёт peer_id см. https://vk.com/dev/messages.send)
			else:# Если же сообщение из ЛС
				print u"Отвечаем пользователю id: %s" % (r['uid'])# Пишем id пользователя
				r = api.messages.send(peer_id = r['uid'], 
				message=random.choice(foo), v = 5.38)# Отправляем рандомное сообщение из списка
