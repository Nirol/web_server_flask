from app import db
from exceptions import ValidationError
from models import YeshuvKnesset


def query_yeshuvknesset_by_sn(yeshuv_sn: int) -> YeshuvKnesset:
    yeshuv_general_info = YeshuvKnesset.query.filter_by(SN=yeshuv_sn).first()
    if yeshuv_general_info is None:
        raise ValidationError
    return yeshuv_general_info


def query_yeshuvknesset_kalfi_num_22_by_sn(yeshuv_sn: int) -> int:
    kalfi_num_22 = db.session.query(YeshuvKnesset.Kalfi_Num_22).filter_by(SN=yeshuv_sn).first()
    if kalfi_num_22 is None:
        raise ValidationError
    return kalfi_num_22[0]




