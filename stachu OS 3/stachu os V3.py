import tkinter as tk
from tkinter import PhotoImage, messagebox, colorchooser
import time

login_username = "admin"
login_password = "password"
lock_password = "password"
legacy_login = False

def apply_timeout():
    global SLEEP_TIMEOUT
    timeout = selected_timeout_option.get()
    if timeout == "10,000":
        SLEEP_TIMEOUT = 10000
        sys_config_sleep_timeout.destroy()

    elif timeout == "20,000":
        SLEEP_TIMEOUT = 20000
        sys_config_sleep_timeout.destroy()

    elif timeout == "30,000":
        SLEEP_TIMEOUT = 30000
        sys_config_sleep_timeout.destroy()

    elif timeout == "60,000":
        SLEEP_TIMEOUT = 30000
        sys_config_sleep_timeout.destroy()
    elif timeout == "never":
        SLEEP_TIMEOUT = None
        sys_config_sleep_timeout.destroy()
        messagebox.showerror("Terminal", "Internal error")


default_icon = True
red_icon = False
lightblue_icon = False
darkblue_icon = False
green_icon = False
yellow_icon = False
pink_icon = False
orange_icon = False
purple_icon = False

def change_background_colour():
    global desktop_background_colour

    new_colour = colorchooser.askcolor(title="Choose a background colour")[1]

    if new_colour:
        desktop_background_colour = new_colour
        messagebox.showinfo("Notification service", "signout or restart to apply changes")

def set_red_icon():
    global red_icon, default_icon, lightblue_icon, darkblue_icon, green_icon, yellow_icon, pink_icon, orange_icon, purple_icon
    default_icon = False
    red_icon = True
    lightblue_icon = False
    darkblue_icon = False
    green_icon = False
    yellow_icon = False
    pink_icon = False
    orange_icon = False
    purple_icon = False

def set_lightblue_icon():
    global red_icon, default_icon, lightblue_icon, darkblue_icon, green_icon, yellow_icon, pink_icon, orange_icon, purple_icon
    default_icon = False
    red_icon = False
    lightblue_icon = True
    darkblue_icon = False
    green_icon = False
    yellow_icon = False
    pink_icon = False
    orange_icon = False
    purple_icon = False

def set_darkblue_icon():
    global red_icon, default_icon, lightblue_icon, darkblue_icon, green_icon, yellow_icon, pink_icon, orange_icon, purple_icon
    default_icon = False
    red_icon = False
    lightblue_icon = False
    darkblue_icon = True
    green_icon = False
    yellow_icon = False
    pink_icon = False
    orange_icon = False
    purple_icon = False

def set_green_icon():
    global red_icon, default_icon, lightblue_icon, darkblue_icon, green_icon, yellow_icon, pink_icon, orange_icon, purple_icon
    default_icon = False
    red_icon = False
    lightblue_icon = False
    darkblue_icon = False
    green_icon = True
    yellow_icon = False
    pink_icon = False
    orange_icon = False
    purple_icon = False

def set_yellow_icon():
    global red_icon, default_icon, lightblue_icon, darkblue_icon, green_icon, yellow_icon, pink_icon, orange_icon, purple_icon
    default_icon = False
    red_icon = False
    lightblue_icon = False
    darkblue_icon = False
    green_icon = False
    yellow_icon = True
    pink_icon = False
    orange_icon = False
    purple_icon = False

def set_pink_icon():
    global red_icon, default_icon, lightblue_icon, darkblue_icon, green_icon, yellow_icon, pink_icon, orange_icon, purple_icon
    default_icon = False
    red_icon = False
    lightblue_icon = False
    darkblue_icon = False
    green_icon = False
    yellow_icon = False
    pink_icon = True
    orange_icon = False
    purple_icon = False

def set_orange_icon():
    global red_icon, default_icon, lightblue_icon, darkblue_icon, green_icon, yellow_icon, pink_icon, orange_icon, purple_icon
    default_icon = False
    red_icon = False
    lightblue_icon = False
    darkblue_icon = False
    green_icon = False
    yellow_icon = False
    pink_icon = False
    orange_icon = True
    purple_icon = False

