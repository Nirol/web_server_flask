import unittest
from app import create_app
from db_queries import *
from tests import YESHUV_SN_FOR_TESTING


class TestKnesset22TopBott(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()



    def tearDown(self):
        db.session.remove()
        self.app_context.pop()


    def test_kalfi_knesset_top_bottom_working(self):
        knesset_22_data_bottom = query_knesset22_kalfi_bottom_n_vote_percent(YESHUV_SN_FOR_TESTING)
        self.assertIsNotNone(knesset_22_data_bottom)
        knesset_22_data_top = query_knesset22_kalfi_top_n_by_vote_percent(YESHUV_SN_FOR_TESTING)
        self.assertIsNotNone(knesset_22_data_top)

    def test_kalfi_knesset_query_bottom(self):
        knesset_22_data_bottom = query_knesset22_kalfi_bottom_n_vote_percent(YESHUV_SN_FOR_TESTING)
        knesset_22_data_first_kalfi = knesset_22_data_bottom[0]
        self.assertTrue(knesset_22_data_first_kalfi.BZB == 301)
        self.assertTrue(knesset_22_data_first_kalfi.Error_Voters == 0)
        self.assertTrue(knesset_22_data_first_kalfi.Kalfi_Num == 994)
        self.assertTrue(knesset_22_data_first_kalfi.Voters == 18)

        knesset_22_data_fifth = knesset_22_data_bottom[4]
        self.assertEqual(700, knesset_22_data_fifth.BZB)
        self.assertTrue(knesset_22_data_fifth.Error_Voters == 1)
        self.assertTrue(knesset_22_data_fifth.Kalfi_Num == 518)
        self.assertTrue(knesset_22_data_fifth.Voters == 93)

    def test_kalfi_knesset_query_top(self):
        knesset_22_data_bottom = query_knesset22_kalfi_top_n_by_vote_percent(YESHUV_SN_FOR_TESTING)

        knesset_22_data_first_kalfi = knesset_22_data_bottom[0]
        self.assertTrue(knesset_22_data_first_kalfi.BZB == 773)
        self.assertTrue(knesset_22_data_first_kalfi.Error_Voters == 14)
        self.assertTrue(knesset_22_data_first_kalfi.Kalfi_Num == 575)
        self.assertTrue(knesset_22_data_first_kalfi.Voters == 673)

        knesset_22_data_fifth = knesset_22_data_bottom[4]
        self.assertTrue(knesset_22_data_fifth.BZB == 752)
        self.assertTrue(knesset_22_data_fifth.Error_Voters == 8)
        self.assertTrue(knesset_22_data_fifth.Kalfi_Num == 811)
        self.assertTrue(knesset_22_data_fifth.Voters == 633)