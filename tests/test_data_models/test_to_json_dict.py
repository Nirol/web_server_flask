import unittest
from flask import current_app
from api.yeshuv import  get_yeshuv_data_api
from app import create_app, db
from tests import YESHUV_SN_FOR_TESTING


class TestToJsonDict(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        self.app_context.pop()

    # def test_to_json_dict(self):
    #     get_yeshuv_data_api(YESHUV_SN_FOR_TESTING)
    #     self.assertFalse(current_app is None)
