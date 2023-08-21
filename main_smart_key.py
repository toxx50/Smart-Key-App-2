#from db_sqlalchemy_file import *
#from features import bell_ring, DoorUnlock
import tkinter as tk
from files_smk.smart_key_konstante import *
from db_sqlalchemy_file import *




def frame_destroy():
    for frame in main_frame.winfo_children():
            frame.destroy()

def bell_ring():
    #output to speaker and return text to interface
    return BELL_RING


def door_unlock():
    frame_destroy()
    lb_door = tk.Label(main_frame, text='\U0001F511 THE DOORS ARE UNLOCKED!', font=("Bold", 19), bg="navy",
                      foreground="white")
    lb_door.place(x=5, y=5)
def guest_profile_act():
    frame_destroy()

    lb_key = tk.Label(main_frame, text='\U0001F511', font=("Bold", 20), bg=NAVY,
                          foreground=WHITE)
    lb_key.place(x=5, y=5)
    btn_enter = tk.Button(main_frame, text=" UNLOCK ", command=door_unlock)
    btn_enter.place(x=10, y=150)

def delete_user():
    frame_destroy()
    def delete():
        username_del = lbl_user_del.get().lower()
        lst_user_log = db_user_list()
        frame_destroy()
        try:
            if username_del in lst_user_log:
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

def edit_password():
    frame_destroy()
    """
    Traži od korisnika da ponovo upiše stari password i onda zamjeni za novi

    """
    def change_password():
        username_check = lb_username.get().lower()
        old_pass = lb_old_pass.get()
        new_pass = lb_new_pass.get()
        new_pass_ck = lb_new_pass_check.get()
        frame_destroy()

        password_ch = session.query(User).filter(User.username == username_check and User.password == old_pass).first()

        if password_ch == None:
            lbl_error = tk.Label(main_frame, text='Username or password are incorrect!!')
            lbl_error.place(x=20, y=20)
            btn_back = tk.Button(main_frame, text=' BACK ', command=edit_password)
            btn_back.place(x=20, y=100)

        elif new_pass_ck != new_pass:
            lbl_error = tk.Label(main_frame, text='NEW PASSWORD DO NOT MATCH')
            lbl_error.place(x=20, y=20)
            btn_back = tk.Button(main_frame, text=' BACK ', command=edit_password)
            btn_back.place(x=20, y=100)

        elif len(new_pass) < 6:
            lbl_error = tk.Label(main_frame, text='NEW PASSWORD IS TOO SHORT, MIN "6" CHARACTERS')
            lbl_error.place(x=20, y=20)
            btn_back = tk.Button(main_frame, text= ' BACK ', command=edit_password)
            btn_back.place(x=20,y=100)

        else:
            password_ch.password = new_pass
            session.commit()
            lbl_complete = tk.Label(main_frame, text='NEW PASSWORD IS CHANGED')
            lbl_complete.place(x=20, y=20)

    lbl_usernm = tk.Label(main_frame, text= 'Enter username:', background=NAVY, foreground=WHITE,font=BODY_FONT)
    lbl_usernm.place(x=20,y=5)
    lb_username = tk.Entry(main_frame, width=25)
    lb_username.place(x=20, y=30)

    lbl_oldpass = tk.Label(main_frame, text='Enter old password:', background=NAVY, foreground=WHITE,font=BODY_FONT)
    lbl_oldpass.place(x=20,y=50)
    lb_old_pass = tk.Entry(main_frame, width=25)
    lb_old_pass.place(x=20, y=75)

    lbl_newpass = tk.Label(main_frame, text='Enter new password twice:', background=NAVY, foreground='red', font=BODY_FONT)
    lbl_newpass.place(x=20, y=105)
    lb_new_pass = tk.Entry(main_frame, width=25)
    lb_new_pass.place(x=20,y=130)

    lb_new_pass_check = tk.Entry(main_frame, width=25)
    lb_new_pass_check.place(x=20,y=160)

    btn_chnge = tk.Button(main_frame, text='CHANGE', command=change_password)
    btn_chnge.place(x=260,y=150)


def edit_admin():
    frame_destroy()

    def submit_admin():
        username_check = lb_username.get().lower()
        admin_new = adm_var.get()
        frame_destroy()
        admin_ch = session.query(User).filter(User.username == username_check).first()
        if admin_ch == None:
            lbl_error = tk.Label(main_frame, text='Username do not exist!', background=NAVY,foreground=WHITE,font=SUBTITLE_FONT)
            lbl_error.place(x=20,y=20)
            btn_back = tk.Button(main_frame, text=' BACK ', command=edit_admin)
            btn_back.place(x=20, y=130)
        else:
            lbl_changed = tk.Label(main_frame, text='Admin rules are updated!', background=NAVY,foreground=WHITE,font=SUBTITLE_FONT)
            lbl_changed.place(x=20,y=20)
            admin_ch.admin = admin_new
            session.commit()


    lbl_username = tk.Label(main_frame, text='Enter username to change admin rules!', background=NAVY,foreground=WHITE,font=SUBTITLE_FONT)
    lbl_username.place(x=20,y=20)
    lb_username = tk.Entry(main_frame, width=25)
    lb_username.place(x=20,y=60)

    adm_var = tk.StringVar()
    adm_var.set('NE')

    rb_y = tk.Radiobutton(main_frame, text='YES', variable=adm_var,
                          value='DA', bg=NAVY, foreground=DARK_GREY)
    rb_y.place(x=20, y=120)

    rb_n = tk.Radiobutton(main_frame, text='NO', variable=adm_var,
                          value='NE', bg=NAVY, foreground=DARK_GREY)
    rb_n.place(x=68, y=120)

    lb_admin = tk.Label(main_frame, text='ADMIN: ', font=("Bold", 13),
                        bg=NAVY, foreground=WHITE)
    lb_admin.place(x=25, y=100)
    # endregion

    btn_enter = tk.Button(main_frame, text="ENTER", command=submit_admin)
    btn_enter.place(x=400, y=170)

