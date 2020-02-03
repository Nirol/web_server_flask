from typing import List

from db import db_queries
from models import Knesset_22


def _parse_knesset22_query_for_sn(query_result: List[Knesset_22]) -> List[int]:
    kalfi_num_list = [x.Kalfi_Num for x in query_result]
    return kalfi_num_list


def query_helper_kalfi_meta_data_top(yeshuv_sn):
    kalfi_data_top_n = db_queries.query_knesset22_kalfi_top_n_by_vote_percent(yeshuv_sn)
    yeshuv_kalfi_list_from_knesset22_query = _parse_knesset22_query_for_sn(kalfi_data_top_n)
    kalfi_meta_top_n = db_queries.query_kalfi_metadata_by_list(yeshuv_sn, yeshuv_kalfi_list_from_knesset22_query)
    return [kalfi_data_top_n,  kalfi_meta_top_n]


def query_helper_kalfi_meta_data_bottom(yeshuv_sn):
    kalfi_data_bottom_n = db_queries.query_knesset22_kalfi_bottom_n_vote_percent(yeshuv_sn)
    yeshuv_kalfi_list_from_knesset22_query = _parse_knesset22_query_for_sn(kalfi_data_bottom_n)
    kalfi_meta_bottom_n = db_queries.query_kalfi_metadata_by_list(yeshuv_sn, yeshuv_kalfi_list_from_knesset22_query)
    return [kalfi_data_bottom_n,  kalfi_meta_bottom_n]