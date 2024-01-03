from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def add_window():
    window = Tk()
    window['bg'] = '#393E46'
    window.title('text-to-speech')
    window.geometry('300x250')
    window.resizable(width=FALSE,height=FALSE)
    return(window)

def button_click():
    login = loginInput.get()
    passwd = passField.get()
    if login != '' and passwd != '': 
        
        
        
        
        
        def button_click_audio():
            print(your_bible.get())
        
        
        
        def button_click_text_to_speech():
            print('its ok')
        
        
        
        
        
        window1.destroy()
        new_window = add_window()
        
        new_canvas=Canvas(new_window, height=300, width=250,bg='#393E46')
        new_canvas.pack


        new_frame=Frame(new_window, bg='red')
        new_frame.place(relx=0.15, rely=0.15, relwidth=0.7,relheight=0.7)

        your_voice = [
            'gggg',
            'ddd',
            'fff'
        ]

        selected_option = StringVar()
        your_bible = ttk.Combobox(new_frame, textvariable=selected_option, values=your_voice, state='readonly')
        your_bible.pack(pady=(20,0))


        press_me_new = Button(new_frame, text = 'select', bg='grey',command=button_click_audio)
        press_me_new.pack(pady=5)
        


        new_title = Label(new_frame, text='Enter your text',bg='grey',font=30)
        new_title.pack(pady=(5,5))

        textField = Entry(new_frame, bg='white')
        textField.pack(pady=(0,5))

        press_me_new1 = Button(new_frame, text = 'text to speech', bg='grey',command=button_click_text_to_speech)
        press_me_new1.pack()





        new_window.mainloop()
        
    else:
        messagebox.showerror(title='sukablyat',message='you fucking stpd beatch')






window1 = add_window()




canvas = Canvas(window1, height=300, width=250,bg='#393E46',highlightcolor='#393E46')
canvas.pack()

frame = Frame(window1,bg='#393E46')
frame.place(relx=0.15, rely=0.15, relwidth=0.7,relheight=0.7)





title = Label(frame, text='Enter your login',bg='#393E46',fg='#00ADB5',font=40)
title.pack(pady=(30,5))

loginInput = Entry(frame,bg = 'white')
loginInput.pack()

title = Label(frame, text='Enter your password',bg='#393E46',fg='#00ADB5',font=40)
title.pack(pady=(10,5))

passField = Entry(frame, bg='white', show='*')
passField.pack(pady=(0,5))






press_me = Button(frame, text = 'confirm', bg='grey',command=button_click)
press_me.pack()



window1.mainloop()