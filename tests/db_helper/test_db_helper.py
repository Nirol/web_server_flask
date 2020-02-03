
import unittest
from app import create_app, db
from db.db_helper import _parse_knesset22_query_for_sn
from db.db_queries import *



class TestKnesset22TopBott(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        self.app_context.pop()


    def test_parse_knesset22_query_for_sn(self):
        knesset_22_data_bottom = query_knesset22_kalfi_bottom_n_vote_percent(3000)
        result_list = _parse_knesset22_query_for_sn(knesset_22_data_bottom)
        expecteled_kalfi_num_list = [994, 742, 832, 519, 519]
        self.assertTrue(result_list == expecteled_kalfi_num_list)

    def test_query_kalfi_by_list(self):
        knesset_22_data_bottom = query_knesset22_kalfi_bottom_n_vote_percent(
            3000)
        result_list = _parse_knesset22_query_for_sn(knesset_22_data_bottom)
        result_kalfi = query_kalfi_metadata_by_list(3000, result_list)
        print("kek")











