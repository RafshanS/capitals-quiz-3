import tkinter as tk
from tkinter import messagebox

questions = ["What is the capital of Bangladesh?", "what is the capital of Sri Lanka?", "What is the capital of Tajikistan","What is the capital of Pakistan", "what is the capital of Malaysia"]
options = [["Dhaka", "Delhi", "Chittagong","Mumbai"], ["Sri Jayawardenepura Kotte", "Mymensingh", "Kandy","Kochi"], ["Ulaanbataar", "Dushanbe","Tripoli","Tashkent"],["Allahabad", "Hyderabad", "Islamabad", "Rangpur"],"Kuala Lumpur", "Jakarta","Bangkok","Kathmandu"]
answers = ["Dhaka","Sri Jayawardenepura Kotte","Dushanbe","Islamabad","Kuala Lumpur"]
Button_text = ("Arial", 40, "bold")
subtitle_text = ("Arial", 20)
Title_text = ("Arial", 50)

root = tk.Tk()
root.geometry("800x800")
root.title("Asian Country Capitals Quiz")

def Learn():
    messagebox.showinfo("All the countries of Asia and their capitals")
    print("")

score = 0
    
def quiz(question_num=0):
    def check_answer(answer_user, answer):
        global score
        if user_answer == answer:
            score = score + 1
        if question_num < len(questions) - 1:
            quiz(question_num + 1)
        else:
            messagebox.showinfo("Score:", "Your score is:", {score}/{len(questions)})
            root.deiconify()
            

    
            
            
        

    

root.mainloop()
    






