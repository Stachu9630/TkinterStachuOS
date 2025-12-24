import tkinter as tk
from tkinter import PhotoImage, messagebox
import time

login_username = "admin"
login_password = "password"
lock_password = login_password
#fix the desktop appearing when lock password is incorrect
#add more power options
#make restart show stachuOS boot screen or bios
#add a reset option
#make stachuOS and option for stachuOS lite(chosen from boot menu)
#finish shell

#abiltiy to change username and maybe password
def show_bios():
    bios_screen = tk.Toplevel()
    bios_screen.attributes("-fullscreen", True)
    bios_screen.config(bg="black")

    bios_os = tk.Label(bios_screen, text="Stachu OS", bg="black", fg="white", font="Helvetica, 50")
    bios_os.pack()

    bios_underscore = tk.Label(bios_screen, text="_", bg="black", fg="white", font="Helvetica, 30")
    bios_underscore.place(x=1, y=100)
    bios_screen.after(3200, lambda: (bios_screen.withdraw(), restart_screen.withdraw(), power.withdraw()))

def show_features_stachuos():
    features_list = tk.Toplevel()
    features_list.geometry("1000x1300")
    features_list.config(bg="#757171")
    features_list.title("what you can do in Stachu OS")

    feature_stachu_os = tk.Label(features_list, text="""
    you can use a command line
    you can see your computers info
    Stachu OS is password protected
    multiple power options to choose from
    recive messages
    recive the latest updates from the Stachu OS developers
    recive security updates
    Stachu OS collects no data from users




    thank you for using Stachu OS :)
    -developers of Stachu OS and the stachu project
    """, bg="#757171", font="Helvetica, 20")
    feature_stachu_os.pack(pady=50)
def show_features_stachuos2():
    features_list = tk.Toplevel()
    features_list.geometry("1000x1300")
    features_list.config(bg="#757171")
    features_list.title("Stachu OS 2 features")
    feature_stachu_os = tk.Label(features_list, text="""Stachu OS 2 features:
    ability to change username
    ability to change password
    new coloured account icons
    new single colour wallpapers
    added signout to power options
    added lock to power options
    start menu has a account icon
    hello(username) added to start menu
    
    estimated release window:
    february 23-28
    
    *new*
    
    release date:
    february 23rd
    
    thank you for using Stachu OS :)""", bg="#757171", font="Helvetica, 20")
    feature_stachu_os.pack(pady=50)


def power_options_back_to_desktop():
    power.withdraw()


def power_options_shutdown():
    shutdown_screen = tk.Toplevel()
    shutdown_screen.attributes("-fullscreen", True)
    shutdown_screen.config(bg="black")

    shutdown_screen_txt1 = tk.Label(shutdown_screen, text="stachu OS", bg="black", fg="white", font="Helvetica, 50")
    shutdown_screen_txt1.pack(pady=200)
    shutdown_screen_txt2 = tk.Label(shutdown_screen, text="shutting down system...", bg="black", fg="white", font="Helvetica, 30")
    shutdown_screen_txt2.pack()
    shutdown_screen.after(5100, lambda:exit())

def power_options_restart():
    global restart_screen
    restart_screen = tk.Toplevel()
    restart_screen.attributes("-fullscreen", True)
    restart_screen.config(bg="black")

    restart_screen_txt1 = tk.Label(restart_screen, text="stachu OS", bg="black", fg="white", font="Helvetica, 50")
    restart_screen_txt1.pack(pady=200)
    restart_screen_txt2 = tk.Label(restart_screen, text="restarting system...", bg="black", fg="white", font="Helvetica, 30")
    restart_screen_txt2.pack()
    restart_screen.after(2300, lambda:show_bios())

def power_options_sleep():
    sleep_screen = tk.Toplevel()
    sleep_screen.attributes("-fullscreen", True)
    sleep_screen.config(bg="black")

    sleep_screen_txt1 = tk.Label(sleep_screen, text="stachu OS", bg="black", fg="white", font="Helvetica, 50")
    sleep_screen_txt1.pack(pady=200)
    sleep_screen_txt2 = tk.Label(sleep_screen, text="press ALT F4 to return to desktop", bg="black", fg="#757171", font="Helvetica, 30")
    sleep_screen_txt2.pack()


def power_options_signout():
    signout_screen = tk.Toplevel()
    signout_screen.attributes("-fullscreen", True)
    signout_screen.config(bg="#757171")

    signout_txt1 = tk.Label(signout_screen, text="stachu OS", bg="black", fg="white", font="Helvetica, 50")
    signout_txt1.pack(pady=200)
    
