from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import psycopg2




def add_window():
    window = Tk()
    window['bg'] = '#fafafa'
    window.title('text-to-speech')
    window.geometry('300x250')
    window.resizable(width=FALSE,height=FALSE)
    return(window)

def button_click():
    login = loginInput.get()
    passwd = passField.get()

    try:
        # connect to exist database
        connection = psycopg2.connect(
        host="127.0.0.1",
        user="postgres",
        password="123",
        database="postgres"    
        )
        connection.autocommit = True
    
 
    
        with connection.cursor() as cursor:
            sql = "select True from Users where (login = %s)and(password = %s)"
            cursor.execute(sql, (login, passwd))
        
            output = cursor.fetchone()
            print(f" {output}")
        
    
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
         # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")



    if output==None:
        messagebox.showerror(title='autentic error',message='you fucking stpd beatch')


    elif login != '' and passwd != '' and output[0]==True: 
        
        
        
        
        
        def button_click_audio():
            print(your_bible.get())
        
        
        
        def button_click_text_to_speech():
            print('its ok')
        
        
        
        
        
        window1.destroy()
        new_window = add_window()
        
        new_canvas=Canvas(new_window, height=300, width=250)
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





def regist_click():
    
    
    def button_click_regist():

        login = loginInput1.get()
        passwd = passField1.get()

        try:
            # connect to exist database
            connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="123",
            database="postgres"    
            )
            connection.autocommit = True
    
 
    
            with connection.cursor() as cursor:
                sql = "INSERT INTO Users(login, password) VALUES (%s, %s); SELECT True FROM Users where login = %s"
                cursor.execute(sql, (login, passwd, login))

                output = cursor.fetchone()
                print(f" {output}")
        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if connection:
            # cursor.close()
                connection.close()
                print("[INFO] PostgreSQL connection closed")

        if output[0]==True:


            def button_click_audior():
                print(your_bibler.get())
        
        
        
            def button_click_text_to_speechr():
                print('its ok')




            new_window1.destroy()
            new_windowr = add_window()
        
            new_canvasr=Canvas(new_windowr, height=300, width=250)
            new_canvasr.pack


            new_framer=Frame(new_windowr, bg='red')
            new_framer.place(relx=0.15, rely=0.15, relwidth=0.7,relheight=0.7)

            your_voice = [
                'gggg',
                'ddd',
                'fff'
            ]

            selected_option = StringVar()
            your_bibler = ttk.Combobox(new_framer, textvariable=selected_option, values=your_voice, state='readonly')
            your_bibler.pack(pady=(20,0))


            press_me_newr = Button(new_framer, text = 'select', bg='grey',command=button_click_audior)
            press_me_newr.pack(pady=5)
        


            new_titler = Label(new_framer, text='Enter your text',bg='grey',font=30)
            new_titler.pack(pady=(5,5))

            textFieldr = Entry(new_framer, bg='white')
            textFieldr.pack(pady=(0,5))

            press_me_new1r = Button(new_framer, text = 'text to speech', bg='grey',command=button_click_text_to_speechr)
            press_me_new1r.pack()





            new_windowr.mainloop()
    
    
    
    
    
    window1.destroy()
    new_window1 = add_window()
        
    new_canvas1=Canvas(new_window1, height=300, width=250)
    new_canvas1.pack


    new_frame1=Frame(new_window1, bg='red')
    new_frame1.place(relx=0.15, rely=0.15, relwidth=0.7,relheight=0.7)
    title1 = Label(new_frame1, text='Enter your login',bg='grey',font=40)
    title1.pack(pady=(30,5))

    loginInput1 = Entry(new_frame1,bg = 'white')
    loginInput1.pack()

    title1 = Label(new_frame1, text='Enter your password',bg='grey',font=40)
    title1.pack(pady=(10,5))

    passField1 = Entry(new_frame1, bg='white', show='*')
    passField1.pack(pady=(0,2))


    press_me1 = Button(new_frame1, text = 'confirm', bg='grey',command=button_click_regist)
    press_me1.pack()





window1 = add_window()




canvas = Canvas(window1, height=300, width=250)
canvas.pack()

frame = Frame(window1,bg='red')
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
press_me.pack(side=LEFT,padx=10)

press_me = Button(frame, text = 'registration', bg='grey',command=regist_click)
press_me.pack(side=LEFT,padx=10)

window1.mainloop()