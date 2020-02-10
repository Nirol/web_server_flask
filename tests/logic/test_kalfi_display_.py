import unittest
from app import create_app, db
from db_helper import query_helper_kalfi_meta_top_or_bottom
from db_queries import query_knesset22_kalfi, query_kalfi_metadata, \
    query_knesset22_kalfi_bottom_n_vote_percent
from tests import YESHUV_SN_FOR_TESTING_B, YESHUV_SN_FOR_TESTING_D, \
    YESHUV_SN_FOR_TESTING_C


class TestToJsonDict(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        self.app_context.pop()

    def test_get_data_vs_meta_reuslts_match_order(self):
        kalfi_data_list = query_knesset22_kalfi(YESHUV_SN_FOR_TESTING_B)
        kalfi_meta_list = query_kalfi_metadata(YESHUV_SN_FOR_TESTING_B)
        self.assertEqual(len(kalfi_data_list), len(kalfi_meta_list))
        for idx, kalfi in enumerate(kalfi_data_list):
            self.assertEqual(kalfi_meta_list[idx].kalfi_num_int,
                             kalfi.Kalfi_Num)


    def test_get_data_vs_meta_reuslts_match_order_2(self):
        kalfi_data_list = query_knesset22_kalfi(YESHUV_SN_FOR_TESTING_D)
        kalfi_meta_list = query_kalfi_metadata(YESHUV_SN_FOR_TESTING_D)
        self.assertEqual(len(kalfi_data_list), len(kalfi_meta_list))
        for idx, kalfi in enumerate(kalfi_data_list):
            self.assertEqual(kalfi_meta_list[idx].kalfi_num_int,
                             kalfi.Kalfi_Num)


    def test_get_data_vs_meta_reuslts_match_order_3(self):
        kalfi_data_bottom_n = query_knesset22_kalfi_bottom_n_vote_percent(
            YESHUV_SN_FOR_TESTING_C)
        kalfi_meta_bottom_n = query_helper_kalfi_meta_top_or_bottom(YESHUV_SN_FOR_TESTING_C,
                                                                    kalfi_data_bottom_n)
        self.assertEqual(len(kalfi_data_bottom_n), len(kalfi_meta_bottom_n))
        for idx, kalfi in enumerate(kalfi_data_bottom_n):
            self.assertEqual(kalfi_meta_bottom_n[idx].kalfi_num_int,
                             kalfi.Kalfi_Num)
