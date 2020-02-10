import unittest
from typing import List
import db_helper_test
from app import create_app, db
from kalfi_display import __sort_kalfi_by_kalfi_num, __sort_kalfi_by_kalfi_num

from models import Yeshuv, Kalfi, Knesset_22


class TestKalfiMeta(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        self.app_context.pop()



    def test_kalfi_metadata_query_working(self):
        yeshuv_sn_list = db.session.query(Yeshuv.yeshuv_sn).all()
        for yeshuv in yeshuv_sn_list:
            kalfi_data_list = db_helper_test.query_db_kalfi_data(yeshuv)
            kalfi_meta_list = db_helper_test.query_db_kalfi_meta(yeshuv)

            __sort_kalfi_by_kalfi_num(kalfi_data_list, kalfi_meta_list)
            result = validate_list_match_test_db(kalfi_data_list, kalfi_meta_list)
            self.assertEqual(result, [])



# testing for number in kalfi in results vs in the meta,
# 4 kalfis in total were missing from the results (probbably based to corruption kalfis
#  in arabic yeshuv, should validate that
# TODO validate 4 missing kalfi are the corrupted kalfis

def validate_list_match_test_db(kalfi_data_list: List[Knesset_22],
                                kalfi_meta_list: List[Kalfi]):
    err_list = []
    len_data_list = len(kalfi_data_list)
    len_meta_list = len(kalfi_meta_list)

    if len_data_list != len_meta_list:
        err_list.append(
            "sdata={}.meta={}".format(len_data_list, len_meta_list))
    else:
        for idx in range(len_meta_list):
            kalfi_num_data = kalfi_data_list[idx].Kalfi_Num
            kalfi_num_meta = kalfi_meta_list[idx].kalfi_num_int
            kalfi_num_meta_double = kalfi_meta_list[idx].sub_kalfi_num
            if kalfi_num_data != kalfi_num_meta:
                if kalfi_num_data > kalfi_num_meta:
                    err_list.append("%%%%%%%")
                err_list.append(
                    "kalfi_data={}.kalfi_meta={}.double={}".format(
                        kalfi_num_data, kalfi_num_meta,
                        kalfi_num_meta_double))
    return err_list