#from db_sqlalchemy_file import *
#from features import bell_ring, DoorUnlock
from smart_key_konstante import *
from db_sqlalchemy_file import *
import tkinter as tk



def frame_destroy():
    for frame in main_frame.winfo_children():
            frame.destroy()

def bell_ring():
    return 'RING!!!RING!!!RING!!!\U0001F514\U0001F514\U0001F514'

def door_unlock():
    frame_destroy()
    lb_door = tk.Label(main_frame, text='\U0001F511 ULAZNA VRATA SU OTKLJUČANA!', font=("Bold", 19), bg="navy",
                      foreground="white")
    lb_door.place(x=5, y=5)
def guest_profile_act():
    frame_destroy()

    lb_key = tk.Label(main_frame, text='\U0001F511', font=("Bold", 20), bg="navy",
                          foreground="white")
    lb_key.place(x=5, y=5)
    btn_enter = tk.Button(main_frame, text=" OTKLJUČAJ ", command=door_unlock)
    btn_enter.place(x=10, y=150)

def delete_user():
    frame_destroy()
    def delete():
        username_del = lbl_user_del.get().lower()
        frame_destroy()
        try:
            if username_del in lst_user:
                user_delete = session.query(User).filter(User.username == username_del).first()
                session.delete(user_delete)
                session.commit()
                lb_deleted = tk.Label(main_frame,text=f'User {username_del} is deleted!')
                lb_deleted.place(x=20,y=20)
            else:
                lb_notdeleted = tk.Label(main_frame, text=f'User >{username_del}< do not exist!',
                                         font=('Bold',18),bg='navy',foreground='white')
                lb_notdeleted.place(x=20, y=20)
                bt_del = tk.Button(main_frame, text=' BACK ', command=delete_user)
                bt_del.place(x=20,y=150)

        except Exception as ex:
            print(f"Dogodila se greska {ex}")

    lb_del_mes = tk.Label(main_frame, text='Type USERNAME to DELETE',
                          font=('Bold',18),bg='navy',foreground='white')
    lb_del_mes.place(x=20,y=20)
    lbl_user_del = tk.Entry(main_frame, width=25)
    lbl_user_del.place(x=50,y=70)
    btn_delete = tk.Button(main_frame, text='DELETE',command=delete)
    btn_delete.place(x=210,y=67)

def edit_user():
    pass

def admin_profile_act():
    frame_destroy()
    #regionDELETE BUTTON
    btn_user_del = tk.Button(main_frame, text=' DELETE USER ', command=delete_user)
    btn_user_del.place(x=390,y=150)
    #endregion
    #regionEDIT BUTTON
    btn_user_del = tk.Button(main_frame, text=' EDIT USER ', command=edit_user)
    btn_user_del.place(x=290, y=150)
    #endregion
    #regionADD USER BUTTON
    btn_enter = tk.Button(main_frame, text=" CREATE NEW USER ", command=create_new_user)
    btn_enter.place(x=140, y=150)
    #endregion #
    #regionUNLOCK DOOR BUTTON
    btn_enter = tk.Button(main_frame, text=" OTKLJUČAJ ", command=door_unlock)
    btn_enter.place(x=30, y=150)
    #endregion

def log_in():
    frame_destroy()
    def submit_login():
        username_login = lbl_usr_log.get()
        password_login = lbl_pass_log.get()

        if username_login in lst_user and password_login in lst_pass and username_login not in lst_admn:
            guest_profile_act()
        elif username_login in lst_user and password_login in lst_pass and username_login in lst_admn:
            admin_profile_act()
        else:
            frame_destroy()
            lb_usr_log = tk.Label(main_frame, text='Username ili password su netočni!', font=("Bold", 14), bg="navy",
                                  foreground="white")
            lb_usr_log.place(x=5, y=5)
            btn_enter = tk.Button(main_frame, text=" BACK ", command=log_in)
            btn_enter.place(x=10, y=150)

    # regionLOGIN WINDOW
    def show_password():
        if lbl_pass_log.cget('show') == '*':
            lbl_pass_log.config(show='')
        else:
            lbl_pass_log.config(show='*')

    lb_usr_log = tk.Label(main_frame, text='LOG IN\n\n  username: ',
                          font=("Bold", 14), bg="navy", foreground="white")
    lb_usr_log.place(x=5, y=5)

    lbl_usr_log = tk.Entry(main_frame, width=25)
    lbl_usr_log.place(x=150, y=54)

    lb_pass_log = tk.Label(main_frame, text='\n  password: ', font=("Bold", 14),
                           bg="navy", foreground="white")
    lb_pass_log.place(x=5, y=70)

    lbl_pass_log = tk.Entry(main_frame,show='*', width=25)
    lbl_pass_log.place(x=150, y=99)

    btn_enter = tk.Button(main_frame, text="ENTER", command=submit_login)
    btn_enter.place(x=260, y=150)

    check_button = tk.Checkbutton(main_frame,text='show password',
                                  bg='navy',foreground='red',
                                  command=show_password)
    check_button.place(x=145, y=120)
    #endregion


