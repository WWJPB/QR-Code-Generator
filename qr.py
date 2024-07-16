import os
import qrcode
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry("500x350")

def get_link():
    return entry.get()

def qr():
    link = get_link()
    img = qrcode.make(link)
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    file_path = os.path.join(desktop_path, 'qrcode.png')
    img.save(file_path)

def exit():
    root.destroy()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Paste the link to the page")
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text= "URL")
entry.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="Save", command=qr)
button1.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Exit", command=exit)
button2.pack(pady=12, padx=10)

root.mainloop()
