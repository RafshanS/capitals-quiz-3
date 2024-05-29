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
root.title = ("Asian Country Capitals Quiz")
root.configure(bg="#856ff8")


Button_text = ("Arial", 20, "bold")
question_text = ("Arial", 20)
Title_text = ("Arial", 30)

score = 0 

title_label = tk.Label(root, text="Welcome to the Capital's Quiz", font=Title_text, bg='#856ff8', fg='white')
title_label.pack(pady=20)

def Learn():
    messagebox.showinfo("All the countries of Asia and their capitals")
   

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
    quiz_window = tk.Tk()
    quiz_window.geometry("800x800")
    quiz_window.configure(bg='#856ff8')  
    question_label = tk.Label(quiz_window, text=questions[question_num], font=question_text, bg='#856ff8', fg='white')
    question_label.pack(pady=20)  
    for i in range(4):
        btn = tk.Radiobutton(quiz_window, text=options[question_num][i], variable=v, value=options[question_num][i], font=Button_text, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
        btn.pack(pady=10)  
    next_button = tk.Button(quiz_window, text="Next", command=lambda: next_question(v.get(), answers[question_num]), font=Button_text, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
    next_button.pack(pady=20) 

def quit():
    root.destroy()
    
def check_score():
    score_window = tk.Tk()
    score_window.geometry("800x800")
    score_window.configure(bg='#856ff8')  
    score_label = tk.Label(score_window, text="Your score is: " + str(score) + "/" + str(len(questions)), font=question_text, bg='#856ff8', fg='white')
    score_label.pack(pady=20)
    quit_button = tk.Button(score_window, text="Quit", command=quit, font=Button_text, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
    quit_button.pack(pady=10)  
    menu_button = tk.Button(score_window, text="Main Menu", command=lambda: [score_window.destroy(), root.deiconify()], font=Button_text, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
    menu_button.pack(pady=10)    

learn_button = tk.Button(root, text="Learn", command=Learn, font=Button_text, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
learn_button.pack(pady=50)  
quiz_button = tk.Button(root, text="Quiz", command=lambda: [quiz(), root.withdraw()], font=Button_text, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
quiz_button.pack(pady=50)  
quit_button = tk.Button(root, text="Quit", command=quit, font=Button_text, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
quit_button.pack(pady=50) 

v = tk.StringVar()
   

root.mainloop()
    






