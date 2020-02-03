from typing import List

from sqlalchemy import desc

from app import db
from constants import NUMBER_KALFI_DISPLAY
from exceptions import ValidationError
from models import YeshuvKnesset, Knesset_22, Kalfi

def query_kalfi_metadata_all() ->List[Kalfi]:
    kalfi_list = Kalfi.query.all()
    return kalfi_list


def query_kalfi_metadata(yeshuv_sn: int) ->List[Kalfi]:
    kalfi_list = Kalfi.query.filter_by(yeshuv_sn= yeshuv_sn).all()

    return kalfi_list


def query_kalfi_metadata_by_list(yeshuv_sn, kalfi_num_list: List[int]) ->List[Kalfi]:
    from sqlalchemy.sql.expression import or_
    clauses = or_(*[Kalfi.kalfi_num_int == x  for x in set(kalfi_num_list)])
    kalfi_list = db.session.query(Kalfi).filter(Kalfi.yeshuv_sn==yeshuv_sn).filter(clauses).distinct(Kalfi.kalfi_num_int).all()
    # kalfi_list = Kalfi.query.  filter_by(clauses).all()
    return kalfi_list

def query_knesset22_kalfi(yeshuv_sn: int) -> List[Knesset_22]:
    knesset_22_model_data = Knesset_22.query.filter_by(SN= yeshuv_sn).all()
    return knesset_22_model_data

def query_knesset22_kalfi_top_n_by_vote_percent(yeshuv_sn: int)-> List[Knesset_22]:
    n = NUMBER_KALFI_DISPLAY
    top_n = Knesset_22.query.filter_by(SN=yeshuv_sn).order_by(desc(Knesset_22.vote_percent)).limit(n).all()
    return top_n

def query_knesset22_kalfi_bottom_n_vote_percent(yeshuv_sn: int)-> List[Knesset_22]:
    n = NUMBER_KALFI_DISPLAY
    bottom_n = Knesset_22.query.filter_by(SN=yeshuv_sn).order_by(
        Knesset_22.vote_percent).limit(n).all()
    return bottom_n



def query_yeshuvknesset_by_sn (yeshuv_sn: int) -> YeshuvKnesset:
    yeshuv_general_info = YeshuvKnesset.query.filter_by(SN=yeshuv_sn).first()
    # yeshuv_general_info = YeshuvKnesset.query.get_or_404.filter_by(SN=yeshuv_sn).first()

    if yeshuv_general_info is None:
        raise ValidationError
    return yeshuv_general_info
