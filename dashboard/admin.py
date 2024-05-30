import customtkinter as ctk
import paynow
from dotenv import load_dotenv
import os
import sys
import os
import datetime
import csv

parent_dir = os.path.abspath(".")
sys.path.insert(0, parent_dir)
from database.models import session, Cars


root = ctk.CTk()
root.title("Admin Dashboard")
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)
root.resizable(False, False)
root.config(background="#fff")


def update_dashboard():
    global total_parked_cars, cars_with_parked_and_vehicle_type, trucks_with_parked, bikes_with_parked

    total_parked_cars = get_total_parked_cars()
    cars_with_parked_and_vehicle_type = get_cars_with_parked_and_vehicle_type()
    trucks_with_parked = get_trucks_with_parked()
    bikes_with_parked = get_bikes_with_parked()

    total.configure(text=f"{total_parked_cars}")
    cars_heading.configure(text=f"{cars_with_parked_and_vehicle_type}")
    trucks_heading.configure(text=f"{trucks_with_parked}")
    bikes_heading.configure(text=f"{bikes_with_parked}")


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

button_texts = ["Home", "Dashboard", "Allotment", "Payments"]

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


def get_total_parked_cars():
    parked_cars = session.query(Cars).filter_by(parked="Yes").all()
    total_parked_cars = len(parked_cars)
    return total_parked_cars


total_parked_cars = get_total_parked_cars()


total = ctk.CTkLabel(
    frame1, text=f"{total_parked_cars}", font=("Inter", 30, "bold"), anchor="w"
)
total.pack(side="top", fill="x", padx=50, pady=25)

total_subheading = ctk.CTkLabel(
    frame1, text=f"Total Parked             ", font=("Inter", 16), anchor="w"
)
total_subheading.pack(side="top", fill="x", padx=50, pady=35)

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


def get_cars_with_parked_and_vehicle_type():
    cars = session.query(Cars).filter_by(parked="Yes", vehicle_type="Car").all()
    total_cars = len(cars)
    return total_cars


cars_with_parked_and_vehicle_type = get_cars_with_parked_and_vehicle_type()


cars_heading = ctk.CTkLabel(
    frame2,
    text=f"{cars_with_parked_and_vehicle_type}",
    font=("Inter", 30, "bold"),
    anchor="w",
)
cars_heading.pack(side="top", fill="x", padx=50, pady=25)

cars_subheading = ctk.CTkLabel(
    frame2, text=f"Cars                          ", font=("Inter", 16), anchor="w"
)
cars_subheading.pack(side="top", fill="x", padx=50, pady=35)


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


def get_trucks_with_parked():
    trucks = session.query(Cars).filter_by(parked="Yes", vehicle_type="Truck").all()
    total_trucks = len(trucks)
    return total_trucks


trucks_with_parked = get_trucks_with_parked()


trucks_heading = ctk.CTkLabel(
    frame3, text=f"{trucks_with_parked}", font=("Inter", 30, "bold"), anchor="w"
)
trucks_heading.pack(side="top", fill="x", padx=50, pady=25)

trucks_subheading = ctk.CTkLabel(
    frame3, text=f"Trucks                       ", font=("Inter", 16), anchor="w"
)
trucks_subheading.pack(side="top", fill="x", padx=50, pady=35)

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


def get_bikes_with_parked():
    bikes = session.query(Cars).filter_by(parked="Yes", vehicle_type="Bike").all()
    total_bikes = len(bikes)
    return total_bikes


bikes_with_parked = get_bikes_with_parked()


bikes_heading = ctk.CTkLabel(
    frame4, text=f"{bikes_with_parked}", font=("Inter", 30, "bold"), anchor="w"
)
bikes_heading.pack(side="top", fill="x", padx=50, pady=25)

bikes_subheading = ctk.CTkLabel(
    frame4, text=f"Bikes                         ", font=("Inter", 16), anchor="w"
)
bikes_subheading.pack(side="top", fill="x", padx=50, pady=35)


