from typing import List
import json
from db import db_queries
from db.db_helper import query_helper_kalfi_meta_data_top
from logic.constants import KalfiDisplayType
from models import Kalfi, Knesset_22, YeshuvKnesset


class KalfiMetaDisplay():
    def __init__(self, diplay: KalfiDisplayType, kalfi_data_list: List[Knesset_22], kalfi_meta_list: List[Kalfi]):
        self.kalfi_data_list = kalfi_data_list
        self.kalfi_meta_list = kalfi_meta_list

    def to_json_dict(self):
        data = {}
        data['data'] = []
        data['meta'] = []
        for kalfi in self.kalfi_data_list:
            dict = {
                'Kalfi_Num' : kalfi.Kalfi_Num,
                'BZB': kalfi.BZB,
                'Voters': kalfi.Voters,
                'Error_Voters':  kalfi.Error_Voters,
                'vote_percent': kalfi.vote_percent
                }
            data['data'].append(dict)
        for kalfi_meta in self.kalfi_meta_list:
            dict= {
                'address': kalfi_meta.address,
                'location': kalfi_meta.location,
                'kalfi_num_full': kalfi_meta.kalfi_num
                }
            data['meta'].append(dict)
        return data

class KalfiSingleDisplay(KalfiMetaDisplay):
    pass



def _sort_kalfi_by_kalfi_num(all_kalfi_data_list, all_kalfi_meta_data_list):
    sorted(all_kalfi_meta_data_list, key=Knesset_22.cmp_kalfi_num_order)
    sorted(all_kalfi_meta_data_list, key=Kalfi.cmp_kalfi_num_order)
    # sorted(all_kalfi_data_list)
    # sorted(all_kalfi_meta_data_list)

def _sort_kalfi_by_vote_percent(kalfi_data_top_n, kalfi_data_bottom_n,  kalfi_meta_top_n, kalfi_meta_bottom_n):
    sorted(kalfi_data_top_n, key=Knesset_22.cmp_vote_percent_order)
    sorted(kalfi_data_bottom_n, key=Knesset_22.cmp_vote_percent_order)


def _query_db_kalfi_data_all(yeshuv_sn: int):
    all_kalfi_data_list = db_queries.query_knesset22_kalfi(yeshuv_sn)
    all_kalfi_meta_data_list = db_queries.query_kalfi_metadata(yeshuv_sn)
    return [all_kalfi_data_list, all_kalfi_meta_data_list]


def get_kalfi_meta_data_for_yeshuv_by_display(yeshuv_sn: int, display: KalfiDisplayType) -> KalfiMetaDisplay:

    if display == KalfiDisplayType.All_Kalfi:
        [kalfi_data_list, kalfi_meta_list] = _query_db_kalfi_data_all(yeshuv_sn)
        _sort_kalfi_by_kalfi_num(kalfi_data_list, kalfi_meta_list)
        return KalfiMetaDisplay(display, kalfi_data_list, kalfi_meta_list)

    elif display == KalfiDisplayType.Top_N_Kalfi:
        [kalfi_data_top_n, kalfi_meta_top_n] = query_helper_kalfi_meta_data_top(yeshuv_sn)
        [kalfi_data_bottom_n, kalfi_meta_bottom_n] = query_herlper_kalfi_meta_data_bottom(yeshuv_sn)
        _sort_kalfi_by_vote_percent(kalfi_data_top_n, kalfi_data_bottom_n, kalfi_meta_top_n, kalfi_meta_bottom_n)




def yeshuv_json_response(kalfi_meta_display: KalfiMetaDisplay, yeshuv_knesset_model_data: YeshuvKnesset):
    json_dict_meta_data = kalfi_meta_display.to_json_dict()
    json_dict_yeshuv_data = yeshuv_knesset_model_data.to_json_dict()
    json_dict_meta_data.update(json_dict_yeshuv_data)
    b = json.dumps(json_dict_meta_data)
    print(b)
    return b
