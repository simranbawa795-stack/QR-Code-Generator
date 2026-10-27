import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
# -----------------------------
# Generate QR Code
# -----------------------------
def generate_qr():
    data = entry.get()

    if data.strip() == "":
        messagebox.showwarning("Warning", "Please enter text or URL.")
        return

    global qr_image

    # Create QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Create image
    qr_image = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    # Display QR Code
    display_image = qr_image.resize((250, 250))
    display_image = ImageTk.PhotoImage(display_image)

    qr_label.config(image=display_image)
    qr_label.image = display_image

    status_label.config(
        text="QR Code Generated Successfully!"
    )


# -----------------------------
# Save QR Code
# -----------------------------
def save_qr():
    if "qr_image" not in globals():
        messagebox.showwarning(
            "Warning",
            "Please generate a QR code first."
        )
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[
            ("PNG Image", "*.png"),
            ("JPEG Image", "*.jpg"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        qr_image.save(file_path)

        messagebox.showinfo(
            "Success",
            "QR Code saved successfully!"
        )


# -----------------------------
# Clear Everything
# -----------------------------
def clear_data():
    entry.delete(0, tk.END)

    qr_label.config(image="")
    qr_label.image = None

    status_label.config(text="")


# -----------------------------
# Exit Application
# -----------------------------
def exit_app():
    root.destroy()


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()

root.title("Python QR Code Generator")
root.geometry("600x700")
root.resizable(False, False)


# -----------------------------
# Heading
# -----------------------------
title_label = tk.Label(
    root,
    text="PYTHON QR CODE GENERATOR",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=25)


# -----------------------------
# Description
# -----------------------------
description_label = tk.Label(
    root,
    text="Enter text, website URL or any information",
    font=("Arial", 12)
)

description_label.pack(pady=5)


# -----------------------------
# Input Label
# -----------------------------
input_label = tk.Label(
    root,
    text="Enter Text / URL:",
    font=("Arial", 13, "bold")
)

input_label.pack(pady=(20, 5))


# -----------------------------
# Input Box
# -----------------------------
entry = tk.Entry(
    root,
    width=50,
    font=("Arial", 12)
)

entry.pack(ipady=8, padx=20)


# -----------------------------
# Generate Button
# -----------------------------
generate_button = tk.Button(
    root,
    text="Generate QR Code",
    command=generate_qr,
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10
)

generate_button.pack(pady=20)


# -----------------------------
# QR Code Display Area
# -----------------------------
qr_label = tk.Label(
    root,
    text="QR Code will appear here",
    font=("Arial", 12)
)

qr_label.pack(pady=10)


# -----------------------------
# Status Message
# -----------------------------
status_label = tk.Label(
    root,
    text="",
    font=("Arial", 11)
)

status_label.pack(pady=10)


# -----------------------------
# Save Button
# -----------------------------
save_button = tk.Button(
    root,
    text="Save QR Code",
    command=save_qr,
    font=("Arial", 11, "bold"),
    padx=20,
    pady=8
)

save_button.pack(pady=5)


# -----------------------------
# Clear Button
# -----------------------------
clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_data,
    font=("Arial", 11, "bold"),
    padx=30,
    pady=8
)

clear_button.pack(pady=5)


# -----------------------------
# Exit Button
# -----------------------------
exit_button = tk.Button(
    root,
    text="Exit",
    command=exit_app,
    font=("Arial", 11, "bold"),
    padx=35,
    pady=8
)

exit_button.pack(pady=5)


# -----------------------------
# Start Application
# -----------------------------
root.mainloop()