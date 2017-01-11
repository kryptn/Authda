from flask_testing import TestCase

from Authda.helpers import create_app
from Authda.models import db

class ViewsTest(TestCase):

    def create_app(self):
        return create_app('Authda.settings.testing')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_test(self):
        self.assertTrue(True)
