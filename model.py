from flask_sqlalchemy import SQLAlchemy
import psycopg2
import secrets

db = SQLAlchemy()

class User(db.Model):
    """stores user data"""
    __tablename = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    password = db.Column(db.String)


class Group(db.Model):
    """stores group data"""
    __tablename__ = "groups"

    group_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    goal = db.Column(db.String)
    leader_1 = db.Column(db.String)
    leader_2 = db.Column(db.String)
    leader_3 = db.Column(db.String)


class GroupMember(db.Model):
    """associates groups with users"""
    __tablename__ = "group_members"

    group_member_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    group_id = db.Column(db.Integer, db.ForeignKey("groups.group_id"))

    user = db.relationship('User', backref='group_members')
    group = db.relationship('Group', backref='group_members')


class Goal(db.Model):
    """stores goals and likes"""
    __tablename__ = "goals"

    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    likes_count = db.Column(db.Integer)
    goal_name - db.Column(db.String)

    user = db.relationship('User', backref='goals')

class Rejection(db.Model):
    """tracks rejections"""
    __tablename__ = "rejections"

    rejection_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    goal_id = db.Column(db.Integer, db.ForeignKey("goals.goal_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    goal = db.relationship('Goal', backref='rejections')
    user = db.relationship('User', backref='rejections')

class Reactions(db.Model):
    """stores reactions to rejections"""
    __tablename__  = "reactions"

    reaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    goal_id = db.Column(db.Integer, db.ForeignKey("goals.goal_id"))
    recipient_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    sender_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    goal = db.relationship('Goal', backref='reactions')
    recipient = db.relationship('User', backref='rejections')
    sender = db.relationship('User', backref='rejections')

class Commnets(db.Model):
    """stores comments on rejections"""
    __tablename__ = "comments"

    commnet_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rejection_id = db.Column(db.Integer, db.ForeignKey("rejections.rejection_id"))
    commenter_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    goal_id = db.Column(db.Integer, bd.ForgeinKey("goals.goal_id"))

    rejection = db.relationship('Rejection', backref='comments')
    commenter = db.relationship('User', backref='comments')
    goal = db.Relationship('Goal', backref='comments')