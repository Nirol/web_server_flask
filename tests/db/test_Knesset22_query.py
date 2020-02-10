import unittest
from app import create_app, db
from db_queries import query_knesset22_kalfi
from tests import YESHUV_SN_FOR_TESTING


class TestKnesset_22(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()


    def tearDown(self):
        db.session.remove()
        self.app_context.pop()


    def test_kalfi_knesset_query_working(self):
        knesset_22_data = query_knesset22_kalfi(YESHUV_SN_FOR_TESTING)
        self.assertIsNotNone(knesset_22_data)


    def test_kalfi_knesset_query_correct_1(self):
        knesset_22_data = query_knesset22_kalfi(YESHUV_SN_FOR_TESTING)
        knesset_22_data_first_kalfi = knesset_22_data[0]
        self.assertTrue(knesset_22_data_first_kalfi.BZB == 699)
        self.assertTrue(knesset_22_data_first_kalfi.Error_Voters == 4)
        self.assertTrue(knesset_22_data_first_kalfi.Kalfi_Num == 3)
        self.assertTrue(knesset_22_data_first_kalfi.Voters == 411)


    def test_kalfi_knesset_query_correct_2(self):
        knesset_22_data = query_knesset22_kalfi(YESHUV_SN_FOR_TESTING)
        knesset_22_data_single_kalfi = knesset_22_data[15]
        self.assertTrue(knesset_22_data_single_kalfi.BZB == 633)
        self.assertTrue(knesset_22_data_single_kalfi.Error_Voters == 0)
        self.assertTrue(knesset_22_data_single_kalfi.Kalfi_Num == 18)
        self.assertTrue(knesset_22_data_single_kalfi.Voters == 163)