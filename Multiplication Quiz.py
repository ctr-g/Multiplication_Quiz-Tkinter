import tkinter as tk
import random

root = tk.Tk()
root.title("Multiplication Quiz")
root.geometry("500x350") 
root.resizable(False, False)
window_width = 500
window_height = 350

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

a = random.randint(1, 10)
b = random.randint(1, 10)
score = 0
questions_attempted = 0
total_questions_limit = 5    
time_elapsed = 0


def update_clock():
    global time_elapsed
    if questions_attempted < total_questions_limit:
        time_elapsed += 1
        timer_label.config(text=f"Time: {time_elapsed}s")
        root.after(1000, update_clock)

def start_quiz():
    global total_questions_limit, score, questions_attempted, time_elapsed, a, b
    
    try:
        total_questions_limit = int(setup_entry.get())
    except ValueError:
        total_questions_limit = 5 
        
    setup_label.pack_forget()
    setup_entry.pack_forget()
    start_button.pack_forget()
    
    score = 0
    questions_attempted = 0
    time_elapsed = 0
    
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    
    score_label.config(text="Score: 0")
    timer_label.config(text="Time: 0s")
    
    question_label.config(text=f"What is {a} x {b}?")
    feedback_label.config(text="")
    play_again_button.pack_forget()
    exit_button.pack_forget() 
    
    timer_label.pack(pady=2)
    score_label.pack(pady=2)
    question_label.pack(pady=15)
    answer_entry.pack(pady=5)
    submit_button.pack(pady=10)
    feedback_label.pack(pady=10)
    
    answer_entry.focus()
    update_clock()

def check_answer(event=None):
    global a, b, score, questions_attempted              
    
    if questions_attempted >= total_questions_limit:
        return
        
    correct_answer = a * b      
    user_answer = answer_entry.get()
    
    if user_answer == str(correct_answer):
        feedback_label.config(text="Correct!", fg="green")
        score += 1
        score_label.config(text=f"Score: {score}")
        
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        question_label.config(text=f"What is {a} x {b}?")
        
        answer_entry.delete(0, tk.END)
        answer_entry.focus()        
    else:
        feedback_label.config(text="Incorrect. Try again!", fg="red")
        answer_entry.delete(0, tk.END)
        answer_entry.focus()

    questions_attempted += 1

    if questions_attempted >= total_questions_limit:
        question_label.config(text="Quiz Complete!")
        feedback_label.config(text=f"Final Score: {score} out of {total_questions_limit}\nTotal Time: {time_elapsed} seconds", fg="black")
        
        answer_entry.pack_forget()
        submit_button.pack_forget()
        play_again_button.pack(pady=15)
        exit_button.pack(pady=10)

def reset_quiz():
    feedback_label.pack_forget()
    play_again_button.pack_forget()
    exit_button.pack_forget()
    timer_label.pack_forget()
    score_label.pack_forget()
    question_label.pack_forget()
    
    setup_entry.delete(0, tk.END)
    
    setup_label.pack(pady=20)
    setup_entry.pack(pady=10)
    start_button.pack(pady=10)
    setup_entry.focus()



setup_label = tk.Label(root, text="How many questions would you like to answer?", font=("Segoe UI", 14, "bold"))
setup_label.pack(pady=20)

setup_entry = tk.Entry(root, font=("Segoe UI", 14), justify="center", width=10)
setup_entry.pack(pady=10)
setup_entry.focus() 

start_button = tk.Button(root, text="Start Quiz", font=("Segoe UI", 12, "bold"))
start_button.config(command=start_quiz)
start_button.pack(pady=10)

setup_entry.bind("<Return>", lambda event: start_quiz())



timer_label = tk.Label(root, text="Time: 0s", font=("Segoe UI", 11, "bold"))
score_label = tk.Label(root, text="Score: 0", font=("Segoe UI", 11, "bold"))
question_label = tk.Label(root, text=f"What is {a} x {b}?", font=("Segoe UI", 22, "bold"))

answer_entry = tk.Entry(root, font=("Segoe UI", 18), justify="center", width=12)
answer_entry.bind("<Return>", check_answer)

submit_button = tk.Button(root, text="Submit", font=("Segoe UI", 12, "bold"), command=lambda: check_answer())
feedback_label = tk.Label(root, text="", font=("Segoe UI", 13, "bold"))

play_again_button = tk.Button(root, text="Play Again?", font=("Segoe UI", 12, "bold"), command=reset_quiz)
exit_button = tk.Button(root, text="Exit", font=("Segoe UI", 12, "bold"), command=root.destroy)


root.mainloop()