def edit_user():
    frame_destroy()

    lbl_change = tk.Label(main_frame, text='EDIT USER SETTINGS',
                          font=('bold', 18), bg='navy',foreground='white')
    lbl_change.place(x=20,y=20)

    btn_ch_pass = tk.Button(main_frame, text='CHANGE PASSWORD',command=edit_password)
    btn_ch_pass.place(x=20,y=100)

    btn_ch_admn = tk.Button(main_frame, text='CHANGE ADMIN', command=edit_admin)
    btn_ch_admn.place(x=150,y=100)


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
    btn_enter = tk.Button(main_frame, text=" UNLOCK ", command=door_unlock)
    btn_enter.place(x=30, y=150)
    #endregion

def log_in():
    frame_destroy()
    def submit_login():
        username_login = lbl_usr_log.get().lower()
        password_login = lbl_pass_log.get()

        lst_admin_log = db_admin_list()

        password_ch = session.query(User).filter(User.username == username_login and User.password == password_login).first()

        if password_ch.username == username_login and password_ch.password == password_login and username_login not in lst_admin_log:
            guest_profile_act()

        elif password_ch.username == username_login and password_ch.password == password_login and username_login in lst_admin_log:
            admin_profile_act()
        else:
            frame_destroy()
            lb_usr_log = tk.Label(main_frame, text='Username ili password su netočni!',
                                  font=("Bold", 14), bg="navy",foreground="white")
            lb_usr_log.place(x=5, y=5)
            btn_enter = tk.Button(main_frame, text=" BACK ", command=log_in)
            btn_enter.place(x=10, y=150)


    #regionLOGIN WINDOW
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
        ssn_bool = lbl_ssn.get().isnumeric()
        ssn = lbl_ssn.get()
        first = lbl_first.get()
        last = lbl_last.get()
        username = lbl_username.get().lower()
        password = lbl_password.get()
        admin = adm_var.get()

        #region DESTROY
        frame_destroy()
        #endregion

        lst_user = db_user_list()
        lst_ssn = db_ssn_lst()

        if  ssn == '' or ssn_bool == False or int(ssn) in lst_ssn:
            lb_ssn = tk.Label(main_frame, text='ERROR: Social Security Number INVALID ENTRY!',
                              font=("Bold", 15), bg="navy", foreground="white")
            lb_ssn.place(x=5, y=5)
            btn_ok = tk.Button(main_frame, text=" BACK ", command=create_new_user)
            btn_ok.place(x=400, y=170)

        elif username in lst_user or username == '':
            lb_user = tk.Label(main_frame, text='USERNAME ALREADY EXIST! TRY AGAIN!',
                          font=("Bold", 15), bg="navy", foreground="white")
            lb_user.place(x=5, y=5)
            btn_ok = tk.Button(main_frame, text=" BACK ", command=create_new_user)
            btn_ok.place(x=400, y=170)

        elif len(password) < 6:
            lb_pass = tk.Label(main_frame, text='PASSWORD MUST CONTAIN OVER 5 CHARACTERS',
                          font=("Bold", 15), bg="navy", foreground="white")
            lb_pass.place(x=5, y=5)
            btn_ok = tk.Button(main_frame, text=" BACK ", command=create_new_user)
            btn_ok.place(x=400, y=170)

        else:
            #DATABASE
            db_user = User(ssn,first,last,username,password,admin)
            session.add(db_user)
            session.commit()
            log_in()


    lb = tk.Label(main_frame, text='CREATE USER',
                  font=("Bold", 15), bg="navy", foreground="white")
    lb.place(x=5, y=5)

    #region SSN
    lb_ssn = tk.Label(main_frame, text='Enter SSN:',
                      font=("Bold", 14), bg="navy", foreground="white")
    lb_ssn.place(x=20, y=35)

    lbl_ssn = tk.Entry(main_frame, width=25)
    lbl_ssn.place(x=200, y=39)
    #endregion

    #region FIRST
    lb_first = tk.Label(main_frame, text='Enter FIRST Name:',
                        font=("Bold", 14), bg="navy", foreground="white")
    lb_first.place(x=20, y=60)

    lbl_first = tk.Entry(main_frame, width=25)
    lbl_first.place(x=200, y=64)
    #endregion

    #region LAST
    lb_last = tk.Label(main_frame, text='Enter LAST Name:',
                       font=("Bold", 14), bg="navy", foreground="white")
    lb_last.place(x=20, y=85)

    lbl_last = tk.Entry(main_frame, width=25)
    lbl_last.place(x=200, y=89)
    #endregion

    #region USERNAME
    lb_username = tk.Label(main_frame, text='Enter USERNAME: ',
                           font=("Bold", 14), bg="navy", foreground="white")
    lb_username.place(x=20, y=110)

    lbl_username = tk.Entry(main_frame, width=25)
    lbl_username.place(x=200, y=114)
    #endregion

    #region PASSWORD
    lb_password = tk.Label(main_frame, text='Enter PASSWORD: ', font=("Bold", 14),
                           bg="navy", foreground="white")
    lb_password.place(x=20, y=135)

    lbl_password = tk.Entry(main_frame, width=25)
    lbl_password.place(x=200, y=139)
    #endregion

    #region ADMIN
    adm_var = tk.StringVar()
    adm_var.set('NE')

    rb_y = tk.Radiobutton(main_frame, text='YES', variable=adm_var,
                          value='DA', bg=NAVY, foreground=DARK_GREY)
    rb_y.place(x=380, y=59)

    rb_n = tk.Radiobutton(main_frame, text='NO', variable=adm_var,
                          value='NE', bg=NAVY, foreground=DARK_GREY)
    rb_n.place(x=428, y=59)

    lb_admin = tk.Label(main_frame, text='ADMIN: ', font=("Bold", 13),
                        bg=NAVY, foreground=WHITE)
    lb_admin.place(x=400, y=39)
    #endregion

    btn_enter = tk.Button(main_frame, text="ENTER", command=submit_user_info)
    btn_enter.place(x=400, y=170)


