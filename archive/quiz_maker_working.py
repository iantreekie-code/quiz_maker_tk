#========================================
# Ian's Quiz/Test creator 
# Concept started 20 March 2026
# Idea is to create multple choice, T/F and scenario based quizes:
# That can be exported to HTML or similar for use in study and learning.
#========================================
#RoadMap
#================================
#V1.1
# - Question review/view option before making test
# - Better UI spacing
#
# V1.2
# - Question pool randomizer
# - Save load question modules
#
# V1.3
# - PDF import/scanning
# - image upload
# - Mobile options
#========================================


import tkinter as tk

# Defining variables
questions = []
current_question = 1
num_questions = 0
test_title = ""


# Defining funtions

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
    question_type = question_type_var.get()
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
        html += f"<div id='question{i}'>"
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
        html += f'<p id="feedback{i}"></p>'
        html += "<hr>"
        html += "</div>"

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
                let feedback = document.getElementById("feedback" + i);
                let selected = "";

                for (let j = 0; j < answers.length; j++) {{
                    if (answers[j].checked) {{
                        selected = answers[j].value;
                    }}
                }}

                if (selected === correct) {{
                    score++;
                    feedback.innerText = "Correct";
                }} else {{
                    feedback.innerText = "Incorrect. Correct answer: " + correct;
                }}
            }}

            let percentage = (score / total) * 100;

            document.getElementById("result").innerHTML =
                "You scored " + score + " out of " + total + "<br>" +
                "Percentage: " + percentage.toFixed(1) + "%";
        }}
        </script>
    </body>
    </html>
    """

    #adding ability to name HTML file as test name instead of quiz.html
    safe_title = test_title.replace(" ", "_")
    filename = safe_title + ".html"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)

    result_label.config(text=filename + " created!")



#Disable unused question options
def update_question_type(*args):
    q_type = question_type_var.get()

    if q_type == "mc":
        type_status_label.config(text="Multiple Choice: Enter answers A–D")

        answer_a_label.pack()
        answer_a_entry.pack()

        answer_b_label.pack()
        answer_b_entry.pack()

        answer_c_label.pack()
        answer_c_entry.pack()

        answer_d_label.pack()
        answer_d_entry.pack()

        correct_answer_var.set("A")
        correct_dropdown["menu"].delete(0, "end")
        for choice in ["A", "B", "C", "D"]:
            correct_dropdown["menu"].add_command(
                label=choice,
                command=tk._setit(correct_answer_var, choice)
            )

    elif q_type == "tf":
        type_status_label.config(text="True/False: Only select correct answer")
        
        answer_a_label.pack_forget()
        answer_a_entry.pack_forget()

        answer_b_label.pack_forget()
        answer_b_entry.pack_forget()

        answer_c_label.pack_forget()
        answer_c_entry.pack_forget()

        answer_d_label.pack_forget()
        answer_d_entry.pack_forget()

        correct_answer_var.set("True")
        correct_dropdown["menu"].delete(0, "end")
        for choice in ["True", "False"]:
            correct_dropdown["menu"].add_command(
                label=choice,
                command=tk._setit(correct_answer_var, choice)
            )

# User interface/tkinter

window = tk.Tk()
window.title("Test Creator")
window.geometry("350x700")

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
question_type_label = tk.Label(window, text="Select question type:")
question_type_label.pack()

question_type_var = tk.StringVar(window)
question_type_var.set("mc")
question_type_var.trace_add("write", update_question_type)

question_type_dropdown = tk.OptionMenu(window, question_type_var, "mc", "tf")
question_type_dropdown.pack()

type_status_label = tk.Label(window, text="")
type_status_label.pack()

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

# multiple choice options
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

update_question_type()

#Run the app
window.mainloop()
