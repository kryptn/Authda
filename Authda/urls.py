from Authda.views import index, WebhookTest, OAuth, Invitations

routes = [{'rule': '/', 'view_func': index},
          {'rule': '/oauth/', 'view_func': OAuth.as_view('oauth')},
          {'rule': '/invite/', 'view_func': Invitations.as_view('new_invite')},
          {'rule': '/invite/<int:id>/', 'view_func': Invitations.as_view('change_invite')}]

