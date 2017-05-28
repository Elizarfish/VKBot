#-*- coding utf8 -*-
import vk
import urllib2
import json
import random
import time

config = {}
execfile("config.py", config)

url = "https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username=%s&password=%s" % (config['username'],config['password'])
response = urllib2.urlopen(url)
response = response.read()
token = json.loads(response)["access_token"] # Token

session = vk.Session(access_token=token)
api = vk.API(session)

foo = [u"Я ебал твою мать арматурой,уёбище!",u"Хуй моей собаки тебя любит))",u"Твоя мать так охуенно сосёт:P",u"Завали ебло,шавка подзаборная!",u"Я думал я тебя в гандоне забыл,но видимо какая-то шлюха  подобрала  его  и  родила  тебя,говноеда!!"]

while(1):
        time.sleep(2)
        r = api.messages.get(count=1,time_offset=1)
        if len(r) > 1:
                r = r[1]
                if('chat_id' in r):
                        print r['chat_id']
                        r = api.messages.send(peer_id=2000000000+r['chat_id'], message=random.choice(foo),v=5.38)
                else:
                        print(r['uid'])
                        r = api.messages.send(user_id=r['uid'], peer_id=r['uid'], message=random.choice(foo),v=5.38)
                        
        else:
                print("Waiting for incoming messages...")
