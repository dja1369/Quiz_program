from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)
     
start = QuizBrain(question_bank)
while start.still_has_question(): # if quiz has still questions
    start.next_question()