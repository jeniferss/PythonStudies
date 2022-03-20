from question import Question
from data import question_data
from brain import QuizBrain

questions = [Question(text=data['text'], answer=data['answer']) for data in question_data]
brain = QuizBrain(question_list=questions)

while brain.still_has_questions():
    brain.next_question()

print("You've completed the Quiz")
print(f"Your final score is {brain.score}/{len(questions)}")
