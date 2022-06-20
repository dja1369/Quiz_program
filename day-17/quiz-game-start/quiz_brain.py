

class QuizBrain:
    t = 0
    f = 0    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
    
    def still_has_question(self):
        return self.question_number < len(self.question_list) # 이렇게 로직을 구성하면 좀더 간결하게 true, false를 반환할수 있다.
        # if self.question_number < len(self.question_list):
        #     return true
        # else:
        #     return false
        
    def next_question(self):

        next_quiz = self.question_list[self.question_number] 
        self.question_number += 1
        
        answer = input(f"Q.{self.question_number} : {next_quiz.text}. (True/False) : ")
        if answer == next_quiz.answer:
            print('정답입니다.')
            self.t += 1
            print(f'Correct answer : {self.t}, Wrong answer : {self.f }')  
        elif answer != next_quiz.answer:
            print('틀렸습니다.')
            self.f += 1
            print(f'Correct answer : {self.t}, Wrong answer : {self.f }') 
        elif answer == 'break':
            pass