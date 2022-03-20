class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Question {self.question_number}: {current_question.text}\n(True or False): ')
        self.check_answer(answer=answer, correct_answer=current_question.answer)

    def check_answer(self, answer, correct_answer):
        is_correct = answer.lower() == correct_answer.lower()
        print('You got it right') if is_correct else print(f'You got it wrong. The correct answer is {correct_answer}')
        self.score += 1 if is_correct else 0
        print(f'Your current score is: {self.score}\n')
