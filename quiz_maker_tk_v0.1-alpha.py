import tkinter as tk

# -------------------
# DATA STORAGE
# -------------------
questions = []
current_question = 1
num_questions = 0
test_title = ""


# -------------------
# FUNCTIONS
# -------------------

def save_info():
    global num_questions, test_title, current_question, questions

    test_title = title_entry.get()

    try:
        num_questions = int(question_count_entry.get())

        if num_questions > 30:
            result_label.config(text="Please enter 30 or less.")
            return

        if num_questions < 1:
            result_label.config(text="Please enter at least 1 question.")
            return

    except:
        result_label.config(text="Please enter a valid number.")
        return

    # Reset test data if user starts over
    questions = []
    current_question = 1

    result_label.config(
        text="You are creating: " + test_title + "\nNumber of questions: " + str(num_questions)
    )

    question_number_label.config(
        text="Enter question " + str(current_question) + " of " + str(num_questions)
    )


def save_question():
    global current_question

    if num_questions == 0:
        result_label.config(text="Please save test info first.")
        return

    if current_question > num_questions:
        result_label.config(text="You already entered all questions.")
        return

    question_text = question_entry.get()
    question_type = question_type_entry.get().lower()
    correct_answer = correct_answer_var.get()

    if question_text == "":
        result_label.config(text="Please enter a question.")
        return

    if question_type not in ["mc", "tf"]:
        result_label.config(text="Enter 'mc' or 'tf' for question type.")
        return

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
            result_label.config(text="For MC, correct answer must be A, B, C, or D.")
            return

        questions.append({
            "question": question_text,
            "type": "mc",
            "answers": answers,
            "correct": correct_answer
        })

    elif question_type == "tf":
        if correct_answer not in ["True", "False"]:
            result_label.config(text="For TF, correct answer must be True or False.")
            return

        questions.append({
            "question": question_text,
            "type": "tf",
            "answers": ["True", "False"],
            "correct": correct_answer
        })

    current_question += 1

    if current_question > num_questions:
        result_label.config(text="All questions entered!")
        question_number_label.config(text="Done")
    else:
        result_label.config(text="Question saved.")
        question_number_label.config(
            text="Enter question " + str(current_question) + " of " + str(num_questions)
        )

    # Clear question fields
    question_entry.delete(0, tk.END)
    question_type_entry.delete(0, tk.END)

    answer_a_entry.delete(0, tk.END)
    answer_b_entry.delete(0, tk.END)
    answer_c_entry.delete(0, tk.END)
    answer_d_entry.delete(0, tk.END)

    correct_answer_var.set("A")


def create_html_file():
    if len(questions) == 0:
        result_label.config(text="No questions saved yet.")
        return

    html = f"""
    <html>
    <head>
        <title>{test_title}</title>
    </head>
    <body>
        <h1>{test_title}</h1>
        <form id="quizForm">
    """

    for i, q in enumerate(questions, start=1):
        html += f"<h3>Question {i}: {q['question']}</h3>"

        if q["type"] == "mc":
            html += f'''
            <input type="radio" name="q{i}" value="A"> A. {q["answers"][0]}<br>
            <input type="radio" name="q{i}" value="B"> B. {q["answers"][1]}<br>
            <input type="radio" name="q{i}" value="C"> C. {q["answers"][2]}<br>
            <input type="radio" name="q{i}" value="D"> D. {q["answers"][3]}<br>
            '''

        elif q["type"] == "tf":
            html += f'''
            <input type="radio" name="q{i}" value="True"> True<br>
            <input type="radio" name="q{i}" value="False"> False<br>
            '''

        html += f'<input type="hidden" id="correct{i}" value="{q["correct"]}">'
        html += "<hr>"

    html += f"""
        <button type="button" onclick="gradeQuiz()">Submit Quiz</button>
        </form>

        <h2 id="result"></h2>

        <script>
        function gradeQuiz() {{
            let score = 0;
            let total = {len(questions)};

            for (let i = 1; i <= total; i++) {{
                let answers = document.getElementsByName("q" + i);
                let correct = document.getElementById("correct" + i).value;
                let selected = "";

                for (let j = 0; j < answers.length; j++) {{
                    if (answers[j].checked) {{
                        selected = answers[j].value;
                    }}
                }}

                if (selected === correct) {{
                    score++;
                }}
            }}

            document.getElementById("result").innerText =
                "You scored " + score + " out of " + total;
        }}
        </script>
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
window.geometry("350x500")

# Test title
title_label = tk.Label(window, text="Enter the name of your test:")
title_label.pack()

title_entry = tk.Entry(window)
title_entry.pack()

# Number of questions
question_count_label = tk.Label(window, text="How many questions? (Max 30):")
question_count_label.pack()

question_count_entry = tk.Entry(window)
question_count_entry.pack()

# Save info button
save_info_button = tk.Button(window, text="Save Info", command=save_info)
save_info_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Current question number
question_number_label = tk.Label(window, text="")
question_number_label.pack()

# Question text
question_label = tk.Label(window, text="Enter your question:")
question_label.pack()

question_entry = tk.Entry(window)
question_entry.pack()

# Question type
question_type_label = tk.Label(window, text="Enter question type (mc/tf):")
question_type_label.pack()

question_type_entry = tk.Entry(window)
question_type_entry.pack()

# Correct answer dropdown
correct_label = tk.Label(window, text="Select correct answer:")
correct_label.pack()

correct_answer_var = tk.StringVar(window)
correct_answer_var.set("A")

correct_dropdown = tk.OptionMenu(
    window,
    correct_answer_var,
    "A", "B", "C", "D", "True", "False"
)
correct_dropdown.pack()

# MC answers
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

# Save question button
save_question_button = tk.Button(window, text="Save Question", command=save_question)
save_question_button.pack()

# Create HTML button
create_html_button = tk.Button(window, text="Create HTML File", command=create_html_file)
create_html_button.pack()

# -------------------
# RUN APP
# -------------------

window.mainloop()
