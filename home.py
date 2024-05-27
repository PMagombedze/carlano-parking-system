import customtkinter as ctk


def check_availability():
    root.destroy()
    import auth.login as login_form

    login_form.show_login_form()


# Create the app
root = ctk.CTk()
root.title("Carlano Parking")
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)
root.resizable(False, False)
root.config(background="#fff")

# Create the centered heading
heading_label_find_your = ctk.CTkLabel(
    root, fg_color="#fff", text="Find Your", font=("Inter", 34)
)
heading_label_parking_space = ctk.CTkLabel(
    root, fg_color="#fff", text="Parking Space", font=("Inter", 34, "bold")
)
heading_label_find_your.place(relx=0.35, rely=0.1, anchor="center")
heading_label_parking_space.place(relx=0.6, rely=0.1, anchor="center")

# Create the three cards
card_frame = ctk.CTkFrame(
    root, bg_color="#fff", fg_color="#fff", border_color="#fff", border_width=0
)
card_frame.place(relx=0.5, rely=0.3, anchor="center")

card_width = 200
card_height = 150

# Card 1
card1 = ctk.CTkFrame(
    card_frame,
    fg_color="#fff",
    width=card_width,
    height=card_height,
    border_width=1,
    border_color="#ddd",
)
card1.grid(row=0, column=0, padx=20)
card1_icon_label = ctk.CTkLabel(card1, text="🚚", font=("Inter", 32), fg_color="white")
card1_label = ctk.CTkLabel(card1, text="Truck", font=("Inter", 16), fg_color="white")
card1_icon_label.place(relx=0.5, rely=0.3, anchor="center")
card1_label.place(relx=0.5, rely=0.6, anchor="center")

# Card 2
card2 = ctk.CTkFrame(
    card_frame,
    fg_color="#fff",
    width=card_width,
    height=card_height,
    border_width=1,
    border_color="#ddd",
)
card2.grid(row=0, column=1, padx=20)
card2_icon_label = ctk.CTkLabel(card2, text="🚘", font=("Inter", 32), fg_color="white")
card2_label = ctk.CTkLabel(card2, text="Car", font=("Inter", 16), fg_color="white")
card2_icon_label.place(relx=0.5, rely=0.3, anchor="center")
card2_label.place(relx=0.5, rely=0.6, anchor="center")

# Card 3
card3 = ctk.CTkFrame(
    card_frame,
    fg_color="#fff",
    width=card_width,
    height=card_height,
    border_width=1,
    border_color="#ddd",
)
card3.grid(row=0, column=2, padx=20)
card3_icon_label = ctk.CTkLabel(card3, text="🚲", font=("Inter", 32), fg_color="white")
card3_label = ctk.CTkLabel(card3, text="Bike", font=("Inter", 16), fg_color="white")
card3_icon_label.place(relx=0.5, rely=0.3, anchor="center")
card3_label.place(relx=0.5, rely=0.6, anchor="center")

button = ctk.CTkButton(
    root,
    bg_color="#fff",
    text="Check Availability",
    height=40,
    width=150,
    fg_color="#18181b",
    hover_color="black",
    font=("Inter", 14, "bold"),
    command=check_availability,
)
button.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()
