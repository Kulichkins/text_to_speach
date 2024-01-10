from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import psycopg2
import numpy as np


from transformers import BarkModel, AutoProcessor
import torch
import scipy




def add_window():
    window = Tk()
    window['bg'] = '#fafafa'
    window.title('text-to-speech')
    window.geometry('300x500')
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
        messagebox.showerror(title='autentic error',message='you write something wrong or please reg')


    elif login != '' and passwd != '' and output[0]==True: 
        
        
       
        
        
        def button_click_audio():
            choice = your_bible.get()
            if choice == '':
                return(messagebox.showerror(title='Warning',message='fild shoud not be empty'))
            str_name = 'r'+str(choice)
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
                    sql = "SELECT preset,rate FROM Files WHERE file_name = %s"
                    cursor.execute(sql, (choice, ))
        
                    row = cursor.fetchone()
                    print(f" {row}")
        
    
            except Exception as _ex:
                print("[INFO] Error while working with PostgreSQL", _ex)
            finally:
                if connection:
                # cursor.close()
                    connection.close()
                    print("[INFO] PostgreSQL connection closed")
            
            audio_data = row[0]
            print(audio_data)
            audio_array = np.frombuffer(audio_data, dtype=np.int64)
            audio_array = audio_array/100000000000000
            audio_array = audio_array.astype(np.float32)
            print(audio_array)
            print(len(audio_array))
            print(type(audio_array))
            print(audio_array.dtype)
            scipy.io.wavfile.write(str_name, rate=row[1], data=audio_array)
        
        
        
        def button_click_text_to_speech(temp_fk_id = login):
            preset = your_bibler_presset.get()
            text_for_using = str(textField.get())
            text_for_name = str(textField1.get())+'.wav'
            text_for_name_temp = str(textField1.get())
            if (preset == '') or (text_for_name_temp == '') or (text_for_using == ''):
                return(messagebox.showerror(title='Warning',message='fild shoud not be empty'))
            

            fk_id = temp_fk_id
            print(fk_id)
            
            model = BarkModel.from_pretrained('suno/bark')
            device = 'cuda' if torch.cuda.is_available() else 'cpu'
            model = model.to(device)
            processor = AutoProcessor.from_pretrained('suno/bark')


                

            inputs = processor(text_for_using, voice_preset = preset).to(device)
            audio_array2 = model.generate(**inputs)
            audio_array2 = audio_array2.cpu().numpy().squeeze()
            print(audio_array2)
            print(len(audio_array2))

            sample_rate = model.generation_config.sample_rate
            scipy.io.wavfile.write(text_for_name,rate = sample_rate,data=audio_array2)
            print('ffffffffffffffffffffffffffff')
            
            
            
            rate, audio_array = scipy.io.wavfile.read(text_for_name)
            print(type(audio_array))
            print(audio_array.dtype)
            print(len(audio_array))
            

            

            # Преобразование аудиофайла в тип bytea
            audio_data = audio_array*100000000000000
            print('file base:', audio_data)
            print('file not base:', audio_data.astype(np.int64))
            audio_data = audio_data.astype(np.int64).tobytes()
            print(len(audio_data))
            
            '''audio_array = np.frombuffer(audio_data, dtype=np.int64)
            audio_array = audio_array/100000000000000
            audio_array = audio_array.astype(np.float32)
            print(audio_array)
            print(len(audio_array))
            print(type(audio_array))
            print(audio_array.dtype)
            scipy.io.wavfile.write('восстановленный_файл1.wav', rate=rate, data=audio_array)'''
            
           


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
                    insert_query1 = "select id from Users where login = %s"
                    cursor.execute(insert_query1, (fk_id,))
                    output = cursor.fetchone()

                    insert_query = "INSERT INTO files (file_name, preset, fk_user_id,rate) VALUES (%s, %s, %s, %s)"
                    cursor.execute(insert_query, (text_for_name, audio_data, output[0], rate))

                    output = cursor.fetchone()
                    print(f" {output}")
            except Exception as _ex:
                print("[INFO] Error while working with PostgreSQL", _ex)
            finally:
                if connection:
                # cursor.close()
                    connection.close()
                    print("[INFO] PostgreSQL connection closed")

        
        
        
        
        
        window1.destroy()
        new_window = add_window()
        
        new_canvas=Canvas(new_window, height=300, width=250)
        new_canvas.pack


        new_frame=Frame(new_window, bg='red')
        new_frame.place(relx=0.15, rely=0.15, relwidth=0.7,relheight=0.7)

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
                insert_query1 = "select id from Users where login = %s"
                cursor.execute(insert_query1, (login,))
                output = cursor.fetchone()



                sql = "select * from Files where fk_user_id = %s"
                cursor.execute(sql, (output[0],))
        
                masss = cursor.fetchall()
                
        
    
        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if connection:
            # cursor.close()
                connection.close()
                print("[INFO] PostgreSQL connection closed")
        your_presset=[]
        for i in range(len(masss)):
            your_presset.append(masss[i][3])
         
        def button_click_refresh():
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
                    insert_query1 = "select id from Users where login = %s"
                    cursor.execute(insert_query1, (login,))
                    output = cursor.fetchone()



                    sql = "select * from Files where fk_user_id = %s"
                    cursor.execute(sql, (output[0],))
        
                    masss = cursor.fetchall()
                
        
    
            except Exception as _ex:
                print("[INFO] Error while working with PostgreSQL", _ex)
            finally:
                if connection:
                # cursor.close()
                    connection.close()
                    print("[INFO] PostgreSQL connection closed")
            your_presset=[]
            for i in range(len(masss)):
                your_presset.append(masss[i][3])
            your_bible['values']=your_presset
        

        selected_option = StringVar()
        your_bible = ttk.Combobox(new_frame, textvariable=selected_option, values=your_presset, state='readonly')
        your_bible.pack(pady=(20,0))


        press_me_new = Button(new_frame, text = 'select', bg='grey',command=button_click_audio)
        press_me_new.pack(pady=5)

        press_me_new = Button(new_frame, text = 'refresh', bg='grey',command=button_click_refresh)
        press_me_new.pack()

        choice_your_voice = ['v2/ru_speaker_1','v2/ru_speaker_2','v2/ru_speaker_3','v2/ru_speaker_5','v2/ru_speaker_6']

        selected_option2 = StringVar()
        your_bibler_presset = ttk.Combobox(new_frame, textvariable=selected_option2, values=choice_your_voice, state='readonly')
        your_bibler_presset.pack(pady=(10,0))

        new_title = Label(new_frame, text='Enter your text',bg='grey',font=30)
        new_title.pack(pady=(5,5))

        textField = Entry(new_frame, bg='white')
        textField.pack(pady=(0,5))
        
        new_title1 = Label(new_frame, text='Enter your text for name',bg='grey',font=30)
        new_title1.pack(pady=(5,5))

        textField1 = Entry(new_frame, bg='white')
        textField1.pack(pady=(0,5))

        press_me_new1 = Button(new_frame, text = 'text to speech', bg='grey',command=button_click_text_to_speech)
        press_me_new1.pack()





        new_window.mainloop()
        
    else:
        messagebox.showerror(title='sukablyat',message='This login is not available')





