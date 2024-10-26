from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

window=Tk()
# Edit Window 
window.geometry("1280x700+0+0")
window.resizable(False,False)
window.config(bg="white")
window.title("Login System of Student Management System")
window.iconbitmap(r"C:\Users\Abhinash Kumar\Downloads\130manstudent2_100617.ico")

backgroundImage=ImageTk.PhotoImage(file=r"C:\Users\Abhinash Kumar\Downloads\pexels-goumbik-590022.jpg")
bgLabel=Label(window)
bgLabel.place(x=0, y=0)

loginFrame=Frame(window, bg='white')
loginFrame.place(x=400, y=150)

#Login Window
def login():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror("Error", "Fields cannot be empty")

    elif usernameEntry.get()=="Avinash" and passwordEntry.get()=="1234":
        messagebox.showinfo("Succesfully", "Welcome")
        window.destroy()
        import sms
        
        
    else: 
        messagebox.showerror("Error", "Invalid username or password")
        



#Login Logo
logoImage=PhotoImage(file=r"C:\Users\Abhinash Kumar\Downloads\graduated.png")
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

# UserName
usernameImage=PhotoImage(file=r"C:\Users\Abhinash Kumar\Downloads\user.png")
usernameLabel=Label(loginFrame,image=usernameImage, text="Username", compound=LEFT, font=("times new roman", 20, "bold"),bg="white")
usernameLabel.grid(row=1, column=0, pady=10, padx=20)
usernameEntry=Entry(loginFrame, font=("times nes roman", 20, "bold"), relief="sunken", bd=5, fg="royalblue")
usernameEntry.grid(row=1, column=1, pady=10, padx=20)

# Password 
passwordImage=PhotoImage(file=r"C:\Users\Abhinash Kumar\Downloads\padlock.png")
passwordLabel=Label(loginFrame,image=passwordImage, text="Password", compound=LEFT, font=("times new roman", 20, "bold"),bg="white")
passwordLabel.grid(row=2, column=0, pady=10, padx=20)
passwordEntry=Entry(loginFrame, font=("times nes roman", 20, "bold"), relief="sunken", bd=5, fg="royalblue")
passwordEntry.grid(row=2, column=1, pady=10, padx=20)

#Button
loginButton=Button(loginFrame, text="Login", font=("times now roman", 14, "bold"), width=15, bg="cornflowerblue", fg="white", activebackground="cornflowerblue", activeforeground="white", cursor="hand2", command=login)
loginButton.grid(row=3, column=1, pady= 10)

window.mainloop()