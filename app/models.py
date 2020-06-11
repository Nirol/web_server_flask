from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import Integer, ForeignKey, Column
from sqlalchemy.ext.declarative import declared_attr

from app import db, login_manager
from constants import KnessetVars, KNESSETS_LIST




class Yeshuv(db.Model):
    __tablename__ = 'yeshuv'
    yeshuv_sn = db.Column(db.Integer, primary_key=True)
    yeshuv_type = db.Column(db.Integer)
    yeshuv_name_en = db.Column(db.Text)
    yeshuv_name_hebrew = db.Column(db.Text)
    # Knesset_22 = db.relationship('Knesset_22', backref='yeshuv', lazy=True)

    def __repr__(self):
        return '[{}]'.format(self.yeshuv_name_hebrew)


class Kalfi(db.Model):
    __tablename__ = 'kalfi'
    yeshuv_sn = db.Column(db.Integer, primary_key=True)
    sub_kalfi_num = db.Column(db.Integer, primary_key=True)
    kalfi_num_int = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.Text)
    address = db.Column(db.Text)
    accessible = db.Column(db.Integer)
    special_accessible = db.Column(db.Integer)
    arabic_printing = db.Column(db.Integer)



    @staticmethod
    def cmp_kalfi_num_order(self, other):
        return self.kalfi_num_int < other.kalfi_num_int


    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.kalfi_num_int, self.sub_kalfi_num) ==
                (other.kalfi_num_int, other.kalfi_num))


    def __gt__(self, kalfi_2):
        return ((self.kalfi_num_int, self.sub_kalfi_num) <
                (kalfi_2.kalfi_num_int, kalfi_2.kalfi_num))

    def get_address(self) -> str:
        return self.address

    def get_location(self) -> str:
        return self.location


    def update_address(self, clean_address: str) -> None:
        self.address = clean_address

    def update_location(self, clean_location: str)  -> None:
        self.location = clean_location

    def __repr__(self):
        return str(self.__dict__)


class Knesset(db.Model):
    __abstract__ = True
    index = db.Column(db.Integer, primary_key=True, nullable=False )
    @declared_attr
    def yeshuv_sn(cls):
        return Column(Integer,primary_key=True, forigen_key= ForeignKey('yeshuv.yeshuv_sn'))
    # SN = db.Column(db.Integer, db.ForeignKey('yeshuv.yeshuv_sn'),
    #                primary_key=True, nullable=False)
    Kalfi_Num = db.Column(db.Integer, primary_key=True, nullable=False)
    BZB = db.Column(db.Integer, nullable=False)
    Voters = db.Column(db.Integer, nullable=False)
    Error_Voters = db.Column(db.Integer, nullable=False)
    Vote_Percent = db.Column(db.Float, nullable=False)
    Error_Vote_Percent = db.Column(db.Float, nullable=False)






class Knesset_22(Knesset):
    __tablename__ = 'knesset_22'


    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.rank < other.rank



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
