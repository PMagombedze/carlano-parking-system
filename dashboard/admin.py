import customtkinter as ctk

root = ctk.CTk()
root.title("Admin Dashboard")
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)
root.resizable(False, False)
root.config(background="#fff")

sidebar = ctk.CTkFrame(
    root,
    bg_color="#F5F5F5",
    fg_color="#F5F5F5",
    border_color="#ddd",
    width=200,
    height=600,
    border_width=0,
    corner_radius=0,
)
sidebar.pack(side="left", fill="y")

button_texts = ["Home", "Dashboard", "Allotment", "Users", "Payments"]

for text in button_texts:
    button = ctk.CTkButton(
        sidebar,
        height=40,
        text=text,
        font=("Inter", 16),
        fg_color="#F5F5F5",
        text_color="#000",
    )
    button.pack(side="top", fill="x", pady=10, padx=20)

for button in sidebar.winfo_children():
    button.configure(hover_color="#ddd")

exit_button = ctk.CTkButton(
    sidebar,
    text_color="#fff",
    hover_color="#000",
    height=40,
    text="Exit",
    fg_color="#16161b",
    font=("Inter", 16),
    command=root.destroy,
)
exit_button.pack(side="bottom", fill="x", pady=10, padx=20)

top_nav = ctk.CTkFrame(
    root,
    bg_color="#fff",
    fg_color="#fff",
    border_color="#ddd",
    width=800,
    height=50,
    border_width=0,
)
top_nav.pack(side="top", fill="x", pady=12)

heading_label = ctk.CTkLabel(
    top_nav, text=f"Dashboard", font=("Inter", 25, "bold"), anchor="w"
)
heading_label.pack(side="left", fill="y", padx=20, pady=5)

search_bar = ctk.CTkEntry(
    top_nav,
    border_width=1,
    border_color="#ddd",
    width=200,
    font=("Inter", 16),
    placeholder_text="Search",
    fg_color="#fff",
)
search_bar.pack(side="right", fill="y", padx=20)

# Add two frames below top nav
frame_container = ctk.CTkFrame(
    root, bg_color="#fff", fg_color="#fff", border_color="#ddd", width=800, height=400
)
frame_container.pack(side="top", fill="x", pady=20)

frame1 = ctk.CTkFrame(
    frame_container,
    bg_color="#fff",
    fg_color="#fff",
    border_color="#ddd",
    width=400,
    height=100,
    border_width=1,
)
frame1.pack(side="left", fill="y", padx=20)

frame1_heading = ctk.CTkLabel(
    frame1, text=f"Frame 1 Heading", font=("Inter", 20, "bold"), anchor="w"
)
frame1_heading.pack(side="top", fill="x", padx=50, pady=25)

frame1_subheading = ctk.CTkLabel(
    frame1, text=f"Total Parked", font=("Inter", 16), anchor="w"
)
frame1_subheading.pack(side="top", fill="x", padx=50, pady=35)

frame2 = ctk.CTkFrame(
    frame_container,
    bg_color="#fff",
    fg_color="#fff",
    border_color="#ddd",
    width=400,
    height=100,
    border_width=1,
)
frame2.pack(side="right", fill="y", padx=20)

frame2_heading = ctk.CTkLabel(
    frame2, text=f"Frame 2 Heading", font=("Inter", 20, "bold"), anchor="w"
)
frame2_heading.pack(side="top", fill="x", padx=50, pady=25)

frame2_subheading = ctk.CTkLabel(frame2, text=f"Cars", font=("Inter", 16), anchor="w")
frame2_subheading.pack(side="top", fill="x", padx=50, pady=35)


frame_container2 = ctk.CTkFrame(
    root, bg_color="#fff", fg_color="#fff", border_color="#ddd", width=800, height=400
)
frame_container2.pack(side="top", fill="x", pady=20)

frame3 = ctk.CTkFrame(
    frame_container2,
    bg_color="#fff",
    fg_color="#fff",
    border_color="#ddd",
    width=400,
    height=100,
    border_width=1,
)
frame3.pack(side="left", fill="y", padx=20)

frame3_heading = ctk.CTkLabel(
    frame3, text=f"Frame 1 Heading", font=("Inter", 20, "bold"), anchor="w"
)
frame3_heading.pack(side="top", fill="x", padx=50, pady=25)