def set_purple_icon():
    global red_icon, default_icon, lightblue_icon, darkblue_icon, green_icon, yellow_icon, pink_icon, orange_icon, purple_icon
    default_icon = False
    red_icon = False
    lightblue_icon = False
    darkblue_icon = False
    green_icon = False
    yellow_icon = False
    pink_icon = False
    orange_icon = False
    purple_icon = True


def update_clock(label):
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_clock, label)


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
    bios_os.pack(pady=200)

    bios_status = tk.Label(bios_screen, text="powered by tkinter", bg="black", fg="white", font="Helvetica, 30")
    bios_status.pack(pady=450)


    bios_screen.after(4700, lambda: restart_computer())

def wake_up(sleep_screen):
    sleep_screen.destroy()


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

    shutdown_screen_txt1 = tk.Label(shutdown_screen, text="Stachu OS", bg="black", fg="white", font="Helvetica, 50")
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

    restart_screen_txt1 = tk.Label(restart_screen, text="Stachu OS", bg="black", fg="white", font="Helvetica, 50")
    restart_screen_txt1.pack(pady=200)
    restart_screen_txt2 = tk.Label(restart_screen, text="restarting system...", bg="black", fg="white", font="Helvetica, 30")
    restart_screen_txt2.pack()
    restart_screen.after(2300, lambda:show_bios())

def power_options_sleep():
    sleep_screen = tk.Toplevel()
    sleep_screen.attributes("-fullscreen", True)
    sleep_screen.config(bg="black")
    sleep_screen.attributes("-topmost", True)

    sleep_screen.bind("<Key>", lambda event: wake_up(sleep_screen))
    sleep_screen.bind("<Motion>", lambda event: wake_up(sleep_screen))
    sleep_screen.bind("<Button>", lambda event: wake_up(sleep_screen))

def power_options_lock():
    global lock_screen
    global lock_entry

    lock_screen = tk.Toplevel()
    lock_screen.attributes("-fullscreen", True)
    lock_screen.config(bg="#757171")
    lock_screen.attributes("-topmost", True)

    lock_txt1 = tk.Label(lock_screen, text="Stachu OS", bg="#757171", fg="white", font="Helvetica, 50")
    lock_txt1.pack(pady=70)
    
    lock_icon = PhotoImage(file="C:/Users/stach/Desktop/Stachu OS/icons/lock_icon.png")
    lock_img = tk.Label(lock_screen, image=lock_icon, bg="#757171")
    lock_img.image = lock_icon
    lock_img.pack(pady=50)

    lock_txt2 = tk.Label(lock_screen, text="Locked", bg="#757171", fg="white", font="Helvetica, 40")
    lock_txt2.pack()

    lock_entry = tk.Entry(lock_screen, font="Helvetica, 40", show="*")
    lock_entry.pack(pady=30)
    lock_entry.focus()

    lock_show_password_btn = tk.Button(lock_screen, text="show/hide password", width=15, bg="#757171", command=show_hide_password_lock)
    lock_show_password_btn.pack(pady=20)

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


