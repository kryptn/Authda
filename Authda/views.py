from flask import Flask, request, json, current_app, redirect, url_for
from flask.views import MethodView

import requests

from Authda.helpers import ApiResult, context_webhook


def index():
    return ''


class OAuth(MethodView):
    def get(self):
        auth_url = 'https://romeosquad.slack.com/oauth?client_id={}&scope={}&redirect_uri={}'
        token_url = 'https://slack.com/api/oauth.access?client_id={}&client_secret={}&code={}&redirect_uri={}'
        uri = 'http://aws.kryptn.com:5000/oauth/'

        client_id = current_app.config.get('SLACK_CLIENT_ID')
        client_secret = current_app.config.get('SLACK_CLIENT_SECRET')

        scope = 'client admin'        

        if 'access_token' in request.args:
            return request.args

        if 'code' in request.args:
            code = request.args.get('code')
            return redirect(token_url.format(client_id, client_secret, code, uri))
        
        return redirect(auth_url.format(client_id, scope, uri))

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
        


