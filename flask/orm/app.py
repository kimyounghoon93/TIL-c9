from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#flask
app = Flask(__name__)

# sqlalchemy 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlalchemy 초기화
db = SQLAlchemy(app)

# mifrate 초기화
migrate = Migrate(app,db)

# table 만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    memo = db.Column(db.Text)
    
    def __repr__(self):
        return f'<USER {self.id}: {self.username}, {self.email}>'
        

# flask db init
# flask db migrate
# flask db upgrade

# [Create]
#  from app import db, User
#  user = User(username='yh', email='kyh2021@naver.com')

#  db.session.add(user)

#  db.session.commit()

#  User.query.all()
# [<User 1>]
#  user = User(username='admin', email='admin@example.com')                                                                                                       
# >>> db.session.add(user)
# >>> db.session.commit()
# >>> User.query.all()
# [<User 1>, <User 2>]
# INSERT INTO users (username, email) VALUES ('name', 'asd@asd.asd')
# user = User(username='name', email='asd@asd.asd')
# db.session.add(user)
# db.session.commit()

# [Read]
# SELECT * FROM users;
# users = User.query.all() # 복수

#  users = user.query.filter_by(username='apple').first()


# SELECT * FROM users WHERE username='apple' LIMIT 1;
# users = User.query.filter_by(username='apple').first()

#  user
# <User 3>

# users = User.query.get(2)
# user
# 2번 유저
# user.username (
# user.username 
# 의 상세정보)
# user.email(user.email)
# primary key만 get으로 가져올 수 있음.

# user = User.query.filter_by(username='water').first()
# SELECT * FROM users WHERE email LIKE '%water%';

# ORDER
# users = User.query.order_by(User.username).all()

# LIMIT
# users = User.query.limit(1).all()

# OFFSET
# users = User.query.offset(2).all()


# ORDER + LIMIT + OFFSET
# users = User.query.order_by(User.username).limit(1).offset(2).all()

# 삭제
# from app import db, user
# user.query.all()
# user = User.query.get(1)
# db.session.delete(user)
# db.session.commit()

# DELETE
# DELETE FROM users WHERE id=1;
# user = User.query.get(1)
# db.session.delete(user)
# db.session.commit()

# ==> 1번이 사라짐

# 이름 바꾸기
# user = User.query.get(2)
# user.username
# '~~~2번이름'
# user.username = 'NewName'
# ==>바뀜

# UPDATE
# UPDATE users SET username='NewName' WHERE id=2;
# user = User.query.get(2)
# user.username = 'NewName'
# db.session.commit()
