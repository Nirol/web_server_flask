import unittest
from app import create_app, db
from constants import get_representation_by_kalfi_num, KalfiDisplayType
from db_queries import query_yeshuvknesset_kalfi_num_22_by_sn
from tests import YESHUV_SN_FOR_TESTING, YESHUV_SN_FOR_TESTING_B


class TestToJsonDict(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        self.app_context.pop()

    def test_get_representation_by_kalfi_num_working(self):
        display_ans = get_representation_by_kalfi_num(YESHUV_SN_FOR_TESTING)
        self.assertFalse(display_ans is None)

    def test_get_representation_by_kalfi_num_correct(self):
        num = query_yeshuvknesset_kalfi_num_22_by_sn(YESHUV_SN_FOR_TESTING)
        display_ans = get_representation_by_kalfi_num(num)
        self.assertEqual(display_ans, KalfiDisplayType.TopN)

    def test_get_representation_by_kalfi_num_correct_2(self):
        num = query_yeshuvknesset_kalfi_num_22_by_sn(YESHUV_SN_FOR_TESTING_B)
        display_ans = get_representation_by_kalfi_num(num)
        self.assertEqual(display_ans, KalfiDisplayType.All)