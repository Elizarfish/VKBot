#!/usr/bin/python
#-*- coding utf8 -*-
# Author: https://vk.com/id181265169
import vk, urllib2, json, random, time

config = {}# Создаём массив с конфигурацией
try:
	execfile("config.py", config)# Загружаем туда конфигурацию из файла
except IOError:
	print u"Нету файла конйфигурации, чтобы его создать, запустите команду \"python auth.py\" "
	quit(1)
url = "https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username=%s&password=%s" % (config['username'], config['password'])
try:
    r = urllib2.urlopen(url)# Переходим по ссылке(логинимся)
except urllib2.HTTPError:
    print u"Не получилось авторизоваться (возможно неправильно указаны логин или пароль)"
    quit(1)
r = r.read()# Читаем, что нам вернул сайт
token = json.loads(r)["access_token"]# Декодируем через JSON и читаем access_token(то, зачем мы вообще логинились)
 
session = vk.Session(access_token = token)# Создаём сессию ВК
api = vk.API(session)
 
foo = [u"Я ебал твою мать арматурой, уёбище!", u"Пиздец ты доблоёб нахуй", u"Твоя мать так охуенно сосёт:P",
u"Завали ебло, шавка подзаборная!", u"Я думал я тебя в гандоне забыл, но видимо какая-то шлюха подобрала его и родила тебя!", u"Заткни ебло, кусок говна!",
u"У меня залупа больше, чем твой мозг.", u"Хуле ты как клоун до меня доёбываешься, не видишь мне похуй?XD", u"Хуйло ссаное",
u"Рот открывать будешь перед хуём", u"Вьеби говна в свой воняющий хуями рот!", u"Прямо сейчас я верчу твою мать на хуе, как на качелях, ты понимаешь?", u"Я тебе ебало разобью", u"Ебись конём, уёбок!", u"Твою мать опустили гопники", u"Позор человечества бля, иди нахуй!!!!",
u"Береги жопу, а не то трахну!!))))", u"Ты мне тут не пизди, а убери свою мать у меня из под столаXDXDXD Если сможешь;)"]
def mainloop():
  try:
    while(1):# Повторять, пока не выключим
        time.sleep(2)# Ждём 2 секунды
        r = api.messages.get(count = 1, time_offset = 1)# Получаем 1 сообщение не старше 1 секунды
        if len(r) > 1:# Если сообщения есть
          r = r[1]
          if('chat_id' in r):# Если сообщение получено из беседы
            print u"Отвечаем беседе id: %s" % (r['chat_id'])# Пишем id беседы
            r = api.messages.send(peer_id = 2000000000 + r['chat_id'],
            message=random.choice(foo), v=5.38)# Отправляем рандомное сообщение из списка(насчёт peer_id см. https://vk.com/dev/messages.send)
          else:# Если же сообщение из ЛС
            print u"Отвечаем пользователю id: %s" % (r['uid'])# Пишем id пользователя
            r = api.messages.send(peer_id = r['uid'],
            message=random.choice(foo), v = 5.38)# Отправляем рандомное сообщение из списка
    pass
  except KeyboardInterrupt:
    pass
  except:
    print u"Истекло время обращения к серверу"
    return
 
mainloop()