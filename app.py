# This is an attempt to make a test maker.
# The idea is that someone runs this program and creates a test.exe file.
# This will allow a 30-question test to be made, either multiple choice
# or true/false.
# Once the test is made, it can be renamed and shared as an EXE.

# Ask the user for a test title
test_title = input("Enter the name of your test: ")

print("You are creating:", test_title)

#Added to account for non int input.
while True:
    try:
        num_questions = int(input("How many questions? (Max 30): "))
        
        if num_questions > 30:
            print("Please enter 30 or less.")
        else:
            break

    except:
        print("Please enter a valid number.")

#Commented out to show old code before non int issues.
# # Ask user number of questions for test, answer will be string
# num_questions = int(input("How many questions do you want? (Max 30): "))

# # If/else to ensure questions fall withing the correct limit.
# if num_questions > 30:
#     print("Please enter a number 30 or less.")
# else:
#     print("Number of questions accepted.")

#If the user enters a number >30 reask to get the number 1-30

# while num_questions > 30:
#     print("Too many questions. Please enter 30 or less.")
#     num_questions = int(input("How many questions do you want? (Max 30): "))

#Statement showing the number of questions user chose
print("Number of questions set to:", num_questions)

#create an empty list titled questions and type to be filled below
questions = []
question_types = []

#Commented out for overhaul change
#Create questions 1-30
#Add questions type and asnwers
# for i in range(1, num_questions + 1):
#     question = input(f"Enter question {i}: ")

#     question_type = input("Enter question type (mc/tf): ").lower()

#     if question_type == "mc": #Multiple choice questions will have four possible answers
#         answers = []
#         answers.append(input("Enter answer A: "))
#         answers.append(input("Enter answer B: "))
#         answers.append(input("Enter answer C: "))
#         answers.append(input("Enter answer D: "))
#         correct = input("Which answer is correct? (A/B/C/D): ").upper()
    
#     elif question_type == "tf":
#         answers = ["True", "False"]
#         correct = input("Is the answer True or False? ").title()

#     # questions.append({
#     #     "question": question,
#     #     "type": question_type
#     # })

#     # question_types.append(question_type)

#     questions.append({
#         "question": question,
#         "type": question_type,
#         "answers": answers,
#         "correct": correct_answer
#     })

#new question loop
for i in range(1, num_questions + 1):
    question = input(f"Enter question {i}: ")
    question_type = input("Enter question type (mc/tf): ").lower()

    if question_type == "mc":  # Multiple choice questions have four possible answers
        answers = []
        answers.append(input("Enter answer A: "))
        answers.append(input("Enter answer B: "))
        answers.append(input("Enter answer C: "))
        answers.append(input("Enter answer D: "))

        while True:
            correct = input("Which answer is correct? (A/B/C/D): ").upper()
            if correct in ["A", "B", "C", "D"]:
                break
            else:
                print("Please enter A, B, C, or D.")

        index = ["A", "B", "C", "D"].index(correct)
        correct_answer = answers[index]

    elif question_type == "tf":
        answers = ["True", "False"]

        while True:
            correct = input("Is the answer True or False? ").title()
            if correct in ["True", "False"]:
                break
            else:
                print("Please enter True or False.")

        correct_answer = correct

    else:
        print("Invalid question type. Please enter mc or tf.")
        continue

    questions.append({
        "question": question,
        "type": question_type,
        "answers": answers,
        "correct": correct_answer
    })



#Lists what questions were created
print("\nYour questions are:")

#Temp commented for testing
# for q in questions:
#     print(q)

#went with printing both the questions and the type to see both
for q in questions:
    print(q["question"], "-", q["type"])

