from wtforms.validators import ValidationError
from app import db
from models import Yeshuv

class Yeshuv_Validator(object):
    def __init__(self, model, field, message=u'Yeshuv does not exist.'):
        self.model = model
        self.field = field
        self.message=message

    def __call__(self, form, field):
        field_data_like = '%'+ field.data + '%'
        optional_yeshuvs_num = db.session.query(Yeshuv.yeshuv_name_hebrew).filter(
                    Yeshuv.yeshuv_name_hebrew.like(field_data_like)).count()
        if optional_yeshuvs_num == 0:
            raise ValidationError(self.message)