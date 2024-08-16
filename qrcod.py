import qrcode
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def generate_qr():
    url = entry.get()
    if not url:
        messagebox.showwarning("Uyarı", "Lütfen bir URL girin.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Başarılı", f"QR kodu {save_path} olarak kaydedildi.")
    else:
        messagebox.showwarning("Uyarı", "Kaydetme işlemi iptal edildi.")

# Tkinter arayüzünü oluşturma
root = tk.Tk()
root.title("QR Kod Üretici")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="URL Girin:")
label.grid(row=0, column=0, padx=5)

entry = tk.Entry(frame, width=50)
entry.grid(row=0, column=1, padx=5)

generate_btn = tk.Button(frame, text="QR Kod Üret", command=generate_qr)
generate_btn.grid(row=1, columnspan=2, pady=10)

root.mainloop()
