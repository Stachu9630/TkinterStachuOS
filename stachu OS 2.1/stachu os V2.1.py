import tkinter as tk
from tkinter import PhotoImage, messagebox



login_username = "admin"
login_password = "password"
lock_password = "password"



default_icon = True
red_icon = False
blue_icon = False
green_icon = False
yellow_icon = False

def set_red_icon():
    global red_icon, default_icon, blue_icon, green_icon, yellow_icon
    red_icon = True
    default_icon = False
    blue_icon = False
    green_icon = False
    yellow_icon = False

def set_blue_icon():
    global blue_icon, default_icon, red_icon, green_icon, yellow_icon
    blue_icon = True
    default_icon = False
    red_icon = False
    green_icon = False
    yellow_icon = False

def set_green_icon():
    global green_icon, default_icon, red_icon, blue_icon, yellow_icon
    green_icon = True
    default_icon = False
    red_icon = False
    blue_icon = False
    yellow_icon = False

def set_yellow_icon():
    global yellow_icon, default_icon, red_icon, blue_icon, green_icon
    yellow_icon = True
    default_icon = False
    red_icon = False
    blue_icon = False
    green_icon = False

default_wallpaper = True
red_wallpaper = False
blue_wallpaper = False
green_wallpaper = False
yellow_wallpaper = False

def set_red_wallpaper():
    global red_wallpaper, blue_wallpaper, green_wallpaper, yellow_wallpaper, default_wallpaper
    default_wallpaper = False
    red_wallpaper = True
    blue_wallpaper = False
    green_wallpaper = False
    yellow_wallpaper = False

def set_blue_wallpaper():
    global red_wallpaper, blue_wallpaper, green_wallpaper, yellow_wallpaper, default_wallpaper
    default_wallpaper = False
    red_wallpaper = False
    blue_wallpaper = True
    green_wallpaper = False
    yellow_wallpaper = False

def set_green_wallpaper():
    global red_wallpaper, blue_wallpaper, green_wallpaper, yellow_wallpaper, default_wallpaper
    default_wallpaper = False
    red_wallpaper = False
    blue_wallpaper = False
    green_wallpaper = True
    yellow_wallpaper = False

def set_yellow_wallpaper():
    global red_wallpaper, blue_wallpaper, green_wallpaper, yellow_wallpaper, default_wallpaper
    default_wallpaper = False
    red_wallpaper = False
    blue_wallpaper = False
    green_wallpaper = False
    yellow_wallpaper = True

def restart_desktop():
    home.destroy()
    desktop()

def restart_computer():
    login_screen()
    home.destroy()

def show_bios():
    global bios_screen
    bios_screen = tk.Toplevel()
    bios_screen.attributes("-fullscreen", True)
    bios_screen.config(bg="black")
    bios_screen.attributes("-topmost", True)

    bios_os = tk.Label(bios_screen, text="Stachu OS", bg="black", fg="white", font="Helvetica, 50")
    bios_os.pack()

    bios_underscore = tk.Label(bios_screen, text="_", bg="black", fg="white", font="Helvetica, 30")
    bios_underscore.place(x=1, y=100)
    bios_screen.after(3200, lambda: restart_computer())

def power_options_back_to_desktop():
    power.withdraw()

def power_options_unlock_btn_pressed():
    global entered_lock_password
    entered_lock_password = lock_entry.get()

    if entered_lock_password == lock_password:
        lock_screen.withdraw()
        home.deiconify()
    else:
        messagebox.showerror("stachu OS", "Password incorrect")
        lock_entry.focus()
        lock_entry.delete(0, tk.END)

def power_options_shutdown():
    shutdown_screen = tk.Toplevel()
    shutdown_screen.attributes("-fullscreen", True)
    shutdown_screen.config(bg="black")
    shutdown_screen.attributes("-topmost", True)

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
    restart_screen.attributes("-topmost", True)

    restart_screen_txt1 = tk.Label(restart_screen, text="stachu OS", bg="black", fg="white", font="Helvetica, 50")
    restart_screen_txt1.pack(pady=200)
    restart_screen_txt2 = tk.Label(restart_screen, text="restarting system...", bg="black", fg="white", font="Helvetica, 30")
    restart_screen_txt2.pack()
    restart_screen.after(2300, lambda:show_bios())

