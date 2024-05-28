import customtkinter as ctk


# Create the app
root = ctk.CTk()
root.title("Admin Dashboard")
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)
root.resizable(False, False)
root.config(background="#fff")

# Create the sidebar
sidebar = ctk.CTkFrame(root,bg_color='#fff',fg_color='#fff',border_color='#ddd', width=200, height=600, border_width=1, corner_radius=0)
sidebar.pack(side="left", fill="y")


# List of button texts
button_texts = ["Home", "Dashboard", "Allotment", "Users", "Payments"]

# Create the buttons
# Create the buttons
for text in button_texts:
    button = ctk.CTkButton(sidebar, height=40,hover_color='#18181b', text=text, font=("Inter", 16), fg_color='#fff', text_color='#000')
    button.pack(side="top", fill="x", pady=10, padx=20)  # Add padx=20 here

# Change the hover_color attribute of the buttons to white
for button in sidebar.winfo_children():
    button.configure(hover_color='#f1f1f1')

# Create the two frames



# Create the exit button at the bottom
exit_button = ctk.CTkButton(sidebar,text_color='#fff',hover_color="#000", height=40, text="Exit",fg_color='#18181b', font=("Inter", 16), command=root.destroy)
exit_button.pack(side="bottom", fill="x", pady=10, padx=20)

# Create the top navigation bar
top_nav = ctk.CTkFrame(root, bg_color='#fff', fg_color='#fff', border_color='#ddd', width=800, height=50, border_width=0, corner_radius=0)
top_nav.pack(side="top", fill="x", pady=12)

# Add the heading label
heading_label = ctk.CTkLabel(top_nav, text= f"Hello, User!", font=("Inter", 25, "bold"), anchor="w")
heading_label.pack(side="left", fill="y", padx=20, pady=5)

# Add the search bar
search_bar = ctk.CTkEntry(top_nav,border_width=1,border_color='#ddd', width=200, font=("Inter", 14), placeholder_text="Search", fg_color='#fff')
search_bar.pack(side="right", fill="y", padx=20)

root.mainloop()