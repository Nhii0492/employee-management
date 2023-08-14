from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', "The user name or password is incorrect")
    elif usernameEntry.get() == 'Nhinguyen' and passwordEntry.get() == 'nhii0492':
        messagebox.showinfo('Success', "WELLCOME")
        window.destroy()
        import mainwindow
    else:
        messagebox.showerror('Error', "The user name or password is incorrect")

window = Tk()
window.title('Employee Management')
window.geometry('1174x680')

#image
background_img = ImageTk.PhotoImage(file='/Users/nguyennhi/Downloads/pastel-ombre-background-pink-purple_53876-120750.jpg.webp', master=window)
username_img = ImageTk.PhotoImage(file='/Users/nguyennhi/projectPY/3f9470b34a8e3f526dbdb022f9f19cf7-2.jpg', master=window)
password_img = ImageTk.PhotoImage(file='/Users/nguyennhi/projectPY/4cf5e5648c33b2543062bc4a71fdf636-2.jpg', master=window)
signin_img = ImageTk.PhotoImage(file='/Users/nguyennhi/Downloads/8fdd82fb737eb9af651088d577d56c08-2.png', master=window)

bgrLabel = Label(window, image=background_img)
bgrLabel.place(x=0, y=0)

#creat Frame
loginFrame = Frame(window, bg='#e5e9fc')
loginFrame.place(x=412, y=200, width=350, height=300)

#design
signinLabel= Label(loginFrame, image=signin_img, bg='#e5e9fc')
signinLabel.grid(row=0, columnspan=2)

loginLabel = Label(loginFrame, text='Sign in', font=('times new roman', 24, 'bold'), bg='#e5e9fc')
loginLabel.grid(row=1, columnspan=2)

text=Label(loginFrame, text='sign in and start managing your canididates!', font=('times new roman', 17), bg='#e5e9fc', fg='#FBA1B7')
text.grid(row=2, columnspan=2)

usernameLabel = Label(loginFrame, image=username_img, text='Username', compound=LEFT, font=('times new roman', 20), bg='#e5e9fc')
usernameLabel.image = username_img
usernameLabel.grid(row=3, column=0)
usernameEntry = Entry(loginFrame)
usernameEntry.grid(row=3, column=1)

passwordLabel = Label(loginFrame, image=password_img, text='Password', compound=LEFT, font=('times new roman', 20), bg='#e5e9fc')
passwordLabel.image = password_img
passwordLabel.grid(row=4, column=0,)
passwordEntry = Entry(loginFrame, show='*')
passwordEntry.grid(row=4, column=1)

buttonlogin = Button(loginFrame, text='Login', command=login, width=20, bg='#e5e9fc')
buttonlogin.grid(row=7, columnspan=2, pady=20)

#end
window.mainloop()