def power_options_sleep():
    sleep_screen = tk.Toplevel()
    sleep_screen.attributes("-fullscreen", True)
    sleep_screen.config(bg="black")
    sleep_screen.attributes("-topmost", True)

    sleep_screen_txt1 = tk.Label(sleep_screen, text="stachu OS", bg="black", fg="white", font="Helvetica, 50")
    sleep_screen_txt1.pack(pady=200)
    sleep_screen_txt2 = tk.Label(sleep_screen, text="press ALT F4 to return to desktop", bg="black", fg="#757171", font="Helvetica, 30")
    sleep_screen_txt2.pack()

def power_options_lock():
    global lock_screen
    global lock_entry

    lock_screen = tk.Toplevel()
    lock_screen.attributes("-fullscreen", True)
    lock_screen.config(bg="#757171")
    lock_screen.attributes("-topmost", True)

    lock_txt1 = tk.Label(lock_screen, text="stachu OS", bg="#757171", fg="white", font="Helvetica, 50")
    lock_txt1.pack(pady=70)
    
    lock_icon = PhotoImage(file="lock_icon.png")
    lock_img = tk.Label(lock_screen, image=lock_icon, bg="#757171")
    lock_img.image = lock_icon
    lock_img.pack(pady=50)

    lock_txt2 = tk.Label(lock_screen, text="Locked", bg="#757171", fg="white", font="Helvetica, 40")
    lock_txt2.pack()

    lock_entry = tk.Entry(lock_screen, text="enter password", font="Helvetica, 40")
    lock_entry.pack(pady=30)
    lock_entry.focus()

    lock_button = tk.Button(lock_screen, text="unlock computer", command=power_options_unlock_btn_pressed)
    lock_button.pack(pady=20)

    home.withdraw()
    lock_screen.deiconify()
    lock_entry.delete(0, tk.END)
    lock_entry.focus()

def power_options_signout():
    login_screen()
    home.destroy()
    
def power_options():
    global power
    power = tk.Toplevel()
    power.attributes("-fullscreen", True)
    power.config(bg="#757171")
    power.attributes("-topmost", True)

    shutdown_txt = tk.Label(power, text="shutdown", font="Helvetica, 30")
    shutdown_btn = tk.Button(power, shutdown_txt, bg="#757171", command=power_options_shutdown)
    shutdown_btn.pack(padx=10, pady=50)

    restart_txt = tk.Label(power, text="restart", font="Helvetica, 30")
    restart_btn = tk.Button(power, restart_txt, bg="#757171", command=power_options_restart)
    restart_btn.pack(padx=10, pady=50)

    sleep_txt = tk.Label(power, text="sleep", font="Helvetica, 30")
    sleep_btn = tk.Button(power, sleep_txt, bg="#757171", command=power_options_sleep)
    sleep_btn.pack(padx=10, pady=50)

    signout_txt = tk.Label(power, text="signout", font="Helvetica, 30")
    signout_btn = tk.Button(power, signout_txt, bg="#757171", command=power_options_signout)
    signout_btn.pack(padx=10, pady=50)

    lock_txt = tk.Label(power, text="lock", font="Helvetica, 30")
    lock_btn = tk.Button(power, lock_txt, bg="#757171", command=power_options_lock)
    lock_btn.pack(padx=10, pady=50)

    back_txt = tk.Label(power, text="back to desktop", font="Helvetica, 30")
    back_btn = tk.Button(power, back_txt, bg="#757171", command=power_options_back_to_desktop)
    back_btn.pack(padx=10, pady=100)

