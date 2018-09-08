from sqlalchemy import Column, String, create_engine, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    user_id = Column(Integer, ForeignKey('user.id'))


engine = create_engine("mysql+pymysql://test:secret@localhost:3306/test", max_overflow = 5)
DBsession = sessionmaker(bind=engine)
session = DBsession()

user = User(name='TT')
session.add(user)
session.commit()

user = session.query(User).filter(User.id == 2).one()
print('type:', type(user), 'name:', user.name, 'books:', user.books)
session.close()
