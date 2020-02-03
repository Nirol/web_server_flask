import unittest
from flask import current_app
from app import create_app, db
from db.db_queries import query_kalfi_metadata_all
from fix_hebrew_text import clean_kalfi_hebrew_texts


class TestCleanHebrew(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()



    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    # Manual check of cleanning results:
    def test_clean_hebew_text_1(self):
        kalfi_meta_data_list = query_kalfi_metadata_all()
        self.assertIsNotNone(kalfi_meta_data_list)
        for knesset_meta in kalfi_meta_data_list:
            clean_kalfi_hebrew_texts(knesset_meta)

