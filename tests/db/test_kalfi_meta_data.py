import unittest
from app import create_app, db
from logic.constants import KALFI_METADATA_COUNT
from db.db_queries import  query_kalfi_metadata, query_kalfi_metadata_all


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
    kalfi_meta_data_list = query_kalfi_metadata("3000")
    self.assertIsNotNone(kalfi_meta_data_list)


def test_kalfi_metadata_query_correct_1(self):
    kalfi_meta_data_list = query_kalfi_metadata(3000)
    kalfi_15_meta_data = kalfi_meta_data_list[15]
    self.assertTrue(kalfi_15_meta_data.address == 'שבטי ישראל27 ')
    self.assertTrue(kalfi_15_meta_data.kalfi_num_int == 18)
    self.assertTrue(kalfi_15_meta_data.kalfi_num == 18.0)
    self.assertTrue(kalfi_15_meta_data.location == 'משרד החינוך')
    self.assertTrue(kalfi_15_meta_data.yeshuv_sn == 3000)

def test_kalfi_metadata_query_correct_1(self):
    kalfi_meta_data_list = query_kalfi_metadata(28)
    kalfi_10_meta_data = kalfi_meta_data_list[10]

    self.assertTrue(kalfi_10_meta_data.address == 'שחם יואב 5 ')
    self.assertTrue(kalfi_10_meta_data.kalfi_num_int == 11)
    self.assertTrue(kalfi_10_meta_data.kalfi_num == 11.3)
    self.assertTrue(kalfi_10_meta_data.yeshuv_sn == 28)
    print("a")

def test_kalfi_metadata_query_all_correct(self):
    kalfi_meta_data_list = query_kalfi_metadata_all()
    self.assertIsNotNone(kalfi_meta_data_list)
    total_number_kalfi = len(kalfi_meta_data_list)
    self.assertTrue(total_number_kalfi == KALFI_METADATA_COUNT)
