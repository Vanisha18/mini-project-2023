import tkinter as tk
from tkinter import ttk

class Quiz:
    def __init__(self, master):
        self.master = master
        self.score = 0
        self.questions = [  {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "Rome", "Madrid"], "answer": "Paris"},
            {"question": "What is the largest planet in our solar system?", "options": ["Jupiter", "Mars", "Venus", "Saturn"], "answer": "Jupiter"},
            {"question": "What is the smallest country in the world?", "options": ["Monaco", "Vatican City", "San Marino", "Maldives"], "answer": "Vatican City"},
            {"question": "What is the currency of Japan?", "options": ["Yen", "Dollar", "Euro", "Pound"], "answer": "Yen"},
            {"question": "What is the highest mountain in the world?","options": ["Mount Everest", "K2", "Kilimanjaro", "Makalu"], "answer": "Mount Everest"},
            {"question": "What is the largest desert in the world?", "options": ["Sahara", "Gobi", "Kalahari", "Atacama"], "answer": "Sahara"},
            {"question": "What is the currency of Australia?", "options": ["Australian dollar", "US dollar", "Euro", "Pound"], "answer": "Australian dollar"},
            {"question": "What is the official language of Brazil?", "options": ["Portuguese", "Spanish", "French", "Italian"], "answer": "Portuguese"},
            {"question": "What is the national animal of India?", "options": ["Tiger", "Elephant", "Lion", "Leopard"], "answer": "Tiger"},
            {"question": "What is the capital of South Africa?", "options": ["Cape Town", "Durban", "Johannesburg", "Pretoria"], "answer": "Pretoria"}
        

        ]
        self.current_question = 0
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#FFB6C1')
        self.style.configure('TButton', background='#FF69B4', foreground='BLACK', font=('Arial', 25))
        self.style.configure('TRadiobutton', background='#FFB6C1', font=('Arial', 25))
        
        self.frame_header = ttk.Frame(self.master, padding=10, style='TFrame')
        self.frame_header.pack()
        
        self.question_label = ttk.Label(self.frame_header, text="", font=('Arial', 30))
        self.question_label.pack()
        
        self.frame_options = ttk.Frame(self.master, padding=10, style='TFrame')
        self.frame_options.pack()
        
        self.radio_var = tk.StringVar()
        self.radio_var.set("")
        self.radio_buttons = []
        for i in range(4):
            rb = ttk.Radiobutton(self.frame_options, text="", variable=self.radio_var, value="", style='TRadiobutton')
            rb.pack(pady=10)
            self.radio_buttons.append(rb)
        
        self.submit_button = ttk.Button(self.master, text="Submit", command=self.submit_answer, style='TButton')
        self.submit_button.pack(pady=20)
        
        self.score_label = ttk.Label(self.master, text="", font=('Arial', 30, 'bold'), foreground='#FFFFFF', background='#FF69B4')
        self.score_label.place(relx=0.5, rely=0.5, anchor='center')
        
        self.show_question()
        
    def show_question(self):
        self.question_label.config(text=self.questions[self.current_question]["question"])
        for i in range(4):
            self.radio_buttons[i].config(text=self.questions[self.current_question]["options"][i], value=self.questions[self.current_question]["options"][i])
        
    def submit_answer(self):
        if self.radio_var.get() == self.questions[self.current_question]["answer"]:
            self.score += 1
        self.current_question += 1
        if self.current_question == len(self.questions):
            self.show_score()
        else:
            self.show_question()
    
    def show_score(self):
        for rb in self.radio_buttons:
            rb.destroy()
        self.submit_button.destroy()
        self.question_label.destroy()
        self.score_label.config(text="Your score is: {}/{}".format(self.score, len(self.questions)))

root = tk.Tk()
root.title("Quiz App")
root.geometry("800x600")

root.configure(background='#FFB6C1')
quiz = Quiz(root)
root.mainloop()
