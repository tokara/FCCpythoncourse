#Questions:
from Question import Question # have to import question classs

questions_prompts = [
    "How many colors does the rainbow have?\n(a) 3\n(b) 5\n(c) 7\n\n",
    "How many States are there in America\n(a) 26\n(b) 45\n(c) 50\n\n",
    "Jesus had\n(a) 12 disciples\n(b) 10 disciples\n(c) 9 disciples\n\n",

]

questions = [
    Question(questions_prompts[0], "c"),
    Question(questions_prompts[1], "c"),
    Question(questions_prompts[2], "a"),

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions))  + " correct")

run_test(questions)