def new_user():
    frame_destroy()
    def submit():
        master = lbl_entry.get()
        if master == MASTER_KEY:
            create_new_user()
        elif master != MASTER_KEY:
            frame_destroy()
            lb = tk.Label(main_frame,
                          text='SENDING WARNING TO OWNER OF APARTMENT \nPOSSIBLE UNAUTHORIZED ENTRY!',
                          font=("Bold", 15), bg=NAVY, foreground="white")
            lb.place(x=10, y=20)


    lb = tk.Label(main_frame, text='TYPE MASTER KEY:', font=("Bold", 15),
                  bg=NAVY,foreground="white")
    lb.place(x=20,y=20)

    btn_enter = tk.Button(main_frame, text="ENTER", command=submit)
    btn_enter.place(x=160,y=60)

    lbl_entry = tk.Entry(main_frame,show='*', width=15)
    lbl_entry.place(x=50,y=62)

def bell():
    frame_destroy()
    lb = tk.Label(main_frame, text=bell_ring(), font=("Bold",15),
                  bg=NAVY, foreground="white")
    lb.place(x=10,y=5)

def numpad():
    """
    Numpad tipkovnica nije u funkciji.
    """
    frame_destroy()
    lb = tk.Label(main_frame, text="NUMPAD IS DISABLED", font=("Bold",15),
                  bg=NAVY, foreground="white")
    lb.place(x=10,y=5)

    """potrebno je kreirati funkciju za unos jednokratnog pina za otkljucavanje
    ulaznih vrata, pin za jednokratnu upotrebu može kreirat samo admin """





#region MAIN WINDOW
main_window = tk.Tk()
main_window.title('SMART KEY')
main_window.geometry('600x800')

background_img = tk.PhotoImage(file='files_smk/hd-modern-dark-blue.png')
tk.Label(main_window, image=background_img).place(x=-2,y=-2)
icon = tk.PhotoImage(file='files_smk/keys.png')
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
btn_create = tk.Button(frm_header, text='7', bg="light blue", command=numpad)
btn_create.grid(row=0,column=2, padx=0, pady=0, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='8', bg="light blue", command=numpad)
btn_create.grid(row=0,column=3, padx=30, pady=0, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='9', bg="light blue", command=numpad)
btn_create.grid(row=0,column=4 , padx=30, pady=0, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='4', bg="light blue", command=numpad)
btn_create.grid(row=1,column=2, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='5', bg="light blue", command=numpad)
btn_create.grid(row=1,column=3, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='6', bg="light blue", command=numpad)
btn_create.grid(row=1,column=4, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='1', bg="light blue", command=numpad)
btn_create.grid(row=2,column=2, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='2', bg="light blue", command=numpad)
btn_create.grid(row=2,column=3, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='3', bg="light blue", command=numpad)
btn_create.grid(row=2,column=4, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='*', bg="light blue", command=numpad)
btn_create.grid(row=3,column=2, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='0', bg="light blue", command=numpad)
btn_create.grid(row=3,column=3, padx=BTN_PADX, pady=BTN_PADY, ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_create = tk.Button(frm_header, text='#', bg="light blue", command=numpad)
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