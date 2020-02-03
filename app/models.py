from datetime import datetime

from flask_login import UserMixin, AnonymousUserMixin

from app import db, login_manager

from markdown import markdown
import bleach
from flask import url_for
from sqlalchemy.dialects.mysql import TINYINT, BOOLEAN
from app.exceptions import ValidationError
from logic.constants import KnessetVars, KNESSETS_LIST


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(64), unique=True, index=True)
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


login_manager.anonymous_user = User


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    disabled = db.Column(db.Boolean)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'code', 'em', 'i',
                        'strong']
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True))

    def to_json(self):
        json_comment = {
            'url': url_for('api.get_comment', id=self.id),
            # 'post_url': url_for('api.get_post', id=self.post_id),
            'body': self.body,
            'body_html': self.body_html,
            'timestamp': self.timestamp,
            'author_url': url_for('api.get_user', id=self.author_id),
        }
        return json_comment

    @staticmethod
    def from_json(json_comment):
        body = json_comment.get('body')
        if body is None or body == '':
            raise ValidationError('comment does not have a body')
        return Comment(body=body)


class Yeshuv(db.Model):
    __tablename__ = 'yeshuv'
    yeshuv_sn = db.Column(db.Integer, primary_key=True)
    yeshuv_type = db.Column(db.Integer)
    yeshuv_name_en = db.Column(db.Text)
    yeshuv_name_hebrew = db.Column(db.Text)
    Knesset_18 = db.relationship('Knesset_18', backref='yeshuv', lazy=True)

    def __repr__(self):
        return '[{}]'.format(self.yeshuv_name_hebrew)


class Kalfi(db.Model):
    __tablename__ = 'kalfi'
    yeshuv_sn = db.Column(db.Integer, primary_key=True)
    kalfi_num = db.Column(db.Float, primary_key=True)
    kalfi_num_int = db.Column(db.Integer)
    address = db.Column(db.Integer)
    location = db.Column(db.Integer)
    accessible = db.Column(db.Integer)
    special_accessible = db.Column(db.Integer)
    arabic_printing = db.Column(db.Integer)



    @staticmethod
    def cmp_kalfi_num_order(self, other):
        return self.kalfi_num_int < other.kalfi_num_int


    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.kalfi_num_int, self.kalfi_num) ==
                (other.kalfi_num_int, other.kalfi_num))


    def __gt__(self, kalfi_2):
        return ((self.kalfi_num_int, self.kalfi_num) <
                (kalfi_2.kalfi_num_int, kalfi_2.kalfi_num))

    def get_address(self) -> str:
        return self.address

    def get_location(self) -> str:
        return self.location


    def update_hebrew_texts(self, clean_address, clean_location):
        self.address = clean_address
        self.location = clean_location

    def __repr__(self):
        return str(self.__dict__)


class Knesset(db.Model):
    __abstract__ = True
    BZB = db.Column(db.Integer, nullable=False)
    Voters = db.Column(db.Integer, nullable=False)
    Error_Voters = db.Column(db.Integer, nullable=False)
    vote_percent = db.Column(db.Float, nullable=False)





class Knesset_18(Knesset):
    __tablename__ = 'knesset_18'
    index = db.Column(db.Integer, primary_key=True, nullable=False)
    SN = db.Column(db.Integer, db.ForeignKey('yeshuv.yeshuv_sn'),
                   primary_key=True, nullable=False)
    Kalfi_Num = db.Column(db.Integer, primary_key=True, nullable=False)


class Knesset_22(Knesset):
    __tablename__ = 'knesset_22'
    index = db.Column(db.Integer, primary_key=True, nullable=False)
    SN = db.Column(db.Integer, db.ForeignKey('yeshuv.yeshuv_sn'),
                   primary_key=True, nullable=False)
    Kalfi_Num = db.Column(db.Integer, primary_key=True, nullable=False)

    @staticmethod
    def cmp_vote_percent_order(self, other):
        return self.vote_percent < other.vote_percent

    @staticmethod
    def cmp_kalfi_num_order(self, other):
        return self.Kalfi_Num < other.Kalfi_Num

    # def __gt__(self, knesset_22_2):
    #     return self.Kalfi_Num > knesset_22_2.Kalfi_Num


