# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 17:15:18 2018

@author: Phoenix
"""

import requests  
import datetime

class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json
    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp
    def get_last_update(self):
        get_result = self.get_updates()
        last_update = None
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            print ('error' + str(len(get_result)))
            if len(get_result) != 0:
                print ('ok')
                last_update = get_result[len(get_result)]
        return last_update

def main():  
    new_offset = None
    today = now.day
    hour = now.hour
    while True:
        print (1)
        greet_bot.get_updates(new_offset)
        print (2)
        last_update = greet_bot.get_last_update()
        print ('hhh' + str(last_update))
        if last_update != None:
            try:
                with open('log.txt', 'a') as f:
                    f.write(str(last_update) + '\n')
                print ('im in')
                last_update_id = last_update['update_id']
                last_chat_text = last_update['message']['text']
                last_chat_id = last_update['message']['from']['id']
#                last_chat_name = last_update['message']['from']['first_name']
                
            except Exception as e:
                print (f'fail first {e}')
                last_update_id = last_update['update_id']
                last_chat_text = ''
                last_chat_id = last_update['message']['from']['id']
            try:
                last_chat_username = last_update['message']['from']['username']
            except Exception as e:
                print (f'fail second {e}')
                last_chat_username = last_update['message']['from']['first_name']
            print (4)
            print (last_chat_text.lower())
            tag = 0
            if last_chat_text.lower() =='/help':
                print ('work in progress')
                greet_bot.send_message(last_chat_id, r'This is still a work in progress ¯\_(ツ)_/¯')
                tag = 1
            if last_chat_text.lower().find('f') != -1:
                print ('hehe')
                greet_bot.send_message(last_chat_id, r'F you too! {}'.format(last_chat_username))
                tag = 1
            if last_chat_text.lower().find('ffffff') != -1:
                print ('hehehe')
                greet_bot.send_message(last_chat_id, r'😋'.format(last_chat_username))
                tag = 1
                
            for greeting in greetings:
                if last_chat_text.lower().startswith(greeting):
                    tag = 1
                    print (hour)
                    greet_bot.send_message(last_chat_id, 'Yeah! Hello {}! Have a good day! '.format(last_chat_username))
                else:
                    if greeting == greetings[-1] and tag != 1:
                        print (hour, today)
                        greet_bot.send_message(last_chat_id, '😘 Thanks for testing out my bot, {}'.format(last_chat_username))
#                    today += 1
                    
        new_offset = last_update_id + 1
        print ('end')
    

greet_bot = BotHandler('')
greetings = ('hello', 'hi', 'greetings', 'sup')
now = datetime.datetime.now()
print (now)

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