def regist_click():
    
    
    def button_click_regist():
        temp_output = [False,True]
        login = loginInput1.get()
        passwd = passField1.get()
        if (login == '') or (passwd == ''):
            return(messagebox.showerror(title='Warning',message='filds shoud not be empty'))

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
                sql = "SELECT True FROM Users where login = %s"
                cursor.execute(sql, (login, ))
                output1 = cursor.fetchone()
                if output1 == None:
                    output1 = temp_output
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
        print(output1)


        if output1[0]==True:
            messagebox.showerror(title='Warning',message='This login is not available')
            

        elif output[0]==True:


            def button_click_audior():
                choice = your_bibler.get()
                

                if choice!='':
                    str_name = 'r'+str(choice)
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
                            sql = "SELECT preset,rate FROM Files WHERE file_name = %s"
                            cursor.execute(sql, (choice, ))
        
                            row = cursor.fetchone()
                            print(f" {row}")
        
    
                    except Exception as _ex:
                        print("[INFO] Error while working with PostgreSQL", _ex)
                    finally:
                        if connection:
                        # cursor.close()
                            connection.close()
                            print("[INFO] PostgreSQL connection closed")
            
                    audio_data = row[0]
                    print(audio_data)
                    audio_array = np.frombuffer(audio_data, dtype=np.int64)
                    audio_array = audio_array/100000000000000
                    audio_array = audio_array.astype(np.float32)
                    print(audio_array)
                    print(len(audio_array))
                    print(type(audio_array))
                    print(audio_array.dtype)
                    scipy.io.wavfile.write(str_name, rate=row[1], data=audio_array)
                else:
                    messagebox.showerror(title='Warning',message='filds shoud not be empty')
        
        
        
            def button_click_text_to_speechr(temp_fk_id = login):
                text_for_using = str(textFieldr.get())
                text_for_name = str(textFieldr1.get())+'.wav'
                text_for_name_temp = str(textFieldr1.get())
                preset = your_bibler_presset.get()
                if (text_for_using != '') and (text_for_name_temp != '') and (preset != ''):
                    fk_id = temp_fk_id
                    print(fk_id)
            
                    model = BarkModel.from_pretrained('suno/bark')
                    device = 'cuda' if torch.cuda.is_available() else 'cpu'
                    model = model.to(device)
                    processor = AutoProcessor.from_pretrained('suno/bark')


                

                    inputs = processor(text_for_using, voice_preset = preset).to(device)
                    audio_array2 = model.generate(**inputs)
                    audio_array2 = audio_array2.cpu().numpy().squeeze()
                    print(audio_array2)
                    print(len(audio_array2))

                    sample_rate = model.generation_config.sample_rate
                    scipy.io.wavfile.write(text_for_name,rate = sample_rate,data=audio_array2)
                    print('ffffffffffffffffffffffffffff')
            
            
            
                    rate, audio_array = scipy.io.wavfile.read(text_for_name)
                    print(type(audio_array))
                    print(audio_array.dtype)
                    print(len(audio_array))
            

            

                    # Преобразование аудиофайла в тип bytea
                    audio_data = audio_array*100000000000000
                    print('file base:', audio_data)
                    print('file not base:', audio_data.astype(np.int64))
                    audio_data = audio_data.astype(np.int64).tobytes()
                    print(len(audio_data))
            
                
            
           


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
                            insert_query1 = "select id from Users where login = %s"
                            cursor.execute(insert_query1, (fk_id,))
                            output = cursor.fetchone()

                            insert_query = "INSERT INTO files (file_name, preset, fk_user_id,rate) VALUES (%s, %s, %s, %s)"
                            cursor.execute(insert_query, (text_for_name, audio_data, output[0], rate))

                            output = cursor.fetchone()
                            print(f" {output}")

                    except Exception as _ex:
                        print("[INFO] Error while working with PostgreSQL", _ex)

                    finally:
                        if connection:
                        # cursor.close()
                            connection.close()
                            print("[INFO] PostgreSQL connection closed")
                else:
                    messagebox.showerror(title='Warning',message='filds shoud not be empty')




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
                    insert_query1 = "select id from Users where login = %s"
                    cursor.execute(insert_query1, (login,))
                    output = cursor.fetchone()



                    sql = "select * from Files where fk_user_id = %s"
                    cursor.execute(sql, (output[0],))
        
                    masss = cursor.fetchall()
                
        
    
            except Exception as _ex:
                print("[INFO] Error while working with PostgreSQL", _ex)
            finally:
                if connection:
                # cursor.close()
                    connection.close()
                    print("[INFO] PostgreSQL connection closed")
            your_presset=[]
            for i in range(len(masss)):
                your_presset.append(masss[i][3])
            
            def button_click_refreshr():
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
                        insert_query1 = "select id from Users where login = %s"
                        cursor.execute(insert_query1, (login,))
                        output = cursor.fetchone()



                        sql = "select * from Files where fk_user_id = %s"
                        cursor.execute(sql, (output[0],))
        
                        masss = cursor.fetchall()
                
        
    
                except Exception as _ex:
                    print("[INFO] Error while working with PostgreSQL", _ex)
                finally:
                    if connection:
                    # cursor.close()
                        connection.close()
                        print("[INFO] PostgreSQL connection closed")
                your_presset=[]
                for i in range(len(masss)):
                    your_presset.append(masss[i][3])
                your_bibler['values']=your_presset


            new_window1.destroy()
            new_windowr = add_window()
        
            new_canvasr=Canvas(new_windowr, height=300, width=250)
            new_canvasr.pack


            new_framer=Frame(new_windowr, bg='red')
            new_framer.place(relx=0.15, rely=0.15, relwidth=0.7,relheight=0.7)

            your_voice = your_presset

            selected_option = StringVar()
            your_bibler = ttk.Combobox(new_framer, textvariable=selected_option, values=your_voice, state='readonly')
            your_bibler.pack(pady=(20,0))


            press_me_newr = Button(new_framer, text = 'select', bg='grey',command=button_click_audior)
            press_me_newr.pack(pady=5)

            press_me_new = Button(new_framer, text = 'refresh', bg='grey',command=button_click_refreshr)
            press_me_new.pack()

            choice_your_voice = ['v2/ru_speaker_1','v2/ru_speaker_2','v2/ru_speaker_3','v2/ru_speaker_5','v2/ru_speaker_6']

            selected_option1 = StringVar()
            your_bibler_presset = ttk.Combobox(new_framer, textvariable=selected_option1, values=choice_your_voice, state='readonly')
            your_bibler_presset.pack(pady=(10,0))
        
           



            new_titler = Label(new_framer, text='Enter your text',bg='grey',font=30)
            new_titler.pack(pady=(5,5))

            textFieldr = Entry(new_framer, bg='white')
            textFieldr.pack(pady=(0,5))
            
            new_titler1 = Label(new_framer, text='Enter your text for name',bg='grey',font=30)
            new_titler1.pack(pady=(5,5))

            textFieldr1 = Entry(new_framer, bg='white')
            textFieldr1.pack(pady=(0,5))



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