class YeshuvKnesset(db.Model):
    __tablename__ = 'yeshuv_knesset'
    SN = db.Column(db.Integer, primary_key=True, nullable=False)
    BZB_18 = db.Column(db.Integer)
    Voters_18 = db.Column(db.Integer)
    Error_Voters_18 = db.Column(db.Integer)
    Kalfi_Num_18 = db.Column(db.Integer)
    vote_percent_18 = db.Column(db.Float)
    Avg_BZB_18 = db.Column(db.Float)
    BZB_19 = db.Column(db.Integer)
    Voters_19 = db.Column(db.Integer)
    Error_Voters_19 = db.Column(db.Integer)
    Kalfi_Num_19 = db.Column(db.Integer)
    vote_percent_19 = db.Column(db.Float)
    Avg_BZB_19 = db.Column(db.Float)
    BZB_20 = db.Column(db.Integer)
    Voters_20 = db.Column(db.Integer)
    Error_Voters_20 = db.Column(db.Integer)
    Kalfi_Num_20 = db.Column(db.Integer)
    vote_percent_20 = db.Column(db.Float)
    Avg_BZB_20 = db.Column(db.Float)
    BZB_21 = db.Column(db.Integer)
    Voters_21 = db.Column(db.Integer)
    Error_Voters_21 = db.Column(db.Integer)
    Kalfi_Num_21 = db.Column(db.Integer)
    vote_percent_21 = db.Column(db.Float)
    Avg_BZB_21 = db.Column(db.Float)
    BZB_22 = db.Column(db.Integer)
    Voters_22 = db.Column(db.Integer)
    Error_Voters_22 = db.Column(db.Integer)
    Kalfi_Num_22 = db.Column(db.Integer)
    vote_percent_22 = db.Column(db.Float)
    Avg_BZB_22 = db.Column(db.Float)


    def get_knesset_var_18(self, variabl: KnessetVars):
        if variabl == KnessetVars.BZB:
            return self.BZB_18
        elif variabl == KnessetVars.Voters:
            return self.Voters_18
        elif variabl == KnessetVars.Error_Voters:
            return self.Error_Voters_18
        elif variabl == KnessetVars.Kalfi_Num:
            return self.Kalfi_Num_18
        elif variabl == KnessetVars.vote_percent:
            return self.vote_percent_18
        elif variabl == KnessetVars.Avg_BZB:
            return self.Avg_BZB_18

    def get_knesset_var_19(self, variabl: KnessetVars):
        if variabl == KnessetVars.BZB:
            return self.BZB_19
        elif variabl == KnessetVars.Voters:
            return self.Voters_19
        elif variabl == KnessetVars.Error_Voters:
            return self.Error_Voters_19
        elif variabl == KnessetVars.Kalfi_Num:
            return self.Kalfi_Num_19
        elif variabl == KnessetVars.vote_percent:
            return self.vote_percent_19
        elif variabl == KnessetVars.Avg_BZB:
            return self.Avg_BZB_19

    def get_knesset_var_20(self, variabl: KnessetVars):
        if variabl == KnessetVars.BZB:
            return self.BZB_20
        elif variabl == KnessetVars.Voters:
            return self.Voters_20
        elif variabl == KnessetVars.Error_Voters:
            return self.Error_Voters_20
        elif variabl == KnessetVars.Kalfi_Num:
            return self.Kalfi_Num_20
        elif variabl == KnessetVars.vote_percent:
            return self.vote_percent_20
        elif variabl == KnessetVars.Avg_BZB:
            return self.Avg_BZB_20

    def get_knesset_var_21(self, variabl: KnessetVars):
        if variabl == KnessetVars.BZB:
            return self.BZB_21
        elif variabl == KnessetVars.Voters:
            return self.Voters_21
        elif variabl == KnessetVars.Error_Voters:
            return self.Error_Voters_21
        elif variabl == KnessetVars.Kalfi_Num:
            return self.Kalfi_Num_21
        elif variabl == KnessetVars.vote_percent:
            return self.vote_percent_21
        elif variabl == KnessetVars.Avg_BZB:
            return self.Avg_BZB_21

    def get_knesset_var_22(self, variabl: KnessetVars):
            if variabl == KnessetVars.BZB:
                return self.BZB_22
            elif variabl == KnessetVars.Voters:
                return self.Voters_22
            elif variabl == KnessetVars.Error_Voters:
                return self.Error_Voters_22
            elif variabl == KnessetVars.Kalfi_Num:
                return self.Kalfi_Num_22
            elif variabl == KnessetVars.vote_percent:
                return self.vote_percent_22
            elif variabl == KnessetVars.Avg_BZB:
                return self.Avg_BZB_22


    def get_knesset_var(self, variabl: KnessetVars, knesset: str):
        if knesset =='18':
            return self.get_knesset_var_18(variabl)
        elif knesset =='19':
            return self.get_knesset_var_19(variabl)
        elif knesset =='20':
            return self.get_knesset_var_20(variabl)
        elif knesset =='21':
            return self.get_knesset_var_21(variabl)
        elif knesset =='22':
            return self.get_knesset_var_22(variabl)



    def to_json_dict(self):
        data = {}
        for knesset in KNESSETS_LIST:
            data[knesset] = []
            knesset_dict = {}
            for var in KnessetVars:
                knesset_var_value= self.get_knesset_var(var, knesset)
                knesset_dict[var.name] = knesset_var_value
            data[knesset].append(knesset_dict)
        return data



    def to_json(self):
        json_user = {
            'url': url_for('api.get_user', id=self.id),
            'username': self.username,
            'member_since': self.member_since,
            'last_seen': self.last_seen,
            'posts_url': url_for('api.get_user_posts', id=self.id),
            'followed_posts_url': url_for('api.get_user_followed_posts',
                                          id=self.id),
            'post_count': self.posts.count()
        }
        return json_user


