from flask import Flask, request, json, current_app
from flask.views import MethodView

import requests

from Authda.helpers import ApiResult
from Authda.slack import AuthBot


bot = AuthBot


bot_name = current_app.config.get('SLACK_BOT_NAME', None)
webhook_uri = current_app.config.get('SLACK_WEBHOOK_URI', None)



def index():
    return ''


class WebhookTest(MethodView):
    def post(self):
#        bot_name = current_app.config.get('SLACK_BOT_NAME', None)
#        webhook_uri = current_app.config.get('SLACK_WEBHOOK_URI', None)

        text = request.form.get('text', 'default yo')
        name = request.form.get('bot_name', None)

        if name == bot_name:
            return ApiResult('nothing lol')

        payload = {'text': 'echo '+json.dumps(request.form),
                   'channel': '#general',
                   'username': 'test-bot',
                   'icon_emoji': ':ghost:'}
        result = requests.post(webhook_uri, json=payload)

        return ApiResult(result.content)