payments_frame = None
textbox1 = None
textbox2 = None
textbox3 = None
textbox4 = None
textbox5 = None
submit_button = None


def show_payments_frame():
    global payments_frame, allotment_frame, textbox1, textbox2, textbox3, textbox4, textbox5, submit_button

    if allotment_frame is not None:
        allotment_frame.pack_forget()
    frame_container.pack_forget()
    frame_container2.pack_forget()

    if payments_frame is None:
        payments_frame = ctk.CTkFrame(
            root,
            bg_color="#fff",
            fg_color="#fff",
            border_color="#ddd",
            width=800,
            height=400,
        )
        payments_frame.pack(side="top", fill="x", pady=20)

        payments_heading = ctk.CTkLabel(
            payments_frame, text="Payments", font=("Inter", 20, "bold"), anchor="w"
        )
        payments_heading.pack(side="top", fill="x", padx=20, pady=25)

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
            placeholder_text="Email",
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

        submit_button = ctk.CTkButton(
            payments_frame,
            text="Submit",
            font=("Inter", 16),
            fg_color="#18181b",
            hover_color="#000",
            command=lambda: make_payment(),
            height=40,
            text_color="#fff",
        )
        submit_button.pack(side="top", fill="x", padx=20, pady=10)
    else:
        payments_frame.pack(side="top", fill="x", pady=20)

    def make_payment():
        bank_account = bank.get()
        amount = textbox4.get()

        load_dotenv()

        paynow_api = paynow.Paynow(
            integration_id=os.getenv("PAYNOW_INTEGRATION_ID"),
            integration_key=os.getenv("PAYNOW_INTEGRATION_KEY"),
            return_url=os.getenv("PAYNOW_RETURN_URL"),
            result_url=os.getenv("PAYNOW_RESULT_URL"),
        )

        payment = paynow_api.create_payment("Parking penalty", bank_account)

        payment.add("Parking penalty", amount)

        response = paynow_api.send_mobile(payment, "0786486538", "ecocash")

        if response.success:
            payment_status = ctk.CTkLabel(
                payments_frame,
                text="Payment successful!",
                font=("Inter", 14),
                anchor="center",
                text_color="#1ca350",
            )
            payment_status.pack(side="top", fill="x", padx=20, pady=10)
        else:
            payment_status = ctk.CTkLabel(
                payments_frame,
                text="Payment failed",
                font=("Inter", 14),
                anchor="center",
                text_color="#fc3c43",
            )
        payment_status.pack(side="top", fill="x", padx=20, pady=10)
        payment_status.after(1000, payment_status.destroy)


for button in sidebar.winfo_children():
    if button.cget("text") == "Payments":
        payments_button = button
        break

payments_button.configure(command=show_payments_frame)


def show_dashboard():
    global payments_frame, allotment_frame

    if payments_frame is not None:
        payments_frame.pack_forget()

    if allotment_frame is not None:
        allotment_frame.pack_forget()

    frame_container.pack(side="top", fill="x", pady=20)
    frame_container2.pack(side="top", fill="x", pady=20)

    update_dashboard()

    root.after(1000, update_dashboard)


for button in sidebar.winfo_children():
    if button.cget("text") == "Dashboard":
        dashboard_button = button
        break

dashboard_button.configure(command=show_dashboard)

allotment_frame = None


