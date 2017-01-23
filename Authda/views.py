from flask import Flask, request, json, current_app, redirect, url_for, render_template
from flask.views import MethodView

import requests

from Authda.helpers import ApiResult, ApiException, context_webhook, slack_context
from Authda.models import Invite


def index():
    return render_template('index.html')


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


class Invitations(MethodView):
    def get(self):
        result = Invite.get_pending()
        return ApiResult([x.to_json() for x in result])

    def post(self):
        email = request.form.get('email', None)
        referrer = request.form.get('referrer', None)

        if email and referrer:
            result = Invite.get_or_create(email, referrer)
            with slack_context() as slack:
                slack.chat.post_message('#bot-test', '{} requested an invite, {} referred'.format(email, referrer))
            return ApiResult(result.to_json())
        else:
            raise ApiException('key `email` or key `referrer` missing')

    def put(self, id):
        notes = request.form.get('notes', None)
        action = request.form.get('action', None)

        if not action:
            raise ApiException('idk something happened')

        result = Invite.query.filter_by(id=id).one_or_none()
        if not result:
            raise ApiException('invitation doesnt exist')

        if action == 'invite':
            tmp = '{} invited'
            result.invite()
            with slack_context() as slack:
                slack.users.admin.invite(result.email)
                slack.chat.post_message('#bot-test', tmp.format(result.email))

        if action == 'reject':
            tmp = '{} rejected'
            result.reject()
            with slack_context() as slack:
                slack.chat.post_message('#bot-test', tmp.format(result.email))

        return ApiResult(result.to_json())


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
        


