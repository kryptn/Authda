from Authda import app
from Authda.models import db

db.init_app(app)

if __name__ == '__main__':
    app.run()
