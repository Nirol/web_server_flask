from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from models import Yeshuv
from validators import Yeshuv_Validator


class YeshuvNameQuery(FlaskForm):
    yeshuv_name = StringField('Yeshuv:', validators=[Yeshuv_Validator(
                                                             Yeshuv,
                                                             Yeshuv.yeshuv_name_hebrew,
                                                             message='Yeshuv does not exist!!')])
    submit1 = SubmitField('Submit')


