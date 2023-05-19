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

def create_new_user():

    key = 1234
    master = int(input("Unesi MASTER KLJUČ kako bi kreirao novog korisnika: "))
    if master != key:
        print("ŠALJEMO UPOZORENJE VLASNIKU STANA ZA MOGUĆE NEOVLAŠTENO KREIRANJE KLJUČA!")

    elif master == key:

        ssn = int(input("Unesi social security number: "))
        first = str(input("Unesi ime: "))
        last = str(input("Unesi prezime: "))
        while True:
            username = str(input("Unesi username: ")).lower()
            if username in lst_user:
                print("Username već postoji, pokušajte ponovo!")
            else:
                break
        while True:
            password = str(input("Unesi šifru: "))
            if len(password) >= 6:
                break
            else:
                print("šifra ima nedovoljno znakova, minimum je 6 znakova!")
        while True:
            admin = str(input("Dajete ADMINSKA PRAVA novom korisniku? DA/NE ")).upper()
            if admin == "DA" or admin == "NE":
                break
            print("Pogrešan unos, pokušajte ponovo!")

        user_db = User(ssn,first,last,username,password,admin)
        session.add(user_db)
        session.commit()




def user_login():

    while True:
        enter_user = str(input("unesi username: ")).lower()
        enter_pass = str(input("unesi sifru: "))
        if enter_user in lst_user and enter_pass in lst_pass:
            break
        else:
            print("username ili sifra su netocni!")

    if enter_user in lst_admn:
        print("Chose action! \n 1 - Otvori vrata!\n 2 - Popis usera\n 3 - Edit user!\n 4 - Delete user!")
        value = int(input("Unesi broj: "))
        if value == 1:
            print("Vrata su otvorena!")
        elif value == 2:
            print("Lista korisnika: ")
            for i in lst_user:
                print(i)

        elif value == 3:
            print("Trenutno ne postoji opcija za editiranje korisnika! Potreban je update na novi software.")
        elif value == 4:
            username_del = str(input("Unesi username koji želiš izbrisati: ")).lower()
            try:
                user_delete = session.query(User).filter(User.username==username_del).first()
                session.delete(user_delete)
                session.commit()
                print(f"Korisnik '{user_delete}' je izbrisan!")
            except Exception as ex:
                print(f"Dogodila se greska {ex}")
    else:
        print("Vrata su otključana!")







#dodani itemi iz baze u listu

lst_user = []
lst_pass = []
lst_admn = []
lst_ssn = []

users = session.query(User)
for i in users:
    lst_user.append(i.username)
    lst_pass.append(i.password)
    lst_ssn.append(i.ssn)
    if i.admin == "DA":
        lst_admn.append(i.username)








