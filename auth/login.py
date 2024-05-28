import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3
from getpass import getpass
from CTkMessagebox import CTkMessagebox


# Create the app
root = ctk.CTk()
root.title("Carlano Parking")
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)
root.resizable(False, False)
root.config(background="#fff")


import os
import webbrowser
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import google.auth
from googleapiclient.discovery import build


import webbrowser
import os
import sqlite3
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import google.auth
import tkinter as tk
from tkinter import messagebox
import customtkinter as CTk


def google_login():
    try:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            scopes=["openid", "https://www.googleapis.com/auth/userinfo.email"],
        )
        auth_url, _ = flow.authorization_url(prompt="select_account")
        webbrowser.open(auth_url)

        # Get the authorization code
        creds = flow.run_local_server(port=0)

        # Get the user's email address
        service = build("oauth2", "v2", credentials=creds)
        user_info = service.userinfo().get().execute()
        user_email = user_info.get("email")

        # Check if the user's email exists in the database
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=?", (user_email,))
        result = cursor.fetchone()

        if result is not None:
            # Open the dashboard/admin.py script
            root.destroy()
            os.system("python dashboard/admin.py")
        else:
            CTkMessagebox(
                title="Error",
                message="Invalid email",
                fg_color="#fff",
                icon="cancel",
                font=("Inter", 14, "bold"),
                button_color="#f1f1f1",
                button_height=40,
                button_hover_color="#aaa",
                width=130,
                bg_color="#fff",
                button_text_color="#000",
                justify="center",
                fade_in_duration=1,
            )

        # Close the database connection
        conn.close()

    except Exception as e:
        print(f"Access blocked: Authorization Error - {e}")
        CTkMessagebox(
            title="Error",
            message="Access blocked: Authorization Error",
            fg_color="#fff",
            icon="cancel",
            font=("Inter", 14, "bold"),
            button_color="#f1f1f1",
            button_height=40,
            button_hover_color="#aaa",
            width=130,
            bg_color="#fff",
            button_text_color="#000",
            justify="center",
        )


def check_credentials():
    role = textbox1.get()
    email = textbox2.get()
    password = textbox3.get()

    # Connect to the database
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    # Check if the email and password exist in the database
    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?", (email, password)
    )
    result = cursor.fetchone()

    # If the result is not None, the email and password exist in the database
    if result is not None:
        # Check if the role is Admin
        if role == "admin":
            root.destroy()
            os.system("python dashboard/admin.py")
        else:
            CTkMessagebox(
                title="Error",
                message="Invalid role",
                fg_color="#fff",
                icon="cancel",
                font=("Inter", 14, "bold"),
                button_color="#f1f1f1",
                button_height=40,
                button_hover_color="#aaa",
                width=130,
                bg_color="#fff",
                button_text_color="#000",
                justify="center",
            )
    else:
        CTkMessagebox(
            title="Error",
            message="Invalid credentials",
            fg_color="#fff",
            icon="cancel",
            font=("Inter", 14, "bold"),
            button_color="#f1f1f1",
            button_height=40,
            button_hover_color="#aaa",
            width=130,
            bg_color="#fff",
            button_text_color="#000",
            justify="center",
        )

    # Close the database connection
    conn.close()


# Create a frame with a border
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

# Centered heading
heading = ctk.CTkLabel(
    master=frame,
    text="Welcome to Carlano Parking",
    font=("Inter", 24, "bold"),
    fg_color="#fff",
)
heading.place(relx=0.5, rely=0.2, anchor="center")

# Button below heading
google_icon = Image.open("images/google.png")
google_icon = google_icon.resize((30, 30), Image.Resampling.LANCZOS)
google_photo = ImageTk.PhotoImage(google_icon)

# Button below heading with Google icon
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
# Centered heading
heading2 = ctk.CTkLabel(master=frame, text="-OR-", font=("Inter", 12), fg_color="#fff")
heading2.place(relx=0.5, rely=0.4, anchor="center")

# Textboxes with placeholders
textbox1 = ctk.CTkEntry(
    master=frame,
    font=("Inter", 16),
    width=200,
    height=40,
    placeholder_text="Enter admin or user",
    border_color="#ddd",
    border_width=1,
    placeholder_text_color="#bbb",
    text_color="#bbb",
)
textbox1.place(relx=0.5, rely=0.5, anchor="center")

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
textbox2.place(relx=0.5, rely=0.6, anchor="center")

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
)
textbox3.place(relx=0.5, rely=0.7, anchor="center")


# Button below textboxes
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
button2.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()
