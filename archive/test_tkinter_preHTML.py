import tkinter as tk

# -------------------
# DATA STORAGE
# -------------------
questions = []

# -------------------
# FUNCTIONS
# -------------------

def save_question():
    question_text = question_entry.get()
    question_type = question_type_entry.get().lower()
    correct_answer = correct_answer_var.get()

    if question_type == "mc":
        answers = [
            answer_a_entry.get(),
            answer_b_entry.get(),
            answer_c_entry.get(),
            answer_d_entry.get()
        ]

        if "" in answers:
            result_label.config(text="All MC answers must be filled.")
            return

        if correct_answer not in ["A", "B", "C", "D"]:
            result_label.config(text="Correct answer must be A, B, C, or D.")
            return

        questions.append({
            "question": question_text,
            "type": "mc",
            "answers": answers,
            "correct": correct_answer
        })

    elif question_type == "tf":
        if correct_answer not in ["True", "False"]:
            result_label.config(text="Correct answer must be True or False.")
            return

        questions.append({
            "question": question_text,
            "type": "tf",
            "answers": ["True", "False"],
            "correct": correct_answer.title()
        })

    else:
        result_label.config(text="Enter 'mc' or 'tf' for question type.")
        return

    result_label.config(text="Question saved!")

    # Clear fields
    question_entry.delete(0, tk.END)
    question_type_entry.delete(0, tk.END)
    
    answer_a_entry.delete(0, tk.END)
    answer_b_entry.delete(0, tk.END)
    answer_c_entry.delete(0, tk.END)
    answer_d_entry.delete(0, tk.END)

def create_html_file():
    html = """
    <html>
    <head>
        <title>Quiz</title>
    </head>
    <body>
        <h1>Practice Quiz</h1>
    """

    for i, q in enumerate(questions, start=1):
        html += f"<h3>Question {i}: {q['question']}</h3>"

        if q["type"] == "mc":
            html += f"""
            <p>A. {q['answers'][0]}</p>
            <p>B. {q['answers'][1]}</p>
            <p>C. {q['answers'][2]}</p>
            <p>D. {q['answers'][3]}</p>
            """

        elif q["type"] == "tf":
            html += """
            <p>True</p>
            <p>False</p>
            """

        html += "<hr>"

    html += """
    </body>
    </html>
    """

    with open("quiz.html", "w", encoding="utf-8") as file:
        file.write(html)

    result_label.config(text="quiz.html created!")
# -------------------
# UI SETUP
# -------------------

window = tk.Tk()
window.title("Test Creator")

# Question
question_label = tk.Label(window, text="Enter your question:")
question_label.pack()
question_entry = tk.Entry(window)
question_entry.pack()

# Question Type
question_type_label = tk.Label(window, text="Enter question type (mc/tf):")
question_type_label.pack()
question_type_entry = tk.Entry(window)
question_type_entry.pack()

# Correct Answer
correct_label = tk.Label(window, text="Select correct answer:")
correct_label.pack()

correct_answer_var = tk.StringVar(window)
correct_answer_var.set("A")

correct_dropdown = tk.OptionMenu(window, correct_answer_var, "A", "B", "C", "D", "True", "False")
correct_dropdown.pack()

# MC Answers
answer_a_label = tk.Label(window, text="Answer A:")
answer_a_label.pack()
answer_a_entry = tk.Entry(window)
answer_a_entry.pack()

answer_b_label = tk.Label(window, text="Answer B:")
answer_b_label.pack()
answer_b_entry = tk.Entry(window)
answer_b_entry.pack()

answer_c_label = tk.Label(window, text="Answer C:")
answer_c_label.pack()
answer_c_entry = tk.Entry(window)
answer_c_entry.pack()

answer_d_label = tk.Label(window, text="Answer D:")
answer_d_label.pack()
answer_d_entry = tk.Entry(window)
answer_d_entry.pack()

# Save Button
save_question_button = tk.Button(window, text="Save Question", command=save_question)
save_question_button.pack()

# Create HTML button
create_html_button = tk.Button(window, text="Create HTML File", command=create_html_file)
create_html_button.pack()

# Result Label
result_label = tk.Label(window, text="")
result_label.pack()

# -------------------
# RUN APP
# -------------------

window.mainloop()

