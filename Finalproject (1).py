import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import csv


class WebsitePage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("www.cíne-seek.com")
        self.geometry("600x700")

        image_path = "/Users/prakhyasantosh/Documents/CS + Programming/image.jpg.png"  # Replace with the path to your image file
        image = Image.open(image_path)
        image = image.resize((500, 600), Image.LANCZOS)  # Resize the image to fit the window

        # Convert the image to PhotoImage format
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        image_label = tk.Label(self, image=photo)
        image_label.place(x=0, y=0, relwidth=1, relheight=1)

        image_label.image = photo  # Keep a reference to avoid garbage collection

        login_button = ttk.Button(self, text="Login", command=self.open_login_page)
        registration_button = ttk.Button(self, text="Registration", command=self.open_registration_page)

        image_label.pack()
        login_button.pack()
        registration_button.pack()

    def open_login_page(self):
        self.destroy()
        LoginPage()

    def open_registration_page(self):
        self.destroy()
        RegistrationPage()

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login Page")
        self.geometry("400x400")
        self.configure(bg='#486ba3')

        login_label = ttk.Label(self, text="Enter your details", font=('Average', 15))
        space_label1= tk.Label(self, text="                  ")
        space_label1.grid(row=0,column=0)
        space_label1.configure(bg="#486ba3")
        login_label.grid(row=0,column=5,columnspan=50,pady=30)
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        username_label = ttk.Label(self, text="Username:")
        username_label.configure(foreground='#6f84a6',background='#29200e')
        username_label.grid(row=2,column=4,columnspan=20,padx=10)
        username_entry = ttk.Entry(self, textvariable=self.username_var)
        username_entry.grid(row=4,column=4,columnspan=20,padx=10,pady=30)

        password_label = ttk.Label(self, text="Password:")
        password_label.grid(row=6,column=4,columnspan=20,padx=20)
        password_entry = ttk.Entry(self, textvariable=self.password_var, show='*')
        password_entry.grid(row=8,column=4,columnspan=20,padx=10,pady=10)

        save_continue_button = ttk.Button(self, text="Save and Continue", command=self.save_and_continue)
        save_continue_button.grid(row=10,column=4,rowspan=60,columnspan=20,padx=10,pady=20)

    def save_and_continue(self):
        with open('user_info.csv', 'a', newline="") as file:
            mywriter = csv.writer(file)
            mywriter.writerow((self.username_var.get(), self.password_var.get()))
        self.destroy()
        open_1()

class RegistrationPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Registration Page")
        self.geometry("400x400")
        self.configure(bg='#486ba3')

        registration_label = ttk.Label(self, text="Enter your details to register", font=('Helvetica', 15))
        space_label2= tk.Label(self, text="                  ")
        space_label2.grid(row=0,column=0)
        space_label2.configure(bg="#486ba3")
        registration_label.grid(row=0,column=5,columnspan=50,pady=30)

        self.username_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()

        username_label = ttk.Label(self, text="Username:")
        username_label.grid(row=2,column=4,columnspan=20,padx=20)
        username_entry = ttk.Entry(self, textvariable=self.username_var)
        username_entry.grid(row=4,column=4,columnspan=20,padx=10,pady=10)

        email_label = ttk.Label(self, text="Email:")
        email_label.grid(row=6,column=4,columnspan=20,padx=20)
        email_entry = ttk.Entry(self, textvariable=self.email_var)
        email_entry.grid(row=8,column=4,columnspan=20,padx=10,pady=10)

        password_label = ttk.Label(self, text="Password:")
        password_label.grid(row=10,column=4,columnspan=20,padx=20)
        password_entry = ttk.Entry(self, textvariable=self.password_var, show='*')
        password_entry.grid(row=12,column=4,columnspan=20,padx=10,pady=10)

        registration_button = ttk.Button(self, text="Registration", command=self.register_and_continue)
        registration_button.grid(row=14,column=4,rowspan=60,columnspan=20,padx=10,pady=20)

    def register_and_continue(self):
        with open('user_info.csv', 'a', newline="") as file:
            mywriter = csv.writer(file)
            mywriter.writerow((self.username_var.get(), self.email_var.get(), self.password_var.get()))
        self.destroy()
        open_1()


def open_1():
    import Finalsome1
    a=Finalsome1.Some1
    a()
    #some1="/Users/prakhyasantosh/Downloads/some1.py"
    #with open(f"/Users/prakhyasantosh/Downloads/some1.py","r")as file:
        #code=file.read()
        #exec(code)


if __name__ == "__main__":
    WebsitePage().mainloop()
