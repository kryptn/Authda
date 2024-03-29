from contextlib import contextmanager

import jwt
from flask import Flask, json, Response, current_app

from Authda.slack import AuthBot, AdminSlacker

class ApiFlask(Flask):
    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)


class ApiResult:
    def __init__(self, value, status=200, payload=None):
        self.value = value
        self.status = status
        self.payload = payload

    def to_response(self):
        token = jwt.encode(self.payload, current_app.secret_key, algorithm='HS256')
        return Response(json.dumps(self.value),
                        status=self.status,
                        mimetype='application/json',
                        headers={'Authorization': token})


class ApiException(Exception):
    def __init__(self, message, status=400):
        Exception.__init__(self)
        self.message = message
        self.status = status

    def to_result(self):
        return ApiResult({'message': self.message},
                         status=self.status)

@contextmanager
def context_webhook(*args, **kwargs):
    auth = {'name': current_app.config.get('SLACK_BOT_NAME'),
            'icon': current_app.config.get('SLACK_BOT_ICON'),
            'channel': current_app.config.get('SLACK_BOT_CHANNEL'),
            'endpoint': current_app.config.get('SLACK_WEBHOOK_URI'),
            'token': current_app.config.get('SLACK_WEBHOOK_TOKEN')}

    kwargs.update(auth)

    api = AuthBot(**kwargs)
    yield api

@contextmanager
def slack_context():
    token = current_app.config.get('DUNGARMATIC_TOKEN', None)
    if not token:
        raise ApiException('Missing Config: `DUNGARMATIC_TOKEN`')

    slack = AdminSlacker(token)
    yield slack

def create_app(settings=None):
    app = ApiFlask(__name__)

    app.config.from_object('Authda.settings.default')
    if settings:
        app.config.from_object(settings)

    from Authda.models import db
    db.init_app(app)

    from Authda.urls import routes
    for route in routes:
        app.add_url_rule(**route)

    app.register_error_handler(ApiException, lambda e: e.to_result())

    return app

    
