import tkinter as tk
from tkinter import messagebox


questions = ["What is the capital of France?",
             "What is the capital of Spain?", 
             "What is the capital of Italy?", 
             "What is the capital of Germany?",
             "What is the capital of England?"]
options = [["Paris", "Madrid", "Rome", "Berlin"], ["Paris", "Madrid", "Rome", "London"], ["Paris", "Madrid", "Rome", "Berlin"], ["Paris", "Madrid", "Rome", "Berlin"], ["Paris", "Madrid", "Rome", "London"]]
answers = ["Paris", "Madrid", "Rome", "Berlin", "London"]



root = tk.Tk()
root.geometry("800x800")
root.configure(bg='#856ff8')  
root.title("Capitals Quiz")
score = 0


title_font = ("Arial", 20, "bold")
question_font = ("Arial", 20)
button_font = ("Arial", 25, )


title_label = tk.Label(root, text="Welcome to the Capital's Quiz", font=title_font, bg='#856ff8', fg='white')
title_label.pack(pady=20) 



def learn():
    learn_window = tk.Toplevel(root)
    learn_window.geometry("800x800")
    learn_window.configure(bg='#856ff8')
    learn_title= tk.Label(root, text="Learn the Capitals Here", font=title_font, bg='#856ff8', fg='white')
    quit_button = tk.Button(learn_window, text="Quit", command=quit, font=button_font, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
    quit_button.place(x=50,y=500)
    menu_button = tk.Button(learn_window, text="Main Menu", command=lambda: [learn_window.destroy(), root.deiconify()], font=button_font, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
    menu_button.place(x=50,y=400)
   
    
    

def quiz(question_num=0):
    def next_question(user_answer, answer):
        nonlocal question_num
        global score
        if user_answer == answer:
            score += 1
        question_num += 1
        if question_num < len(questions):
            quiz_window.destroy()
            quiz(question_num)
        else:
            quiz_window.destroy()
            check_score()

    root.withdraw()
    quiz_window = tk.Toplevel(root)
    quiz_window.geometry("800x800")
    quiz_window.configure(bg='#856ff8')  
    question_label = tk.Label(quiz_window, text=questions[question_num], font=question_font, bg='#856ff8', fg='white')
    question_label.pack(pady=20)  
    for i in range(4):
        btn = tk.Radiobutton(quiz_window, text=options[question_num][i], variable=v, value=options[question_num][i])
        btn.pack(pady=10)  
    next_button = tk.Button(quiz_window, text="Next", command=lambda: next_question(v.get(), answers[question_num]), font=button_font, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='black')
    next_button.pack(pady=20)  
    quit_button = tk.Button(quiz_window, text="Quit", command=quit, font=button_font, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
    quit_button.pack(pady=10)  

def quit():
    root.destroy()

def check_score():
    score_window = tk.Toplevel(root)
    score_window.geometry("800x800")
    score_window.configure(bg='#856ff8')  
    score_label = tk.Label(score_window, text="Your score is: " + str(score) + "/" + str(len(questions)), font=question_font, bg='#856ff8', fg='white')
    score_label.pack(pady=20) 
    quit_button = tk.Button(score_window, text="Quit", command=quit, font=button_font, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
    quit_button.pack(pady=10)  
    menu_button = tk.Button(score_window, text="Main Menu", command=lambda: [score_window.destroy(), root.deiconify()], font=button_font, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
    menu_button.pack(pady=10)  
    
learn_button = tk.Button(root, text="Learn", command=learn, font=button_font, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
learn_button.pack(pady=50)  
quiz_button = tk.Button(root, text="Quiz", command=lambda: [quiz(), root.withdraw()], font=button_font, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
quiz_button.pack(pady=50)  
quit_button = tk.Button(root, text="Quit", command=quit, font=button_font, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
quit_button.pack(pady=50) 
 

v = tk.StringVar()

root.mainloop()