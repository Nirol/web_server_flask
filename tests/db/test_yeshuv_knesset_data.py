import unittest
from app import create_app, db
from db_queries import query_yeshuvknesset_by_sn, \
    query_yeshuvknesset_kalfi_num_22_by_sn
from tests import YESHUV_SN_FOR_TESTING, YESHUV_SN_FOR_TESTING_B


class TestYeshuvKnesset(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        self.app_context.pop()

    def test_yeshuv_knesset_kalfi_num_query_working(self):
        num = query_yeshuvknesset_kalfi_num_22_by_sn(YESHUV_SN_FOR_TESTING)
        self.assertIsNotNone(num)


    def test_yeshuv_knesset_kalfi_num_query_correct(self):
        num = query_yeshuvknesset_kalfi_num_22_by_sn(YESHUV_SN_FOR_TESTING)
        self.assertEqual(num,667)

    def test_yeshuv_knesset_kalfi_num_query_correct_2(self):
        num = query_yeshuvknesset_kalfi_num_22_by_sn(YESHUV_SN_FOR_TESTING_B)
        self.assertEqual(num, 2)



    def test_yeshuv_knesset_data_query_working(self):
        yeshuvKnesset_model_data = query_yeshuvknesset_by_sn(YESHUV_SN_FOR_TESTING)
        self.assertIsNotNone(yeshuvKnesset_model_data)

    def test_yeshuv_knesset_data_query_correct_1(self):
        yeshuvKnesset_model_data = query_yeshuvknesset_by_sn(YESHUV_SN_FOR_TESTING)

        self.assertTrue(yeshuvKnesset_model_data.SN == YESHUV_SN_FOR_TESTING)
        self.assertTrue(yeshuvKnesset_model_data.Voters_18 == 217905)
        self.assertTrue(yeshuvKnesset_model_data.vote_percent_18 == 61.59)
        self.assertTrue(yeshuvKnesset_model_data.BZB_22 == 413140)
        self.assertTrue(yeshuvKnesset_model_data.Kalfi_Num_22 == 667)
        self.assertAlmostEqual(yeshuvKnesset_model_data.Avg_BZB_22, 619.4002999,3)
        self.assertTrue(yeshuvKnesset_model_data.Error_Voters_21 == 2054)
        self.assertTrue(yeshuvKnesset_model_data.Error_Voters_22 == 1840)


    def test_yeshuv_knesset_data_query_correct_2(self):
        yeshuvKnesset_model_data = query_yeshuvknesset_by_sn(YESHUV_SN_FOR_TESTING_B)
        self.assertTrue(yeshuvKnesset_model_data.SN == YESHUV_SN_FOR_TESTING_B)
        self.assertTrue(yeshuvKnesset_model_data.Voters_18 == 467)
        self.assertTrue(yeshuvKnesset_model_data.vote_percent_18 == 77.83)
        self.assertTrue(yeshuvKnesset_model_data.BZB_22 == 798)
        self.assertTrue(yeshuvKnesset_model_data.Kalfi_Num_22 == 2)
        self.assertTrue(yeshuvKnesset_model_data.Avg_BZB_22 == 399.0)
        self.assertTrue(yeshuvKnesset_model_data.Error_Voters_21 == 1)
        self.assertTrue(yeshuvKnesset_model_data.Error_Voters_22 == 0)

