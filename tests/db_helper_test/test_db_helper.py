import unittest


from app import create_app
from db_helper import query_helper_kalfi_meta_top_or_bottom

from db_queries import *
from tests import YESHUV_SN_FOR_TESTING, YESHUV_SN_FOR_TESTING_B, \
    YESHUV_SN_FOR_TESTING_C


class TestKnesset22TopBott(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()


    def tearDown(self):
        db.session.remove()
        self.app_context.pop()


    # TODO complete test
    def test_query_meta_by_kalfi_data_list_1(self):

        kalfi_data_bottom_n = query_knesset22_kalfi_bottom_n_vote_percent(
            YESHUV_SN_FOR_TESTING_B)

        kalfi_meta_bottom_n = query_helper_kalfi_meta_top_or_bottom(
            YESHUV_SN_FOR_TESTING_B, kalfi_data_bottom_n)
        for idx, kalfi in enumerate(kalfi_data_bottom_n):
            self.assertEqual(kalfi_meta_bottom_n[idx].kalfi_num_int, kalfi.Kalfi_Num)


    def test_query_meta_by_kalfi_data_list_2(self):
        kalfi_data_bottom_n = query_knesset22_kalfi_bottom_n_vote_percent(
            YESHUV_SN_FOR_TESTING)
        kalfi_meta_bottom_n = query_helper_kalfi_meta_top_or_bottom(
            YESHUV_SN_FOR_TESTING, kalfi_data_bottom_n)
        self.assertEqual(len(kalfi_data_bottom_n), len(kalfi_meta_bottom_n))
        for idx, kalfi in enumerate(kalfi_data_bottom_n):
            self.assertEqual(kalfi_meta_bottom_n[idx].kalfi_num_int, kalfi.Kalfi_Num)



    def test_query_meta_by_kalfi_data_list_3(self):
        kalfi_data_bottom_n = query_knesset22_kalfi_top_n_by_vote_percent(
            YESHUV_SN_FOR_TESTING)
        kalfi_meta_bottom_n = query_helper_kalfi_meta_top_or_bottom(
            YESHUV_SN_FOR_TESTING, kalfi_data_bottom_n)
        self.assertEqual(len(kalfi_data_bottom_n), len(kalfi_meta_bottom_n))
        for idx, kalfi in enumerate(kalfi_data_bottom_n):
            self.assertEqual(kalfi_meta_bottom_n[idx].kalfi_num_int, kalfi.Kalfi_Num)



    def test_query_meta_by_kalfi_data_list_4(self):
        kalfi_data_bottom_n = query_knesset22_kalfi_bottom_n_vote_percent(
            YESHUV_SN_FOR_TESTING_C)
        kalfi_meta_bottom_n = query_helper_kalfi_meta_top_or_bottom(
            YESHUV_SN_FOR_TESTING_C, kalfi_data_bottom_n)
        self.assertEqual(len(kalfi_data_bottom_n), len(kalfi_meta_bottom_n))
        for idx, kalfi in enumerate(kalfi_data_bottom_n):
            self.assertEqual(kalfi_meta_bottom_n[idx].kalfi_num_int, kalfi.Kalfi_Num)

















