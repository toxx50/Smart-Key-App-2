#from db_sqlalchemy_file import *
#from features import bell_ring, DoorUnlock
from smart_key_konstante import *
from db_sqlalchemy_file import *
import tkinter as tk

def lb_select_handler():
    pass
def bell_ring():
    return 'RING!!!RING!!!RING!!!\U0001F514\U0001F514\U0001F514'

def frame_destroy():
    for frame in main_frame.winfo_children():
            frame.destroy()



def log_in():
    frame_destroy()
    def submit_login():
        username_login = lbl_usr_log.get()
        password_login = lbl_pass_log.get()

        if username_login in lst_user and password_login in lst_pass:
            print("wazzupp")
        else:
            frame_destroy()
            lb_usr_log = tk.Label(main_frame, text='Username ili password su netočni!', font=("Bold", 14), bg="navy",
                                  foreground="white")
            lb_usr_log.place(x=5, y=5)
            btn_enter = tk.Button(main_frame, text=" BACK ", command=log_in)
            btn_enter.place(x=10, y=150,)



    lb_usr_log = tk.Label(main_frame, text='LOG IN\n\n  username: ', font=("Bold", 14), bg="navy", foreground="white")
    lb_usr_log.place(x=5, y=5)

    lbl_usr_log = tk.Entry(main_frame, width=25)
    lbl_usr_log.place(x=150, y=54)

    lb_pass_log = tk.Label(main_frame, text='\n  password: ', font=("Bold", 14), bg="navy", foreground="white")
    lb_pass_log.place(x=5, y=70)

    lbl_pass_log = tk.Entry(main_frame, width=25)
    lbl_pass_log.place(x=150, y=99)

    btn_enter = tk.Button(main_frame, text="ENTER", command=submit_login)
    btn_enter.place(x=250, y=130)

def create_new_user():
    frame_destroy()

    def submit_user_info():
        ssn = lbl_ssn.get()
        first = lbl_first.get()
        last = lbl_last.get()
        username = lbl_username.get().lower()
        password = lbl_password.get()
        #admin = lbl_admin.get()
        print(ssn)
        print(type(ssn))

        #region DESTROY
        frame_destroy()
        lbl_ssn.destroy()
        lbl_first.destroy()
        lbl_last.destroy()
        lbl_username.destroy()
        lbl_password.destroy()
        #endregion
        if username in lst_user:
            lb_user = tk.Label(main_frame, text='USERNAME VEĆ POSTOJI! POKUŠAJTE PONOVO',
                          font=("Bold", 15), bg="navy", foreground="white")
            lb_user.place(x=5, y=5)
            btn_ok = tk.Button(main_frame, text=" BACK ", command=create_new_user)
            btn_ok.place(x=400, y=170)
        elif int(ssn) in lst_ssn:
            lb_ssn = tk.Label(main_frame, text='ERROR: Social Security Number VEĆ POSTOJI!',
                               font=("Bold", 15), bg="navy", foreground="white")
            lb_ssn.place(x=5, y=5)
            btn_ok = tk.Button(main_frame, text=" BACK ", command=create_new_user)
            btn_ok.place(x=400, y=170)

        elif len(password) <= 6:
            lb_pass = tk.Label(main_frame, text='PASWORD MORA SADRŽAVAT PREKO 5 ZNAKOVA',
                          font=("Bold", 15), bg="navy", foreground="white")
            lb_pass.place(x=5, y=5)
            btn_ok = tk.Button(main_frame, text=" BACK ", command=create_new_user)
            btn_ok.place(x=400, y=170)

        else:
            #region DATABASE
            db_user = User(ssn,first,last,username,password,admin="DA")
            session.add(db_user)
            session.commit()
            #endregion
            log_in()


        print(ssn, first, last, username, password)






    lb = tk.Label(main_frame, text='KREIRANJE KORISNIKA', font=("Bold", 15), bg="navy", foreground="white")
    lb.place(x=5, y=5)

    #region SSN
    lb_ssn = tk.Label(main_frame, text='Unesi SSN: ', font=("Bold", 14), bg="navy", foreground="white")
    lb_ssn.place(x=20, y=35)

    lbl_ssn = tk.Entry(main_frame, width=25)
    lbl_ssn.place(x=200, y=39)
    #endregion

    #region FIRST
    lb_first = tk.Label(main_frame, text='Unesi IME: ', font=("Bold", 14), bg="navy", foreground="white")
    lb_first.place(x=20, y=60)

    lbl_first = tk.Entry(main_frame, width=25)
    lbl_first.place(x=200, y=64)
    #endregion

    #region LAST
    lb_last = tk.Label(main_frame, text='Unesi PREZIME: ', font=("Bold", 14), bg="navy", foreground="white")
    lb_last.place(x=20, y=85)

    lbl_last = tk.Entry(main_frame, width=25)
    lbl_last.place(x=200, y=89)
    #endregion

    #region USERNAME
    lb_username = tk.Label(main_frame, text='Unesi USERNAME: ', font=("Bold", 14), bg="navy", foreground="white")
    lb_username.place(x=20, y=110)

    lbl_username = tk.Entry(main_frame, width=25)
    lbl_username.place(x=200, y=114)
    #endregion

    #region PASSWORD
    lb_password = tk.Label(main_frame, text='Unesi PASSWORD: ', font=("Bold", 14), bg="navy", foreground="white")
    lb_password.place(x=20, y=135)

    lbl_password = tk.Entry(main_frame, width=25)
    lbl_password.place(x=200, y=139)
    #endregion

    #region ADMIN
    #insert checkbox y/n
    lb_admin = tk.Label(main_frame, text='ADMIN: ', font=("Bold", 13), bg="navy", foreground="white")
    lb_admin.place(x=400, y=39)

    #lbl_admin = tk.Entry(main_frame, width=25)
    #lbl_admin.place(x=160, y=54)
    #endregion

    print(lst_user)
    print(lst_ssn)

    if 43343434 in lst_ssn:
        print("hi")


    btn_enter = tk.Button(main_frame, text="ENTER", command=submit_user_info)
    btn_enter.place(x=400, y=170)



