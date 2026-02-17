class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions_list = questions
        self.game_active = True

    def generate_question(self):
        answer = input(f'{self.questions_list[self.question_number].text}\n')
        self.check_answer(answer)

    def check_answer(self, answer):
        correct_answer = self.questions_list[self.question_number].answer
        if answer == correct_answer:
            self.question_number += 1
            if self.question_number < len(self.questions_list):
                self.generate_question()
            else:
                print('You\'ve completed the quiz! Congrats!')
        else:
            self.game_active = False
            print(f'Game Over. Correct questions: {self.question_number}/{len(self.questions_list)}')

