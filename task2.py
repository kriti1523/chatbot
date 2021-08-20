import random
from tkinter import *
root = Tk()
root.title('Chat Bot')
root.configure(bg='teal')
root.geometry('550x450')
root.resizable(False,False)
scroll_bar = Scrollbar(root)
  
scroll_bar.pack( side = RIGHT,
                fill = Y )
txt=Text(root)
txt.configure(bg='black',fg='white',font=('Times New Roman',12,'bold'),yscrollcommand= scroll_bar.set,height=20)




def send():
    send="You :"+ e.get()
    txt.insert(END,"\n "+send)

    if(e.get()=="hello")or(e.get()=="hi") or (e.get()=="hey"):
        greeting1=['hey !' ,'hi !','hello']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting1))

    elif(e.get()=="how are you?")or(e.get()=="how's it going?") or (e.get()=="how do you do?"):
        greeting2=['good ! what about you?','I am good and you ?','fine, thankyou']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting2))

    elif(e.get()=="I am also fine")or(e.get()=="fine") or (e.get()=="good"):
        greeting0=['How may i help you?','what can i do for you ?']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting0))


    elif(e.get()=="I am also good") or (e.get()=='good') or (e.get()=="fine") or (e.get()=="great"):
        greetings=['how can i help you?','what can i do for you?']
        txt.insert(END,"\n"+"Bot : "+random.choice(greetings))
    elif(e.get()=="good morning") or (e.get()=='morning'):
        greeting3=['good morning','morning ! have a great day','good day']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting3))
    elif(e.get()=="good night") or (e.get()=='night'):
        greeting4=['good night','night ! have a good sleep']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting4))
    elif(e.get()=="good evening"):
        greeting5=['good evening']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting5))
    elif(e.get()=="good afternoon") or (e.get()=='afternoon'):
        greeting6=['good afternoon','afternoon']
        txt.insert(END,"\n"+"Bot : "+random.choice(greeting6))
    elif(e.get()=="what is your name?") or (e.get()=="who are you?"):
        intro=['My name is baby bot.','I am baby bot.','baby bot.']
        txt.insert(END,"\n"+"Bot : "+random.choice(intro))
    elif(e.get()=="what are you?"):
        origin=['I am a chat bot','chat bot']
        txt.insert(END,"\n"+"Bot : "+random.choice(origin))
    elif(e.get()=="namaste") or (e.get()=="namaskaar"):
        origin=['namaste','namaskaar']
        txt.insert(END,"\n"+"Bot : "+random.choice(origin))
    elif(e.get()=="bye") or (e.get()=='goodbye') or (e.get()=="see you") :
        greetings=['bye','goodbye','see you','have a great day']
        txt.insert(END,"\n"+"Bot : "+random.choice(greetings))
    else:
        txt.insert(END,"\n"+ "Bot : sorry, I didn't get it. I am still learning ")
    e.delete(0,END)
    
txt.pack()
scroll_bar.config(command=txt.yview)

def clear():
    txt.delete('1.0',END)
e=Entry(root,width=20,font=('Times New Roman',16))
e.place(x=20,y=400)
send=Button(root,width=7,text='Send',bg='white',fg='black',command=send,font=('Times New Roman',14))
send.place(x=300,y=400)
clear=Button(root,width=7,text='Clear',bg='white',fg='black',command=clear,font=('Times New Roman',14))
clear.place(x=400,y=400)

root.mainloop()