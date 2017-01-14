import requests


class AuthBot:

    def __init__(self, endpoint, token, name='auth-bot', icon=':ghost:', channel='#general'):
        self.endpoint = endpoint
        self.token = token
        self.name = name
        self.icon = icon


    def send(self):
        payload = {'text': self.text,
                   'channel': self.channel,
                   'username': self.name,
                   'icon_emoji': ':ghost:'}
        result = requests.post(self.endpoint, json=payload)

        return result




class Webhook:

    endpoint = ''
    token = ''
    text = ''
    username = ''
    user_icon = ''

    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.token = token

    def send(self):
        payload = {'text': self.text
                   'channel' = 'self.channel
