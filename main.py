from tkinter import *
import random

def clicked():
    answer = ("бесспорно",
        "предрешено",
        "никаких сомнений",
        "определенно да",
        "можеш быть уверен в этом",
        "мне кажется - да",
        "вероятнее всего",
        "хорошие перспективы",
        "знаки говорят - да",
        "да",
        "пока не ясно, попробуй снова",
        "спроси позже",
        "лучше не рассказывать",
        "сейчас нельзя предсказать",
        "сконцентрируйся и спроси опять",
        "даже не думай",
        "мой ответ - нет",
        "по моим данным - нет",
        "перспективы не очень хорошие",
        "весьма сомнительно")
    ans = random.choice(answer)
    lbl1.configure(text=ans)

root = Tk()
root.title('Игра')
root.geometry('920x789')
root.resizable(width=False, height=False)


root.image = PhotoImage(file='ball.png')
ball_8 = Label(root, image=root.image)
ball_8.grid(row=0, column=0)



lbl = Label(root, text='Задайте ваш вопрос:', bg = 'black', fg='yellow', font=('Helvetika', 30, 'bold'))
lbl.place(relx=0.5, rely=0.2, anchor=CENTER)
txt = Entry(root, width=38, font=('Helvetika', 20, 'bold'))
txt.place(relx=0.5, rely=0.3, anchor=CENTER)

btn = Button(root, text='предсказание', command=clicked, font='Arial 25', bg='black', fg='yellow')
btn.place(relx=0.3, rely=0.7, anchor=CENTER)
lbl1 = Label(root, text='', font='Arial 25')
lbl1.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()