from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    username = Column("username", String)
    password = Column("password", String)
    admin = Column("admin", String)

    def __init__(self, ssn, first, last, username, password,admin):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.username = username
        self.password = password
        self.admin = admin

    def __repr__(self):
        return f"{self.ssn} {self.firstname} {self.lastname} {self.password} {self.admin}"


engine = create_engine("sqlite:///db-smk/users.db", echo=False)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()




def db_user_list():
    lst_user = []
    for i in users:
        lst_user.append(i.username)
    return lst_user

def db_pass_list():
    lst_pass = []
    for i in users:
        lst_pass.append(i.password)
    return lst_pass

def db_admin_list():
    lst_admn = []
    for i in users:
        if i.admin == "DA":
            lst_admn.append(i.username)
    return lst_admn

def db_ssn_lst():
    lst_ssn = []
    for i in users:
        lst_ssn.append(i.ssn)
    return lst_ssn



#podatci iz baze iz baze u listi
users = session.query(User)
"""
lst_user = db_user_list()
lst_pass = db_pass_list()
lst_admn = db_admin_list()
lst_ssn = db_ssn_lst()
"""







