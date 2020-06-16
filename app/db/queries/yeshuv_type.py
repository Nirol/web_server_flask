from exceptions import ValidationError
from models import YeshuvType
from yeshuv_sn_by_name import query_yeshuv_type_by_name
import json


def query_yeshuv_type_info(yeshuv_type):
    yeshuv_type_info = YeshuvType.query.filter_by(type_sn=yeshuv_type).first()
    if yeshuv_type_info is None:
        raise ValidationError
    return yeshuv_type_info


def __turn_yeshuv_type_into_json(yeshuv_type_info: YeshuvType):
    result_dict = {}
    result_dict["type_sn"] = yeshuv_type_info.type_sn
    result_dict["type_name"] = yeshuv_type_info.type_name
    result_dict["type_vote_percent"] = yeshuv_type_info.type_vote_percent
    result_dict["type_error_vote_percent"] = yeshuv_type_info.type_error_vote_percent
    result_dict["type_avg_bzb"] = yeshuv_type_info.type_avg_bzb


    json_answer_ready = json.dumps(result_dict,
                                        ensure_ascii=False)
    return json_answer_ready


def query_yeshuv_type_json_by_name(yeshuv_name: str):
    yeshuv_type = query_yeshuv_type_by_name(yeshuv_name)
    yeshuv_type_info = query_yeshuv_type_info(yeshuv_type)
    json_answer_ready = __turn_yeshuv_type_into_json(yeshuv_type_info)

    return json_answer_ready