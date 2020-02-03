from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField, \
    PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import InputRequired, Length, DataRequired
from models import Yeshuv
from validators import Yeshuv_Validator

#
# class NameForm(FlaskForm):
#     name = StringField('What is your name?', validators=[InputRequired()])
#     submit = SubmitField('Submit')
#
#
# class different_query(FlaskForm):
#     yeshuv_name = StringField('Yeshuv', validators=[InputRequired(),
#                                                      Yeshuv_Validator(
#                                                          Yeshuv,
#                                                          Yeshuv.yeshuv_name_en1,
#                                                          message='Yeshuv does not exist!!')])
#     knesset_choices = [("18", "18"), ("19", "19"), ("20", "20"), ("21", "21"), ("22", "22")]
#     knesset_year = SelectMultipleField('Knesset:', choices=knesset_choices, coerce=str,
#                                        validators=[InputRequired()])
#     submit = SubmitField('Submit')
class YeshuvNameQuery(FlaskForm):
    yeshuv_name = StringField('Yeshuv:', validators=[Yeshuv_Validator(
                                                             Yeshuv,
                                                             Yeshuv.yeshuv_name_hebrew,
                                                             message='Yeshuv does not exist!!')])
    submit1 = SubmitField('Submit')

#
# def choice_query():
#     return Yeshuv.query
#
# class QueryYeshuvData(FlaskForm):
#     opts = QuerySelectField(query_factory=choice_query, allow_blank=True, get_label='yeshuv_name_hebrew')
