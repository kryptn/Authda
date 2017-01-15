import requests


class AuthBot:

    handlers = {'echo': lambda d: d['text']}

    def __init__(self, endpoint, token, name='auth-bot', icon=':ghost:', channel='#general'):
        self.endpoint = endpoint
        self.channel = channel
        self.token = token
        self.name = name
        self.icon = icon

    def handle(self, data):

        if self.token != data['token']:
            return
        
        if self.name == data['bot_name']:
            return
        
        handler = self.handlers.get(data['trigger_word'], None)
        if handler:
            result = handler(data)
            self.send(result)

    def payload(self, text):
        return {'text': text,
                'channel': self.channel,
                'username': self.name,
                'icon_emoji': self.icon}

    def send(self, text):
        payload = self.payload(text)
        result = requests.post(self.endpoint, json=payload)




