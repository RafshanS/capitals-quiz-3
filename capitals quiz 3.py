import tkinter as tk
from tkinter import messagebox

questions = ["What is the capital of Bangladesh?", "what is the capital of Sri Lanka?", "What is the capital of Tajikistan","What is the capital of Pakistan", "what is the capital of Malaysia"]
options = [["Dhaka", "Delhi", "Chittagong","Mumbai"], ["Sri Jayawardenepura Kotte", "Mymensingh", "Kandy","Kochi"], ["Ulaanbataar", "Dushanbe","Tripoli","Tashkent"],["Allahabad", "Hyderabad", "Islamabad", "Rangpur"],"Kuala Lumpur", "Jakarta","Bangkok","Kathmandu"]
answers = ["Dhaka","Sri Jayawardenepura Kotte","Dushanbe","Islamabad","Kuala Lumpur"]
Button_text = ("Arial", 20, "bold")
question_font = ("Arial", 20)
Title_text = ("Arial", 50)

root = tk.Tk()
root.geometry("800x800")
root.title("Asian Country Capitals Quiz")
root.configure(bg="#856ff8")

score = 0 

title_label=tk.Label(root, text="Welcome to the Asian Country Capitals Quiz")
title_label.pack(pady=20)

def Learn():
    messagebox.showinfo("All the countries of Asia and their capitals")
   

    
def quiz(question_num=0):
    def next_question(answer_user, answer):
        nonlocal question_num
        global score
        if answer_user == answer:
            score = score + 1
        question_num += 1
        if question_num < len(questions) - 1:
            quiz_window.destroy()
            quiz(question_num + 1)
        else:
            quiz_window.destroy()
            check_score()
    
    root.withdraw()
    quiz_window = tk.Toplevel(root)
    quiz_window.geometry("800x800")
    quiz_window.configure(bg = "#856ff8")
    question_label = tk.Label(quiz_window, text=questions[question_num], font=question_font, bg="#56ff8", fg="white")
    question_label.pack(pady=20)
    
    for i in range(4):
        btn = tk.Radiobutton(quiz_window, text=options[question_num][i], variable=v, value=options[question_num][i], font = Title_text, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white')
        btn.pack()
    next_button = tk.Button(quiz_window, text="Next", command=lambda: next_question(v.get(), answers[question_num]))
    next_button.pack()            

    
            
            
        

    

root.mainloop()
    






