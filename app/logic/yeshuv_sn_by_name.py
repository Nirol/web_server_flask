
from typing import List
from sqlalchemy import desc
from app import db
from constants import NUMBER_KALFI_DISPLAY
from exceptions import ValidationError
from models import YeshuvKnesset, Knesset_22, Kalfi, Yeshuv

def query_yeshuv_sn_by_name(yeshuv_name: str) -> int:
    yeshuv_sn = db.session.query(Yeshuv.yeshuv_sn).filter_by(
        yeshuv_name_hebrew=yeshuv_name).first()
    if yeshuv_sn:
        return yeshuv_sn[0]

    else:
        return -1