frame3_subheading = ctk.CTkLabel(
    frame3, text=f" Trucks", font=("Inter", 16), anchor="w"
)
frame3_subheading.pack(side="top", fill="x", padx=50, pady=35)

frame4 = ctk.CTkFrame(
    frame_container2,
    bg_color="#fff",
    fg_color="#fff",
    border_color="#ddd",
    width=400,
    height=100,
    border_width=1,
)
frame4.pack(side="right", fill="y", padx=20)

frame4_heading = ctk.CTkLabel(
    frame4, text=f"Frame 2 Heading", font=("Inter", 20, "bold"), anchor="w"
)
frame4_heading.pack(side="top", fill="x", padx=50, pady=25)

frame4_subheading = ctk.CTkLabel(
    frame4, text=f"Bikes", font=("Inter", 16), anchor="w"
)
frame4_subheading.pack(side="top", fill="x", padx=50, pady=35)


payments_frame = None
textbox1 = None
textbox2 = None
textbox3 = None
textbox4 = None
textbox5 = None
submit_button = None

def show_payments_frame():
    global payments_frame, textbox1, textbox2, textbox3, textbox4, textbox5, submit_button

    # Hide frame_container and frame_container2
    frame_container.pack_forget()
    frame_container2.pack_forget()

    if payments_frame is None:
        # Create frame for payments
        payments_frame = ctk.CTkFrame(
            root,
            bg_color="#fff",
            fg_color="#fff",
            border_color="#ddd",
            width=800,
            height=400,
        )
        payments_frame.pack(side="top", fill="x", pady=20)

        # Create heading for payments
        payments_heading = ctk.CTkLabel(
            payments_frame, text="Payments", font=("Inter", 20, "bold"), anchor="w"
        )
        payments_heading.pack(side="top", fill="x", padx=20, pady=25)

        # Create 5 textboxes aligned vertically
        

        textbox3 = ctk.CTkEntry(
            payments_frame,
            border_width=1,
            border_color="#ddd",
            width=200,
            height=40,
            font=("Inter", 16),
            placeholder_text="Reg Number",
            fg_color="#fff",
        )
        textbox3.pack(side="top", fill="x", padx=20, pady=10)

        bank = ctk.CTkEntry(
            payments_frame,
            border_width=1,
            border_color="#ddd",
            width=200,
            height=40,
            font=("Inter", 16),
            placeholder_text="Bank Account",
            fg_color="#fff",
        )
        bank.pack(side="top", fill="x", padx=20, pady=10)

        textbox4 = ctk.CTkEntry(
            payments_frame,
            border_width=1,
            border_color="#ddd",
            width=200,
            font=("Inter", 16),
            height=40,
            placeholder_text="Amount",
            fg_color="#fff",
        )
        textbox4.pack(side="top", fill="x", padx=20, pady=10)

        textbox5 = ctk.CTkEntry(
            payments_frame,
            border_width=1,
            border_color="#ddd",
            width=200,
            font=("Inter", 16),
            height=40,
            placeholder_text="Reason",
            fg_color="#fff",
        )
        textbox5.pack(side="top", fill="x", padx=20, pady=10)

        # Create a button below the textboxes
        submit_button = ctk.CTkButton(
            payments_frame,
            text="Submit",
            font=("Inter", 16),
            fg_color="#18181b",
            hover_color="#000",
            command=lambda: print("Submit button clicked"),
            height=40,
            text_color="#fff"
        )
        submit_button.pack(side="top", fill="x", padx=20, pady=10)
    else:
        payments_frame.pack(side="top", fill="x", pady=20)

# Get the "Payments" button
for button in sidebar.winfo_children():
    if button.cget("text") == "Payments":
        payments_button = button
        break

# Configure the "Payments" button to trigger the show_payments_frame function
payments_button.configure(command=show_payments_frame)


def show_dashboard():
    global payments_frame

    # Hide payments_frame
    if payments_frame is not None:
        payments_frame.pack_forget()

    # Re-pack frame_container and frame_container2
    frame_container.pack(side="top", fill="x", pady=20)
    frame_container2.pack(side="top", fill="x", pady=20)

# Get the "Dashboard" button
for button in sidebar.winfo_children():
    if button.cget("text") == "Dashboard":
        dashboard_button = button
        break

# Configure the "Dashboard" button to trigger the show_dashboard function
dashboard_button.configure(command=show_dashboard)

root.mainloop()
