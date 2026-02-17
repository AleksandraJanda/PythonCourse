from question_model import Question
from quiz_brain import QuizBrain
import data
import random

questions = []

# FUNCTIONS
def rand_id():
    return random.randint(0,len(questions))

def create_question_list():
    for i in range(len(data.question_data)):
        questions.append(
            create_question(
                data.question_data[i]['text'],
                data.question_data[i]['answer'])
        )

def create_question(question, answer):
    return Question(question, answer)

create_question_list()

quiz_brain = QuizBrain(questions)

quiz_brain.generate_question()