def power_options():
    global power
    power = tk.Toplevel()
    power.attributes("-fullscreen", True)
    power.config(bg="#757171")

    shutdown_txt = tk.Label(power, text="shutdown", font="Helvetica, 30")
    shutdown_btn = tk.Button(power, shutdown_txt, bg="#757171", command=power_options_shutdown)
    shutdown_btn.pack(padx=10, pady=50)

    restart_txt = tk.Label(power, text="restart", font="Helvetica, 30")
    restart_btn = tk.Button(power, restart_txt, bg="#757171", command=power_options_restart)
    restart_btn.pack(padx=10, pady=50)

    sleep_txt = tk.Label(power, text="sleep", font="Helvetica, 30")
    sleep_btn = tk.Button(power, sleep_txt, bg="#757171", command=power_options_sleep)
    sleep_btn.pack(padx=10, pady=50)

    #signout_txt = tk.Label(power, text="signout", font="Helvetica, 30")
    #signout_btn = tk.Button(power, signout_txt, bg="#757171", command=power_options_signout)
    #signout_btn.pack(padx=10, pady=50)

    #implement later
    #lock_txt = tk.Label(power, text="lock", font="Helvetica, 30")
    #lock_btn = tk.Button(power, lock_txt, bg="#757171", command=power_options_lock)
    #lock_btn.pack(padx=10, pady=50)

    back_txt = tk.Label(power, text="back to desktop", font="Helvetica, 30")
    back_btn = tk.Button(power, back_txt, bg="#757171", command=power_options_back_to_desktop)
    back_btn.pack(padx=10, pady=100)

def show_OS_info():
    os_info = tk.Toplevel()
    os_info.geometry("1000x1000")
    os_info.config(bg="#757171")
    os_info.title("Stachu OS info")
    
    info_OS_name = tk.Label(os_info, text="Stachu OS", bg="#757171", fg="white", font="Helvetica, 50")
    info_OS_name.pack(pady=10)

    info_OS_ver = tk.Label(os_info, text="Stachu OS 1", bg="#757171", fg="white", font="Helvetica, 30")
    info_OS_ver.place(x=10, y=200)

    info_OS_bit = tk.Label(os_info, text="64 bit version", bg="#757171", fg="white", font="Helvetica, 30")
    info_OS_bit.place(x=10, y=300)

    info_OS_build = tk.Label(os_info, text="2/25 build", bg="#757171", fg="white", font="Helvetica, 30")
    info_OS_build.place(x=10, y=400)

    info_OS_dev = tk.Label(os_info, text="developed by the stachu project", bg="#757171", fg="white", font="Helvetica, 30")
    info_OS_dev.place(x=10, y=500)

