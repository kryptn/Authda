from Authda.views import index, WebhookTest, OAuth

routes = [{'rule': '/', 'view_func': index},
          {'rule': '/oauth/', 'view_func': OAuth.as_view('oauth')},
          {'rule': '/webhook/', 'view_func': WebhookTest.as_view('webhook')}]


