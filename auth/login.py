import customtkinter as ctk
from PIL import Image, ImageTk

# Create the app
root = ctk.CTk()
root.title("Carlano Parking")
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)
root.resizable(False, False)
root.config(background='#fff')

# Create a frame with a border
frame = ctk.CTkFrame(master=root,fg_color='#fff',bg_color='#fff', width=600, height=500, border_color="#ddd", border_width=1)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Centered heading
heading = ctk.CTkLabel(master=frame, text="Welcome to Carlano Parking", font=("Inter", 24, "bold"), fg_color="#fff")
heading.place(relx=0.5, rely=0.2, anchor='center')

# Button below heading
google_icon = Image.open("images/google.png")
google_icon = google_icon.resize((30, 30), Image.Resampling.LANCZOS)
google_photo = ImageTk.PhotoImage(google_icon)

# Button below heading with Google icon
button = ctk.CTkButton(master=frame, text="Continue with Google", font=("Inter", 13), command=lambda: print("Button clicked"), height=40, width=200, fg_color='#fff', bg_color='#fff', border_color='#ddd', border_width=1, hover_color='#f1f1f1', text_color='#000', image=google_photo, compound='left')
button.place(relx=0.5, rely=0.4, anchor='center')
# Centered heading
heading2 = ctk.CTkLabel(master=frame, text="-OR-", font=("Inter", 12), fg_color="#fff")
heading2.place(relx=0.5, rely=0.5, anchor='center')

# Textboxes with placeholders
textbox1 = ctk.CTkEntry(master=frame, font=("Inter", 16), width=200, height=40, placeholder_text='Enter Email', border_color='#ddd', border_width=1,placeholder_text_color='#bbb', text_color='#bbb')
textbox1.place(relx=0.5, rely=0.6, anchor='center')

textbox2 = ctk.CTkEntry(master=frame, font=("Inter", 16), width=200, height=40, placeholder_text='Enter Password', border_color='#ddd', border_width=1, placeholder_text_color='#bbb', text_color='#bbb')
textbox2.place(relx=0.5, rely=0.7, anchor='center')

# Button below textboxes
button2 = ctk.CTkButton(master=frame, text="Continue", font=("Inter", 14, "bold"),width=200, height=40, command=lambda: print("Button clicked"),fg_color="#18181b", hover_color='#000')
button2.place(relx=0.5, rely=0.8, anchor='center')

root.mainloop()