import abc
from typing import List, Type, Dict, Mapping
import json

from db_helper import query_helper_kalfi_meta_top_or_bottom
from queries.kalfi import query_kalfi_metadata

from queries.knesset22 import query_knesset22_kalfi, \
    query_knesset22_kalfi_top_n_by_vote_percent, \
    query_knesset22_kalfi_bottom_n_vote_percent
from constants import KalfiDisplayType
from models import Kalfi, Knesset_22, YeshuvKnesset
import constants
from queries.yeshuv_knesset import query_yeshuvknesset_by_sn




def fill_data_dict(kalfi_data, data_dict):
    for kalfi in kalfi_data:
        dict = {
            'Kalfi_Num': kalfi.Kalfi_Num,
            'BZB': kalfi.BZB,
            'Voters': kalfi.Voters,
            'Error_Voters': kalfi.Error_Voters,
            'Vote_Percent': kalfi.Vote_Percent,
            'Error_Vote_Percent': kalfi.Error_Vote_Percent,
        }
        data_dict.append(dict)

def fill_meta_dict(kalfi_meta: List[Kalfi], meta_dict):
    for kalfi in kalfi_meta:
        dict = {
            'sub_kalfi_num': kalfi.sub_kalfi_num,
            'address': kalfi.address,
            'location': kalfi.location,
            'accessible': kalfi.accessible,
            'special_accessible': kalfi.special_accessible,
            'arabic_printing': kalfi.arabic_printing
        }
        meta_dict.append(dict)




class KalfiDisplay:
    def __init__(self, display: KalfiDisplayType):
        self.display = display

    @abc.abstractmethod
    def to_json_dict(self):
        pass


class KalfiAllDisplay(KalfiDisplay):
    def __init__(self, diplay: KalfiDisplayType, kalfi_data_list: List[Knesset_22], kalfi_meta_list: List[Kalfi]):
        super().__init__(diplay)
        self.kalfi_data_list = kalfi_data_list
        self.kalfi_meta_list = kalfi_meta_list

    def to_json_dict(self) -> Dict[str, str]:
        data = {}
        data['display'] = "All"
        data['data'] = []
        data['meta'] = []
        fill_data_dict(self.kalfi_data_list, data['data'])

        fill_meta_dict(self.kalfi_meta_list, data['meta'])
        return data





class KalfiTopBotDisplay(KalfiDisplay):
    def __init__(self,display: KalfiDisplayType,  kalfi_data_top_n: List[Knesset_22], kalfi_data_bottom_n: List[Knesset_22],
                 kalfi_meta_top_n: List[Kalfi], kalfi_meta_bottom_n: List[Kalfi] ):
        super().__init__(display)
        self.kalfi_data_top_n = kalfi_data_top_n
        self.kalfi_data_bottom_n = kalfi_data_bottom_n
        self.kalfi_meta_top_n = kalfi_meta_top_n
        self.kalfi_meta_bottom_n = kalfi_meta_bottom_n




    def to_json_dict(self):
        data = {}
        data['display'] = "TopN"

        data['data_top'] = []
        data['data_bot'] = []

        data['meta_top'] = []
        data['meta_bot'] = []

        fill_data_dict(self.kalfi_data_top_n, data['data_top'])
        fill_data_dict(self.kalfi_data_bottom_n, data['data_bot'])

        fill_meta_dict(self.kalfi_meta_top_n, data['meta_top'])
        fill_meta_dict(self.kalfi_meta_bottom_n, data['meta_bot'])

        return data



def __sort_kalfi_by_kalfi_num(all_kalfi_data_list: List[Knesset_22], all_kalfi_meta_data_list: List[Kalfi]):
    # sorted(all_kalfi_data_list, key=Knesset_22.cmp_kalfi_num_order)
    # sorted(all_kalfi_meta_data_list, key=Kalfi.cmp_kalfi_num_order)

    # sorted(all_kalfi_data_list, key=lambda Knesset_22: Knesset_22.vote_percent)
    sorted(all_kalfi_data_list, key=lambda Knesset_22: Knesset_22.Kalfi_Num)
    sorted(all_kalfi_meta_data_list, key=lambda Kalfi: Kalfi.kalfi_num)


# TODO complete the function
def __sort_kalfi_by_vote_percent(kalfi_data_top_n, kalfi_data_bottom_n,  kalfi_meta_top_n, kalfi_meta_bottom_n):
    sorted(kalfi_data_top_n, key=Knesset_22.cmp_vote_percent_order)
    sorted(kalfi_data_bottom_n, key=Knesset_22.cmp_vote_percent_order)


def get_kalfi_meta_data_for_yeshuv_by_display(yeshuv_sn: int, display: KalfiDisplayType) -> Type[KalfiDisplay]:
    if display.value is KalfiDisplayType.All.value:
        kalfi_data_list = query_knesset22_kalfi(yeshuv_sn)
        kalfi_meta_list = query_kalfi_metadata(yeshuv_sn)


        return KalfiAllDisplay(display, kalfi_data_list, kalfi_meta_list)

    elif display.value is KalfiDisplayType.TopN.value:
        kalfi_data_top_n = query_knesset22_kalfi_top_n_by_vote_percent(yeshuv_sn)
        kalfi_meta_top_n = query_helper_kalfi_meta_top_or_bottom(yeshuv_sn, kalfi_data_top_n)

        kalfi_data_bottom_n = query_knesset22_kalfi_bottom_n_vote_percent(yeshuv_sn)
        kalfi_meta_bottom_n = query_helper_kalfi_meta_top_or_bottom(yeshuv_sn, kalfi_data_bottom_n)

        return KalfiTopBotDisplay(display, kalfi_data_top_n, kalfi_data_bottom_n, kalfi_meta_top_n, kalfi_meta_bottom_n)



def __yeshuv_json_data_response(yeshuv_knesset_model_data: YeshuvKnesset):
    json_dict_yeshuv_data = yeshuv_knesset_model_data.to_json_dict()
    json_answer_ready_data = json.dumps(json_dict_yeshuv_data,
                                        ensure_ascii=False)
    return json_answer_ready_data

def get_yeshuv_knesset_elections_data_json(yeshuv_sn):
    yeshuv_knesset_model_data = query_yeshuvknesset_by_sn(yeshuv_sn)
    return __yeshuv_json_data_response(yeshuv_knesset_model_data)




def __yeshuv_json_meta_response(kalfi_meta_display: Type[KalfiDisplay]):
    json_dict_meta_data = kalfi_meta_display.to_json_dict()
    json_answer_ready_meta = json.dumps(json_dict_meta_data,
                                        ensure_ascii=False)
    return json_answer_ready_meta



def get_yeshuv_kalfi_json(yeshuv_sn: int, kalfi_num: int)->[str, 'JSON']:

    display = constants.get_representation_by_kalfi_num(
        kalfi_num)
    kalfi_meta_display = get_kalfi_meta_data_for_yeshuv_by_display(yeshuv_sn,
                                                                   display)
    return __yeshuv_json_meta_response(kalfi_meta_display)