def show_OS_info():
    os_info = tk.Toplevel()
    os_info.geometry("1000x1000")
    os_info.config(bg="#757171")
    os_info.title("Stachu OS info")
    os_info.attributes("-topmost", True)
    
    info_OS_name = tk.Label(os_info, text="Stachu OS", bg="#757171", fg="white", font="Helvetica, 50")
    info_OS_name.pack(pady=10)

    info_OS_ver = tk.Label(os_info, text="Stachu OS 2.1", bg="#757171", fg="white", font="Helvetica, 30")
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
        help_shell.attributes("-topmost", True)

        shell_help_txt1 = tk.Label(help_shell, text="shutdown qck : forces quick shutdown", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt1.place(x=10, y=50)

        shell_help_txt2 = tk.Label(help_shell, text="sys.info : displays system information", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt2.place(x=10, y=100)

        shell_help_txt3 = tk.Label(help_shell, text="reboot : reboots computer", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt3.place(x=10, y=150)

        shell_help_txt4 = tk.Label(help_shell, text="sys.reboot : reboots stachuOS", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt4.place(x=10, y=200)

        shell_help_txt5 = tk.Label(help_shell, text="user.change : change username", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt5.place(x=10, y=250)

        shell_help_txt6 = tk.Label(help_shell, text="pass.change : change password", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt6.place(x=10, y=300)

    elif shell_request == "shutdown qck":
        exit()

    elif shell_request == "sys.info":
        sys_info_shell = tk.Toplevel()
        sys_info_shell.geometry("1000x1000")
        sys_info_shell.config(bg="black")
        sys_info_shell.title("<shell> <sys><info>")
        sys_info_shell.attributes("-topmost", True)

        sys_info_shell_txt1 = tk.Label(sys_info_shell, text="proccesor : intel i7-7700", bg="black", fg="white", font="Helvetica, 15")
        sys_info_shell_txt1.place(x=1, y=50)
        sys_info_shell_txt2 = tk.Label(sys_info_shell, text="graphics card : intel i7-7700(integrated)", bg="black", fg="white", font="Helvetica, 15")
        sys_info_shell_txt2.place(x=1, y=100)
        sys_info_shell_txt3 = tk.Label(sys_info_shell, text="RAM : 8GB DDR4", bg="black", fg="white", font="Helvetica, 15")
        sys_info_shell_txt3.place(x=1, y=150)
        sys_info_shell_txt4 = tk.Label(sys_info_shell, text="disk(SSD/SATA) : kingston 220GB ", bg="black", fg="white", font="Helvetica, 15")
        sys_info_shell_txt4.place(x=1, y=200)

    elif shell_request == "reboot":
        power_options_restart()

    elif shell_request == "sys.reboot":
        restart_desktop()

    elif shell_request == "user.change":
        change_login_username()

    elif shell_request == "pass.change":
        change_login_password()

    else:
        messagebox.showerror("stachu OS", "no command found")

def open_shell():
    global shell_entry

    shell = tk.Toplevel()
    shell.geometry("1000x1000")
    shell.config(bg="black")
    shell.title("<shell>")
    shell.attributes("-topmost", True)
    #shell ver 1st number is stachu os ver and second number is shell version
    shell_ver_show = tk.Label(shell, text="stachu OS shell version 2/2", bg="black", fg="white", font="Helvetica, 20")
    shell_ver_show.place(x=1,y=1)

    shell_entry = tk.Entry(shell, bg="black", fg="white", width=100, font="helvetica, 17")
    shell_entry.config(bg="black", fg="white")
    shell_entry.place(x=1, y=50)

    shell_entry_done = tk.Button(shell, width=10, command=shell_commands)
    shell_entry_done.pack(pady=200)

def show_features_stachuos2():
    features_list = tk.Toplevel()
    features_list.geometry("1000x1300")
    features_list.config(bg="#757171")
    features_list.title("Stachu OS 2 features")
    features_list.attributes("-topmost", True)
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

def open_message_stachuos():
    stachuos_messages = tk.Toplevel()
    stachuos_messages.geometry("600x1000")
    stachuos_messages.config(bg="#757171")
    stachuos_messages.title("stachu os messages")
    stachuos_messages.attributes("-topmost", True)

    stachuos_1message = tk.Label(stachuos_messages, text="""thank you for using stachu OS :)""", bg="#757171", fg="white", font="Helvetica, 15")
    stachuos_1message.place(y=50, x=1)

    stachuos_2message = tk.Label(stachuos_messages, text="""stachu OS 2 is coming out on feb 23rd.
        Check out the new features in Stachu OS 2.""", bg="#757171", fg="white", font="Helvetica, 15")
    stachuos_2message.place(y=150, x=1)

    stachuos_2message_btnlinked = tk.Button(stachuos_messages, text="link", bg="#757171",command=show_features_stachuos2)
    stachuos_2message_btnlinked.pack(pady=240)

def open_messages():
    message_app = tk.Toplevel()
    message_app.geometry("1000x1000")
    message_app.config(bg="#757171")
    message_app.title("messages app")
    message_app.attributes("-topmost", True)

    message_stachuos_txt = tk.Label(message_app, text="stachu os", font="Helvetica, 30")
    message_stachuos_btn = tk.Button(message_app, message_stachuos_txt, bg="#757171", command=open_message_stachuos)
    message_stachuos_btn.pack(padx=10, pady=50)

#V2 features start here

def change_account_username(entry_widget, label_widget):
    global login_username
    changed_username = entry_widget.get()
    if len(changed_username) == 0:
        messagebox.showerror("stachu OS", "username change was unsuccessful")
        account_username.withdraw()
        return
    elif len(changed_username) > 20:
        messagebox.showerror("stachu OS", "username change was unsuccessful")
        account_username.withdraw()
        return

    login_username = changed_username
    messagebox.showinfo("Stachu OS", "username successfully changed")
    account_username.withdraw()

def change_account_password(entry_widget, label_widget):
    global login_password, lock_password
    changed_password = entry_widget.get()
    login_password = changed_password
    lock_password = changed_password
    messagebox.showinfo("Stachu OS", "password successfully changed")
    account_password.withdraw()

def change_login_username():
    global account_username
    account_username = tk.Toplevel()
    account_username.geometry("500x500")
    account_username.config(bg="#757171")
    account_username.title("account settings")
    account_username.attributes("-topmost", True)

    current_account_username = tk.Label(account_username, text=f"Current account name: {login_username}",bg="#757171", font="Helvetica, 15")
    current_account_username.place(y=20, x=1)

    new_account_username = tk.Entry(account_username, bg="#757171", font="Helvetica, 15")
    new_account_username.place(y=70, x=1)

    save_new_username = tk.Button(account_username, text="save changes", width=20, command=lambda: change_account_username(new_account_username, current_account_username))
    save_new_username.place(y=120, x=1)

def change_login_password():
    global account_password
    account_password = tk.Toplevel()
    account_password.geometry("500x500")
    account_password.config(bg="#757171")
    account_password.title("account settings")
    account_password.attributes("-topmost", True)

    current_account_password = tk.Label(account_password, text=f"Current account password: {login_password}",bg="#757171", font="Helvetica, 15")
    current_account_password.place(y=20, x=1)

    new_account_password = tk.Entry(account_password, bg="#757171", font="Helvetica, 15")
    new_account_password.place(y=70, x=1)

    save_new_password = tk.Button(account_password, text="save changes", width=20, command=lambda: change_account_password(new_account_password, current_account_password))
    save_new_password.place(y=120, x=1)

def change_login_icon():
    global account_icon
    account_icon = tk.Toplevel()
    account_icon.geometry("500x500")
    account_icon.config(bg="#757171")
    account_icon.title("account settings")
    account_icon.attributes("-topmost", True)

    account_icon_txt = tk.Label(account_icon, text="choose a icon colour", bg="#757171", font="Helvetica, 25")
    account_icon_txt.place(y=10, x=1)

    account_red_icon = PhotoImage(file="account_icon_red.png")
    account_btn = tk.Button(account_icon, image=account_red_icon, bg="#757171", command=set_red_icon)
    account_btn.image = account_red_icon
    account_btn.place(x=1, y=110)

    account_blue_icon = PhotoImage(file="account_icon_dark_blue.png")
    account_blue_btn = tk.Button(account_icon, image=account_blue_icon, bg="#757171", command=set_blue_icon)
    account_blue_btn.image = account_blue_icon
    account_blue_btn.place(x=111, y=110)

    account_green_icon = PhotoImage(file="account_icon_green.png")
    account_green_btn = tk.Button(account_icon, image=account_green_icon, bg="#757171", command=set_green_icon)
    account_green_btn.image = account_green_icon
    account_green_btn.place(x=221, y=110)

    account_yellow_icon = PhotoImage(file="account_icon_yellow.png")
    account_yellow_btn = tk.Button(account_icon, image=account_yellow_icon, bg="#757171", command=set_yellow_icon)
    account_yellow_btn.image = account_yellow_icon
    account_yellow_btn.place(x=331, y=110)

def change_wallpaper():
    global wallpaper
    account_wallpaper = tk.Toplevel()
    account_wallpaper.geometry("500x500")
    account_wallpaper.config(bg="#757171")
    account_wallpaper.title("account settings")
    account_wallpaper.attributes("-topmost", True)

    account_wallpaper_txt = tk.Label(account_wallpaper, text="choose a wallpaper colour", bg="#757171", font="Helvetica, 25")
    account_wallpaper_txt.place(y=10, x=1)

    red_wallpaper_txt = tk.Label(account_wallpaper, text="red", font="Helvetica, 30")
    red_wallpaper_btn = tk.Button(account_wallpaper, red_wallpaper_txt, bg="#757171", fg="red", command=set_red_wallpaper)
    red_wallpaper_btn.place(x=1, y=100)

    blue_wallpaper_txt = tk.Label(account_wallpaper, text="blue", font="Helvetica, 30")
    blue_wallpaper_btn = tk.Button(account_wallpaper, blue_wallpaper_txt, bg="#757171", command=set_blue_wallpaper)
    blue_wallpaper_btn.place(x=1, y=180)

    green_wallpaper_txt = tk.Label(account_wallpaper, text="green", font="Helvetica, 30")
    green_wallpaper_btn = tk.Button(account_wallpaper, green_wallpaper_txt, bg="#757171", command=set_green_wallpaper)
    green_wallpaper_btn.place(x=1, y=260)

    yellow_wallpaper_txt = tk.Label(account_wallpaper, text="yellow", font="Helvetica, 30")
    yellow_wallpaper_btn = tk.Button(account_wallpaper, yellow_wallpaper_txt, bg="#757171", command=set_yellow_wallpaper)
    yellow_wallpaper_btn.place(x=1, y=340)

    wallpaper_btn = tk.Button(account_wallpaper, text="restart desktop", command=restart_desktop, font="Helvetica, 25")
    wallpaper_btn.place(x=1, y=420)

def account_settings_show():
    account_settings = tk.Toplevel()
    account_settings.geometry("1000x1000")
    account_settings.config(bg="#757171")
    account_settings.title("account settings")
    account_settings.attributes("-topmost", True)

    changeuser_txt = tk.Label(account_settings, text="change username", font="Helvetica, 30")
    changeuser_btn = tk.Button(account_settings, changeuser_txt, bg="#757171", command=change_login_username)
    changeuser_btn.pack(padx=10, pady=50)

    changepass_txt = tk.Label(account_settings, text="change password", font="Helvetica, 30")
    changepass_btn = tk.Button(account_settings, changepass_txt, bg="#757171", command=change_login_password)
    changepass_btn.pack(padx=10, pady=50)

    changeicon_txt = tk.Label(account_settings, text="change account icon", font="Helvetica, 30")
    changeicon_btn = tk.Button(account_settings, changeicon_txt, bg="#757171", command=change_login_icon)
    changeicon_btn.pack(padx=10, pady=50)

    changewallpaper_txt = tk.Label(account_settings, text="change desktop wallpaper", font="Helvetica, 30")
    changewallpaper_btn = tk.Button(account_settings, changewallpaper_txt, bg="#757171", command=change_wallpaper)
    changewallpaper_btn.pack(padx=10, pady=50)

#V2 features end here

def start_menu():
    global start
    start = tk.Toplevel()
    start.geometry("1000x1000")
    start.config(bg="#757171")
    start.title("start menu")
    start.attributes("-topmost", True)

    greeting_startmenu = tk.Label(start, text="hello " + login_username, bg="#757171", font="helvetica, 35")
    greeting_startmenu.place(x=115, y=1)

    if default_icon == True:
        account_icon = PhotoImage(file="account_icon.png")
        account_btn = tk.Button(start, image=account_icon, bg="#757171", command=account_settings_show)
        account_btn.image = account_icon
        account_btn.place(x=1, y=1)

    elif red_icon == True:
        account_icon = PhotoImage(file="account_icon_red.png")
        account_btn = tk.Button(start, image=account_icon, bg="#757171", command=account_settings_show)
        account_btn.image = account_icon
        account_btn.place(x=1, y=1)

    elif blue_icon == True:
        account_icon = PhotoImage(file="account_icon_dark_blue.png")
        account_btn = tk.Button(start, image=account_icon, bg="#757171", command=account_settings_show)
        account_btn.image = account_icon
        account_btn.place(x=1, y=1)

    elif green_icon == True:
        account_icon = PhotoImage(file="account_icon_green.png")
        account_btn = tk.Button(start, image=account_icon, bg="#757171", command=account_settings_show)
        account_btn.image = account_icon
        account_btn.place(x=1, y=1)

    elif yellow_icon == True:
        account_icon = PhotoImage(file="account_icon_yellow.png")
        account_btn = tk.Button(start, image=account_icon, bg="#757171", command=account_settings_show)
        account_btn.image = account_icon
        account_btn.place(x=1, y=1)


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

    #calculator_icon = PhotoImage(file="C:/Users/stach/Desktop/Stachu OS/icons/calculator_icon.png")
    #calculator_btn = tk.Button(start, image=calculator_icon, bg="#757171", command=open_calculator)
    #calculator_btn.image = calculator_icon
    #calculator_btn.place(x=440, y=900)

def desktop():
    global home
    home = tk.Tk()
    home.attributes("-fullscreen", True)

    if default_wallpaper == True:
        home.config(bg="#757171")
    elif red_wallpaper == True:
        home.config(bg="#aa0f0f")
    elif blue_wallpaper == True:
        home.config(bg="#14afe6")
    elif green_wallpaper == True:
        home.config(bg="#25770e")
    elif yellow_wallpaper == True:
        home.config(bg="#dad014")

    start_icon = PhotoImage(file="start_icon.png")
    start_btn = tk.Button(home, image=start_icon, bg="#757171", command=start_menu)
    start_btn.image = start_icon
    start_btn.place(x=10, y=1330)

def login_btn_pressed():
    entered_password = login_input_password.get()
    if entered_password == login_password:
        login_input_password.delete(0, tk.END)
        login.destroy()
        desktop()
    else:
        messagebox.showerror("Stachu OS", "Password incorrect")

def login_screen():
    global login
    global login_input_password


    login = tk.Tk()
    login.attributes("-fullscreen", True)
    login.config(bg="#757171")

    login_user = tk.Label(login, text=login_username, bg="#757171", anchor="center", font="helvetica, 50")
    login_user.pack(pady=300)

    login_input_password = tk.Entry(login, width=30, font="helvetica, 17")
    login_input_password.pack(pady=100)

    login_confirm_btn = tk.Button(login, text="login", width=10, command=login_btn_pressed)
    login_confirm_btn.pack()

root = tk.Tk()
root.attributes("-fullscreen", True)
root.config(bg="#757171")
root.after(1, lambda: (login_screen(), root.destroy()))
root.mainloop()


