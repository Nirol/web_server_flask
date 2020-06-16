from wtforms.validators import ValidationError
from app import db

from models import Yeshuv
from yeshuv_sn_by_name import query_yeshuv_sn_by_name


class Yeshuv_Validator(object):
    def __init__(self, model, field, message=u'Yeshuv does not exist.'):
        self.model = model
        self.field = field
        self.message=message

    def __call__(self, form, field):

        yeshuv_sn =  query_yeshuv_sn_by_name(field.data)
        if yeshuv_sn == -1:
            raise ValidationError(self.message)
