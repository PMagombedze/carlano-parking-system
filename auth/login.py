import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3
import sys
import os

parent_dir = os.path.abspath(".")
sys.path.insert(0, parent_dir)
from database.models import session, Admins

import os
import webbrowser
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build


import webbrowser
import os
import sqlite3


root = ctk.CTk()
root.title("Carlano Parking")
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)
root.resizable(False, False)
root.config(background="#fff")


def google_login():
    try:
        flow = InstalledAppFlow.from_client_secrets_file(
            ".credentials.json",
            scopes=["openid", "https://www.googleapis.com/auth/userinfo.email"],
        )
        auth_url, _ = flow.authorization_url(prompt="select_account")
        webbrowser.open(auth_url)

        creds = flow.run_local_server(port=0)

        service = build("oauth2", "v2", credentials=creds)
        user_info = service.userinfo().get().execute()
        user_email = user_info.get("email")

        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admins WHERE email=?", (user_email,))
        result = cursor.fetchone()

        if result is not None:
            root.destroy()
            os.system("python dashboard/admin.py")
        else:
            error_label = ctk.CTkLabel(
                master=frame,
                text="Invalid email",
                font=("Inter", 12, "bold"),
                fg_color="#fff",
                text_color="#fc3c43",
            )
        error_label.place(relx=0.5, rely=0.8, anchor="center")
        root.after(1000, lambda: error_label.destroy())

        conn.close()

    except Exception as e:
        error_label = ctk.CTkLabel(
            master=frame,
            text="Authorization Error",
            font=("Inter", 12, "bold"),
            fg_color="#fff",
            text_color="#fc3c43",
        )
        error_label.place(relx=0.5, rely=0.8, anchor="center")
        root.after(1000, lambda: error_label.destroy())


def check_credentials():
    email = textbox2.get()
    password = textbox3.get()

    admin = session.query(Admins).filter_by(email=email).first()
    if admin is not None and admin.check_password(password):
        root.destroy()
        os.system("python dashboard/admin.py")
    else:
        error_label = ctk.CTkLabel(
            master=frame,
            text="Invalid credentials",
            font=("Inter", 12, "bold"),
            fg_color="#fff",
            text_color="#fc3c43",
        )
        error_label.place(relx=0.5, rely=0.8, anchor="center")
        root.after(1000, lambda: error_label.destroy())


frame = ctk.CTkFrame(
    master=root,
    fg_color="#fff",
    bg_color="#fff",
    width=600,
    height=500,
    border_color="#ddd",
    border_width=1,
)
frame.place(relx=0.5, rely=0.5, anchor="center")

heading = ctk.CTkLabel(
    master=frame,
    text="Welcome to Carlano Parking",
    font=("Inter", 24, "bold"),
    fg_color="#fff",
)
heading.place(relx=0.5, rely=0.2, anchor="center")


google_icon = Image.open("images/google.png")
google_icon = google_icon.resize((30, 30), Image.Resampling.LANCZOS)
google_photo = ImageTk.PhotoImage(google_icon)

button = ctk.CTkButton(
    master=frame,
    text="Continue with Google",
    font=("Inter", 13),
    command=google_login,
    height=40,
    width=200,
    fg_color="#fff",
    bg_color="#fff",
    border_color="#ddd",
    border_width=1,
    hover_color="#f1f1f1",
    text_color="#000",
    image=google_photo,
    compound="left",
)
button.place(relx=0.5, rely=0.3, anchor="center")

heading2 = ctk.CTkLabel(master=frame, text="-OR-", font=("Inter", 12), fg_color="#fff")
heading2.place(relx=0.5, rely=0.4, anchor="center")


textbox2 = ctk.CTkEntry(
    master=frame,
    font=("Inter", 16),
    width=200,
    height=40,
    placeholder_text="Enter Email",
    border_color="#ddd",
    border_width=1,
    placeholder_text_color="#bbb",
    text_color="#bbb",
)
textbox2.place(relx=0.5, rely=0.5, anchor="center")

textbox3 = ctk.CTkEntry(
    master=frame,
    font=("Inter", 16),
    width=200,
    height=40,
    placeholder_text="Enter Password",
    border_color="#ddd",
    border_width=1,
    placeholder_text_color="#bbb",
    text_color="#bbb",
    show="•",
)
textbox3.place(relx=0.5, rely=0.6, anchor="center")


button2 = ctk.CTkButton(
    master=frame,
    text="Continue",
    font=("Inter", 14, "bold"),
    width=200,
    height=40,
    command=check_credentials,
    fg_color="#18181b",
    hover_color="#000",
)
button2.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()
