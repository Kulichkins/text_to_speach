from tkinter import *
from tkinter import messagebox



def button_click():
    login = loginInput.get()
    passwd = passField.get()
    if login != '' and passwd != '': 
        info = f'login :{str(login)}, password:{str(passwd)}'
        messagebox.showinfo(title='IFO',message=info)
    else:
        messagebox.showerror(title='sukablyat',message='you fucking stpd beatch')






window = Tk()
window['bg'] = '#fafafa'
window.title('text-to-speech')
window.geometry('300x250')


window.resizable(width=FALSE,height=FALSE)

canvas = Canvas(window, height=300, width=250)
canvas.pack()

frame = Frame(window,bg='red')
frame.place(relx=0.15, rely=0.15, relwidth=0.7,relheight=0.7)



title = Label(frame, text='Enter your login',bg='grey',font=40)
title.pack(pady=(30,5))

loginInput = Entry(frame,bg = 'white')
loginInput.pack()

title = Label(frame, text='Enter your password',bg='grey',font=40)
title.pack(pady=(10,5))

passField = Entry(frame, bg='white', show='*')
passField.pack(pady=(0,2))




press_me = Button(frame, text = 'confirm', bg='grey',command=button_click)
press_me.pack()



window.mainloop()