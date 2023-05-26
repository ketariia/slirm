import tkinter as tk

window = tk.Tk()
window.title("Вход на сайт университета")

username_label = tk.Label(window, text="Имя пользователя:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Пароль:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

def login():
    username = username_entry.get()
    password = password_entry.get()
    print("Пользователь", username, "нажал кнопку Войти")

login_button = tk.Button(window, text="Войти", command=login)
login_button.pack()

window.mainloop()
