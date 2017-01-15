from flask import Flask, request, json, current_app
from flask.views import MethodView

import requests

from Authda.helpers import ApiResult, context_webhook


def index():
    return ''


class WebhookTest(MethodView):
    def post(self):

        default = {'token': '',
                   'team_id': '',
                   'team_domain': '',
                   'channel_id': '',
                   'channel_name': '',
                   'timestamp': '',
                   'user_id': '',
                   'user_name': '',
                   'bot_id': '',
                   'bot_name': '',
                   'text': '',
                   'trigger_word': ''}

        received = {k: request.form.get(k, v) for k, v in default.items()}

        with context_webhook() as api:
            result = api.handle(received)

        return ApiResult('Success')
        


