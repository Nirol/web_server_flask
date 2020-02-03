import unittest
from flask import current_app
from api.yeshuv import  get_yeshuv_data_api
from app import create_app, db



class TestToJsonDict(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        self.app_context.pop()

    def test_to_json_dict(self):
        get_yeshuv_data_api(3000)
        self.assertFalse(current_app is None)