def new_user():
    frame_destroy()
    def submit():
        master = lbl_entry.get()
        if master == "1234":
            create_new_user()
        elif master != "1234":
            lb = tk.Label(main_frame,
                          text='ŠALJEMO UPOZORENJE VLASNIKU STANA \nZA MOGUĆE NEOVLAŠTENO KREIRANJE KLJUČA!',
                          font=("Bold", 15), bg="navy", foreground="white")
            lb.place(x=10, y=20)




    lb = tk.Label(main_frame, text='UNESI MASTER KEY:', font=("Bold", 15), bg="navy",foreground="white")
    lb.place(x=20,y=20)

    btn_enter = tk.Button(main_frame, text="ENTER", command=submit)
    btn_enter.place(x=160,y=60)

    lbl_entry = tk.Entry(main_frame, width=15)
    lbl_entry.place(x=50,y=62)


def bell():
    frame_destroy()
    lb = tk.Label(main_frame, text=bell_ring(),font=("Bold",15), bg="navy", foreground="white")
    lb.place(x=10,y=5)








#region MAIN WINDOW
main_window = tk.Tk()
main_window.title('SMART KEY')
main_window.geometry('600x800')

lbl_app_title = tk.Label(main_window, text=f'WELCOME TO {NAME} FAMILY', font=TITLE_FONT)
lbl_app_title.pack(pady=TITLE_PADY,padx=TITLE_PADX)

frm_header = tk.LabelFrame(main_window, text='Portofon', font=BODY_FONT)
frm_header.pack(padx=BODY_PADX, pady=BODY_PADY, fill=tk.BOTH)
frm_header.columnconfigure(index=0,weight=2)
frm_header.columnconfigure(index=1,weight=4)
frm_header.columnconfigure(index=2,weight=2)

btn_create = tk.Button(frm_header, text='Create User', bg="light blue", command=new_user)
btn_create.grid(row=0,column=0, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_login = tk.Button(frm_header, text='Login', bg="light blue", command=log_in)
btn_login.grid(row=1,column=0, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_bellring = tk.Button(frm_header, text='Bell Ring', bg="light blue", command=bell)
btn_bellring.grid(row=2,column=0 , padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)
#endregion

#region NUMPAD
btn_create = tk.Button(frm_header, text='7', bg="light blue", command=1)
btn_create.grid(row=0,column=2, padx=0, pady=0, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='8', bg="light blue", command=1)
btn_create.grid(row=0,column=3, padx=30, pady=0, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='9', bg="light blue", command=1)
btn_create.grid(row=0,column=4 , padx=30, pady=0, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='4', bg="light blue", command=1)
btn_create.grid(row=1,column=2, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='5', bg="light blue", command=1)
btn_create.grid(row=1,column=3, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='6', bg="light blue", command=1)
btn_create.grid(row=1,column=4, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='1', bg="light blue", command=1)
btn_create.grid(row=2,column=2, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='2', bg="light blue", command=1)
btn_create.grid(row=2,column=3, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='3', bg="light blue", command=1)
btn_create.grid(row=2,column=4, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='*', bg="light blue", command=1)
btn_create.grid(row=3,column=2, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='0', bg="light blue", command=1)
btn_create.grid(row=3,column=3, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='#', bg="light blue", command=1)
btn_create.grid(row=3,column=4, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)
#endregion

#region BODY
frm_body = tk.LabelFrame(main_window, text='Display', font=BODY_FONT)
frm_body.pack(padx=BODY_PADX, pady=BODY_PADY, fill='both')




main_frame = tk.Frame(frm_body, bg='navy')


main_frame.pack()
main_frame.pack_propagate(False)
main_frame.configure(width=500, height=200)

#endregion



main_window.mainloop()