def create_new_user():
    frame_destroy()

    def submit_user_info():
        ssn = lbl_ssn.get()
        first = lbl_first.get()
        last = lbl_last.get()
        username = lbl_username.get().lower()
        password = lbl_password.get()
        admin = adm_var.get()


        #region DESTROY
        frame_destroy()
        """lbl_ssn.destroy()
        lbl_first.destroy()
        lbl_last.destroy()
        lbl_username.destroy()
        lbl_password.destroy()"""
        #endregion
        if username in lst_user:
            lb_user = tk.Label(main_frame, text='USERNAME VEĆ POSTOJI! POKUŠAJTE PONOVO',
                          font=("Bold", 15), bg="navy", foreground="white")
            lb_user.place(x=5, y=5)
            btn_ok = tk.Button(main_frame, text=" BACK ", command=create_new_user)
            btn_ok.place(x=400, y=170)

        elif ssn == '' or int(ssn) in lst_ssn:
            lb_ssn = tk.Label(main_frame, text='ERROR: Social Security Number INVALID ENTRY!',
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
            db_user = User(ssn,first,last,username,password,admin)
            session.add(db_user)
            session.commit()
            #endregion
            log_in()


    lb = tk.Label(main_frame, text='KREIRANJE KORISNIKA',
                  font=("Bold", 15), bg="navy", foreground="white")
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
    adm_var = tk.StringVar()
    adm_var.set('NO')

    rb_y = tk.Radiobutton(main_frame, text='YES', variable=adm_var, value='YES', bg='navy', foreground='dark grey')
    rb_y.place(x=380, y=59)

    rb_n = tk.Radiobutton(main_frame, text='NO', variable=adm_var, value='NO', bg='navy', foreground='dark grey')
    rb_n.place(x=428, y=59)

    lb_admin = tk.Label(main_frame, text='ADMIN: ', font=("Bold", 13), bg="navy", foreground="white")
    lb_admin.place(x=400, y=39)
    #endregion

    btn_enter = tk.Button(main_frame, text="ENTER", command=submit_user_info)
    btn_enter.place(x=400, y=170)


def new_user():
    frame_destroy()
    def submit():
        master = lbl_entry.get()
        if master == "1234":
            create_new_user()
        elif master != "1234":
            frame_destroy()
            lb = tk.Label(main_frame,
                          text='ŠALJEMO UPOZORENJE VLASNIKU STANA \nZA MOGUĆE NEOVLAŠTENO KREIRANJE KLJUČA!',
                          font=("Bold", 15), bg="navy", foreground="white")
            lb.place(x=10, y=20)


    lb = tk.Label(main_frame, text='UNESI MASTER KEY:', font=("Bold", 15),
                  bg="navy",foreground="white")
    lb.place(x=20,y=20)

    btn_enter = tk.Button(main_frame, text="ENTER", command=submit)
    btn_enter.place(x=160,y=60)

    lbl_entry = tk.Entry(main_frame,show='*', width=15)
    lbl_entry.place(x=50,y=62)

def bell():
    frame_destroy()
    lb = tk.Label(main_frame, text=bell_ring(),font=("Bold",15),
                  bg="navy", foreground="white")
    lb.place(x=10,y=5)



#region MAIN WINDOW
main_window = tk.Tk()
main_window.title('SMART KEY')
main_window.geometry('600x800')

background_img = tk.PhotoImage(file='hd-modern-dark-blue.png')
tk.Label(main_window, image=background_img).place(x=-2,y=-2)
icon = tk.PhotoImage(file='keys.png')
main_window.iconphoto(True,icon)

lbl_app_title = tk.Label(main_window, text='SLAVONSKA AVENUE St.\n205',bg='#212121', font=TITLE_FONT,foreground='white')
lbl_app_title.pack(pady=TITLE_PADY,padx=TITLE_PADX)

frm_header = tk.LabelFrame(main_window, text='Portofon',font=BODY_FONT,bg='#212121',foreground='#1080F0')
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
frm_body = tk.LabelFrame(main_window, text='Display',bg='#212121', font=BODY_FONT,foreground='#1080F0')
frm_body.pack(padx=BODY_PADX, pady=BODY_PADY, fill='both')




main_frame = tk.Frame(frm_body, bg='navy')


main_frame.pack()
main_frame.pack_propagate(False)
main_frame.configure(width=500, height=200)

#endregion



main_window.mainloop()