import tkinter as tk
from tkinter import messagebox

quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars",
    },
    {
        "question": "Who is the CEO of Tesla?",
        "options": ["Jeff Bezos", "Elon Mask", "Tim Cook", "Bill Gates"],
        "correct_answer": "Elon Mask",
    },
    {
        "question": "The iPhone was created by which company?",
        "options": ["Meta", "Google", "Apple", "IBM"],
        "correct_answer": "Apple",
    },
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.question_index = 0
        self.score = 0

        self.bg_color = "#f0f0f0"
        self.button_color = "#4CAF50"
        self.button_text_color = "white"
        self.text_color = "black"

        self.root.configure(bg=self.bg_color)

        self.question_label = tk.Label(
            root, text="", font=("Arial", 14), bg=self.bg_color, fg=self.text_color
        )
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            option_button = tk.Button(
                root,
                text="",
                font=("Arial", 12),
                command=lambda i=i: self.check_answer(i),
                bg=self.button_color,
                fg=self.button_text_color,
            )
            option_button.pack(pady=5)
            self.option_buttons.append(option_button)

        self.next_question()

    def next_question(self):
        if self.question_index < len(quiz_data):
            question_data = quiz_data[self.question_index]
            self.question_label.config(text=question_data["question"])

            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])

            self.question_index += 1
        else:
            self.show_results()

    def check_answer(self, selected_option):
        question_data = quiz_data[self.question_index - 1]
        correct_answer = question_data["correct_answer"]

        if question_data["options"][selected_option] == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Correct answer!")
        else:
            messagebox.showerror(
                "Incorrect", f"Incorrect answer! The correct answer is {correct_answer}"
            )

        self.next_question()

    def show_results(self):
        result_message = f"Your Score: {self.score}/{len(quiz_data)}"
        messagebox.showinfo("Quiz Completed", result_message)
        self.root.destroy()

root = tk.Tk()
root.geometry("400x300")
root.configure(bg="#f0f0f0")

welcome_label = tk.Label(
    root, text="Welcome to the Quiz Game!", font=("Arial", 16), bg="#f0f0f0", fg="blue"
)
welcome_label.pack(pady=20)

start_button = tk.Button(
    root,
    text="Start",
    command=lambda: QuizGame(root),
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
)
start_button.pack()

root.mainloop()