def Terminal_commands():
    global legacy_login, sys_config_sleep_timeout, selected_timeout_option
    shell_request = shell_entry.get()
    shell_entry.delete(0, tk.END)
    if shell_request == "help":
        help_shell = tk.Toplevel()
        help_shell.geometry("1000x1000")
        help_shell.config(bg="#757171")
        help_shell.attributes("-topmost", True)

        shell_help_txt1 = tk.Label(help_shell, text="shutdown qck : forces quick shutdown", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt1.place(x=10, y=50)

        shell_help_txt2 = tk.Label(help_shell, text="sys.info : displays system information", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt2.place(x=10, y=100)

        shell_help_txt3 = tk.Label(help_shell, text="reboot : reboots computer", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt3.place(x=10, y=150)

        shell_help_txt4 = tk.Label(help_shell, text="sys.reboot : reboots stachuOS", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt4.place(x=10, y=200)

        shell_help_txt5 = tk.Label(help_shell, text="legacyloginTrue : enables legacy login", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt5.place(x=10, y=250)

        shell_help_txt6 = tk.Label(help_shell, text="legacyloginFalse : disables legacy login", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt6.place(x=10, y=300)

        shell_help_txt7 = tk.Label(help_shell, text="changewallpapercolour", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt7.place(x=10, y=350)

        #shell_help_txt8 = tk.Label(help_shell, text="changewallpapercolourHEX", bg="#757171", fg="white", font="Helvetica, 15")
        #shell_help_txt8.place(x=10, y=400)

        #shell_help_txt9 = tk.Label(help_shell, text="changewallpapercolourRGB", bg="#757171", fg="white", font="Helvetica, 15")
        #shell_help_txt9.place(x=10, y=450)

        shell_help_txt10 = tk.Label(help_shell, text="", bg="#757171", fg="white", font="Helvetica, 15")
        shell_help_txt10.place(x=10, y=500)

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
        sys_info_shell_txt5 = tk.Label(sys_info_shell, text="System Info", bg="black", fg="white", font="Helvetica, 15")
        sys_info_shell_txt5.place(x=1, y=300)
        sys_info_shell_txt6 = tk.Label(sys_info_shell, text="Stachu OS 3", bg="black", fg="white", font="Helvetica, 15")
        sys_info_shell_txt6.place(x=1, y=350)
        sys_info_shell_txt7 = tk.Label(sys_info_shell, text="Desktop version : UI version 2", bg="black", fg="white", font="Helvetica, 15")
        sys_info_shell_txt7.place(x=1, y=400)
        sys_info_shell_txt8 = tk.Label(sys_info_shell, text="Login version : UI version 2", bg="black", fg="white", font="Helvetica, 15")
        sys_info_shell_txt8.place(x=1, y=450)
        sys_info_shell_txt10 = tk.Label(sys_info_shell, text="Terminal version : UI version 2, commands version 3", bg="black", fg="white", font="Helvetica, 15")
        sys_info_shell_txt10.place(x=1, y=500)
        sys_info_shell_txt11 = tk.Label(sys_info_shell, text="", bg="black", fg="white", font="Helvetica, 15")
        sys_info_shell_txt11.place(x=1, y=550)

    elif shell_request == "reboot":
        power_options_restart()

    elif shell_request == "sys.reboot":
        restart_desktop()

    elif shell_request == "legacyloginTrue":
        legacy_login = True
        messagebox.showinfo("Terminal", "legacy login has been enabled")

    elif shell_request == "legacyloginFalse":
        legacy_login = False
        messagebox.showinfo("Terminal", "legacy login has been disabled")

    elif shell_request == "changewallpapercolour":
        change_background_colour()

    elif shell_request == "changewallpapercolourHEX":
        HEXcolourwindow = tk.Tk()
        HEXcolourwindow.config(bg="black")
        HEXcolourwindow.geometry("300x300")

        colour_entry_HEX = tk.Entry(HEXcolourwindow)
        colour_entry_HEX.pack(pady=5)

        colour_apply_HEX = tk.Button(HEXcolourwindow, text="apply")
        colour_apply_HEX.pack(pady=2)

    elif shell_request == "sys.sleepTimeout":
        sys_config_sleep_timeout = tk.Tk()
        sys_config_sleep_timeout.geometry("300x300")
        sys_config_sleep_timeout.config(bg="black")
        sys_config_sleep_timeout.title("Internal settings")
        sys_config_sleep_timeout.attributes("-topmost", True)

        timeout_options = ["10,000", "20,000", "30,000", "60,000", "never"]

        selected_timeout_option = tk.StringVar()
        selected_timeout_option.set(timeout_options[0])


        dropdown = tk.OptionMenu(sys_config_sleep_timeout, selected_timeout_option, *timeout_options)
        dropdown.pack(pady=20)

        apply_button = tk.Button(sys_config_sleep_timeout, text="Apply", command=apply_timeout, bg="black", fg="white")
        apply_button.pack(pady=10)



    elif shell_request == "":
        messagebox.showerror("Terminal", "no command entered")

    else:
        messagebox.showerror("Terminal", "unknown command : " + shell_request)

def open_shell():
    global shell_entry

    Terminal = tk.Toplevel()
    Terminal.geometry("1000x1000")
    Terminal.config(bg="black")
    Terminal.title("Terminal")
    Terminal.attributes("-topmost", True)
    #shell ver 1st number is stachu os ver and second number is shell version
    shell_ver_show = tk.Label(Terminal, text="stachu OS Terminal version 3/3", bg="black", fg="white", font="Helvetica, 20")
    shell_ver_show.place(x=1,y=1)

    shell_entry = tk.Entry(Terminal, bg="black", fg="white", width=100, font="helvetica, 17")
    shell_entry.config(bg="black", fg="white")
    shell_entry.place(x=1, y=50)

    shell_entry_done = tk.Button(Terminal, text="execute", width=10, command=Terminal_commands)
    shell_entry_done.pack(pady=200)



def change_account_username(entry_widget, label_widget):
    global login_username
    changed_username = entry_widget.get()
    if len(changed_username) == 0:
        messagebox.showerror("stachu OS", "username change was unsuccessful : no username enteredpass")
        return
    elif len(changed_username) > 20:
        messagebox.showerror("stachu OS", "username change was unsuccessful : username too long")
        return

    login_username = changed_username
    messagebox.showinfo("Stachu OS", "username successfully changed. Your new username is :" + login_username)

def change_account_password(entry_widget, label_widget):
    global login_password, lock_password
    changed_password = entry_widget.get()
    login_password = changed_password
    lock_password = changed_password
    messagebox.showinfo("Stachu OS", "password successfully changed")

def set_legacy_login():
    global legacy_login
    legacy_login = not legacy_login

    legacy_login_txt.config(text=f"Use legacy login screen : {legacy_login}")
    legacy_login_toggle_btn.config(text="Disable" if legacy_login else "Enable")

def settings_personalization():
    global personalization_settings, legacy_login_txt, legacy_login_toggle_btn
    personalization_settings = tk.Toplevel()
    personalization_settings.geometry("1000x1000")
    personalization_settings.config(bg="#757171")
    personalization_settings.title("personalization settings")
    personalization_settings.attributes("-topmost", True)


    account_wallpaper_txt = tk.Label(personalization_settings, text="change wallpaper colour", bg="#757171", font="Helvetica, 25")
    account_wallpaper_btn = tk.Button(personalization_settings, account_wallpaper_txt, bg="#757171")
    account_wallpaper_btn.place(y=10, x=1)

    change_wallpaper_btn = tk.Button(personalization_settings, text="Change", bg="#757171", font="Helvetica, 30", command=change_background_colour)
    change_wallpaper_btn.place(x=1, y=100)

    account_icon_txt = tk.Label(personalization_settings, text="choose a icon colour", bg="#757171", font="Helvetica, 25")
    account_icon_txt.place(y=300, x=1)

    account_red_icon = PhotoImage(file="C:/Users/stach/Desktop/Stachu OS/icons/account_icons/account_icon_red.png")
    account_btn = tk.Button(personalization_settings, image=account_red_icon, bg="#757171", command=set_red_icon)
    account_btn.image = account_red_icon
    account_btn.place(x=1, y=350)

    account_lightblue_icon = PhotoImage(file="C:/Users/stach/Desktop/Stachu OS/icons/account_icons/account_icon_light_blue.png")
    account_lightblue_btn = tk.Button(personalization_settings, image=account_lightblue_icon, bg="#757171", command=set_lightblue_icon)
    account_lightblue_btn.image = account_lightblue_icon
    account_lightblue_btn.place(x=111, y=350)

    account_darkblue_icon = PhotoImage(file="C:/Users/stach/Desktop/Stachu OS/icons/account_icons/account_icon_dark_blue.png")
    account_darkblue_btn = tk.Button(personalization_settings, image=account_darkblue_icon, bg="#757171", command=set_darkblue_icon)
    account_darkblue_btn.image = account_darkblue_icon
    account_darkblue_btn.place(x=221, y=350)

    account_green_icon = PhotoImage(file="C:/Users/stach/Desktop/Stachu OS/icons/account_icons/account_icon_green.png")
    account_green_btn = tk.Button(personalization_settings, image=account_green_icon, bg="#757171", command=set_green_icon)
    account_green_btn.image = account_green_icon
    account_green_btn.place(x=331, y=350)

    account_yellow_icon = PhotoImage(file="C:/Users/stach/Desktop/Stachu OS/icons/account_icons/account_icon_yellow.png")
    account_yellow_btn = tk.Button(personalization_settings, image=account_yellow_icon, bg="#757171", command=set_yellow_icon)
    account_yellow_btn.image = account_yellow_icon
    account_yellow_btn.place(x=441, y=350)

    account_pink_icon = PhotoImage(file="C:/Users/stach/Desktop/Stachu OS/icons/account_icons/account_icon_pink.png")
    account_pink_btn = tk.Button(personalization_settings, image=account_pink_icon, bg="#757171", command=set_pink_icon)
    account_pink_btn.image = account_pink_icon
    account_pink_btn.place(x=551, y=350)

    account_orange_icon = PhotoImage(file="C:/Users/stach/Desktop/Stachu OS/icons/account_icons/account_icon_orange.png")
    account_orange_btn = tk.Button(personalization_settings, image=account_orange_icon, bg="#757171", command=set_orange_icon)
    account_orange_btn.image = account_orange_icon
    account_orange_btn.place(x=661, y=350)

    account_purple_icon = PhotoImage(file="C:/Users/stach/Desktop/Stachu OS/icons/account_icons/account_icon_purple.png")
    account_purple_btn = tk.Button(personalization_settings, image=account_purple_icon, bg="#757171", command=set_purple_icon)
    account_purple_btn.image = account_purple_icon
    account_purple_btn.place(x=771, y=350)


    legacy_login_txt = tk.Label(personalization_settings, text=f"Use legacy login screen : {legacy_login}", bg="#757171", font="Helvetica, 25")
    legacy_login_txt.place(x=1, y=500)

    legacy_login_toggle_btn = tk.Button(personalization_settings, text="Enable" if not legacy_login else "Disable", bg="#757171", font="Helvetica, 30", command=set_legacy_login)
    legacy_login_toggle_btn.place(x=1, y=550)

def settings_connection():
    connection_settings = tk.Toplevel()
    connection_settings.geometry("1000x1000")
    connection_settings.config(bg="#757171")
    connection_settings.title("connection settings")
    connection_settings.attributes("-topmost", True)

def settings_account():
    account_settings = tk.Toplevel()
    account_settings.geometry("1000x1000")
    account_settings.config(bg="#757171")
    account_settings.title("account settings")
    account_settings.attributes("-topmost", True)

    current_account_username = tk.Label(account_settings, text=f"Current account name: {login_username}",bg="#757171", font="Helvetica, 25")
    current_account_username.place(y=20, x=1)
    new_account_username = tk.Entry(account_settings, bg="#757171", font="Helvetica, 25")
    new_account_username.place(y=70, x=1)
    save_new_username = tk.Button(account_settings, text="change username", width=20, command=lambda: change_account_username(new_account_username, current_account_username))
    save_new_username.place(y=120, x=1)



    current_account_password = tk.Label(account_settings, text=f"Current account password: {login_password}",bg="#757171", font="Helvetica, 25")
    current_account_password.place(y=220, x=1)
    new_account_password = tk.Entry(account_settings, bg="#757171", font="Helvetica, 25")
    new_account_password.place(y=270, x=1)
    save_new_password = tk.Button(account_settings, text="change password", width=20, command=lambda: change_account_password(new_account_password, current_account_password))
    save_new_password.place(y=320, x=1)

def settings_OS_info():
    os_info_settings = tk.Toplevel()
    os_info_settings.geometry("1000x1000")
    os_info_settings.config(bg="#757171")
    os_info_settings.title("Stachu OS info")
    os_info_settings.attributes("-topmost", True)

    info_OS_name = tk.Label(os_info_settings, text="Stachu OS", bg="#757171", fg="black", font="Helvetica, 50")
    info_OS_name.pack(pady=10)

    info_OS_ver = tk.Label(os_info_settings, text="Stachu OS 3", bg="#757171", fg="black", font="Helvetica, 30")
    info_OS_ver.place(x=10, y=200)

    info_OS_bit = tk.Label(os_info_settings, text="64 bit version", bg="#757171", fg="black", font="Helvetica, 30")
    info_OS_bit.place(x=10, y=300)

    info_OS_build = tk.Label(os_info_settings, text=" built in 3/25", bg="#757171", fg="black", font="Helvetica, 30")
    info_OS_build.place(x=10, y=400)

    info_OS_dev = tk.Label(os_info_settings, text="developed by the stachu project", bg="#757171", fg="black", font="Helvetica, 30")
    info_OS_dev.place(x=10, y=500)

def open_settings():
    settings = tk.Toplevel()
    settings.geometry("1000x1000")
    settings.config(bg="#757171")
    settings.title("settings")
    settings.attributes("-topmost", True)

    personalization_txt = tk.Label(settings, text="personalization", font="Helvetica, 30")
    personalization_btn = tk.Button(settings, personalization_txt, bg="#757171", command=settings_personalization)
    personalization_btn.place(x=1, y=50)

    #connections_txt = tk.Label(settings, text="connections", font="Helvetica, 30")
    #connections_btn = tk.Button(settings, connections_txt, bg="#757171", command=settings_connection)
    #connections_btn.place(x=1, y=150)

    account_txt = tk.Label(settings, text="account", font="Helvetica, 30")
    account_btn = tk.Button(settings, account_txt, bg="#757171", command=settings_account)
    account_btn.place(x=1, y=150)

    update_txt = tk.Label(settings, text="os info", font="Helvetica, 30")
    update_btn = tk.Button(settings, update_txt, bg="#757171", command=settings_OS_info)
    update_btn.place(x=1, y=250)


def button_click(number):
    current = calculator_display.get()
    calculator_display.delete(0, tk.END)
    calculator_display.insert(0, current + str(number))

def do_calculation():
    try:
        result = eval(calculator_display.get())
        calculator_display.delete(0, tk.END)
        calculator_display.insert(0, str(result))
    except Exception:
        calculator_display.delete(0, tk.END)
        calculator_display.insert(0, "Error")

def remove_last():
    current = calculator_display.get()
    calculator_display.delete(0, tk.END)
    calculator_display.insert(0, current[:-1])

def open_calculator():
    global calculator_display
    calculator = tk.Tk()
    calculator.geometry("600x925")
    calculator.config(bg="#757171")
    calculator.title("Calculator")
    calculator.attributes("-topmost", True)

    calculator_display = tk.Entry(calculator, bg="#757171", width=13, justify="left", font=("Helvetica", 50))
    calculator_display.place(y=10)
    calculator_display.focus_force()

    # Creating buttons
    calculator_num1 = tk.Button(calculator, text="1", width=15, height=7, command=lambda: button_click(1))
    calculator_num2 = tk.Button(calculator, text="2", width=15, height=7, command=lambda: button_click(2))
    calculator_num3 = tk.Button(calculator, text="3", width=15, height=7, command=lambda: button_click(3))
    calculator_num4 = tk.Button(calculator, text="4", width=15, height=7, command=lambda: button_click(4))
    calculator_num5 = tk.Button(calculator, text="5", width=15, height=7, command=lambda: button_click(5))
    calculator_num6 = tk.Button(calculator, text="6", width=15, height=7, command=lambda: button_click(6))
    calculator_num7 = tk.Button(calculator, text="7", width=15, height=7, command=lambda: button_click(7))
    calculator_num8 = tk.Button(calculator, text="8", width=15, height=7, command=lambda: button_click(8))
    calculator_num9 = tk.Button(calculator, text="9", width=15, height=7, command=lambda: button_click(9))
    calculator_num0 = tk.Button(calculator, text="0", width=15, height=7, command=lambda: button_click(0))

    calculator_remove = tk.Button(calculator, text="<", width=15, height=5, command=remove_last)
    calculator_add = tk.Button(calculator, text="+", width=15, height=5, command=lambda: button_click("+"))
    calculator_minus = tk.Button(calculator, text="-", width=15, height=5, command=lambda: button_click("-"))
    calculator_times = tk.Button(calculator, text="*", width=15, height=5, command=lambda: button_click("*"))
    calculator_divide = tk.Button(calculator, text="/", width=15, height=5, command=lambda: button_click("/"))
    calculator_equal = tk.Button(calculator, text="=", width=15, height=5, command=do_calculation)

    calculator_num1.place(y=200, x=50)
    calculator_num2.place(y=200, x=200)
    calculator_num3.place(y=200, x=350)
    calculator_num4.place(y=350, x=50)
    calculator_num5.place(y=350, x=200)
    calculator_num6.place(y=350, x=350)
    calculator_num7.place(y=500, x=50)
    calculator_num8.place(y=500, x=200)
    calculator_num9.place(y=500, x=350)
    calculator_num0.place(y=650, x=200)

    calculator_remove.place(y=700, x=475)
    calculator_add.place(y=200, x=475)
    calculator_minus.place(y=300, x=475)
    calculator_times.place(y=400, x=475)
    calculator_divide.place(y=500, x=475)
    calculator_equal.place(y=600, x=475)

    calculator.mainloop()


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
        account_txt = tk.Label(start, image=account_icon, bg="#757171")
        account_txt.image = account_icon
        account_txt.place(x=1, y=1)

    elif red_icon == True:
        account_icon = PhotoImage(file="account_icon_red.png")
        account_txt = tk.Label(start, image=account_icon, bg="#757171")
        account_txt.image = account_icon
        account_txt.place(x=1, y=1)

    elif lightblue_icon == True:
        account_icon = PhotoImage(file="account_icon_light_blue.png")
        account_txt = tk.Label(start, image=account_icon, bg="#757171")
        account_txt.image = account_icon
        account_txt.place(x=1, y=1)

    elif darkblue_icon == True:
        account_icon = PhotoImage(file="account_icon_dark_blue.png")
        account_txt = tk.Label(start, image=account_icon, bg="#757171")
        account_txt.image = account_icon
        account_txt.place(x=1, y=1)

    elif green_icon == True:
        account_icon = PhotoImage(file="account_icon_green.png")
        account_txt = tk.Label(start, image=account_icon, bg="#757171")
        account_txt.image = account_icon
        account_txt.place(x=1, y=1)

    elif yellow_icon == True:
        account_icon = PhotoImage(file="account_icon_yellow.png")
        account_txt = tk.Label(start, image=account_icon, bg="#757171")
        account_txt.image = account_icon
        account_txt.place(x=1, y=1)

    elif pink_icon == True:
        account_icon = PhotoImage(file="account_icon_pink.png")
        account_txt = tk.Label(start, image=account_icon, bg="#757171")
        account_txt.image = account_icon
        account_txt.place(x=1, y=1)

    elif orange_icon == True:
        account_icon = PhotoImage(file="account_icon_orange.png")
        account_txt = tk.Label(start, image=account_icon, bg="#757171")
        account_txt.image = account_icon
        account_txt.place(x=1, y=1)

    elif purple_icon == True:
        account_icon = PhotoImage(file="account_icon_purple.png")
        account_txt = tk.Label(start, image=account_icon, bg="#757171")
        account_txt.image = account_icon
        account_txt.place(x=1, y=1)

    power_icon = PhotoImage(file="power_icon.png")
    power_btn = tk.Button(start, image=power_icon, bg="#757171", command=power_options)
    power_btn.image = power_icon
    power_btn.place(x=1, y=900)


    settings_icon = PhotoImage(file="settings_icon.png")
    settings_btn = tk.Button(start, image=settings_icon, bg="#757171", command=open_settings)
    settings_btn.image = settings_icon
    settings_btn.place(x=110, y=900)

    shell_icon = PhotoImage(file="terminal_icon.png")
    shell_btn = tk.Button(start, image=shell_icon, bg="#757171", command=open_shell)
    shell_btn.image = shell_icon
    shell_btn.place(x=220, y=900)

    calculator_icon = PhotoImage(file="calculator_icon.png")
    calculator_btn = tk.Button(start, image=calculator_icon, bg="#757171", command=open_calculator)
    calculator_btn.image = calculator_icon
    calculator_btn.place(x=330, y=900)

def desktop():
    global home
    home = tk.Tk()
    home.attributes("-fullscreen", True)
    home.config(bg="#757171")


    start_icon = PhotoImage(file="start_icon.png")
    start_btn = tk.Button(home, image=start_icon, bg="#757171", command=start_menu)
    start_btn.image = start_icon
    start_btn.place(x=10, y=1330)

    clock_label = tk.Label(home, bg="#757171", font="helvetica, 24")
    clock_label.place(x=2400, y=1400)
    update_clock(clock_label)

    home.config(bg=desktop_background_colour)

    start_icon = PhotoImage(file="start_icon.png")
    start_btn = tk.Button(home, image=start_icon, bg=desktop_background_colour, command=start_menu)
    start_btn.image = start_icon
    start_btn.place(x=10, y=1330)

    clock_label = tk.Label(home, bg=desktop_background_colour, font="helvetica, 24")
    clock_label.place(x=2400, y=1400)
    update_clock(clock_label)


def login_btn_pressed(event=None):
    entered_password = login_input_password.get()
    if entered_password == login_password:
        login_input_password.delete(0, tk.END)
        login.destroy()
        desktop()
    else:
        messagebox.showerror("Stachu OS", "Password incorrect")

def show_hide_password_lock():
    if lock_entry.cget("show") == "*":
        lock_entry.configure(show="")
    else:
        lock_entry.configure(show="*")

def show_hide_password():
    if login_input_password.cget("show") == "*":
        login_input_password.configure(show="")
    else:
        login_input_password.configure(show="*")

def login_screen():
    global login
    global login_input_password

    if legacy_login == True:
        login = tk.Tk()
        login.attributes("-fullscreen", True)
        login.config(bg="#757171")


        login_user = tk.Label(login, text=login_username, bg="#757171", anchor="center", font="helvetica, 50")
        login_user.pack(pady=300)

        login_input_password = tk.Entry(login, width=30, font="helvetica, 17")
        login_input_password.pack(pady=100)

        login_confirm_btn = tk.Button(login, text="login", width=10, command=login_btn_pressed)
        login_confirm_btn.pack()

    else:

        login = tk.Tk()
        login.attributes("-fullscreen", True)
        login.config(bg="#757171")


        login_user = tk.Label(login, text=login_username, bg="#757171", anchor="center", font="helvetica, 50")
        login_user.pack(pady=200)

        login_input_password = tk.Entry(login, width=30, font="helvetica, 23", show="*")
        login_input_password.pack()
        login_input_password.bind("<Return>", login_btn_pressed)

        login_show_password_btn = tk.Button(login, text="show/hide password", width=15, bg="#757171", command=show_hide_password)
        login_show_password_btn.pack(pady=20)

        login_confirm_btn = tk.Button(login, text="login", width=10, font="helvetica, 14", bg="#757171", command=login_btn_pressed)
        login_confirm_btn.pack(pady=50)





root = tk.Tk()
root.attributes("-fullscreen", True)
root.config(bg="#757171")
root.after(1, lambda: (login_screen(), root.destroy()))



root.mainloop()





