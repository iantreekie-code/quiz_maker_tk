import tkinter as tk

current_question = 1
num_questions = 0
questions = []


def get_valid_question_type():
    while True:
        q_type = question_type_entry.get().lower()

        if q_type in ["mc", "tf"]:
            return q_type
        else:
            print("Invalid input! Enter 'mc' or 'tf'")

def save_info():
    global num_questions

    test_title = title_entry.get()

    try:
        num_questions = int(question_count_entry.get())

        if num_questions > 30:
            result_label.config(text="Please enter 30 or less.")
            return

    except:
        result_label.config(text="Please enter a valid number.")
        return

    result_label.config(
        text="You are creating: " + test_title + "\nNumber of questions: " + str(num_questions)
    )

    question_number_label.config(
        text="Enter question " + str(current_question) + " of " + str(num_questions)
    )


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


window = tk.Tk()
window.title("Test Creator")

title_label = tk.Label(window, text="Enter the name of your test:")
title_label.pack()

title_entry = tk.Entry(window)
title_entry.pack()

question_count_label = tk.Label(window, text="How many questions? (Max 30):")
question_count_label.pack()

question_count_entry = tk.Entry(window)
question_count_entry.pack()

save_info_button = tk.Button(window, text="Save Info", command=save_info)
save_info_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

question_label = tk.Label(window, text="Enter your question:")
question_label.pack()

question_entry = tk.Entry(window)
question_entry.pack()

question_type_label = tk.Label(window, text="Enter question type (mc/tf):")
question_type_label.pack()

question_type_entry = tk.Entry(window)
question_type_entry.pack()

correct_label = tk.Label(window, text="Enter correct answer:")
correct_label.pack()

correct_entry = tk.Entry(window)
correct_entry.pack()

save_question_button = tk.Button(window, text="Save Question", command=save_question)
save_question_button.pack()

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

answer_a_entry.delete(0, tk.END)
answer_b_entry.delete(0, tk.END)
answer_c_entry.delete(0, tk.END)
answer_d_entry.delete(0, tk.END)

window.mainloop()