def show_allotment_frame():
    global allotment_frame, payments_frame, treeview

    if payments_frame is not None:
        payments_frame.pack_forget()

    frame_container.pack_forget()
    frame_container2.pack_forget()

    if allotment_frame is None:
        allotment_frame = ctk.CTkFrame(
            root,
            bg_color="#fff",
            fg_color="#fff",
            border_color="#ddd",
            width=800,
            height=400,
        )
        allotment_frame.pack(side="top", fill="x", pady=20)

        allotment_heading = ctk.CTkLabel(
            allotment_frame, text="Allotment", font=("Inter", 20, "bold"), anchor="w"
        )
        allotment_heading.pack(side="top", fill="x", padx=20, pady=25)

    entry_frame = ctk.CTkFrame(
        allotment_frame, bg_color="#fff", fg_color="#fff", border_color="#ddd"
    )
    entry_frame.pack(side="top", fill="x", pady=20)

    placeholder_texts = [
        "First Name",
        "Last Name",
        "Reg Number",
        "Make",
        "Model",
        "Year",
        "Parked (Yes/No)",
        "Car/Truck/Bike",
        "Time In",
        "Time Out",
    ]

    entries = []
    for i in range(10):
        entry = ctk.CTkEntry(
            entry_frame,
            border_width=1,
            border_color="#ddd",
            width=200,
            height=40,
            font=("Inter", 16),
            placeholder_text=placeholder_texts[i],
            fg_color="#fff",
        )
        entry.grid(row=i // 2, column=i % 2, padx=10, pady=10)
        entries.append(entry)

        button_frame = ctk.CTkFrame(
            entry_frame, bg_color="#fff", fg_color="#fff", border_color="#ddd"
        )
        button_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        def check_status():
            reg_number = entries[2].get()
            vehicle = session.query(Cars).filter_by(reg_number=reg_number).first()

            if vehicle:
                parked_status = (
                    "Parked" if vehicle.parked.lower() == "yes" else "Not parked"
                )
                status_label = ctk.CTkLabel(
                    allotment_frame,
                    text=f"Status: {parked_status}",
                    font=("Inter", 14),
                    anchor="center",
                    text_color="#1ca350",
                )
                status_label.pack(side="top", fill="x", padx=20, pady=5)
            else:
                status_label = ctk.CTkLabel(
                    allotment_frame,
                    text="Vehicle not found",
                    font=("Inter", 14),
                    anchor="center",
                    text_color="#fc3c43",
                )
                status_label.pack(side="top", fill="x", padx=20, pady=5)

            status_label.after(2000, status_label.destroy)

        status = ctk.CTkButton(
            button_frame,
            text="Status",
            font=("Inter", 16),
            fg_color="#f5f5f5",
            hover_color="#ddd",
            text_color="#000",
            height=40,
            command=check_status,
        )
        status.pack(side="left", padx=5)

        sign_in = ctk.CTkButton(
            button_frame,
            text="Sign In",
            font=("Inter", 16),
            fg_color="#18181b",
            hover_color="#000",
            height=40,
        )
        sign_in.pack(side="left", padx=5)

        sign_out = ctk.CTkButton(
            button_frame,
            text="Sign Out",
            font=("Inter", 16),
            fg_color="#18181b",
            hover_color="#000",
            height=40,
        )
        sign_out.pack(side="left", padx=5)

        report = ctk.CTkButton(
            button_frame,
            text="Report",
            font=("Inter", 16),
            text_color="#000",
            fg_color="#f5f5f5",
            hover_color="#ddd",
            height=40,
            command=show_report
        )
        report.pack(side="left", padx=5)

        def on_sign_in_click():
            first_name = entries[0].get()
            last_name = entries[1].get()
            reg_number = entries[2].get()
            make = entries[3].get()
            model = entries[4].get()
            year = entries[5].get()
            parked = entries[6].get()
            vehicle_type = entries[7].get()
            time_in_str = entries[8].get()
            time_out_str = entries[9].get()

            try:
                time_in = datetime.datetime.strptime(time_in_str, "%Y-%m-%d %H:%M:%S")
                time_out = datetime.datetime.strptime(time_out_str, "%Y-%m-%d %H:%M:%S")
            except ValueError as e:
                error_message = ctk.CTkLabel(
                    payments_frame,
                    text="Invalid date format",
                    font=("Inter", 14),
                    anchor="center",
                    text_color="#fc3c43",
                    fg_color="#fff",
                )
                error_message.pack(side="top", fill="x", padx=20, pady=0)
                error_message.after(1000, error_message.destroy)
                return

            vehicle = session.query(Cars).filter_by(reg_number=reg_number).first()

            if vehicle:
                # Update existing record
                if first_name:
                    vehicle.first_name = first_name
                if last_name:
                    vehicle.last_name = last_name
                if reg_number:
                    vehicle.reg_number = reg_number
                if make:
                    vehicle.make = make
                if model:
                    vehicle.model = model
                if year:
                    vehicle.year = year
                if parked:
                    vehicle.parked = parked
                if vehicle_type:
                    vehicle.vehicle_type = vehicle_type
                if time_in:
                    vehicle.time_in = time_in
                if time_out:
                    vehicle.time_out = time_out

                try:
                    session.commit()
                    success_message = ctk.CTkLabel(
                        payments_frame,
                        text="Vehicle updated successfully!",
                        font=("Inter", 14),
                        anchor="center",
                        text_color="#1ca350",
                        fg_color="#fff",
                    )
                    success_message.pack(side="top", fill="x", padx=20, pady=0)
                    success_message.after(1000, success_message.destroy)
                except Exception as e:
                    error_message = ctk.CTkLabel(
                        payments_frame,
                        text="An error occurred",
                        font=("Inter", 14),
                        anchor="center",
                        text_color="#fc3c43",
                    )
                    error_message.pack(side="top", fill="x", padx=20, pady=0)
                    error_message.after(1000, error_message.destroy)
            else:
                # Add new record
                new_vehicle = Cars(
                    first_name=first_name,
                    last_name=last_name,
                    reg_number=reg_number,
                    make=make,
                    model=model,
                    year=year,
                    parked=parked,
                    vehicle_type=vehicle_type,
                    time_in=time_in,
                    time_out=time_out,
                )

                try:
                    session.add(new_vehicle)
                    session.commit()
                    success_message = ctk.CTkLabel(
                        payments_frame,
                        text="Vehicle added successfully!",
                        font=("Inter", 14),
                        anchor="center",
                        text_color="#1ca350",
                        fg_color="#fff",
                    )
                    success_message.pack(side="top", fill="x", padx=20, pady=0)
                    success_message.after(1000, success_message.destroy)
                except Exception as e:
                    error_message = ctk.CTkLabel(
                        payments_frame,
                        text="An error occurred",
                        font=("Inter", 14),
                        anchor="center",
                        text_color="#fc3c43",
                    )
                    error_message.pack(side="top", fill="x", padx=20, pady=0)
                    error_message.after(1000, error_message.destroy)

        def on_sign_out_click():
            reg_number = entries[2].get()

            vehicle = session.query(Cars).filter_by(reg_number=reg_number).first()

            if vehicle:
                session.delete(vehicle)
                session.commit()

        sign_in.configure(command=on_sign_in_click)
        sign_out.configure(command=on_sign_out_click)

    else:
        allotment_frame.pack(side="top", fill="x", pady=20)


for button in sidebar.winfo_children():
    if button.cget("text") == "Allotment":
        allotment_button = button
        break

allotment_button.configure(command=show_allotment_frame)

def show_report():
    parked_cars = session.query(Cars).filter_by(parked="Yes").all()

    with open('parked_cars.csv', mode='w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'reg_number', 'make', 'model', 'year', 'parked', 'vehicle_type', 'time_in', 'time_out']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for car in parked_cars:
            writer.writerow({'first_name': car.first_name, 'last_name': car.last_name, 'reg_number': car.reg_number, 'make': car.make, 'model': car.model, 'year': car.year, 'parked': car.parked, 'vehicle_type': car.vehicle_type, 'time_in': car.time_in, 'time_out': car.time_out})

    report_status = ctk.CTkLabel(
        allotment_frame,
        text="Report generated successfully!",
        font=("Inter", 14),
        anchor="center",
        text_color="#1ca350",
        fg_color="#fff"
    )
    report_status.pack(side="top", fill="x", padx=20, pady=0)
    report_status.after(1000, report_status.destroy)

root.mainloop()
