import unittest
from app import create_app, db
from constants import KALFI_METADATA_COUNT
from queries.yeshuv_knesset import  query_kalfi_metadata, query_kalfi_metadata_all
from tests import YESHUV_SN_FOR_TESTING, YESHUV_SN_FOR_TESTING_C


class TestKalfiMeta(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()



    def tearDown(self):
        db.session.remove()
        self.app_context.pop()
    def test_kalfi_metadata_query_working(self):
        kalfi_meta_data_list = query_kalfi_metadata(YESHUV_SN_FOR_TESTING)
        self.assertIsNotNone(kalfi_meta_data_list)


    def test_kalfi_metadata_query_correct_1(self):
        kalfi_meta_data_list = query_kalfi_metadata(YESHUV_SN_FOR_TESTING)
        kalfi_15_meta_data = kalfi_meta_data_list[15]
        self.assertEqual('שבטי ישראל 27', kalfi_15_meta_data.address)

        self.assertEqual(kalfi_15_meta_data.kalfi_num_int, 18)
        self.assertEqual(kalfi_15_meta_data.sub_kalfi_num, 0)
        self.assertEqual(kalfi_15_meta_data.location, 'משרד החינוך')
        self.assertEqual(kalfi_15_meta_data.yeshuv_sn , 3000)


    def test_kalfi_metadata_query_correct_2(self):
        kalfi_meta_data_list = query_kalfi_metadata(YESHUV_SN_FOR_TESTING_C)
        kalfi_10_meta_data = kalfi_meta_data_list[10]

        self.assertEqual( 'שחם יואב 5', kalfi_10_meta_data.address,)
        self.assertEqual(kalfi_10_meta_data.kalfi_num_int, 11)
        self.assertEqual(kalfi_10_meta_data.sub_kalfi_num, 3)
        self.assertEqual(kalfi_10_meta_data.yeshuv_sn, 28)


    def test_kalfi_metadata_query_all_correct(self):
        kalfi_meta_data_list = query_kalfi_metadata_all()
        self.assertIsNotNone(kalfi_meta_data_list)
        total_number_kalfi = len(kalfi_meta_data_list)
        self.assertTrue(total_number_kalfi == KALFI_METADATA_COUNT)