# ready to go knesset_18 table:

# class Knesset_18(db.Model):
#     __tablename__ = 'knesset_18'
#     index = db.Column(db.Integer, primary_key=True, nullable=False)
#     SN = db.Column(db.Integer, db.ForeignKey('yeshuv.yeshuv_sn'), primary_key=True,  nullable=False)
#     Kalfi_Num = db.Column(db.Integer, primary_key=True, nullable=False)
#     BZB = db.Column(db.Integer, nullable=False)
#     Voters = db.Column(db.Integer, nullable=False)
#     Error_Voters = db.Column(db.Integer, nullable=False)
#     vote_percent = db.Column(db.Float, nullable=False)
#

#
#
#
# class Knesset_19(db.Model):
#     __tablename__ = 'knesset_19'
#     index = db.Column(db.Integer)
#     SN = db.Column(db.Integer)
#     Kalfi_Num = db.Column(db.Integer)
#     BZB = db.Column(db.Integer)
#     Voters = db.Column(db.Integer)
#     Error_Voters = db.Column(db.Integer)
#     vote_percent = db.Column(db.Float)
#     Yeshuv_Type = db.Column(db.String(5))
#
# class Knesset_20(db.Model):
#     __tablename__ = 'knesset_20'
#     index = db.Column(db.Integer)
#     SN = db.Column(db.Integer)
#     Kalfi_Num = db.Column(db.Integer)
#     BZB = db.Column(db.Integer)
#     Voters = db.Column(db.Integer)
#     Error_Voters = db.Column(db.Integer)
#     vote_percent = db.Column(db.Float)
#     Yeshuv_Type = db.Column(db.String(5))
#
# class Knesset_21(db.Model):
#     __tablename__ = 'knesset_21'
#     index = db.Column(db.Integer)
#     SN = db.Column(db.Integer)
#     Kalfi_Num = db.Column(db.Integer)
#     BZB = db.Column(db.Integer)
#     Voters = db.Column(db.Integer)
#     Error_Voters = db.Column(db.Integer)
#     vote_percent = db.Column(db.Float)
#     Yeshuv_Type = db.Column(db.String(5))
#
# class Knesset_22(db.Model):
#     __tablename__ = 'knesset_22'
#     index = db.Column(db.Integer)
#     SN = db.Column(db.Integer)
#     Kalfi_Num = db.Column(db.Integer)
#     BZB = db.Column(db.Integer)
#     Voters = db.Column(db.Integer)
#     Error_Voters = db.Column(db.Integer)
#     vote_percent = db.Column(db.Float)
#     Yeshuv_Type = db.Column(db.String(5))


db.event.listen(Comment.body, 'set', Comment.on_changed_body)