def shell_commands():
    shell_request = shell_entry.get()
    if shell_request == "help":
        help_shell = tk.Toplevel()
        help_shell.geometry("1000x1000")
        help_shell.config(bg="#757171")
        help_shell.title("<shell> <commands>")

        shell_help_txt1 = tk.Label(help_shell, text="shutdown qck : forces quick shutdown", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt1.place(x=10, y=50)

        shell_help_txt2 = tk.Label(help_shell, text="system info : displays system information", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt2.place(x=10, y=100)    

    elif shell_request == "shutdown qck":
        exit()
    elif shell_request == "system info":
        sys_info_shell = tk.Toplevel()
        sys_info_shell.geometry("1000x1000")
        sys_info_shell.config(bg="#757171")
        sys_info_shell.title("<shell> <sys><info>")

        sys_info_shell_txt1 = tk.Label(sys_info_shell, text="proccesor : intel i7-7700", bg="#757171", fg="white", font="Helvetica, 15")
        sys_info_shell_txt1.place(x=1, y=50)
        sys_info_shell_txt2 = tk.Label(sys_info_shell, text="graphics card : intel i7-7700(integrated)", bg="#757171", fg="white", font="Helvetica, 15")
        sys_info_shell_txt2.place(x=1, y=100)
        sys_info_shell_txt3 = tk.Label(sys_info_shell, text="RAM : 8GB DDR4", bg="#757171", fg="white", font="Helvetica, 15")
        sys_info_shell_txt3.place(x=1, y=150)
        sys_info_shell_txt4 = tk.Label(sys_info_shell, text="disk(SSD/SATA) : kingston 220GB ", bg="#757171", fg="white", font="Helvetica, 15")
        sys_info_shell_txt4.place(x=1, y=200)

    elif shell_request == "reboot ui":
        power_options_restart()
    else:
        messagebox.showerror("stachu OS", "no command found")

def open_shell():
    global shell_entry

    shell = tk.Toplevel()
    shell.geometry("1000x1000")
    shell.config(bg="black")
    shell.title("<shell>")

    shell_ver_show = tk.Label(shell, text="stachu OS shell version 1/1", bg="black", fg="white", font="Helvetica, 20")
    shell_ver_show.place(x=1,y=1)

    shell_entry = tk.Entry(shell, bg="black", fg="white", width=100, font="helvetica, 17")
    shell_entry.config(bg="black", fg="white")
    shell_entry.place(x=1, y=50)

    shell_entry_done = tk.Button(shell, width=10, command=shell_commands)
    shell_entry_done.pack(pady=200)

def open_message_stachuos():
    stachuos_messages = tk.Toplevel()
    stachuos_messages.geometry("600x1000")
    stachuos_messages.config(bg="#757171")
    stachuos_messages.title("stachu os messages")

    stachuos_1message = tk.Label(stachuos_messages, text="""welcome to stachuOS user.
     Click this link to see what you can do in stachuOS V1""", bg="#757171", fg="white", font="Helvetica, 15")
    stachuos_1message.place(y=50, x=1)

    stachuos_1message_btnlinked = tk.Button(stachuos_messages, text="link", bg="#757171", command=show_features_stachuos)
    stachuos_1message_btnlinked.pack(pady=100)

    stachuos_2message = tk.Label(stachuos_messages, text="""stachu OS 2 is coming out on feb 23rd.
    Check out the new features in Stachu OS 2.""", bg="#757171", fg="white", font="Helvetica, 15")
    stachuos_2message.place(y=150, x=1)

    stachuos_2message_btnlinked = tk.Button(stachuos_messages, text="link", bg="#757171", command=show_features_stachuos2)
    stachuos_2message_btnlinked.pack(pady=1)

def open_messages():
    message_app = tk.Toplevel()
    message_app.geometry("1000x1000")
    message_app.config(bg="#757171")
    message_app.title("messages app")

    message_stachuos_txt = tk.Label(message_app, text="stachu os", font="Helvetica, 30")
    message_stachuos_btn = tk.Button(message_app, message_stachuos_txt, bg="#757171", command=open_message_stachuos)
    message_stachuos_btn.pack(padx=10, pady=50)

def start_menu():
    start = tk.Toplevel()
    start.geometry("1000x1000")
    start.config(bg="#757171")
    start.title("start menu")

    power_icon = PhotoImage(file="power_icon.png")
    power_btn = tk.Button(start, image=power_icon, bg="#757171", command=power_options)
    power_btn.image = power_icon
    power_btn.place(x=1, y=900)


    info_icon = PhotoImage(file="info_icon.png")
    info_btn = tk.Button(start, image=info_icon, bg="#757171", command=show_OS_info)
    info_btn.image = info_icon
    info_btn.place(x=110, y=900)

    shell_icon = PhotoImage(file="code_icon.png")
    shell_btn = tk.Button(start, image=shell_icon, bg="#757171", command=open_shell)
    shell_btn.image = shell_icon
    shell_btn.place(x=220, y=900)

    messages_icon = PhotoImage(file="messages_icon.png")
    messages_btn = tk.Button(start, image=messages_icon, bg="#757171", command=open_messages)
    messages_btn.image = messages_icon
    messages_btn.place(x=330, y=900)

def desktop():
    home = tk.Tk()
    home.attributes("-fullscreen", True)
    home.config(bg="#747171")

    start_icon = PhotoImage(file="start_icon.png")
    start_btn = tk.Button(home, image=start_icon, bg="#757171", command=start_menu)
    start_btn.image = start_icon
    start_btn.place(x=10, y=700)

def login_btn_pressed():
    entered_password = login_input_password.get()
    if entered_password == login_password:
        login.destroy()
        desktop()
    else:
        messagebox.showerror("Stachu OS", "password incorrect")

login = tk.Tk()
login.attributes("-fullscreen", True)
login.config(bg="#757171")

login_user = tk.Label(login, text=login_username, bg="#757171", anchor="center", font="helvetica, 50")
login_user.pack(pady=300)

login_input_password = tk.Entry(login, width=30, font="helvetica, 17")
login_input_password.pack(pady=100)

login_confirm_btn = tk.Button(login, text="login", width=10, command=login_btn_pressed)
login_confirm_btn.pack()


login.mainloop()