import unittest
from flask import current_app
from app import create_app, db
from db.db_queries import query_yeshuvknesset_by_sn


class TestYeshuvKnesset(unittest.TestCase):
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




    def test_yeshuv_knesset_data_query_working(self):
        yeshuvKnesset_model_data = query_yeshuvknesset_by_sn(3000)
        self.assertIsNotNone(yeshuvKnesset_model_data)

    def test_yeshuv_knesset_data_query_correct_1(self):
        yeshuvKnesset_model_data = query_yeshuvknesset_by_sn(3000)

        self.assertTrue(yeshuvKnesset_model_data.SN == 3000)
        self.assertTrue(yeshuvKnesset_model_data.Voters_18 == 217905)
        self.assertTrue(yeshuvKnesset_model_data.vote_percent_18 == 61.59)
        self.assertTrue(yeshuvKnesset_model_data.BZB_22 == 413140)
        self.assertTrue(yeshuvKnesset_model_data.Kalfi_Num_22 == 667)
        self.assertTrue(yeshuvKnesset_model_data.Avg_BZB_22 == 619.4002999)
        self.assertTrue(yeshuvKnesset_model_data.Error_Voters_21 == 2054)
        self.assertTrue(yeshuvKnesset_model_data.Error_Voters_22 == 1840)


    def test_yeshuv_knesset_data_query_correct_2(self):
        yeshuvKnesset_model_data = query_yeshuvknesset_by_sn(446)
        self.assertTrue(yeshuvKnesset_model_data.SN == 446)
        self.assertTrue(yeshuvKnesset_model_data.Voters_18 == 467)
        self.assertTrue(yeshuvKnesset_model_data.vote_percent_18 == 77.83)
        self.assertTrue(yeshuvKnesset_model_data.BZB_22 == 798)
        self.assertTrue(yeshuvKnesset_model_data.Kalfi_Num_22 == 2)
        self.assertTrue(yeshuvKnesset_model_data.Avg_BZB_22 == 399.0)
        self.assertTrue(yeshuvKnesset_model_data.Error_Voters_21 == 1)
        self.assertTrue(yeshuvKnesset_model_data.Error_Voters_22 == 0)

