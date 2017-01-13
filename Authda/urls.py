from Authda.views import index, WebhookTest

routes = [{'rule': '/', 'view_func': index},
          {'rule': '/webhook/', 'view_func': WebhookTest.as_view('webhook')}]


