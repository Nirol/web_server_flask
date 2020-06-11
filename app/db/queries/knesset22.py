from typing import List

from sqlalchemy import desc

from app import db
from constants import NUMBER_KALFI_DISPLAY
from models import Knesset_22


def query_knesset22_kalfi(yeshuv_sn: int) -> List[Knesset_22]:
    knesset_22_model_data = Knesset_22.query.filter_by(yeshuv_sn=yeshuv_sn).order_by(Knesset_22.Kalfi_Num).all()
    return knesset_22_model_data


def query_knesset22_kalfi_top_n_by_vote_percent(yeshuv_sn: int) -> List[
    Knesset_22]:
    n = NUMBER_KALFI_DISPLAY
    top_n = Knesset_22.query.filter_by(yeshuv_sn=yeshuv_sn).order_by(
        desc(Knesset_22.Vote_Percent)).group_by(Knesset_22.Kalfi_Num).limit(n).all()
    return top_n


def query_knesset22_kalfi_bottom_n_vote_percent(yeshuv_sn: int) -> List[
    Knesset_22]:
    n = NUMBER_KALFI_DISPLAY
    bottom_n = db.session.query( Knesset_22).filter_by(yeshuv_sn=yeshuv_sn).order_by(
            Knesset_22.Vote_Percent).group_by(Knesset_22.Kalfi_Num).limit(n).all()
    return bottom_n