import requests

from slacker import BaseAPI, Users, Slacker


class Admin(BaseAPI):
    def invite(self, email, channels=None, first_name=None, last_name=None, resend=True):
        return self.post('users.admin.invite', params={
            'email': email,
            'channels': channels,
            'first_name': first_name,
            'last_name': last_name,
            'resend': resend})

class UsersAdmin(Users):
    def __init__(self, *args, **kwargs):
        super(UsersAdmin, self).__init__(*args, **kwargs)
        self._admin = Admin(*args, **kwargs)

    @property
    def admin(self):
        return self._admin

class AdminSlacker(Slacker):
    def __init__(self, token, url=None, timeout=10):
        super(AdminSlacker, self).__init__(token, incoming_webhook_url=url, timeout=timeout)
        self.users = UsersAdmin(token=token, timeout=timeout)


class AuthBot:

    handlers = {'echo': lambda d: d['text'],}

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




