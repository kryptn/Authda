from contextlib import contextmanager

from flask import Flask, json, Response, current_app

from Authda.slack import AuthBot

class ApiFlask(Flask):
    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)


class ApiResult:
    def __init__(self, value, status=200):
        self.value = value
        self.status = status

    def to_response(self):
        return Response(json.dumps(self.value),
                        status=self.status,
                        mimetype='application/json')


class ApiException(Exception):
    def __init__(self, message, status=400):
        Exception.__init__(self)
        self.message = message
        self.status = status

    def to_result(self):
        return ApiResult({'message': self.message},
                         status=self.status)

@contextmanager
def context_webhook():
    auth = {'name': current_app.config.get('SLACK_BOT_NAME'),
            'icon': current_app.config.get('SLACK_BOT_ICON'),
            'channel': current_app.config.get('SLACK_BOT_CHANNEL'),
            'endpoint': current_app.config.get('SLACK_WEBHOOK_URI'),
            'token': current_app.config.get('SLACK_WEBHOOK_TOKEN')}

    api = AuthBot(**auth)
    yield api

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

    
