
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app import db


class User( db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):
    __tablename__ = 'roles'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')
    #
    #
    # def __init__(self, **kwargs):
    #     super(Role, self).__init__(**kwargs)
    #     if self.permissions is None:
    #         self.permissions = 0
    #
    #
    # @staticmethod
    # def insert_roles():
    #     roles = {
    #         'User': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
    #         'Moderator': [Permission.FOLLOW, Permission.COMMENT,
    #                       Permission.WRITE, Permission.MODERATE],
    #         'Administrator': [Permission.FOLLOW, Permission.COMMENT,
    #                           Permission.WRITE, Permission.MODERATE,
    #                           Permission.ADMIN],
    #     }
    #     default_role = 'User'
    #     for r in roles:
    #         role = Role.query.filter_by(name=r).first()
    #         if role is None:
    #             role = Role(name=r)
    #         role.reset_permissions()
    #         for perm in roles[r]:
    #             role.add_permission(perm)
    #         role.default = (role.name == default_role)
    #         db.session.add(role)
    #     db.session.commit()
    #
    # def add_permission(self, perm):
    #     if not self.has_permission(perm):
    #         self.permissions += perm
    #
    # def remove_permission(self, perm):
    #     if self.has_permission(perm):
    #         self.permissions -= perm
    #
    # def reset_permissions(self):
    #     self.permissions = 0
    #
    # def has_permission(self, perm):
    #     return self.permissions & perm == perm
    #
    # def __repr__(self):
    #     return '<Role %r>' % self.name
    #

# class Follow(db.Model):
#     __tablename__ = 'follows'
#     __table_args__ = {'extend_existing': True}
#     follower_id = db.Column(db.Integer, db.ForeignKey('users.id'),
#                             primary_key=True)
#     followed_id = db.Column(db.Integer, db.ForeignKey('users.id'),
#                             primary_key=True)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)




    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # email = db.Column(db.String(64), unique=True, index=True)
    # name = db.Column(db.String(64))
    # location = db.Column(db.String(64))
    # about_me = db.Column(db.Text())
    # member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    # last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    # avatar_hash = db.Column(db.String(32))
    #posts = db.relationship('Post', backref='author', lazy='dynamic')
    # followed = db.relationship('Follow',
    #                            foreign_keys=[Follow.follower_id],
    #                            backref=db.backref('follower', lazy='joined'),
    #                            lazy='dynamic',
    #                            cascade='all, delete-orphan')
    # followers = db.relationship('Follow',
    #                             foreign_keys=[Follow.followed_id],
    #                             backref=db.backref('followed', lazy='joined'),
    #                             lazy='dynamic',
    #                             cascade='all, delete-orphan')
    #comments = db.relationship('Comment', backref='author', lazy='dynamic')

    # @staticmethod
    # def add_self_follows():
    #     for user in User.query.all():
    #         if not user.is_following(user):
    #             user.follow(user)
    #             db.session.add(user)
    #             db.session.commit()

    # def __init__(self, **kwargs):
    #     super(User, self).__init__(**kwargs)
    #     if self.role is None:
    #         if self.role is None:
    #             self.role = Role.query.filter_by(default=True).first()
    #     if self.email is not None and self.avatar_hash is None:
    #         self.avatar_hash = self.gravatar_hash()
    #     self.follow(self)
    #
    # @property
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')
    #
    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)
    #

