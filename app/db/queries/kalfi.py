from typing import List
from app import db
from models import Kalfi





def query_kalfi_metadata_all() -> List[Kalfi]:
    kalfi_list = Kalfi.query.all()
    return kalfi_list


def query_kalfi_metadata(yeshuv_sn: int) -> List[Kalfi]:
    kalfi_list = Kalfi.query.filter_by(yeshuv_sn=yeshuv_sn).order_by(Kalfi.kalfi_num_int, Kalfi.sub_kalfi_num).all()
    return kalfi_list


def query_kalfi_metadata_by_list(yeshuv_sn, kalfi_num_list: List[int]) -> List[
    Kalfi]:
    from sqlalchemy.sql.expression import or_
    clauses = or_(*[Kalfi.kalfi_num_int == x for x in set(kalfi_num_list)])
    kalfi_list = db.session.query(Kalfi).filter(
        Kalfi.yeshuv_sn == yeshuv_sn).filter(clauses).group_by(Kalfi.kalfi_num_int).all()
    return kalfi_list