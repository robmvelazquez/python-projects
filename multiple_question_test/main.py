from Question import Question

# Prompts for all three questions
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Grey\n\n",
    "What color are bananas?\n(a) White\n(b) Blue\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b)Red\n(c) Green\n\n"
]

# Creating the array for questions/answers
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    if score == 3:
        print("You've got " + str(score) + " out of " + str(len(questions)) + "correct.\nPerfect!")
    if score == 2:
        print("You've got " + str(score) + " out of " + str(len(questions)) + "correct.\nGood job!")
    if score <= 1:
        print("You've got " + str(score) + " out of " + str(len(questions)) + "correct.\nDon't worry, try harder next time!")

run_test(questions)


# Trigger additional attempt
response = input("Would you like to try again? (y) or (n): ")
if response == "y":
    run_test(questions)
else:
    print("Have a great day!")
    raise SystemExit